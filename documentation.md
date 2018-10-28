---
title: Technical Documentation, Docker Container | RAPIDS
layout: default
name: DOCUMENTATION
tagline: Getting started with RAPIDS
button_name: DOWNLOAD CHEAT SHEET
button_link: assets/files/cheatsheet.pdf
---

<section class="introduction-section intro-content">
    <div class="fixed-content">
        <div class="getting-started-small-warp">
            <div class="intro-text">
                <h2>Introduction to RAPIDS</h2>
                <p>The RAPIDS data science framework includes a collection of libraries for executing end-to-end data science pipelines completely in the GPU. It is designed to have a familiar look and feel to data scientists working in Python. Here’s a code snippet where we read in a CSV file and output some descriptive statistics.</p>
            </div>
            <div class="programing-box">
                <p>import pygdf as cudf<br><br>
                    gdf = cudf.read_csv(‘path/to/file.csv’)<br>
                    for column in gdf.columns: <br>
                    &nbsp; &nbsp; &nbsp; &nbsp; print(column.mean())
                </p>
            </div>
            <p class="no-padding-bottom">RAPIDS uses optimized NVIDIA® CUDA® primitives and high-bandwidth GPU memory to accelerate data preparation and machine learning. The goal of RAPIDS is not only to accelerate the individual parts of the typical data science workflow, but to accelerate the complete end-to-end workflow.
            We suggest that you take a look at the sample workflow in our Docker container (described below), which illustrates just how straightforward a basic XGBoost model training and testing looks in RAPIDS.</p>
        </div>
    </div>
</section>

<section class="documentation-gray intro-content">
    <div class="documentation-gray-top"></div>
    <div class="documentation-inner-content">
        <div class="fixed-content">
            <div class="getting-started-small-warp">
                <h2>Download and Setup</h2>
                <div class="intro-text">
                    <p>RAPIDS is currently supported on Linux systems only, and we recommend using Docker when you’re just getting started.</p>
                </div>
                <h3>Prerequisites</h3>
                <ul>
                    <li>GPU support
                        <ul>
                            <li>NVIDIA Pascal™ architecture or better</li>
                        </ul>
                    </li>
                    <li>CUDA support
                        <ul>
                            <li>
                                <a href="https://developer.nvidia.com/cuda-92-download-archive" target="_blank">9.2</a>
                                (tags below for each version)
                            </li>
                            <li>
                                <a href="https://developer.nvidia.com/cuda-downloads" target="_blank">10.0</a>
                                (tags below for each version)
                            </li>
                        </ul>
                    </li>
                    <li>OS support
                        <ul>
                            <li><a href="http://releases.ubuntu.com/16.04/" target="_blank">Ubuntu 16.04 LTS</a> (tested
                                and confirmed working)
                            </li>
                            <li><a href="http://releases.ubuntu.com/18.04/" target="_blank">Ubuntu 18.04 LTS</a> (tested
                                and confirmed working)
                            </li>
                        </ul>
                    </li>
                    <li>Docker support
                        <ul>
                            <li><a href="https://docs.docker.com/install/linux/docker-ce/ubuntu/" target="_blank">
                                Docker CE v18+</a> - apt for Ubuntu 16.04 doesn't include v18+ by default
                            </li>
                            <li><a href="https://github.com/nvidia/nvidia-docker/wiki/Installation-(version-2.0)"
                                   target="_blank">nvidia-docker v2+</a></li>
                        </ul>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</section>

