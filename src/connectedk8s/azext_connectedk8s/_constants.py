# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


# pylint: disable=line-too-long

Distribution_Enum_Values = [
    "generic",
    "openshift",
    "rancher_rke",
    "kind",
    "k3s",
    "minikube",
    "gke",
    "eks",
    "aks",
    "aks_management",
    "aks_workload",
    "capz",
    "aks_engine",
    "tkg",
    "canonical",
    "karbon",
    "aks_edge_k3s",
    "aks_edge_k8s",
]
Public_Cloud_Distribution_List = ["gke", "eks", "aks"]
Infrastructure_Enum_Values = [
    "generic",
    "azure",
    "aws",
    "gcp",
    "azure_stack_hci",
    "azure_stack_hub",
    "azure_stack_edge",
    "vsphere",
    "windows_server",
    "Windows 11 Enterprise",
    "Windows 11 Enterprise N",
    "Windows 11 IoT Enterprise",
    "Windows 11 Pro",
    "Windows 10 Enterprise",
    "Windows 10 Enterprise N",
    "Windows 10 Enterprise LTSC 2021",
    "Windows 10 Enterprise N LTSC 2021",
    "Windows 10 IoT Enterprise",
    "Windows 10 IoT Enterprise LTSC 2021",
    "Windows 10 Pro",
    "Windows 10 Enterprise LTSC 2019",
    "Windows 10 Enterprise N LTSC 2019",
    "Windows 10 IoT Enterprise LTSC 2019",
    "Windows Server 2022",
    "Windows Server 2022 Datacenter",
    "Windows Server 2022 Standard",
    "Windows Server 2019",
    "Windows Server 2019 Datacenter",
    "Windows Server 2019 Standard",
    "Windows 10 IoT Enterprise",
    "LTSCWindows 10 Enterprise LTSC",
]
AHB_Enum_Values = ["True", "False", "NotApplicable"]
Feature_Values = ["cluster-connect", "azure-rbac", "custom-locations"]
CRD_FOR_FORCE_DELETE = [
    "arccertificates.clusterconfig.azure",
    "azureclusteridentityrequests.clusterconfig.azure",
    "azureextensionidentities.clusterconfig.azure",
    "connectedclusters.arc.azure",
    "customlocationsettings.clusterconfig.azure",
    "extensionconfigs.clusterconfig.azure",
    "gitconfigs.clusterconfig.azure",
]
Helm_Install_Release_Userfault_Messages = [
    "forbidden",
    "timed out waiting for the condition",
    "connection refused",
]
Custom_Locations_Provider_Namespace = "Microsoft.ExtendedLocation"
Connected_Cluster_Provider_Namespace = "Microsoft.Kubernetes"
Kubernetes_Configuration_Provider_Namespace = "Microsoft.KubernetesConfiguration"
Hybrid_Compute_Provider_Namespace = "Microsoft.HybridCompute"
Arc_Namespace = "azure-arc"
Azure_PublicCloudName = "AZUREPUBLICCLOUD"
Azure_USGovCloudName = "AZUREUSGOVERNMENTCLOUD"
Azure_ChinaCloudName = "AZURECHINACLOUD"
Azure_DogfoodCloudName = "AZUREDOGFOOD"
PublicCloud_OriginalName = "AZURECLOUD"
MSI_Certificate_Secret_Name = "azure-identity-certificate"
KAP_Certificate_Secret_Name = "kube-aad-proxy-certificate"
USGovCloud_OriginalName = "AZUREUSGOVERNMENT"
Dogfood_RMEndpoint = "https://api-dogfood.resources.windows-int.net/"
Client_Request_Id_Header = "x-ms-client-request-id"
Default_Onboarding_Source_Tracking_Guid = "77ade16b-0f55-403b-b7d2-739554a897f2"
Custom_Access_Token_Env_Var_Sub_Id_Missing_Fault_Type = "Required environment variable SubscriptionId not set, for custom Azure access token"
Custom_Access_Token_Env_Var_Tenant_Id_Missing_Fault_Type = (
    "Required environment variable TenantId not set, for custom Azure access token"
)
Custom_Token_Env_Var_Sub_Id_Missing_Fault_Type = "Required environment variable 'AZURE_SUBSCRIPTION_ID' is not set, when using Custom Acces Token."
Release_Install_Namespace = "azure-arc-release"
Workload_Identity_Release_Name = "wiextension"
Workload_Identity_Release_Namespace = "arc-workload-identity"
Helm_Environment_File_Fault_Type = "helm-environment-file-error"
Invalid_Location_Fault_Type = "location-validation-error"
Location_Fetch_Fault_Type = "location-fetch-error"
Pls_Location_Mismatch_Fault_Type = "pls-location-mismatch-error"
Pls_Resource_Not_Found = "pls-resource-not-found"
Invalid_Argument_Fault_Type = "argument-validation-error"
Load_Kubeconfig_Fault_Type = "kubeconfig-load-error"
Read_ConfigMap_Fault_Type = "configmap-read-error"
Get_ResourceProvider_Fault_Type = "resource-provider-fetch-error"
Get_ConnectedCluster_Fault_Type = "connected-cluster-fetch-error"
Create_ConnectedCluster_Fault_Type = "connected-cluster-create-error"
Update_ConnectedCluster_Fault_Type = "connected-cluster-update-error"
Delete_ConnectedCluster_Fault_Type = "connected-cluster-delete-error"
Bad_DeleteRequest_Fault_Type = "bad-delete-request-error"
Cluster_Already_Onboarded_Fault_Type = "cluster-already-onboarded-error"
Resource_Already_Exists_Fault_Type = "resource-already-exists-error"
Resource_Does_Not_Exist_Fault_Type = "resource-does-not-exist-error"
Create_ResourceGroup_Fault_Type = "resource-group-creation-error"
Add_HelmRepo_Fault_Type = "helm-repo-add-error"
List_HelmRelease_Fault_Type = "helm-list-release-error"
KeyPair_Generate_Fault_Type = "keypair-generation-error"
PublicKey_Export_Fault_Type = "publickey-export-error"
PrivateKey_Export_Fault_Type = "privatekey-export-error"
Install_HelmRelease_Fault_Type = "helm-release-install-error"
Delete_HelmRelease_Fault_Type = "helm-release-delete-error"
Check_PodStatus_Fault_Type = "check-pod-status-error"
Kubernetes_Connectivity_FaultType = "kubernetes-cluster-connection-error"
Helm_Version_Fault_Type = "helm-not-updated-error"
Check_HelmVersion_Fault_Type = "helm-version-check-error"
Helm_Installation_Fault_Type = "helm-not-installed-error"
Check_HelmInstallation_Fault_Type = "check-helm-installed-error"
Get_HelmRegistery_Path_Fault_Type = "helm-registry-path-fetch-error"
Pull_HelmChart_Fault_Type = "helm-chart-pull-error"
Export_HelmChart_Fault_Type = "helm-chart-export-error"
Get_Kubernetes_Distro_Fault_Type = "kubernetes-get-distribution-error"
Get_Kubernetes_Namespace_Fault_Type = "kubernetes-get-namespace-error"
Get_Kubernetes_Helm_Release_Namespace_Fault_Type = (
    "kubernetes-get-helm-release-namespace-error"
)
Delete_Kubernetes_Helm_Release_Namespace_Fault_Type = (
    "kubernetes-delete-helm-release-namespace-error"
)
Update_Agent_Success = "Agents for Connected Cluster {} have been updated successfully"
Update_Agent_Failure = 'Error while updating agents. Please run "kubectl get pods -n azure-arc" to check the pods in case of timeout error. Error: {}'
Agent_State_Succeeded = "Succeeded"
Agent_State_Failed = "Failed"
Agent_State_Timeout = 15
Get_Credentials_Failed_Fault_Type = "failed-to-get-list-cluster-user-credentials"
Failed_To_Merge_Credentials_Fault_Type = "failed-to-merge-credentials"
Kubeconfig_Failed_To_Load_Fault_Type = "failed-to-load-kubeconfig-file"
Failed_To_Load_K8s_Configuration_Fault_Type = "failed-to-load-kubernetes-configuration"
Failed_To_Merge_Kubeconfig_File = "failed-to-merge-kubeconfig-file"
Download_Helm_Fault_Type = "helm-client-download-error"
Create_HelmExe_Fault_Type = "helm-client-create-error"
Extract_HelmExe_Fault_Type = "helm-client-extract-error"
DP_Health_Check_Fault_Type = "dp-health-check-error"
Different_Object_With_Same_Name_Fault_Type = "Kubeconfig has an object with same name"
Download_Exe_Fault_Type = (
    "Error while downloading client proxy executable from storage account"
)
Create_Directory_Fault_Type = (
    "Error while creating directory for placing the executable"
)
Remove_File_Fault_Type = "Error while deleting the specified file"
Run_Clientproxy_Fault_Type = "Error while starting client proxy process."
Post_Hybridconn_Fault_Type = (
    "Error while posting hybrid connection details to proxy process"
)
Post_RefreshToken_Fault_Type = (
    "Error while posting refresh token details to proxy process"
)
Merge_Kubeconfig_Fault_Type = "Error while merging kubeconfig."
Create_CSPExe_Fault_Type = "Error while creating csp executable"
Remove_Config_Fault_Type = "Error while removing old csp config"
Load_Creds_Fault_Type = "Error while loading accessToken.json"
Creds_NotFound_Fault_Type = "Credentials of user not found"
Create_Config_Fault_Type = "Error while creating config file for proxy"
Run_RefreshThread_Fault_Type = "Error while starting refresh thread"
Run_Check_CSP_Thread_Fault_Type = "Error while starting 'check csp thread'."
Proxy_Closed_Externally_Fault_Type = "Proxy closed externally."
Client_Proxy_Port_Fault_Type = "Client proxy port was in use."
Unsupported_Fault_Type = (
    "Error while checking operating system.Unsupported OS detected."
)
Helm_Unsupported_OS_Fault_Type = "helm-client-unsupported-os-error."
Port_Check_Fault_Type = "Error while checking if port is in use."
Proxy_Cert_Path_Does_Not_Exist_Fault_Type = "proxy-cert-path-does-not-exist-error"
Proxy_Cert_Path_Does_Not_Exist_Error = (
    "Proxy cert path {} does not exist. Please check the path provided"
)
Get_Kubernetes_Infra_Fault_Type = "kubernetes-get-infrastructure-error"
No_Param_Error = "No parameters were specified with update command. Please run az connectedk8s update --help to check parameters available for update"
Gateway_ArmId_Is_Invalid = "The provided Gateway ArmID in --gateway-resource-id  {} is invalid. Please provide a valid Gateway ArmID."
EnableProxy_Conflict_Error = "Conflict detected: --disable-proxy can not be set with --https-proxy, --http-proxy, --proxy-skip-range and --proxy-cert at the same time. Please run az connectedk8s update --help for more information about the parameters"
Manual_Upgrade_Called_In_Auto_Update_Enabled = (
    "Manual Upgrade was called while in auto_Update enabled mode"
)
Upgrade_Agent_Success = (
    "Agents for Connected Cluster {} have been upgraded successfully"
)
Upgrade_Agent_Failure = (
    'Error while upgrading agents. Please run "kubectl get pods -n azure-arc" to check the pods in case of '
    "timeout error. Error: {}"
)
Release_Namespace_Not_Found = "Error while getting azure-arc releasenamespace"
Get_Helm_Values_Failed = "Error while doing helm get values azure-arc"
Helm_Existing_User_Supplied_Value_Get_Fault = (
    "Error while loading the user supplied helm values"
)
Error_Flattening_User_Supplied_Value_Dict = (
    "Error while flattening the user supplied helm values dict"
)
Upgrade_RG_Cluster_Name_Conflict = (
    "The provided cluster name and rg correspond to different cluster"
)
Corresponding_CC_Resource_Deleted_Fault = (
    "CC resource corresponding to this cluster has been deleted by the customer"
)
Kubernetes_Node_Type_Fetch_Fault_OS = (
    "Error while trying to find a linux node for scheduling pods"
)
Kubernetes_Node_Type_Fetch_Fault_Arch = (
    "Error while trying to find an arm64 node for scheduling pods"
)
Linux_Node_Not_Exists = "Kubernetes cluster doesnt have linux node"
Operate_RG_Cluster_Name_Conflict = (
    "The provided cluster name and rg correspond to different cluster being operated on"
)
Custom_Locations_Registration_Check_Fault_Type = (
    "Error while checking resource provider registration of custom locations."
)
Custom_Locations_OID_Fetch_Fault_Type_CLOid_None = (
    "Error while fetching oid for custom locations. CL_Oid is None"
)
Custom_Locations_OID_Fetch_Fault_Type_Exception = (
    "Exception while fetching oid for custom locations."
)
Successfully_Enabled_Features = (
    "Successsfully enabled features: {} for the Connected Cluster {}"
)
Successfully_Disabled_Features = (
    "Successsfully disabled features: {} for the Connected Cluster {}"
)
Error_enabling_Features = (
    'Error while updating agents for enabling features. Please run "kubectl get pods -n azure-arc" to check the '
    "pods in case of timeout error. Error: {}"
)
Error_disabling_Features = (
    'Error while updating agents for disabling features. Please run "kubectl get pods -n '
    'azure-arc" to check the pods in case of timeout error. Error: {}'
)
Proxy_Kubeconfig_During_Deletion_Fault_Type = (
    "Encountered proxy kubeconfig during deletion."
)
Cannot_Create_ClusterRoleBindings_Fault_Type = (
    "Cannot create cluster role bindings on this Kubernets cluster"
)
CC_Provider_Namespace_Not_Registered_Fault_Type = (
    "Connected Cluster Provider MS.K8 namespace not registered"
)
Kubernetes_Configuration_Provider_Namespace_Not_Registered_Fault_Type = "Kubernetes Configuration Provider MS.KubernetesConfiguration namespace not registered"
HC_Provider_Namespace_Not_Registered_Fault_Type = (
    "Hybrid Compute Provider MS.HybridCompute namespace not registered"
)
Default_Namespace_Does_Not_Exist_Fault_Type = "The default namespace defined in the kubeconfig doesn't exist on the kubernetes cluster."
KAP_1P_Server_App_Scope = "6256c85f-0aad-4d50-b960-e6e9b21efe35/.default"
KAP_1P_Server_AppId = "6256c85f-0aad-4d50-b960-e6e9b21efe35"
Get_PublicKey_Info_Fault_Type = (
    "Error while fetching the PoP publickey information from client proxy"
)
PoP_Public_Key_Expried_Fault_Type = (
    "The PoP public key used to generate the at has expired"
)
Post_AT_To_ClientProxy_Failed_Fault_Type = "Failed to post access token to client proxy"
Kubectl_Get_Events_Failed_Fault_Type = "Error occured while doing kubectl get events"
Kubectl_Get_Secrets_Failed_Fault_Type = "Error occured while doing kubectl get secrets"
Fetch_Kubectl_Get_Secrets_Fault_Type = (
    "Exception occured while doing kubectl get secrets"
)
Helm_Values_Save_Failed_Fault_Type = (
    "Error occured while doing helm get values for azure-arc release"
)
Fetch_Helm_Values_Save_Failed_Fault_Type = (
    "Exception occured while doing helm get values for azure-arc release"
)
Wiextension_Helm_Values_Save_Failed_Fault_Type = (
    "Error occured while doing helm get values for wiextension release"
)
Fetch_Wiextension_Helm_Values_Save_Failed_Fault_Type = (
    "Exception occured while doing helm get values for wiextension release"
)
Metadata_CR_Save_Failed_Fault_Type = "Error occured while fetching metadata CR snapshot"
Fetch_Metadata_CR_Save_Failed_Fault_Type = (
    "Exception occured while fetching metadata CR snapshot"
)
Signingkey_CR_Save_Failed_Fault_Type = (
    "Error occured while fetching signingkey CR snapshot"
)
Fetch_Signingkey_CR_Save_Failed_Fault_Type = (
    "Exception occured while fetching signingkey CR snapshot"
)
KAP_CR_Save_Failed_Fault_Type = "Error occured while fetching KAP CR snapshot"
Fetch_KAP_CR_Save_Failed_Fault_Type = "Exception occured while fetching KAP CR snapshot"
Fetch_Arc_Agent_Logs_Failed_Fault_Type = "Error occured in arc agents logger"
Fetch_Arc_Agents_Events_Logs_Failed_Fault_Type = (
    "Error occured in arc agents events logger"
)
Fetch_Arc_Deployment_Logs_Failed_Fault_Type = "Error occured in deployments logger"
Fetch_Arc_Workload_Identity_Pod_Logs_Failed_Fault_Type = (
    "Error occured in arc agents logger"
)
Fetch_Arc_Workload_Identity_Events_Logs_Failed_Fault_Type = (
    "Error occured in arc agents events logger"
)
Fetch_Arc_Workload_Identity_Deployment_Logs_Failed_Fault_Type = (
    "Error occured in deployments logger"
)
Agent_State_Check_Fault_Type = "Error occured while performing the agent state check"
Agent_Version_Check_Fault_Type = (
    "Error occured while performing the agent version check"
)
Diagnoser_Job_Failed_Fault_Type = "Error while executing Diagnoser Job"
Diagnoser_Container_Check_Failed_Fault_Type = (
    "Error occured while performing the diagnoser container checks"
)
Cluster_DNS_Check_Fault_Type = "Error occured while performing cluster DNS check"
Outbound_Connectivity_Check_Fault_Type = (
    "Error occured while performing outbound connectivity check in the cluster"
)
Outbound_Connectivity_Failed_Fault_Type = (
    "Outbound network connectivity failed in cluster diagnostic checks"
)
DNS_Failed_Fault_Type = "DNS resolution failed in cluster diagnostic checks"
MSI_Cert_Check_Fault_Type = (
    "Error occurred while trying to perform MSI ceritificate presence check"
)
Cluster_Security_Policy_Check_Fault_Type = (
    "Error occured while performing cluster security policy check"
)
KAP_Cert_Check_Fault_Type = (
    "Error occurred while trying to perform KAP ceritificate presence check"
)
MSI_Cert_Expiry_Check_Fault_Type = (
    "Error occured while trying to perform the MSI cert expiry check"
)
Diagnostics_Folder_Creation_Failed_Fault_Type = (
    "Error while trying to create diagnostic logs folder"
)
Describe_Stuck_Agents_Fault_Type = (
    "Error occured while storing the description of non running agents"
)
No_Storage_Space_Available_Fault_Type = "No space left on device"
Connected_Cluster_Resource_Fetch_Fault_Type = (
    "Error occured while fetching the Get output of connected cluster"
)
Diagnoser_Result_Fault_Type = "Error while storing the diagnoser results"
Kubectl_Cluster_Info_Failed_Fault_Type = "Error while doing kubectl cluster-info"
Fetch_Kubectl_Cluster_Info_Fault_Type = "Error occured while fetching cluster-info"
Fetch_Kubectl_Cluster_Info = "kubectl_cluster_info"
Operation_Not_Supported_Fault_Type = (
    "This CLI version does not support this operation for Agents older than v1.14"
)
Failed_To_Change_Telemetry_Push_Interval = (
    "Failed to change the telemetry push interval to 1 hr"
)
Diagnostic_Check_Passed = "Passed"
Diagnostic_Check_Failed = "Failed"
Diagnostic_Check_Incomplete = "Incomplete"
# Name of the checks and operations
Retrieve_Arc_Agents_Event_Logs = "retrieved_arc_agents_event_logs"
Retrieve_Arc_Agents_Logs = "retrieved_arc_agents_logs"
Retrieve_Deployments_Logs = "retrieved_deployments_logs"
Retrieve_Arc_Workload_Identity_Events_Logs = (
    "retrieved_arc_workload_identity_event_logs"
)
Retrieve_Arc_Workload_Identity_Pod_Logs = "retrieved_arc_workload_identity_pod_logs"
Retrieve_Arc_Workload_Identity_Deployments_Logs = (
    "retrieved_arc_workload_identity_deployments_logs"
)
Fetch_Connected_Cluster_Resource = "fetch_connected_cluster_resource"
Storing_Diagnoser_Results_Logs = "storing_diagnoser_results_logs"
MSI_Cert_Expiry_Check = "msi_cert_expiry_check"
KAP_Security_Policy_Check = "kap_security_policy_check"
KAP_Cert_Check = "kap_cert_check"
Diagnoser_Check = "diagnoser_check"
MSI_Cert_Check = "msi_cert_check"
Agent_Version_Check = "agent_version_check"
Arc_Agent_State_Check = "arc_agent_state_check"
# Diagnoser files name
Arc_Agents_Logs = "arc_agents_logs"
Arc_Deployment_Logs = "arc_deployment_logs"
Arc_Diagnostic_Logs = "arc_diagnostic_logs"
Arc_Workload_Identity_Pod_Logs = "arc_workload_identity_pod_logs"
Arc_Workload_Identity_Deployment_Logs = "arc_workload_identity_deployment_logs"
Pre_Onboarding_Check_Logs = "pre_onboarding_check_logs"
Pre_Onboarding_Helm_Charts_Folder_Name = "PreOnboardingChecksCharts"
Pre_Onboarding_Helm_Charts_Release_Name = "clusterdiagnosticchecks"
Describe_Non_Ready_Arc_Agents = "describe_non_ready_arc_agents"
Agent_State = "agent_state.txt"
Arc_Agents_Events = "arc_agent_events.txt"
Arc_Workload_Identity_Events = "arc_workload_identity_events.txt"
Diagnoser_Results = "diagnoser_output.txt"
Connected_Cluster_Resource = "connected_cluster_resource_snapshot.txt"
DNS_Check = "dns_check.txt"
K8s_Cluster_Info = "k8s_cluster_info.txt"
Outbound_Network_Connectivity_Check = "outbound_network_connectivity_check.txt"
Outbound_Network_Connectivity_Check_for_onboarding = (
    "outbound_network_connectivity_check_for_onboarding.txt"
)
Outbound_Network_Connectivity_Check_for_cluster_connect = (
    "outbound_network_connectivity_check_for_cluster_connect.txt"
)
Events_of_Incomplete_Diagnoser_Job = "diagnoser_failure_events.txt"
Wiextension_Helm_Values = "helm_values_arc_workload_identity.txt"
SigningKey_CR_Snapshot = "signingkey_cr_snapshot.txt"

