#!/usr/bin/env python3
"""
generate_selector.py

Script generates output for the following files based on the configuration
arrays below:
- _includes/selector-commands-stable.html
- _includes/selector-commands-nightly.html
"""

"""
Selector configurations
"""
STABLE_CONFIG ={
    "name": "stable",
    "file": "_includes/selector-commands-stable.html",
    "os": ['ubuntu18.04','ubuntu20.04','centos7','centos8'],
    "cuda": ['11.0','11.2', '11.4', '11.5'],
    "py": ['3.7','3.8'],
    "libs": ['cudf', 'cuml', 'cugraph', 'cusignal', 'cuspatial', 'cuxfilter'],
    "cmds": [] # Leave empty
}

NIGHTLY_CONFIG ={
    "name": "nightly",
    "file": "_includes/selector-commands-nightly.html",
    "os": ['ubuntu18.04','ubuntu20.04','centos7','centos8'],
    "cuda": ['11.0','11.2', '11.4', '11.5'],
    "py": ['3.7','3.8'],
    "libs": ['cudf', 'cuml', 'cugraph', 'cusignal', 'cuspatial', 'cuxfilter'],
    "cmds": [] # Leave empty
}

def generate_docker(config, docker_repo, docker_type):
    """Generates docker commands"""
    rapids_ver = "{{" + f"site.data.releases.{config['name']}-version" +"}}" # Use "{{ var }}" syntax to get version number from Jekyll site data
    for os_ver in config["os"]:
        config["cmds"].append("\n<!-- docker "+docker_type+" "+os_ver+" -->\n")
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
{: ."+tag_name+"-all-"+docker_type+"-"+tag_os+"-py"+tag_py+"-cuda"+tag_cuda+" .hidden }\n"
                config["cmds"].append(cmd)

def generate_source(config):
    """Generates source install commands"""
    tag_name = config["name"]
    url_path = "/tree/main" if tag_name == "stable" else ""
    config["cmds"].append("\n<!-- source installs -->\n")
    cmd = "<div class='"+tag_name+"-cudf-source hidden'>\n\
    <pre># See <a href='https://github.com/rapidsai/cudf"+url_path+"#buildinstall-from-source' _target='blank'>cuDF README</a> for "+tag_name+" build instructions</pre>\n\
</div>\n\
<div class='"+tag_name+"-cuml-source hidden'>\n\
    <pre># See <a href='https://github.com/rapidsai/cuml"+url_path+"#buildinstall-from-source' _target='blank'>cuML README</a> for "+tag_name+" build instructions</pre>\n\
</div>\n\
<div class='"+tag_name+"-cugraph-source hidden'>\n\
    <pre># See <a href='https://github.com/rapidsai/cugraph"+url_path+"#build-from-source-and-contributing' _target='blank'>cuGraph README</a> for "+tag_name+" build instructions</pre>\n\
</div>\n\
<div class='"+tag_name+"-cusignal-source hidden'>\n\
    <pre># See <a href='https://github.com/rapidsai/cusignal"+url_path+"#dependencies' _target='blank'>cuSignal README</a> for "+tag_name+" build instructions</pre>\n\
</div>\n\
<div class='"+tag_name+"-cuspatial-source hidden'>\n\
    <pre># See <a href='https://github.com/rapidsai/cuspatial"+url_path+"#clone-build-and-install-cuspatial' _target='blank'>cuSpatial README</a> for "+tag_name+" build instructions</pre>\n\
</div>\n\
<div class='"+tag_name+"-cuxfilter-source hidden'>\n\
    <pre># See <a href='https://github.com/rapidsai/cuxfilter"+url_path+"#installation' _target='blank'>cuxfilter README</a> for "+tag_name+" build instructions</pre>\n\
</div>\n"
    config["cmds"].append(cmd)

def generate_conda_all(config, meta_package):
    """Generates conda install commands with all libraries"""
    rapids_ver = "{{" + f"site.data.releases.{config['name']}-version" +"}}" # Use "{{ var }}" syntax to get version number from Jekyll site data
    for cuda_ver in config["cuda"]:
        config["cmds"].append("\n<!-- conda "+"all "+cuda_ver+" -->\n")
        for py_ver in config["py"]:
            tag_name = config["name"]
            tag_cuda = cuda_ver.replace('.','')
            tag_py = py_ver.replace('.','')
            channel = "rapidsai" + ("-nightly" if config["name"] == "nightly" else "")
            cmd = "```bash\n\
conda create -n rapids-"+rapids_ver+" -c "+channel+" -c nvidia -c conda-forge \\\n\
    "+meta_package+"="+rapids_ver+" python="+py_ver+" cudatoolkit="+cuda_ver+"\n\
```\n\
{: ."+tag_name+"-all-conda-py"+tag_py+"-cuda"+tag_cuda+" .hidden }\n"
            config["cmds"].append(cmd)

def generate_conda_lib(config):
    """Generates conda install commands for each library"""
    rapids_ver = "{{" + f"site.data.releases.{config['name']}-version" +"}}" # Use "{{ var }}" syntax to get version number from Jekyll site data
    for lib in config["libs"]:
        for cuda_ver in config["cuda"]:
            config["cmds"].append("\n<!-- conda-lib "+lib+" "+cuda_ver+" -->\n")
            for py_ver in config["py"]:
                tag_name = config["name"]
                tag_cuda = cuda_ver.replace('.','')
                tag_py = py_ver.replace('.','')
                channel = "rapidsai" + ("-nightly" if config["name"] == "nightly" else "")
                cmd = "```bash\n\
conda create -n rapids-"+rapids_ver+" -c "+channel+" -c nvidia -c conda-forge \\\n\
    "+lib+"="+rapids_ver+" python="+py_ver+" cudatoolkit="+cuda_ver+"\n\
```\n\
{: ."+tag_name+"-"+lib+"-conda-py"+tag_py+"-cuda"+tag_cuda+" .hidden }\n"
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
        generate_docker(config, "rapidsai/rapidsai-core", "runtime")
        generate_docker(config, "rapidsai/rapidsai-core-dev", "devel")
        generate_source(config)
        generate_conda_all(config, "rapids")
        generate_conda_lib(config)
        print(f"Writing {name} commands to file '{filename}'")
        write_output(config)
        print(f"Finished writing {name} commands to file '{filename}'")

if __name__ == "__main__":
    main()
