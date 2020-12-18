---
title: "RAPIDS + Cloud"
description: "Deploying RAPIDS in the Cloud"
tagline: "Deploying RAPIDS in the Cloud"
button_text: "Deploy Now"
button_link: "#deploy"
layout: default
---

![cloud]({{ site.baseurl }}{% link /assets/images/RAPIDs-cloud.png %}){: .projects-logo}

{% capture intro_content %}

RAPIDS’s GPU accelerated data science tools can be deployed on all of the major clouds, allowing anyone to take advantage of the speed increases and TCO reductions that RAPIDS enables.
{: .subtitle}

RAPIDS can be deployed in a number of ways, from hosted Jupyter notebooks, to the major HPO services, all the way up to large-scale clusters via Dask or Kubernetes. Deploying on the cloud will require you to make use of supported GPU instances. Each major cloud provider has GPU instances that are supported by RAPIDS with varying capabilities and price points - the below charts identifies the major instance types of each cloud.


{% endcapture %}

{% include section-single.html
    background="background-white"
    padding-top="0em" padding-bottom="10em"
    content-single=intro_content
%}

{% capture csp_sel %}
# Cloud Providers

For the various deployment options on each cloud, as well as instructions and links to more details, please select the cloud provider you wish to deploy on.
{: .subtitle}

