import { getTransformedRoutes } from "@vercel/routing-utils";
import { readFileSync } from "node:fs";
import path from "node:path";

const DEFAULT_REDIRECT_CODE = 301;

const makeTrailingSlashRedirects = () => (
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

const makeRedirects = () => {
  const redirects = [];
  redirects.push(...makeRedirectsFromFile(), ...makeTrailingSlashRedirects());
  return redirects;
};

const makeRewrites = () => {
  const rewrites = [];
  return rewrites;
};

export const makeRoutes = () => {
  const { routes, error } = getTransformedRoutes({
    redirects: makeRedirects(),
    rewrites: makeRewrites(),
  });

  if (error) throw error;
  return [
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
