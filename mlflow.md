Things I liked
https://www.mlflow.org/docs/latest/model-registry.html

* Registry has queryable API in Python so no dual language problem. Any REST SDK could use some Python bindings on top
Worth looking into doing this for other offerings https://realpython.com/api-integration-in-python/
* Format to describe ML projects including environment ML code in a Python file
* Kubernetes support is experimental: https://www.mlflow.org/docs/latest/projects.html - (Kubernetes runs Docker on multiple nodes)
* TODO: example of multistage workflow https://github.com/mlflow/mlflow/tree/master/examples/multistep_workflow
* Filees have their source, metrics and artifacts and can store them all in a SQL database which is helpful to compare experiments and their runs
* Projects contain their docker environment, dependencies data etc.
* Plugin system vs handler system: https://www.mlflow.org/docs/latest/plugins.html

## Kubernetes
Pods are the smallest deployable unit
Each pod has a shared context of linux namespaces, cgroups and other facets of isolation. 
A pod is like a group of docker container with shared namespaces and shared filesystem

https://prometheus.io/ - monitoring and alerting for time series data
https://grafana.com/ - dashboards on top of prometheus



## References I liked
* https://airflow.apache.org/docs/apache-airflow/stable/tutorial.html#setting-up-dependencies -> The simple code to set upstream vs downstream tasks is so nice, much better than visual languages for this stuff
* https://codelabs.developers.google.com/codelabs/cloud-kubeflow-minikf-kale#2 -> from GCP Kubeflow to notebook using Kale and minkf
* https://www.kubeflow.org/docs/components/notebooks/setup/
* Can make different cells part of a DAG -> https://codelabs.developers.google.com/codelabs/cloud-kubeflow-minikf-kale#3



But in general notebook story for this stuff isn't great, need to use GCP for Kubeflow or AWS for airflow for ideal user experience

## Kubernetes in action book summary
We used to have seperate ops teams but now it's the same skillset
Managing hundreds of microservices helps you scale easier but much harder to manage manually

Kubernetes abstracts away hardware and cloud providers

Kubernetes is like a distributed OS where apps interact with it directly

Has features for service discovery (manual configs is a pain), horizontal scaling, load balancing, self healing and leader election

Takes care of running different microapps concurrently on the same machine to increase hardware utilization or increasing resources per app if it's overloaded

Master nodes Control plane components which control the cluster which worker nodes in workload plane where apps are run



## Torchserve handlers
Torchserve handler read more about it https://github.com/pytorch/serve/blob/38eed4703664175160304b9e9880fa40d8481f11/ts/torch_handler/base_handler.py#L17

Can do lots of stuff here with these handlers support online training or do whatever - main constraint seems to be torchscripting

Handler should do some more logging of performance