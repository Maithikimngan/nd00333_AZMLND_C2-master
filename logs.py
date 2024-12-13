from azureml.core import Workspace
from azureml.core.webservice import Webservice

subscription_id = "f5091c60-1c3c-430f-8d81-d802f6bf2414"
resource_group = "aml-quickstarts-270582"
workspace_name = "quick-starts-ws-270582"


# Requires the config to be downloaded first to the current working directory
ws = Workspace.from_config(path="./config.json")

# Set with the deployment name
name = "best-model"

# load existing web service
service = Webservice(name=name, workspace=ws)

# enable application insight
service.update(enable_app_insights=True)

logs = service.get_logs()

for line in logs.split('\n'):
    print(line)