<section class="docker-container">
    <div class="fixed-content">
        <div class="getting-started-small-warp">
            <h2>RAPIDS Docker Container</h2>
            <div class="intro-text">
                <p>We’ve built a container with everything you need to experiment with RAPIDS.</p>
            </div>

            <h3>What’s Included in the Container:</h3>
            <ul>
                <li>RAPIDS libraries</li>
                <li>Jupyter notebooks:
                    <ul>
                        <li>Getting started notebook</li>
                        <li>Mortgage_Pandas</li>
                        <li>Mortgage_ETL_XGBoost</li>
                        <li>Dask_gdf_etl_to_ml</li>
                        <li>dask_gdf_ml</li>
                    </ul>
                </li>
                <li>Partial mortgage demo dataset</li>
            </ul>

            <h3>Getting the Container</h3>
            <ul>
                <li>Retrieve the container from the repo on <a href="https://hub.docker.com" target="_blank">DockerHub</a>.</li>
                <li>Go to <a href="https://hub.docker.com/r/rapidsai/rapidsai/" target="_blank">https://hub.docker.com/r/rapidsai/rapidsai/</a> and choose a tag based on the NVIDIA driver version you’re running (You can check your NVIDIA driver version by typing [nvidia-smi] in the terminal).</li>

                <!--
                <li>Go to <a href="https://hub.docker.com/r/nvcollab/ibeta-pygdf/" target="_blank">
                    https://hub.docker.com/r/nvcollab/ibeta-pygdf/ </a>and chose a tag based on the version of Cuda you
                    are running. (You can check your Cuda version by typing <span> cat /usr/local/cuda/version.txt in the terminal)</span>
                    -->
                </li>
                <li>The version of the container build is available in the file /rapids/notebooks/container-version that comes with the container:</li>
            </ul>
            <div class="programing-box">
                <p>cat /rapids/notebooks/container-version<br>
                    Container Release &nbsp;: &nbsp; 0.14a<br>
                    Build Date &nbsp; &nbsp; &nbsp; &nbsp; : &nbsp; Thu Sep 13 15:31:44 PDT 2018<br>
                    CUDA Version &nbsp; &nbsp; &nbsp; : &nbsp; 9.2<br>
                    Python Version &nbsp; &nbsp; : &nbsp; 3.5 <br>
                </p>
            </div>
            <h3>Installing RAPIDS</h3>
            <p>Pull the Docker Container</p>
            <div class="programing-box">
                <p>docker pull rapidsai/rapidsai:TAG</p>
            </div>
            <p class="no-padding-bottom">Available tags:</p>
            <ul>
                <li>
                    <pre>cuda9.2_py3.5 or latest</pre>
                    - CUDA 9.2 & Python 3.5
                </li>
                <li>
                    <pre>cuda9.1_py3.5</pre>
                    - CUDA 9.1 & Python 3.5
                </li>
                <li>
                    <pre>cuda9.0_py3.5</pre>
                    - CUDA 9.0 & Python 3.5
                </li>
            </ul>

            <h4>Option 1 - JupyterLab for Development and Examples</h4>
            <p>This is the recommended option, as the notebook server contains examples and a getting started notebook.
                To launch the container and run the notebook server, run:</p>
            <div class="programing-box">
                <p>docker run --runtime=nvidia -v <br>
                    /path/to/your/data/directory:/datasets -p 8888:8888 <br>
                    -p 8787:8787 -p 8790-8798:8790-8798 -it <br>
                    rapidsai/rapidsai:latest
                </p>
            </div>
            <p><strong>NOTE:</strong> This container runs <a href="https://jupyterlab.readthedocs.io/en/stable/"
                                                             target="_blank"> JupyterLab</a> on start, which will be
                accessible at port 8888 on your host machine with a default token/password of rapids.</p>
            <p class="no-padding-bottom"><strong>NOTE:</strong>  If you want to use a subset of the GPUs available
                on a system, you can do so using the NVIDIA_VISIBLE_DEVICES variable of nvidia-docker.. When starting the container, run: </p>
            <div class="programing-box">
                <p>docker run --runtime=nvidia -e <br>
                    NVIDIA_VISIBLE_DEVICES=0,1,2,3 -v <br>
                    /path/to/your/data/directory:/datasets -p 8888:8888 -p <br>
                    8787:8787 -p 8790-8798:8790-8798 -it <br>
                    rapidsai/rapidsai:latest
                </p>
            </div>
            <p><strong>ACCESSING THE GETTING STARTED GUIDE</strong></p>
            <p>Click on the <strong>Files</strong> tab on the left-hand side, then double-click on <em>getting_started.ipynb</em>
                to open the introductory notebook and start using cuDF.</p>

            <h4>Option 2 - BASH command-line for Development</h4>
            <p>If you prefer not to run JupyterLab, you may start the container with your own commands:</p>
            <div class="programing-box">
                <p>docker run --runtime=nvidia -it <br>
                    rapidsai/rapidsai:latest bash
                </p>
            </div>
            <p><strong>NOTE:</strong> Be sure to activate the 'gdf' conda environment in the container as shown below.
            </p>

            <h3>Activate Conda Environment</h3>
            <p>The container is configured with cuDF and related packages in the 'gdf' conda environment. To activate
                and use this environment inside the container, run:</p>
            <div class="programing-box">
                <p>source activate gdf</p>
            </div>
            <p><strong>NOTE:</strong> This is not necessary to do when using the notebook server, only when developing
                on the command line of the container.</p>

            <h3>Install Additional Python Packages using Conda or Pip</h3>
            <p>To install packages in the 'gdf' environment, use either method below to install the required
                package.</p>

            <div class="programing-box">
                <p>conda install some-package <br>
                    pip install some-package </p>
            </div>

            <p><strong><em>[NOTE: Bare metal and various other cloud installations will follow a similar layout
                pattern]</em></strong></p>


        </div>
    </div>
