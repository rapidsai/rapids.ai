#!/usr/bin/env python3
"""
generate_selector.py

Script generates output for the following files based on the configuration
arrays below:
- _includes/selector-commands-stable.html
- _includes/selector-commands-nightly.html
"""

import glob
import os

"""
Selector configurations
"""
STABLE_CONFIG ={
    "name": "stable",
    "file": "_includes/selector-commands-stable-test.html", #TODO update path after testing
    "ver": "0.18",
    "os": ['ubuntu16.04','ubuntu18.04','ubuntu20.04','centos7','centos8'],
    "cuda": ['10.1','10.2','11.0'],
    "py": ['3.7','3.8'],
    "libs": ['cudf', 'cuml', 'cugraph', 'cusignal', 'cuspatial', 'cuxfilter'],
    "cmds": [] # Leave empty
}

NIGHTLY_CONFIG ={
    "name": "nightly",
    "file": "_includes/selector-commands-nightly-test.html", #TODO update path after testing
    "ver": "0.19",
    "os": ['ubuntu16.04','ubuntu18.04','ubuntu20.04','centos7','centos8'],
    "cuda": ['10.1','10.2','11.0'],
    "py": ['3.7','3.8'],
    "libs": ['cudf', 'cuml', 'cugraph', 'cusignal', 'cuspatial', 'cuxfilter'],
    "cmds": [] # Leave empty
}

def generate_docker(config, selector_name, docker_repo, docker_type):
    """ Generates docker commands"""
    rapids_ver = config["ver"]
    for os_ver in config["os"]:
        config["cmds"].append("\n<!-- docker "+selector_name+"-"+docker_type+" "+os_ver+" -->\n")
        for cuda_ver in config["cuda"]:
            for py_ver in config["py"]:
                tag_name = config["name"]
                tag_os = os_ver.replace('.','')
                tag_cuda = cuda_ver.replace('.','')
                tag_py = py_ver.replace('.','')
                repo = docker_repo + ("-nightly" if config["name"] == "nightly" else "")
                cmd = "```bash\n\
docker pull "+repo+":"+rapids_ver+"-cuda"+cuda_ver+"-"+docker_type+"-"+os_ver+"-py"+py_ver+"\n\
docker run --gpus all --rm -it -p 8888:8888 -p 8787:8787 -p 8786:8786 \\\n\
    "+repo+":"+rapids_ver+"-cuda"+cuda_ver+"-"+docker_type+"-"+os_ver+"-py"+py_ver+"\n\
```\n\
{: ."+tag_name+"-"+selector_name+"-all-"+docker_type+"-"+tag_os+"-py"+tag_py+"-cuda"+tag_cuda+" .hidden }\n"
                config["cmds"].append(cmd)

def generate_source(config):
    tag_name = config["name"]
    url_path = "/tree/main" if tag_name == "stable" else ""
    cmd = "<div class='"+tag_name+"-cudf-source hidden'>\n\\n\
    <pre># See <a href='https://github.com/rapidsai/cudf"+url_path+"#buildinstall-from-source' _target='blank'>cuDF Stable README</a> for build instructions</pre>\n\\n\
</div>\n\
<div class='"+tag_name+"-cuml-source hidden'>\n\
    <pre># See <a href='https://github.com/rapidsai/cuml"+url_path+"#buildinstall-from-source' _target='blank'>cuML Stable README</a> for build instructions</pre>\n\
</div>\n\
<div class='"+tag_name+"-cugraph-source hidden'>\n\
    <pre># See <a href='https://github.com/rapidsai/cugraph"+url_path+"#build-from-source-and-contributing' _target='blank'>cuGraph Stable README</a> for build instructions</pre>\n\
</div>\n\
<div class='"+tag_name+"-cusignal-source hidden'>\n\
    <pre># See <a href='https://github.com/rapidsai/cusignal"+url_path+"#dependencies' _target='blank'>cuSignal Stable README</a> for build instructions</pre>\n\
</div>\n\
<div class='"+tag_name+"-cuspatial-source hidden'>\n\
    <pre># See <a href='https://github.com/rapidsai/cuspatial"+url_path+"#clone-build-and-install-cuspatial' _target='blank'>cuSpatial Stable README</a> for build instructions</pre>\n\
</div>\n\
<div class='"+tag_name+"-cuxfilter-source hidden'>\n\
    <pre># See <a href='https://github.com/rapidsai/cuxfilter"+url_path+"#installation' _target='blank'>cuxfilter Stable README</a> for build instructions</pre>\n\
</div>"
    config["cmds"].append(cmd)


def write_output(config):
    """Write output to file"""
    f = open(config["file"], 'wt')
    f.writelines(config["cmds"])
    f.close()

def main():
    """Generates commands for both stable and nightly releases"""
    for config in STABLE_CONFIG, NIGHTLY_CONFIG:
        name = config["name"]
        filename = config["file"]
        print(f"Generating {name} commands")
        generate_docker(config, "rapids", "rapidsai/rapidsai", "base")
        generate_docker(config, "rapids", "rapidsai/rapidsai", "runtime")
        generate_docker(config, "rapids", "rapidsai/rapidsai-dev", "devel")
        generate_docker(config, "rapidscore", "rapidsai/rapidsai-core", "base")
        generate_docker(config, "rapidscore", "rapidsai/rapidsai-core", "runtime")
        generate_docker(config, "rapidscore", "rapidsai/rapidsai-core-dev", "devel")
        generate_source(config)
        print(f"Writing {name} commands to file '{filename}'")
        write_output(config)
        print(f"Finished writing {name} commands to file '{filename}'")

if __name__ == "__main__":
    main()