# Connect Precheck Diagnoser constants
Cluster_Diagnostic_Checks_Job_Registry_Path = (
    "azurearck8s/helmchart/stable/clusterdiagnosticchecks:0.2.2"
)
Cluster_Diagnostic_Checks_Helm_Install_Failed_Fault_Type = (
    "Error while installing cluster diagnostic checks helm release"
)
Cluster_Diagnostic_Checks_Execution_Failed_Fault_Type = (
    "Error occured while executing cluster diagnostic checks"
)
Cluster_Diagnostic_Checks_Release_Cleanup_Failed = (
    "Error occured while cleaning up the cluster diagnostic checks helm release"
)
Cluster_Diagnostic_Checks_Job_Not_Scheduled = (
    "Unable to schedule cluster-diagnostic-checks job"
)
Cluster_Diagnostic_Checks_Job_Not_Complete = (
    "Unable to complete cluster-diagnostic-checks job after scheduling"
)
Pre_Onboarding_Diagnostic_Checks_Execution_Failed = (
    "Exception occured while trying to execute pre-onboarding diagnostic checks"
)
Outbound_Connectivity_Check_Failed = "Outbound network connectivity check failed"
Outbound_Connectivity_Check_Failed_For_Onboarding = (
    "Outbound network connectivity check failed for onboarding"
)
DNS_Check_Failed = "DNS Resolution failed"
Cluster_Diagnostic_Prechecks_Failed = "Cluster diagnostic prechecks failed"
Cluster_Diagnostic_Prechecks_Incomplete = (
    "Cluster diagnostic prechecks failed to complete"
)
Cluster_Diagnostic_Checks_Pod_Description_Save_Failed = (
    "Failed to save cluster diagnostic checks pod description"
)
Cluster_Diagnostic_Checks_Job_Log_Save_Failed = (
    "Failed to save cluster diagnostic checks job log"
)