{% endcapture %}
{% capture csp_left %}
[![aws]({{ site.baseurl }}{% link /assets/images/AWS-logo.png %})](#aws) <br>
**[<i class="fad fa-chevron-double-down"></i> Amazon Web Services ](#aws)**

[<i class="fas fa-caret-right"></i> Single EC2 instance](#AWS-EC2){: .block}
[<i class="fas fa-caret-right"></i> Cluster using Dask](#AWS-Dask){: .block}
[<i class="fas fa-caret-right"></i> Cluster using Kubernetes](#AWS-Kubernetes){: .block}
[<i class="fas fa-caret-right"></i> Amazon Sagemaker](#AWS-Sagemaker){: .block}

{% endcapture %}
{% capture csp_mid %}

[![azure]({{ site.baseurl }}{% link /assets/images/MS-azure-logo.png %})](#azure) <br>
**[<i class="fad fa-chevron-double-down"></i> Microsoft Azure ](#azure)**

[<i class="fas fa-caret-right"></i> Single instance](#AZ-single){: .block}
[<i class="fas fa-caret-right"></i> Cluster via Dask](#AZ-Dask){: .block}
[<i class="fas fa-caret-right"></i> Cluster via Kubernetes](#AZ-Kubernetes){: .block}
[<i class="fas fa-caret-right"></i> Azure’s AzureML service](#AZ-ML){: .block}

{% endcapture %}
{% capture csp_right %}

[![gcp]({{ site.baseurl }}{% link /assets/images/GCP-logo.png %})](#googlecloud) <br>
**[<i class="fad fa-chevron-double-down"></i> Google Cloud ](#googlecloud)**

[<i class="fas fa-caret-right"></i> Single instance](#GC-single){: .block}
[<i class="fas fa-caret-right"></i> Cluster using Dask (via Dataproc)](#GC-Dask){: .block}
[<i class="fas fa-caret-right"></i> Cluster using Kubernetes](#GC-Kubernetes){: .block}
[<i class="fas fa-caret-right"></i> On CloudAI](#GC-AI){: .block}

{% endcapture %}

<div id="deploy"></div>
{% include slopecap.html
    background="background-purple"
    position="top"
    slope="down"
%}
{% include section-single.html
    background="background-purple"
    padding-top="5em" padding-bottom="3em"
    content-single=csp_sel
%}
{% include section-thirds.html
    background="background-purple"
    padding-top="0em" padding-bottom="5em"
    content-left-third=csp_left
    content-middle-third=csp_mid
    content-right-third=csp_right
%}
{% include slopecap.html
    background="background-purple"
    position="bottom"
    slope="up"
%}

<!-- AWS -->
<div id="aws"></div>
{% capture aws_intro %}

![aws]({{ site.baseurl }}{% link /assets/images/AWS-logo.png %})
## <i class="fab fa-aws"></i> Amazon Web Services

RAPIDS can be deployed on Amazon Web Services (AWS) in several ways:

**[<i class="fas fa-caret-right"></i> Single EC2 instance](#AWS-EC2)**{: .block}
**[<i class="fas fa-caret-right"></i> Cluster using Dask](#AWS-Dask)**{: .block}
**[<i class="fas fa-caret-right"></i> Cluster using Kubernetes and EKS/GKE/AKS](#AWS-Kubernetes)**{: .block}
**[<i class="fas fa-caret-right"></i> Amazon Sagemaker](#AWS-Sagemaker)**{: .block}

| Cloud <br> Provider | Inst. <br> Type | Inst. <br> Name  |  GPU <br> Count | GPU <br> Type | xGPU <br> RAM | xGPU <br> Perf. |
|----------------|---------------|----------------|---------|----------|------------ --------|---------------------------------|
| AWS            | G4            | g4dn\.xlarge   | 1       | T4       | 16 (GB)            | 8.1 (TFLOPS)                 |
| AWS            | G4            | g4dn\.8xlarge  | 1       | T4       | 16 (GB)            | 8.1 (TFLOPS)                 |
| AWS            | G4            | g4dn\.12xlarge | 4       | T4       | 16 (GB)            | 8.1 (TFLOPS)                 |
| AWS            | G4            | g4dn\.16xlarge | 1       | T4       | 16 (GB)            | 8.1 (TFLOPS)                 |
| AWS            | G4            | g4dn\.metal    | 8       | T4       | 16 (GB)            | 8.1 (TFLOPS)                 |
| AWS            | P3            | p3\.2xlarge    | 1       | V100     | 16 (GB)            | 14.1 (TFLOPS)                  |
| AWS            | P3            | p3\.8xlarge    | 4       | V100     | 16 (GB)            | 14.1 (TFLOPS)                  |
| AWS            | P3            | p3\.16xlarge   | 8       | V100     | 16 (GB)            | 14.1 (TFLOPS)                  |
| AWS            | P3            | p3dn\.24xlarge | 8       | V100     | 32 (GB)            | 14.1 (TFLOPS)                  |
{: .cloud-table}

**[Jump to Top <i class="fad fa-chevron-double-up"></i>](#deploy)**

{% endcapture %}

{% include section-single.html
    background="background-gray"
    padding-top="10em" padding-bottom="3em"
    content-single=aws_intro
%}
{% include slopecap.html
    background="background-gray"
    position="bottom"
    slope="down"
%}

{% capture aws_ec2 %}
## <i class="fab fa-aws"></i> AWS Single Instance (EC2)

There are multiple ways you can deploy RAPIDS on a single instance, but the easiest is to use the RAPIDS docker image:

**1. Initiate.** Initiate an instance supported by RAPIDS. See the introduction section for a list of supported instance types. It is recommended to use an AMI that already includes the required NVIDIA drivers, such as the **[Amazon Linux 2 AMI with NVIDIA TESLA GPU Driver](https://aws.amazon.com/marketplace/pp/Amazon-Web-Services-Amazon-Linux-2-AMI-with-NVIDIA/B07S5G9S1Z)** or the **[AWS Deep Learning AMI.](https://docs.aws.amazon.com/dlami/latest/devguide/what-is-dlami.html)**

**2. Credentials.** Using the credentials supplied by AWS, log into the instance via SSH. For a short guide on launching your instance and accessing it, read the Getting Started with Amazon EC2 documentation.

**3. Install.** Install docker in the AWS instance. This step is not required if you are using AWS Deep Learning AMI.

**4. Install.** Install RAPIDS docker image. The docker container can be customized by using the options provided in the **[Getting Started](https://rapids.ai/start.html)** page of RAPIDS. Example of an image that can be used is provided below:
```shell
>>> docker pull rapidsai/rapidsai:cuda10.2-runtime-ubuntu18.04
>>> docker run --gpus all --rm -it -p 8888:8888 -p 8787:8787 -p 8786:8786 \
    rapidsai/rapidsai:cuda10.2-runtime-ubuntu18.04
```
{: .margin-bottom-3em}

**5. Test RAPIDS.** Test it! The RAPIDS docker image will start a Jupyter notebook instance automatically. You can log into it by going to the IP address provided by AWS on port 8888.


**[Jump to Top <i class="fad fa-chevron-double-up"></i>](#deploy)**

{% endcapture %}

{% capture aws_dask %}
## <i class="fab fa-aws"></i> AWS Cluster via Dask

RAPIDS can be deployed on a multi-node ECS cluster using Dask’s dask-cloudprovider management tools. For more details, see our **[blog post on deploying on ECS.](https://medium.com/rapids-ai/getting-started-with-rapids-on-aws-ecs-using-dask-cloud-provider-b1adfdbc9c6e)**

**0. Run from within AWS.** The following steps assume you are running them from within the same AWS VPC. One way to ensure this is to run through the [AWS Single Instance (EC2)](#AWS-EC2) instructions and then run these steps from there.

**1. Setup AWS credentials.** First, you will need AWS credentials to allow us to interact with the AWS CLI. If someone else manages your AWS account, you will need to get these keys from them. You can provide these credentials to dask-cloudprovider in a number of ways, but the easiest is to setup your local environment using the AWS command line tools:
```shell
>>> pip install awscli
>>> aws configure
```
{: .margin-bottom-3em}

**2. Install dask-cloudprovider.** To install, you will need to run the following:
```shell
>>> pip install dask-cloudprovider[aws]
```
{: .margin-bottom-3em}

**3. Create an EC2 cluster:**
In the AWS console, visit the ECS dashboard. From the “Clusters” section on the left hand side, click “Create Cluster”.

Make sure to select an EC 2 Linux + Networking cluster so that we can specify our networking options.

Give the cluster a name EX. `rapids-cluster`.

Change the instance type to one that supports RAPIDS-supported GPUs (see introduction section for list of supported instance types). For this example, we will use `p3.2xlarge`, each of which comes with one NVIDIA V100 GPU.

In the networking section, select the default VPC and all the subnets available in that VPC.

All other options can be left at defaults. You can now click “create” and wait for the cluster creation to complete.

**4. Create a Dask cluster:**

Get the Amazon Resource Name (ARN) for the cluster you just created.

Set `AWS_DEFAULT_REGION` environment variable to your **[default region](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-regions)**:
```shell
export AWS_DEFAULT_REGION=[REGION]
```
[REGION] = code fo the region being used.
{: .margin-bottom-3em}

Create the ECSCluster object in your Python session:
```shell
>>> from dask_cloudprovider.aws import ECSCluster
>>> cluster = ECSCluster(
                            cluster_arn=<CLUSTER_ARN>,
                            n_workers=<NUM_WORKERS>,
                            worker_gpu=<NUM_GPUS>
                         )
```
[CLUSTER_ARN] = The ARN of an existing ECS cluster to use for launching tasks <br />
[NUM_WORKERS] = Number of workers to start on cluster creation. <br />
[NUM_GPUS] = The number of GPUs to expose to the worker, this must be less than or equal to the number of GPUs in the instance type you selected for the ECS cluster (e.g `1` for `p3.2xlarge`).
{: .margin-bottom-3em}

**5. Test RAPIDS.** Create a distributed client for our cluster:
```shell
>>> from dask.distributed import Client
>>> client = Client(cluster)
```
{: .margin-bottom-3em}

Load sample data and test the cluster!
```shell
>>> import dask, cudf, dask_cudf
>>> ddf = dask.datasets.timeseries()
>>> gdf = ddf.map_partitions(cudf.from_pandas)
>>> gdf.groupby(‘name’).id.count().compute().head()
Out[34]:
Xavier 99495
Oliver 100251
Charlie 99354
Zelda 99709
Alice 100106
Name: id, dtype: int64
```
{: .margin-bottom-3em}

**6. Cleanup.** Your cluster will continue to run (and incur charges!) until you shut it down. You can either scale the number of nodes down to zero instances, or shut it down altogether. If you are planning to use the cluster again soon, it is probably preferable to reduce the nodes to zero.


**[Jump to Top <i class="fad fa-chevron-double-up"></i>](#deploy)**

{% endcapture %}

{% capture aws_kub %}
## <i class="fab fa-aws"></i> AWS Cluster via Kubernetes

RAPIDS can be deployed on AWS via AWS’s managed Kubernetes service (EKS) using Helm. More details can be found at our **[helm docs.](https://helm.rapids.ai/docs/csp.html)**

**1. Install.** Install and configure dependencies in your local environment: kubectl, helm, awscli, and eksctl.

**2. Public Key.** Create a public key if you don't have one.

**3. Create your cluster:**
```shell
>>> eksctl create cluster \
    --name [CLUSTER_NAME] \
    --version 1.14 \
    --region [REGION] \
    --nodegroup-name gpu-workers \
    --node-type [NODE_INSTANCE] \
    --nodes  [NUM_NODES] \
    --nodes-min 1 \
    --nodes-max [MAX_NODES] \
    --node-volume-size [NODE_SIZE] \
    --ssh-access \
    --ssh-public-key ~/path/to/id_rsa.pub \
    --managed
```
[CLUSTER_NAME] = Name of the EKS cluster. This will be auto generated if not specified. <br>
[NODE_INSTANCE] = Node instance type to be used. Select one of the instance types supported by RAPIDS Refer to the introduction section for a list of supported instance types. <br>
[NUM_NODES] = Number of nodes to be used. <br>
[MAX_NODES] = Maximum size of the nodes. <br>
[NODE_SIZE] = Size of the nodes. <br>

Update the path to the ssh-public-key to point to the folder and file where your public key is saved.
{: .margin-bottom-3em}

**4. Install GPU addon:**
```shell
>>> kubectl create -f https://raw.githubusercontent.com/NVIDIA/k8s-device-plugin/1.0.0-beta4/nvidia-device-plugin.yml
```
{: .margin-bottom-3em}

**5. Install RAPIDS helm repo:**
```shell
>>> helm repo add rapidsai https://helm.rapids.ai
>>> helm repo update
```
{: .margin-bottom-3em}

**6. Install helm chart:**
```shell
>>> helm install rapidstest rapidsai/rapidsai
```
{: .margin-bottom-3em}

**7. Accessing your cluster:**
```shell
>>> kubectl get svc
NAME                 TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)                       AGE
kubernetes           ClusterIP      10.100.0.1       <none>        443/TCP                       14m
rapidsai-jupyter     LoadBalancer   10.100.208.179   1.2.3.4       80:32332/TCP                  3m30s
rapidsai-scheduler   LoadBalancer   10.100.19.121    5.6.7.8       8786:31779/TCP,80:32011/TCP   3m30s
```
{: .margin-bottom-3em}

You can now visit the external IP of the rapidsai-jupyter service in your browser!


**[Jump to Top <i class="fad fa-chevron-double-up"></i>](#deploy)**

{% endcapture %}

{% capture aws_sage %}
## <i class="fab fa-aws"></i> AWS Sagemaker

RAPIDS also works with AWS Sagemaker. We’ve written a **[detailed guide](https://medium.com/rapids-ai/running-rapids-experiments-at-scale-using-amazon-sagemaker-d516420f165b)** with **[examples](https://github.com/rapidsai/cloud-ml-examples/tree/main/aws)** for how to use Sagemaker with RAPIDS, but the simplest version is:

**1. Start.** Start a Sagemaker hosted Jupyter notebook instance on AWS.

**2. Clone.** **[Clone the example repository](https://github.com/shashankprasanna/sagemaker-rapids.git)** which includes all required setup and some example data and code.

**3. Run.** Start running the sagemaker-rapids.ipynb jupyter notebook.

For more details, including on running large-scale HPO jobs on Sagemaker with RAPIDS, check out the **[detailed guide](https://medium.com/rapids-ai/running-rapids-experiments-at-scale-using-amazon-sagemaker-d516420f165b)** and **[examples.](https://github.com/rapidsai/cloud-ml-examples/tree/main/aws)**


**[Jump to Top <i class="fad fa-chevron-double-up"></i>](#deploy)**

{% endcapture %}
<div id="AWS-EC2"></div>
{% include section-single.html
    background="background-white"
    padding-top="6em" padding-bottom="0em"
    content-single=aws_ec2
%}
<div id="AWS-Dask"></div>
{% include section-single.html
    background="background-white"
    padding-top="3em" padding-bottom="0em"
    content-single=aws_dask
%}
<div id="AWS-Kubernetes"></div>
{% include section-single.html
    background="background-white"
    padding-top="3em" padding-bottom="0em"
    content-single=aws_kub
%}
<div id="AWS-Sagemaker"></div>
{% include section-single.html
    background="background-white"
    padding-top="3em" padding-bottom="10em"
    content-single=aws_sage
%}

<!-- Azure -->
<div id="azure"></div>
{% capture azure_intro %}
![azure]({{ site.baseurl }}{% link /assets/images/MS-azure-logo.png %})
## <i class="fab fa-microsoft"></i> Microsoft Azure

RAPIDS can be deployed on Microsoft Azure via several methods:
**[<i class="fas fa-caret-right"></i> Single instance](#AZ-single)**{: .block}
**[<i class="fas fa-caret-right"></i> Cluster via Dask](#AZ-Dask)**{: .block}
**[<i class="fas fa-caret-right"></i> Cluster via Kubernetes](#AZ-Kubernetes)**{: .block}
**[<i class="fas fa-caret-right"></i> Azure’s AzureML service](#AZ-ML)**{: .block}

| Cloud <br> Provider | Inst. <br> Type | Inst. <br> Name  |  GPU <br> Count | GPU <br> Type | xGPU <br> RAM | xGPU <br> Perf. |
|----------------|---------------|---------------|---------|----------|----------------------|---------------|-----------------|
| Azure          | NDs Series    | ND6s          | 1       | P40      | 24 (GB)               | 11.7 (TFLOPS)                     |
| Azure          | NDs Series    | ND12s         | 2       | P40      | 24 (GB)               | 11.7 (TFLOPS)                     |
| Azure          | NDs Series    | ND24s         | 4       | P40      | 24 (GB)               | 11.7 (TFLOPS)                     |
| Azure          | NDs Series    | ND24rs        | 4       | P40      | 24 (GB)               | 11.7 (TFLOPS)                     |
| Azure          | NCs v2 Series | NC6s v2       | 1       | P100     | 16 (GB)              | 10.6 (TFLOPS)                   |
| Azure          | NCs v2 Series | NC12s v2      | 2       | P100     | 16 (GB)              | 10.6 (TFLOPS)                   |
| Azure          | NCs v2 Series | NC24s v2      | 4       | P100     | 16 (GB)              | 10.6 (TFLOPS)                   |
| Azure          | NCs v2 Series | NC24rs v2     | 4       | P100     | 16 (GB)              | 10.6 (TFLOPS)                   |
| Azure          | NCs v3 Series | NC6s v3       | 1       | V100     | 16 (GB)              | 14.1 (TFLOPS)                     |
| Azure          | NCs v3 Series | NC12s v3      | 2       | V100     | 16 (GB)              | 14.1 (TFLOPS)                     |
| Azure          | NCs v3 Series | NC24s v3      | 4       | V100     | 16 (GB)              | 14.1 (TFLOPS)                     |
| Azure          | NCs v3 Series | NC24rs v3     | 4       | V100     | 16 (GB)              | 14.1 (TFLOPS)                     |
| Azure          | NDs v2 Series | ND40rs        | 8       | V100     | 32 (GB)              | 14.1 (TFLOPS)                     |
{: .cloud-table}

**[Jump to Top <i class="fad fa-chevron-double-up"></i>](#deploy)**

{% endcapture %}

{% include slopecap.html
    background="background-gray"
    position="top"
    slope="down"
%}
{% include section-single.html
    background="background-gray"
    padding-top="3em" padding-bottom="3em"
    content-single=azure_intro
%}
{% include slopecap.html
    background="background-gray"
    position="bottom"
    slope="up"
%}

{% capture az_single %}
## <i class="fab fa-microsoft"></i> Azure Single Instance (VM)

There are multiple ways you can deploy RAPIDS on a single VM instance, but the easiest is to use the RAPIDS docker image:

**1. Initiate VM.** **[Initiate a VM instance](https://docs.microsoft.com/en-us/azure/virtual-machines/linux/quick-create-portal)** using a VM supported by RAPIDS. See the introduction section for a list of supported instance types. It is recommended to use an image that already includes the required NVIDIA drivers, such as **[this one.](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/nvidia.ngc_azure_17_11?tab=Overview)**

**2. Credentials.** Using the credentials supplied by Azure, log into the instance via SSH.

**3. Docker Permissions.** **[Setup docker user permissions.](https://docs.docker.com/engine/install/linux-postinstall/)**

**4. Install.** **[Install RAPIDS docker image](https://rapids.ai/start.html)**. The docker container can be customized by using the options provided in the **[Getting Started](https://rapids.ai/start.html)** page of RAPIDS. Example of an image that can be used is provided below:
```shell
>>> docker pull rapidsai/rapidsai:cuda10.2-runtime-ubuntu18.04
>>> docker run --gpus all --rm -it -p 8888:8888 -p 8787:8787 -p 8786:8786 \
    rapidsai/rapidsai:cuda10.2-runtime-ubuntu18.04
```
{: .margin-bottom-3em}

**5. Test RAPIDS.** Test it! The RAPIDS docker image will start a Jupyter notebook instance automatically. You can log into it by going to the IP address provided by Azure on port 8888.


**[Jump to Top <i class="fad fa-chevron-double-up"></i>](#deploy)**

{% endcapture %}

{% capture az_dask %}
## <i class="fab fa-microsoft"></i> Azure Cluster via Dask

RAPIDS can be deployed on a Dask cluster on Azure ML Compute using dask-cloudprovider.

**1. Install.** Install Azure tools (azure-cli).

**2. Install dask-cloudprovider:**
```shell
>>> pip install dask-cloudprovider
```
{: .margin-bottom-3em}

**3. Config.** Create your workspace config file -see **[Azure docs](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-configure-environment#workspace)** for details.

**4. Setup.** Setup your Azure ML Workspace using the config file created in the previous step:
```shell
>>> from azureml.core import Workspace
>>> ws = Workspace.from_config()
```
{: .margin-bottom-3em}

**5. Create the AzureMLCluster:**
```shell
>>> from dask_cloudprovider import AzureMLCluster
>>> cluster = AzureMLCluster(ws)
```
{: .margin-bottom-3em}

**6. Run Notebook.** In a Jupyter notebook, the cluster object will return a widget allowing you to scale up and containing links to the Jupyter Lab session running on the headnode and Dask dashboard, which are forwarded to local ports for you -unless running on a remote Compute Instance.


**[Jump to Top <i class="fad fa-chevron-double-up"></i>](#deploy)**

{% endcapture %}

{% capture az_kub %}
## <i class="fab fa-microsoft"></i> Azure Cluster via Kubernetes

RAPIDS can be deployed on a Kubernetes cluster on Azure using Helm. More details can be found at our **[helm docs.](https://helm.rapids.ai/docs/csp.html)**

**1. Install.** Install and configure dependencies on your local environment: kubectl, helm, and az (azure-cli).

**2. Configure.** Configure az and create a resource group if you don't already have one.
```shell
>>> az login
>>> az group create --name [RESOURCE_GROUP] --location [REGION]
```
[RESOURCE_GROUP] = resource group to be created. <br>
[REGION] = the location where the resource group should be created.
{: .margin-bottom-3em}

**3. Create your cluster:**
```shell
>>> az aks create \
    --resource-group [RESOURCE_GROUP] \
    --name [CLUSTER_NAME] \
    --node-vm-size [VM_SIZE] \
    --node-count [NUM_NODES]
```
[CLUSTER_NAME] = Name of the managed cluster. <br>
[NUM_NODES] = Number of nodes in the Kubernetes node pool. <br>
[VM_SIZE] = the size of the VM you would like to target. This must include a RAPIDS-compatible GPU. Ex. `Standard_NC12`

Please refer to the **[Microsoft Azure CLI documentation](https://docs.microsoft.com/en-us/cli/azure/aks?view=azure-cli-latest#az-aks-create)** for more information.
{: .margin-bottom-3em}

**4. Update your local kubectl config file:**
```shell
>>> az aks get-credentials --resource-group myResourceGroup --name rapids
```
{: .margin-bottom-3em}

**5. Install.** **[Install Kubernetes NVIDIA Device Plugin:](https://github.com/NVIDIA/k8s-device-plugin)**
```shell
>>> helm repo add nvdp https://nvidia.github.io/k8s-device-plugin
>>> helm repo update
>>> helm install \
    --version=0.6.0 \
    --generate-name \
    nvdp/nvidia-device-plugin
```
{: .margin-bottom-3em}

**6. Install RAPIDS helm repo:**
```shell
>>> helm repo add rapidsai https://helm.rapids.ai
>>> helm repo update
```
{: .margin-bottom-3em}

**7. Install helm chart:**
```shell
>>> helm install rapidstest rapidsai/rapidsai
```
{: .margin-bottom-3em}

**8. Accessing your cluster:**
```shell
>>> kubectl get svc
NAME                 TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)                       AGE
kubernetes           ClusterIP      10.100.0.1       <none>        443/TCP                       14m
rapidsai-jupyter     LoadBalancer   10.100.208.179   1.2.3.4       80:32332/TCP                  3m30s
rapidsai-scheduler   LoadBalancer   10.100.19.121    5.6.7.8       8786:31779/TCP,80:32011/TCP   3m30s
```
{: .margin-bottom-3em}

You can now visit the external IP of the rapidsai-jupyter service in your browser!


**[Jump to Top <i class="fad fa-chevron-double-up"></i>](#deploy)**

{% endcapture %}

{% capture az_ml %}
## <i class="fab fa-microsoft"></i> AzureML Service

RAPIDS can be deployed at scale using Azure Machine Learning Service--and easily scales up to any size needed. We have written a **[detailed guide](https://medium.com/rapids-ai/rapids-on-microsoft-azure-machine-learning-b51d5d5fde2b)** with **[helper scripts](https://github.com/rapidsai/cloud-ml-examples/tree/main/azure)** to get everything deployed, but the high level procedure is:

**1. Create.** Create your Azure Resource Group.

**2. Workspace.** Within the Resource Group, create an Azure Machine Learning service Workspace.

**3. Config.** Within the Workspace, download the config.json file and verify that subscription_id, resource_group, and workspace_name are set correctly for your environment.

**4. Quota.** Within your Workspace, check your Usage + Quota to ensure you have enough quota to launch your desired cluster size.

**5. Clone.** From your local machine, clone the RAPIDS demonstration code and helper scripts.

**6. Run Utility.** Run the RAPIDS helper utility script to initialize the Azure Machine Learning service Workspace:
```shell
>>> ./start_azureml.py \
 --config=[CONFIG_PATH] \
 --vm_size=[VM_SIZE] \
 --node_count=[NUM_NODES]
```
[CONFIG_PATH] = the path to the config file you downloaded in step three.
{: .margin-bottom-3em}

**7. Start.** Open your browser to http://localhost:8888 and get started!

See **[the guide](https://medium.com/rapids-ai/rapids-on-microsoft-azure-machine-learning-b51d5d5fde2b#fee3)** or **[GitHub](https://github.com/rapidsai/cloud-ml-examples/tree/main/azure)** for more details.


**[Jump to Top <i class="fad fa-chevron-double-up"></i>](#deploy)**

{% endcapture %}
<div id="AZ-single"></div>
{% include section-single.html
    background="background-white"
    padding-top="6em" padding-bottom="0em"
    content-single=az_single
%}
<div id="AZ-Dask"></div>
{% include section-single.html
    background="background-white"
    padding-top="5em" padding-bottom="0em"
    content-single=az_dask
%}
<div id="AZ-Kubernetes"></div>
{% include section-single.html
    background="background-white"
    padding-top="3em" padding-bottom="0em"
    content-single=az_kub
%}
<div id="AZ-ML"></div>
{% include section-single.html
    background="background-white"
    padding-top="3em" padding-bottom="10em"
    content-single=az_ml
%}

<!-- Google Cloud -->
<div id="googlecloud"></div>
{% capture gcp_intro %}
![gcp]({{ site.baseurl }}{% link /assets/images/GCP-logo.png %})
## <i class="fab fa-google"></i> Google Cloud

RAPIDS can be used in Google Cloud in several different ways:
**[<i class="fas fa-caret-right"></i> Single instance](#GC-single)**{: .block}
**[<i class="fas fa-caret-right"></i> Cluster using Dask (via Dataproc)](#GC-Dask)**{: .block}
**[<i class="fas fa-caret-right"></i> Cluster using Kubernetes](#GC-Kubernetes)**{: .block}
**[<i class="fas fa-caret-right"></i> On CloudAI](#GC-AI)**{: .block}


| Cloud <br> Provider | Inst. <br> Type | Inst. <br> Name  |  GPU <br> Count | GPU <br> Type | xGPU <br> RAM | xGPU <br> Perf. |
|----------------|----------------------------|------------------|------------|----------|--------------------|----------------|
| Google Cloud   | GPU Compute Workload Addon | Any Machine Type | As desired | P4       | 8 (GB)             | 5.5 (TFLOPS)                              |
| Google Cloud   | GPU Compute Workload Addon | Any Machine Type | As desired | P100     | 16 (GB)            | 10.6 (TFLOPS)                             |
| Google Cloud   | GPU Compute Workload Addon | Any Machine Type | As desired | T4       | 16 (GB)            | 8.1 (TFLOPS)                              |
| Google Cloud   | GPU Compute Workload Addon | Any Machine Type | As desired | V100     | 16 (GB)            | 14.1 (TFLOPS)                             |
| Google Cloud   | A2                         | TBD \- In beta   | As desired | A100     | 40 (GB)            | 19.5 (TFLOPS)                             |
{: .cloud-table}

**[Jump to Top <i class="fad fa-chevron-double-up"></i>](#deploy)**

{% endcapture %}

{% include slopecap.html
    background="background-gray"
    position="top"
    slope="down"
%}
{% include section-single.html
    background="background-gray"
    padding-top="3em" padding-bottom="3em"
    content-single=gcp_intro
%}
{% include slopecap.html
    background="background-gray"
    position="bottom"
    slope="up"
%}

{% capture gc_single %}

## <i class="fab fa-google"></i> Google Single Instance
RAPIDS can be deployed on Google Cloud as a single instance:

**1. Create.** Create a Project in your Google Cloud account.

**2. Launch VM.** See the introduction section for a list of supported GPUs. We recommend using an image that already includes prerequisites such as drivers and docker, such as the **[NVIDIA GPU-Optimized Image for Deep Learning, ML & HPC VM](https://console.cloud.google.com/marketplace/details/nvidia-ngc-public/nvidia_gpu_cloud_image?supportedpurview=project)** image.

**3. Drivers.** Enter Y (Yes) when asked if you would like to download the latest NVIDIA drivers.

**4. Permissions.** **[Setup Docker user permission.](https://docs.docker.com/engine/install/linux-postinstall/)**

**5. Install.** **[Install RAPIDS docker image](https://rapids.ai/start.html)**. The docker container can be customized by using the options provided in the **[Getting Started](https://rapids.ai/start.html)** page of RAPIDS. Example of an image that can be used is provided below:
```shell
>>> docker pull rapidsai/rapidsai:cuda10.2-runtime-ubuntu18.04-py3.7
>>> docker run --gpus all --rm -it -p 8888:8888 -p 8787:8787 -p 8786:8786 \
    rapidsai/rapidsai:cuda10.2-runtime-ubuntu18.04-py3.7
```
{: .margin-bottom-3em}

**6. Test RAPIDS.** The above command should start your docker container. To test the container, start a python instance and then import any one of the RAPIDS libraries in it.

**[Jump to Top <i class="fad fa-chevron-double-up"></i>](#deploy)**

{% endcapture %}

{% capture gc_dask %}
## <i class="fab fa-google"></i> Google Cluster via Dask (Dataproc)

RAPIDS can be deployed on Google Cloud Dataproc using Dask. We have **[helper scripts and detailed instructions](https://github.com/GoogleCloudDataproc/initialization-actions/tree/master/rapids)** to help.

**1. Create Dataproc cluster with Dask RAPIDS.** Use the gcloud command to create a new cluster with the below initialization action. Because of an Anaconda version conflict, script deployment on older images is slow, we recommend using Dask with Dataproc 2.0+.
```shell
>>> GCS_BUCKET=[BUCKET_NAME]
>>> CLUSTER_NAME=[CLUSTER_NAME]
>>> REGION=[REGION]
>>> gcloud dataproc clusters create $CLUSTER_NAME \
    --region $REGION \
    --image-version 1.4-ubuntu18 \
    --master-machine-type n1-standard-32 \
    --master-accelerator type=nvidia-tesla-t4,count=4 \
    --worker-machine-type n1-standard-32 \
    --worker-accelerator type=nvidia-tesla-t4,count=4 \
    --optional-components=ANACONDA \
    --initialization-actions gs://goog-dataproc-initialization-actions-${REGION}/gpu/install_gpu_driver.sh,gs://goog-dataproc-initialization-actions-${REGION}/rapids/rapids.sh \
    --initialization-action-timeout=60m \
    --metadata gpu-driver-provider=NVIDIA,rapids-runtime=DASK \
    --enable-component-gateway
```
[BUCKET_NAME] = name of the bucket to use. <br>
[CLUSTER_NAME] = name of the cluster. <br>
[REGION] = name of region where cluster is to be created.
{: .margin-bottom-3em}

**2. Run Dask RAPIDS Workload.** Once the cluster has been created, the Dask scheduler listens for workers on port 8786, and its status dashboard is on port 8787 on the Dataproc master node. To connect to the Dask web interface, you will need to create an SSH tunnel as described in the **[Dataproc web interfaces documentation.](https://cloud.google.com/dataproc/docs/concepts/accessing/cluster-web-interfaces)** You can also connect using the Dask Client Python API from a Jupyter notebook, or from a Python script or interpreter session.

For more, see our **[detailed instructions and helper scripts.](https://github.com/GoogleCloudDataproc/initialization-actions/tree/master/rapids)**


**[Jump to Top <i class="fad fa-chevron-double-up"></i>](#deploy)**

{% endcapture %}

{% capture gc_kub %}
## <i class="fab fa-google"></i> Google Cluster via Kubernetes

RAPIDS can be deployed in a Kubernetes cluster on GCP. For more information, see the **[detailed instructions and helm charts.](https://helm.rapids.ai/docs/csp.html)**

**1. Install.** Install and configure dependencies in your local environment: **[kubectl, helm, gcloud.](https://helm.rapids.ai/docs/csp.html)**

**2. Configure cloud:**
```shell
>>> gcloud init
```
{: .margin-bottom-3em}

**3. Set your default computer zone:**
```shell
>>> gcloud config set compute/zone [REGION]
```
{: .margin-bottom-3em}

**4. [Create the cluster](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create):**
```shell
>>> gcloud container clusters create \
    rapids \
    --machine-type n1-standard-4 \
    --accelerator type=[GPU_TYPE],count=[NUM_GPU] \
    --region [REGION] \
    --node-locations [NODE_REGION] \
    --num-nodes [NUM_NODES] \
    --min-nodes 0 \
    --max-nodes [MAX_NODES] \
    --enable-autoscaling
```
[GPU_TYPE] = the type of GPU. See the introduction section for a list of supported GPU types. Ex. `nvidia-tesla-v100`.<br>
[NUM_GPU] = the number of GPUs. <br>
[NODE_REGION] = The node locations to be used in the default regions. Ex. `us-west1-b` <br>
[NUM_NODES] = number of nodes to be created in each of the cluster's zones. <br>
[MAX_NODES] = Maximum number of nodes to which the node pool specified by `--node-pool` (or default node pool if unspecified) can scale.


Example:
```shell
>>> gcloud container clusters create \
    rapids \
    --machine-type n1-standard-4 \
    --accelerator type=nvidia-tesla-v100,count=2 \
    --region us-west1 \
    --node-locations us-west1-a,us-west1-b \
    --num-nodes 1 \
    --min-nodes 0 \
    --max-nodes 4 \
    --enable-autoscaling
```
{: .margin-bottom-3em}
**5. Update local kubectl:**
```shell
>>> gcloud container clusters get-credentials rapids
```
{: .margin-bottom-3em}

**6. Install kubectl GPU add on:**
```shell
>>> kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/container-engine-accelerators/master/nvidia-driver-installer/cos/daemonset-preloaded.yaml
```
{: .margin-bottom-3em}

**7. Install RAPIDS helm repo:**
```shell
>>> helm repo add rapidsai https://helm.rapids.ai
>>> helm repo update
```
{: .margin-bottom-3em}

**8. Install the helm chart:**
```shell
>>> helm install rapidstest rapidsai/rapidsai
```
{: .margin-bottom-3em}

**9. Access your cluster:**
```shell
>>> kubectl get svc
NAME                 TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)                       AGE
kubernetes           ClusterIP      10.100.0.1       <none>        443/TCP                       14m
rapidsai-jupyter     LoadBalancer   10.100.208.179   1.2.3.4       80:32332/TCP                  3m30s
rapidsai-scheduler   LoadBalancer   10.100.19.121    5.6.7.8       8786:31779/TCP,80:32011/TCP   3m30s
```
{: .margin-bottom-3em}

To run notebooks on jupyter in your browser, visit the external IP of rapidsai-jupyter.


**[Jump to Top <i class="fad fa-chevron-double-up"></i>](#deploy)**

{% endcapture %}

{% capture gc_ai %}
## <i class="fab fa-google"></i> Google CloudAI

RAPIDS can be deployed on Google’s CloudAI platform. This deployment can range from a simple pre-made notebook (instructions below!) all the way up to a custom training container and HPO job. For more, see our **[detailed instructions and helper scripts.](https://github.com/rapidsai/cloud-ml-examples/tree/main/gcp)**

**1. Login.** Log into your GCP console.

**2. Select.** Select AI-Platform, then Notebooks.

**3. Create and Run.** Select a "Create new notebook" and select the RAPIDS XGBoost variant (comes with Conda installed):
- Select 'install gpu driver for me'
- Select 'customize'
- Pick the CUDA variant you want (10.1, 10.0, etc..)
- Select a GPU type
- Select the number of GPUs
- Launch your notebook service

**4. Run Script.** Once JupyterLab is running:
- Open a new terminal
- Copy the `rapids-py37-kernel.sh` GCP script into the local environment.
- Run the script
- Once completed, you will have a new kernel in your jupyter notebooks called `rapids_py37` which will have RAPIDS installed.

For more details, or for other ways to deploy on Google CloudAI, see the **[detailed instructions and helper scripts.](https://github.com/rapidsai/cloud-ml-examples/tree/main/gcp)**


**[Jump to Top <i class="fad fa-chevron-double-up"></i>](#deploy)**

{% endcapture %}
<div id="GC-single"></div>
{% include section-single.html
    background="background-white"
    padding-top="6em" padding-bottom="0em"
    content-single=gc_single
%}
<div id="GC-Dask"></div>
{% include section-single.html
    background="background-white"
    padding-top="3em" padding-bottom="0em"
    content-single=gc_dask
%}
<div id="GC-Kubernetes"></div>
{% include section-single.html
    background="background-white"
    padding-top="3em" padding-bottom="0em"
    content-single=gc_kub
%}
<div id="GC-AI"></div>
{% include section-single.html
    background="background-white"
    padding-top="3em" padding-bottom="10em"
    content-single=gc_ai
%}


{% capture end_bottom %}
# TRY RAPIDS in the Cloud
{: .section-title-full .text-white}

{% endcapture %}
{% include slopecap.html
    background="background-darkpurple"
    position="top"
    slope="down"
%}
{% include section-single.html
    background="background-darkpurple"
    padding-top="0em" padding-bottom="0em"
    content-single=end_bottom
%}
{% include cta-footer.html
    name="Experience Data Science on GPUs with RAPIDS"
    tagline=""
    button="GET STARTED"
    link="start.html"
%}