</section>

<section class="intro-content ">
    <div class="documentation-gray-top"></div>
    <div class="documentation-inner-content">
        <div class="fixed-content">
            <div class="getting-started-small-warp">
                <h2>Jupyter Notebooks</h2>

                <h3>1. Getting Started Notebook</h3>
                <p>This notebook walks you through a tour of some of the basic functionality of cuDF. This uses an
                    included dataset taken from the US Census.</p>
                <div class="programing-box white-box">
                    <img src="assets/images/slice-the-gdf.png"
                         alt="The getting started notebook walks you through the basic functions of PyGDF."
                         title="The getting started notebook walks you through the basic functions of PyGDF.">
                </div>

                <h3>2. Mortgage_ETL_XGBoost</h3>
                <p>This notebook shows an end-to-end workflow that you might find in the financial sector. The data is
                    the month-by-month history of mortgages made in the first quarter of 2017.</p>
                <div class="programing-box">
                    <img src="assets/images/Mortgage_ETL_XGBoost.png" alt="mortgages etl">
                </div>
                <p>The program then performs various variable transformations and joins on the data.</p>
                <div class="programing-box white-box">
                    <img src="assets/images/Mortgage_ETL_XGBoost-2.png" alt="mortgages etl">
                </div>
                <p>Finally, a very simple model predicting default probability is fit using XGBoost.</p>
                <div class="programing-box white-box">
                    <img src="assets/images/Mortgage_ETL_XGBoost-3.png" alt="mortgages etl">
                </div>
                <h3>3. Mortgage_Pandas</h3>
                <p>This notebook shows the same workflow as the above, but written entirely without cuDF. You’ll notice
                    that the API is very similar, and in some cases identical, but that the time to complete the
                    workflow is much less in cuDF. </p>

                <h3>4. dask_gdf_etl_to_ml</h3>
                <p>This notebook executes the complete end-to-end data science workflow seen in the Mortgage_ETL_XGBoost
                    notebook, but uses multiple GPUs in parallel.</p>
                
                <div class="programing-box white-box">
                    <img src="assets/images/dask_gdf_etl_to_ml.png" alt="dask gdf to etl to ml">
                </div>

                <h3>5. dask_gdf_ml </h3>
                <p>This notebook reads in data that has already had ETL and feature engineering performed, and then fits
                    and evaluates and XGBoost model.</p>
                <div class="programing-box white-box">
                    <img src="assets/images/dask_gdf_ml.png" alt="dask gdf ml">
                </div>
            </div>
        </div>
    </div>
</section>

<section class="footer-cta-main">
    <div class="fixed-content">
        <h2>Join the Community</h2>
        <p>Learn how you can be an adopter, contributor, and more.</p>
        <a href="community.html" class="blue-btn">Join Today</a>
    </div>
</section>
