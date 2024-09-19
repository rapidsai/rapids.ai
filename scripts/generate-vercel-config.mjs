import { getTransformedRoutes } from "@vercel/routing-utils";
import * as url from "node:url";
// TODO: dynamically generate rewrites based on libs.yaml & releases.yaml
const makeConfig = () => {
  const { routes } = getTransformedRoutes({
    trailingSlash: true,
    redirects: [
      {
        source: "/cudf/",
        destination: "/cudf/stable/",
        statusCode: 301,
      }
    ],
    rewrites: [
      {
        source: "/cudf/stable/(.*)",
        destination: "https://d1664dvumjb44w.cloudfront.net/cudf/html/24.02/$1",
      },
      {
        source: "/libcudf/stable/(.*)",
        destination:
          "https://d1664dvumjb44w.cloudfront.net/libcudf/html/24.02/$1",
      },
    ],
  });
  return {
    version: 3,
    routes: [
      ...routes,
      {
        handle: "error",
      },
      {
        status: 404,
        src: "^.*$",
        dest: "/404.html",
      },
    ],
  };
}
if (import.meta.url.startsWith("file:")) {
  const modulePath = url.fileURLToPath(import.meta.url);
  if (process.argv[1] === modulePath) {
    // Main ESM module
    console.log(JSON.stringify(makeConfig(), null, 2));
  }
}
