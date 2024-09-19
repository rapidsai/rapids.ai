import { getTransformedRoutes } from "@vercel/routing-utils";
import { getLibraryVersions } from "./site-data.mjs"
import { readFileSync } from "node:fs";
import path from "node:path";

const DEFAULT_REDIRECT_CODE = 301;

const makeTrailingSlashRoutes = () => (
  [
    // special case for redirecting /docs/cudf/23.04 to /docs/cudf/23.04/
    {
      "src": "^(/docs/.*\\d{1,2}\\.\\d{1,2})$",
      "headers": {
        "Location": "/$1/"
      },
      "status": DEFAULT_REDIRECT_CODE
    },
    // adds trailing slash to all directories.
    // copied from:
    // https://github.com/vercel/vercel/blob/6f46b1f/packages/routing-utils/src/superstatic.ts#L168-L192
    {
      "src": "^/((?:[^/]+/)*[^/\\.]+)$",
      "headers": {
        "Location": "/$1/"
      },
      "status": DEFAULT_REDIRECT_CODE
    },
    // removes trailing slash from all files (e.g. paths with a dot in the last segment).
    // adapted from:
    // https://github.com/vercel/vercel/blob/6f46b1f/packages/routing-utils/src/superstatic.ts#L168-L192
    // tweaked to prevent redirecting the following:
    //   - /docs/cudf/23.04/ to /docs/cudf/23.04
    //   - /docs/ucx/0.37/ to /docs/ucx/0.37
    {
      "src": "^/((?:[^/]+/)*[^/]+\\.\\w+)(?<!/\\d\\d\\.\\d\\d|/\\d\.\\d\\d)/$",
      "headers": {
        "Location": "/$1"
      },
      "status": DEFAULT_REDIRECT_CODE
    },
  ]
)

const makeRedirectsFromFile = () => {
  const redirectsFile = path.join(import.meta.dirname, "..", "..", "_redirects");
  const redirectsFileContents = readFileSync(redirectsFile, "utf8");
  const redirects = redirectsFileContents
    .split("\n")
    .filter(Boolean)
    .map((line) => {
      const [source, destination] = line.split(/\s+/).filter(Boolean);
      return {
        source,
        destination,
        statusCode: DEFAULT_REDIRECT_CODE,
      };
    });
  return redirects;
}

const makeRedirects = (libraryVersions) => {
  const redirects = [];
  redirects.push(...makeRedirectsFromFile());

  for (const lib of libraryVersions) {
    // redirects for /docs/cudf/ => /docs/cudf/stable/
    if (!lib.version_strings.includes("stable")) continue;
    redirects.push({
      source: `/docs/${lib.name}/`,
      destination: `/docs/${lib.name}/stable/`,
      statusCode: DEFAULT_REDIRECT_CODE,
    })
  }
  return redirects;
};

const makeRewrites = (libraryVersions) => {
  // rewrite /docs/cudf/stable/* => https://d1664dvumjb44w.cloudfront.net/cudf/html/24.02/*
  // rewrite /docs/cudf/* => https://d1664dvumjb44w.cloudfront.net/cudf/html/*

  const rewrites = [];
  for (const lib of libraryVersions) {
    for (let index = 0; index < lib.version_numbers.length; index++) {
      const versionString = lib.version_strings[index];
      const versionNumber = lib.version_numbers[index];

      rewrites.push({
        source: `/docs/${lib.name}/${versionString}/(.*)`,
        destination: `https://d1664dvumjb44w.cloudfront.net/${lib.name}/html/${versionNumber}/$1`,
      });
    }
    rewrites.push({
      source: `/docs/${lib.name}/(.*)`,
      destination: `https://d1664dvumjb44w.cloudfront.net/${lib.name}/html/$1`,
    });
  }
  return rewrites;
};

export const makeRoutes = () => {
  const libraryVersions = getLibraryVersions();
  const { routes, error } = getTransformedRoutes({
    redirects: makeRedirects(libraryVersions),
    rewrites: makeRewrites(libraryVersions),
  });

  if (error) throw error;
  return [
    ...makeTrailingSlashRoutes(),
    ...routes,
    {
      handle: "error",
    },
    {
      status: 404,
      src: "^.*$",
      dest: "/404.html",
    },
  ]
};
