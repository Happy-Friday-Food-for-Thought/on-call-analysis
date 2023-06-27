# Build a data-driven on-call workflow with on-call analysis tools
![alt text](cover.png)

This repo contains the code and the data to reproduce the analysis described in this [blog post](https://blog.developer.adobe.com/creating-a-thriving-on-call-engineering-workflow-by-embracing-healthy-team-habits-f05841e62ea1).


## Prerequisites

- Install a python & poetry (steps below using the excellent [asdf](https://asdf-vm.com/) version manager)

```bash
asdf plugin add python
asdf install python latest
pip install poetry
```

- Install the dependencies and create the venv

```
poetry install
```

- Get some help

```
poetry run oncall-analysis pagerduty --help
Usage: oncall-analysis pagerduty [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
    analytics      Get analytics data in the data/analytics.csv file for...
    incidents-log  Get incident log data in the data/incident_log.json file...
```

- Get analytics data

```
poetry run oncall-analysis pagerduty analytics --start-date 2023-01-01
```

- Or the log data

```
poetry run oncall-analysis pagerduty incidents-log --start-date 2023-01-01
```

- Fire up a notebook

```
poetry run jupyter-lab
```

and play with the notebooks

- [Analytics.ipynb](Analytics.ipynb) - plot interactive on call stats
- [Clustering.ipynb](Clustering.ipynb) - cluster related incidents together using K-Means