Manual_Custom_Location_Oid_Warning = """Important! Custom Location feature enablement can't be validated when using a manually provided OID. If the custom location feature is not enabled, you may encounter an error when creating the custom location.
After creating the custom location, run `az customlocation show` and check that ProvisioningState is Succeeded. If ProvisoningState is Failed, then re-try this command with a  valid custom location OID to enable the feature.
For guidance, refer to: https://aka.ms/enable-customlocation"""

Custom_Location_Enable_Failed_warning = """Important! Custom Location feature wasn't enabled due to insufficient privileges on the Service Principal Name. If the custom location feature is not enabled, you will encounter an error when creating the custom location. Refer to: https://aka.ms/enable-cl-spn"""

KubeApi_Connectivity_Failed_Warning = """Unable to verify connectivity to the Kubernetes cluster.
Please check https://learn.microsoft.com/en-us/azure/azure-arc/kubernetes/diagnose-connection-issues"""

Kubeconfig_Load_Failed_Warning = """Unable to load the kubeconfig file.
Please check https://learn.microsoft.com/en-us/azure/azure-arc/kubernetes/diagnose-connection-issues#is-kubeconfig-pointing-to-the-right-cluster"""

Cluster_Already_Onboarded_Error = """The kubernetes cluster is already onboarded.
Please check if the Kubeconfig is pointing to the correct cluster using  command: kubectl config current-context."""

