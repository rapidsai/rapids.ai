#!/usr/bin/env python3
"""
selector_generator.py

Script generates output for the following files based on the configuration
arrays below:
- _includes/selector-commands-stable.html
- _includes/selector-commands-nightly.html
"""

import glob
import os

"""
Configurations
"""
STABLE_CONFIG ={
    "name": "stable",
    "file": "_includes/selector-commands-stable-test.html",
    "ver": "0.18",
    "os": ['ubuntu16.04','ubuntu18.04','ubuntu20.04','centos7','centos8'],
    "cuda": ['cuda10.1','cuda10.2','cuda11.0'],
    "py": ['py3.7','py3.8'],
    "cmds": [] # Leave empty
}

NIGHTLY_CONFIG ={
    "name": "nightly",
    "file": "_includes/selector-commands-nightly-test.html",
    "ver": "0.19",
    "os": ['ubuntu16.04','ubuntu18.04','ubuntu20.04','centos7','centos8'],
    "cuda": ['cuda10.1','cuda10.2','cuda11.0'],
    "py": ['py3.7','py3.8'],
    "cmds": [] # Leave empty
}

"""
GENERATOR FUNCTIONS
"""
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
docker pull "+repo+":"+rapids_ver+"-"+cuda_ver+"-"+docker_type+"-"+os_ver+"-"+py_ver+"\n\
docker run --gpus all --rm -it -p 8888:8888 -p 8787:8787 -p 8786:8786 \\\n\
    "+repo+":"+rapids_ver+"-"+cuda_ver+"-"+docker_type+"-"+os_ver+"-"+py_ver+"\n\
```\n\
{: ."+tag_name+"-"+selector_name+"-all-"+docker_type+"-"+tag_os+"-"+tag_py+"-"+tag_cuda+" .hidden }\n"
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
        print(f"Writing {name} commands to file '{filename}'")
        write_output(config)
        print(f"Finished writing {name} commands to file '{filename}'")

if __name__ == "__main__":
    main()