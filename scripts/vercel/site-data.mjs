import YAML from 'yaml'
import { readFileSync } from "node:fs";
import * as url from "node:url";
import * as path from "node:path";

const DATA_DIR = path.join(path.dirname(url.fileURLToPath(import.meta.url)), "..", "..", "data");

const getVersions = () => {
  const releasesFile = path.join(DATA_DIR, "releases.yaml");
  const text = readFileSync(releasesFile, "utf8");
  const versions = YAML.parse(text);
  return {
    nightly: versions[1].version,
    stable: versions[2].version,
    legacy: versions[3].version,
  };
};

const getLibraries = () => {
  const librariesFile = path.join(DATA_DIR, "libraries.yaml");
  const text = readFileSync(librariesFile, "utf8");
  return YAML.parse(text).map((lib) => ({
    name: lib.name.toLowerCase(),
    version_strings: lib.versions,
  }));
};

const validateLibraryVersions = (libraries, versions) => {
  const versionStrings = Object.keys(versions);
  for (const lib of libraries) {
    for (const version of lib.version_strings) {
      if (!versionStrings.includes(version)) {
        throw new Error(`Invalid version: ${version}`);
      }
    }
  }
};

const mapVersionStringsToNumbers = (libraries, versions) => {
  return libraries.map((lib) => ({
    ...lib,
    version_numbers: lib.version_strings.map((version) => versions[version]),
  }));
};

export const getLibraryVersions = () => {
  const libraries = getLibraries();
  const versions = getVersions();
  validateLibraryVersions(libraries, versions);
  return mapVersionStringsToNumbers(libraries, versions);
};

if (import.meta.url.startsWith("file:")) {
  const modulePath = url.fileURLToPath(import.meta.url);
  if (process.argv[1] === modulePath) {
    console.log(getLibraryVersions());
  }
}