# Diagnostic Results Name
Outbound_Connectivity_Check_Result_String = "Outbound Network Connectivity"
Outbound_Connectivity_Check_Failed_For_Cluster_Connect = (
    "Outbound network connectivity check failed for Cluster Connect"
)
DNS_Check_Result_String = "DNS Result:"
AZ_CLI_ADAL_TO_MSAL_MIGRATE_VERSION = "2.30.0"
CLIENT_PROXY_VERSION = "1.3.029301"
CLIENT_PROXY_FOLDER = ".clientproxy"
API_SERVER_PORT = 47011
CLIENT_PROXY_PORT = 47010
CLIENTPROXY_CLIENT_ID = "04b07795-8ddb-461a-bbee-02f9e1bf7b46"
API_CALL_RETRIES = 12
DEFAULT_REQUEST_TIMEOUT = 10  # seconds
CSP_REFRESH_TIME = 300

# Default timeout in seconds for Onboarding Helm Install
DEFAULT_MAX_ONBOARDING_TIMEOUT_HELMVALUE_SECONDS = "1200"

# URL constants
CLIENT_PROXY_MCR_TARGET = "azureconnectivity/proxy"
HELM_MCR_URL = "azurearck8s/helm"
HELM_VERSION = "v3.12.2"
Download_And_Install_Kubectl_Fault_Type = "Failed to download and install kubectl"
Azure_Access_Token_Variable = "AZURE_ACCESS_TOKEN"
Provisioned_Cluster_Kind = "provisionedcluster"
Helm_Values_Fetch_isProxyEnabled_Failed_Fault_Type = (
    "Helm Values Fetch isProxyEnabled Failed"
)
Helm_Values_Fetch_isCustomCert_Failed_Fault_Type = (
    "Helm Values Fetch isCustomCert Failed"
)
Helm_Values_Fetch_proxyCert_Failed_Fault_Type = "Helm Values Fetch proxyCert Failed"
Doc_Onboarding_PreRequisites_Url = (
    "'https://learn.microsoft.com/en-us/azure/azure-arc/kubernetes/quickstart-"
    "connect-cluster?tabs=azure-cli%2Cazure-cloud#prerequisites'"
)
Doc_Network_Requirements_Url = "https://learn.microsoft.com/en-us/azure/azure-arc/kubernetes/network-requirements?tabs=azure-cloud"
Doc_Quick_Start_NW_Requirements_Url = (
    "https://learn.microsoft.com/en-us/azure/azure-arc/kubernetes/quickstart-connect-cluster?"
    "tabs=azure-cli#meet-network-requirements"
)
Doc_Quick_Start_Outbound_Proxy_Url = (
    "https://learn.microsoft.com/en-us/azure/azure-arc/kubernetes/quickstart-connect-cluster?"
    "tabs=azure-cli#connect-using-an-outbound-proxy-server"
)
Doc_Provisioned_Cluster_Delete_Url = "https://learn.microsoft.com/en-us/cli/azure/aksarc?view=azure-cli-latest#az-aksarc-delete"
Doc_Provisioned_Cluster_Update_Url = "https://learn.microsoft.com/en-us/cli/azure/aksarc?view=azure-cli-latest#az-aksarc-update"
Doc_Provisioned_Cluster_Upgrade_Url = "https://learn.microsoft.com/en-us/cli/azure/aksarc?view=azure-cli-latest#az-aksarc-upgrade"
Doc_Agent_Version_Support_Policy_Url = "https://learn.microsoft.com/en-us/azure/azure-arc/kubernetes/agent-upgrade#version-support-policy"

# Acceptable states for required RP registrations to be in
#
# "Application code shouldn't block the creation of resources for a resource provider that is in the registering state."
# See https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/resource-providers-and-types#register-resource-provider
allowed_rp_registration_states = ["Registering", "Registered"]
