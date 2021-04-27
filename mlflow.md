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