# Go API client for flyteadmin

No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

## Overview
This API client was generated by the [swagger-codegen](https://github.com/swagger-api/swagger-codegen) project.  By using the [swagger-spec](https://github.com/swagger-api/swagger-spec) from a remote server, you can easily generate an API client.

- API version: version not set
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.GoClientCodegen

## Installation
Put the package under your project folder and add the following in import:
```golang
import "./flyteadmin"
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AdminServiceApi* | [**CreateExecution**](docs/AdminServiceApi.md#createexecution) | **Post** /api/v1/executions | 
*AdminServiceApi* | [**CreateLaunchPlan**](docs/AdminServiceApi.md#createlaunchplan) | **Post** /api/v1/launch_plans | 
*AdminServiceApi* | [**CreateNodeEvent**](docs/AdminServiceApi.md#createnodeevent) | **Post** /api/v1/events/nodes | 
*AdminServiceApi* | [**CreateTask**](docs/AdminServiceApi.md#createtask) | **Post** /api/v1/tasks | 
*AdminServiceApi* | [**CreateTaskEvent**](docs/AdminServiceApi.md#createtaskevent) | **Post** /api/v1/events/tasks | 
*AdminServiceApi* | [**CreateWorkflow**](docs/AdminServiceApi.md#createworkflow) | **Post** /api/v1/workflows | 
*AdminServiceApi* | [**CreateWorkflowEvent**](docs/AdminServiceApi.md#createworkflowevent) | **Post** /api/v1/events/workflows | 
*AdminServiceApi* | [**GetActiveLaunchPlan**](docs/AdminServiceApi.md#getactivelaunchplan) | **Get** /api/v1/active_launch_plans/{id.project}/{id.domain}/{id.name} | 
*AdminServiceApi* | [**GetExecution**](docs/AdminServiceApi.md#getexecution) | **Get** /api/v1/executions/{id.project}/{id.domain}/{id.name} | 
*AdminServiceApi* | [**GetExecutionData**](docs/AdminServiceApi.md#getexecutiondata) | **Get** /api/v1/data/executions/{id.project}/{id.domain}/{id.name} | 
*AdminServiceApi* | [**GetLaunchPlan**](docs/AdminServiceApi.md#getlaunchplan) | **Get** /api/v1/launch_plans/{id.project}/{id.domain}/{id.name}/{id.version} | 
*AdminServiceApi* | [**GetNamedEntity**](docs/AdminServiceApi.md#getnamedentity) | **Get** /api/v1/named_entities/{resource_type}/{id.project}/{id.domain}/{id.name} | 
*AdminServiceApi* | [**GetNodeExecution**](docs/AdminServiceApi.md#getnodeexecution) | **Get** /api/v1/node_executions/{id.execution_id.project}/{id.execution_id.domain}/{id.execution_id.name}/{id.node_id} | 
*AdminServiceApi* | [**GetNodeExecutionData**](docs/AdminServiceApi.md#getnodeexecutiondata) | **Get** /api/v1/data/node_executions/{id.execution_id.project}/{id.execution_id.domain}/{id.execution_id.name}/{id.node_id} | 
*AdminServiceApi* | [**GetTask**](docs/AdminServiceApi.md#gettask) | **Get** /api/v1/tasks/{id.project}/{id.domain}/{id.name}/{id.version} | 
*AdminServiceApi* | [**GetTaskExecution**](docs/AdminServiceApi.md#gettaskexecution) | **Get** /api/v1/task_executions/{id.node_execution_id.execution_id.project}/{id.node_execution_id.execution_id.domain}/{id.node_execution_id.execution_id.name}/{id.node_execution_id.node_id}/{id.task_id.project}/{id.task_id.domain}/{id.task_id.name}/{id.task_id.version}/{id.retry_attempt} | 
*AdminServiceApi* | [**GetTaskExecutionData**](docs/AdminServiceApi.md#gettaskexecutiondata) | **Get** /api/v1/data/task_executions/{id.node_execution_id.execution_id.project}/{id.node_execution_id.execution_id.domain}/{id.node_execution_id.execution_id.name}/{id.node_execution_id.node_id}/{id.task_id.project}/{id.task_id.domain}/{id.task_id.name}/{id.task_id.version}/{id.retry_attempt} | 
*AdminServiceApi* | [**GetWorkflow**](docs/AdminServiceApi.md#getworkflow) | **Get** /api/v1/workflows/{id.project}/{id.domain}/{id.name}/{id.version} | 
*AdminServiceApi* | [**ListActiveLaunchPlans**](docs/AdminServiceApi.md#listactivelaunchplans) | **Get** /api/v1/active_launch_plans/{project}/{domain} | 
*AdminServiceApi* | [**ListExecutions**](docs/AdminServiceApi.md#listexecutions) | **Get** /api/v1/executions/{id.project}/{id.domain} | 
*AdminServiceApi* | [**ListLaunchPlanIds**](docs/AdminServiceApi.md#listlaunchplanids) | **Get** /api/v1/launch_plan_ids/{project}/{domain} | 
*AdminServiceApi* | [**ListLaunchPlans**](docs/AdminServiceApi.md#listlaunchplans) | **Get** /api/v1/launch_plans/{id.project}/{id.domain}/{id.name} | 
*AdminServiceApi* | [**ListLaunchPlans2**](docs/AdminServiceApi.md#listlaunchplans2) | **Get** /api/v1/launch_plans/{id.project}/{id.domain} | 
*AdminServiceApi* | [**ListNamedEntities**](docs/AdminServiceApi.md#listnamedentities) | **Get** /api/v1/named_entities/{resource_type}/{project}/{domain} | 
*AdminServiceApi* | [**ListNodeExecutions**](docs/AdminServiceApi.md#listnodeexecutions) | **Get** /api/v1/node_executions/{workflow_execution_id.project}/{workflow_execution_id.domain}/{workflow_execution_id.name} | 
*AdminServiceApi* | [**ListNodeExecutionsForTask**](docs/AdminServiceApi.md#listnodeexecutionsfortask) | **Get** /api/v1/children/task_executions/{task_execution_id.node_execution_id.execution_id.project}/{task_execution_id.node_execution_id.execution_id.domain}/{task_execution_id.node_execution_id.execution_id.name}/{task_execution_id.node_execution_id.node_id}/{task_execution_id.task_id.project}/{task_execution_id.task_id.domain}/{task_execution_id.task_id.name}/{task_execution_id.task_id.version}/{task_execution_id.retry_attempt} | 
*AdminServiceApi* | [**ListProjects**](docs/AdminServiceApi.md#listprojects) | **Get** /api/v1/projects | 
*AdminServiceApi* | [**ListTaskExecutions**](docs/AdminServiceApi.md#listtaskexecutions) | **Get** /api/v1/task_executions/{node_execution_id.execution_id.project}/{node_execution_id.execution_id.domain}/{node_execution_id.execution_id.name}/{node_execution_id.node_id} | 
*AdminServiceApi* | [**ListTaskIds**](docs/AdminServiceApi.md#listtaskids) | **Get** /api/v1/task_ids/{project}/{domain} | 
*AdminServiceApi* | [**ListTasks**](docs/AdminServiceApi.md#listtasks) | **Get** /api/v1/tasks/{id.project}/{id.domain}/{id.name} | 
*AdminServiceApi* | [**ListTasks2**](docs/AdminServiceApi.md#listtasks2) | **Get** /api/v1/tasks/{id.project}/{id.domain} | 
*AdminServiceApi* | [**ListWorkflowIds**](docs/AdminServiceApi.md#listworkflowids) | **Get** /api/v1/workflow_ids/{project}/{domain} | 
*AdminServiceApi* | [**ListWorkflows**](docs/AdminServiceApi.md#listworkflows) | **Get** /api/v1/workflows/{id.project}/{id.domain}/{id.name} | 
*AdminServiceApi* | [**ListWorkflows2**](docs/AdminServiceApi.md#listworkflows2) | **Get** /api/v1/workflows/{id.project}/{id.domain} | 
*AdminServiceApi* | [**RegisterProject**](docs/AdminServiceApi.md#registerproject) | **Post** /api/v1/projects | 
*AdminServiceApi* | [**RelaunchExecution**](docs/AdminServiceApi.md#relaunchexecution) | **Post** /api/v1/executions/relaunch | 
*AdminServiceApi* | [**TerminateExecution**](docs/AdminServiceApi.md#terminateexecution) | **Delete** /api/v1/executions/{id.project}/{id.domain}/{id.name} | 
*AdminServiceApi* | [**UpdateLaunchPlan**](docs/AdminServiceApi.md#updatelaunchplan) | **Put** /api/v1/launch_plans/{id.project}/{id.domain}/{id.name}/{id.version} | 
*AdminServiceApi* | [**UpdateNamedEntity**](docs/AdminServiceApi.md#updatenamedentity) | **Put** /api/v1/named_entities/{resource_type}/{id.project}/{id.domain}/{id.name} | 
*AdminServiceApi* | [**UpdateProjectDomainAttributes**](docs/AdminServiceApi.md#updateprojectdomainattributes) | **Put** /api/v1/project_domain_attributes/{attributes.project}/{attributes.domain} | 


## Documentation For Models

 - [AdminAbortMetadata](docs/AdminAbortMetadata.md)
 - [AdminAnnotations](docs/AdminAnnotations.md)
 - [AdminAuth](docs/AdminAuth.md)
 - [AdminDomain](docs/AdminDomain.md)
 - [AdminEmailNotification](docs/AdminEmailNotification.md)
 - [AdminExecution](docs/AdminExecution.md)
 - [AdminExecutionClosure](docs/AdminExecutionClosure.md)
 - [AdminExecutionCreateRequest](docs/AdminExecutionCreateRequest.md)
 - [AdminExecutionCreateResponse](docs/AdminExecutionCreateResponse.md)
 - [AdminExecutionList](docs/AdminExecutionList.md)
 - [AdminExecutionMetadata](docs/AdminExecutionMetadata.md)
 - [AdminExecutionRelaunchRequest](docs/AdminExecutionRelaunchRequest.md)
 - [AdminExecutionSpec](docs/AdminExecutionSpec.md)
 - [AdminExecutionTerminateRequest](docs/AdminExecutionTerminateRequest.md)
 - [AdminExecutionTerminateResponse](docs/AdminExecutionTerminateResponse.md)
 - [AdminFixedRate](docs/AdminFixedRate.md)
 - [AdminFixedRateUnit](docs/AdminFixedRateUnit.md)
 - [AdminLabels](docs/AdminLabels.md)
 - [AdminLaunchPlan](docs/AdminLaunchPlan.md)
 - [AdminLaunchPlanClosure](docs/AdminLaunchPlanClosure.md)
 - [AdminLaunchPlanCreateRequest](docs/AdminLaunchPlanCreateRequest.md)
 - [AdminLaunchPlanCreateResponse](docs/AdminLaunchPlanCreateResponse.md)
 - [AdminLaunchPlanList](docs/AdminLaunchPlanList.md)
 - [AdminLaunchPlanMetadata](docs/AdminLaunchPlanMetadata.md)
 - [AdminLaunchPlanSpec](docs/AdminLaunchPlanSpec.md)
 - [AdminLaunchPlanState](docs/AdminLaunchPlanState.md)
 - [AdminLaunchPlanUpdateRequest](docs/AdminLaunchPlanUpdateRequest.md)
 - [AdminLaunchPlanUpdateResponse](docs/AdminLaunchPlanUpdateResponse.md)
 - [AdminLiteralMapBlob](docs/AdminLiteralMapBlob.md)
 - [AdminNamedEntity](docs/AdminNamedEntity.md)
 - [AdminNamedEntityIdentifier](docs/AdminNamedEntityIdentifier.md)
 - [AdminNamedEntityIdentifierList](docs/AdminNamedEntityIdentifierList.md)
 - [AdminNamedEntityList](docs/AdminNamedEntityList.md)
 - [AdminNamedEntityMetadata](docs/AdminNamedEntityMetadata.md)
 - [AdminNamedEntityUpdateRequest](docs/AdminNamedEntityUpdateRequest.md)
 - [AdminNamedEntityUpdateResponse](docs/AdminNamedEntityUpdateResponse.md)
 - [AdminNodeExecutionClosure](docs/AdminNodeExecutionClosure.md)
 - [AdminNodeExecutionEventRequest](docs/AdminNodeExecutionEventRequest.md)
 - [AdminNodeExecutionEventResponse](docs/AdminNodeExecutionEventResponse.md)
 - [AdminNodeExecutionGetDataResponse](docs/AdminNodeExecutionGetDataResponse.md)
 - [AdminNodeExecutionList](docs/AdminNodeExecutionList.md)
 - [AdminNotification](docs/AdminNotification.md)
 - [AdminNotificationList](docs/AdminNotificationList.md)
 - [AdminPagerDutyNotification](docs/AdminPagerDutyNotification.md)
 - [AdminProject](docs/AdminProject.md)
 - [AdminProjectDomainAttributes](docs/AdminProjectDomainAttributes.md)
 - [AdminProjectDomainAttributesUpdateRequest](docs/AdminProjectDomainAttributesUpdateRequest.md)
 - [AdminProjectDomainAttributesUpdateResponse](docs/AdminProjectDomainAttributesUpdateResponse.md)
 - [AdminProjectRegisterRequest](docs/AdminProjectRegisterRequest.md)
 - [AdminProjectRegisterResponse](docs/AdminProjectRegisterResponse.md)
 - [AdminProjects](docs/AdminProjects.md)
 - [AdminSchedule](docs/AdminSchedule.md)
 - [AdminSlackNotification](docs/AdminSlackNotification.md)
 - [AdminSort](docs/AdminSort.md)
 - [AdminTask](docs/AdminTask.md)
 - [AdminTaskClosure](docs/AdminTaskClosure.md)
 - [AdminTaskCreateRequest](docs/AdminTaskCreateRequest.md)
 - [AdminTaskCreateResponse](docs/AdminTaskCreateResponse.md)
 - [AdminTaskExecutionClosure](docs/AdminTaskExecutionClosure.md)
 - [AdminTaskExecutionEventRequest](docs/AdminTaskExecutionEventRequest.md)
 - [AdminTaskExecutionEventResponse](docs/AdminTaskExecutionEventResponse.md)
 - [AdminTaskExecutionGetDataResponse](docs/AdminTaskExecutionGetDataResponse.md)
 - [AdminTaskExecutionList](docs/AdminTaskExecutionList.md)
 - [AdminTaskList](docs/AdminTaskList.md)
 - [AdminTaskSpec](docs/AdminTaskSpec.md)
 - [AdminUrlBlob](docs/AdminUrlBlob.md)
 - [AdminWorkflow](docs/AdminWorkflow.md)
 - [AdminWorkflowClosure](docs/AdminWorkflowClosure.md)
 - [AdminWorkflowCreateRequest](docs/AdminWorkflowCreateRequest.md)
 - [AdminWorkflowCreateResponse](docs/AdminWorkflowCreateResponse.md)
 - [AdminWorkflowExecutionEventRequest](docs/AdminWorkflowExecutionEventRequest.md)
 - [AdminWorkflowExecutionEventResponse](docs/AdminWorkflowExecutionEventResponse.md)
 - [AdminWorkflowExecutionGetDataResponse](docs/AdminWorkflowExecutionGetDataResponse.md)
 - [AdminWorkflowList](docs/AdminWorkflowList.md)
 - [AdminWorkflowSpec](docs/AdminWorkflowSpec.md)
 - [BlobTypeBlobDimensionality](docs/BlobTypeBlobDimensionality.md)
 - [ComparisonExpressionOperator](docs/ComparisonExpressionOperator.md)
 - [ConjunctionExpressionLogicalOperator](docs/ConjunctionExpressionLogicalOperator.md)
 - [ConnectionSetIdList](docs/ConnectionSetIdList.md)
 - [CoreAlias](docs/CoreAlias.md)
 - [CoreBinary](docs/CoreBinary.md)
 - [CoreBinding](docs/CoreBinding.md)
 - [CoreBindingData](docs/CoreBindingData.md)
 - [CoreBindingDataCollection](docs/CoreBindingDataCollection.md)
 - [CoreBindingDataMap](docs/CoreBindingDataMap.md)
 - [CoreBlob](docs/CoreBlob.md)
 - [CoreBlobMetadata](docs/CoreBlobMetadata.md)
 - [CoreBlobType](docs/CoreBlobType.md)
 - [CoreBooleanExpression](docs/CoreBooleanExpression.md)
 - [CoreBranchNode](docs/CoreBranchNode.md)
 - [CoreComparisonExpression](docs/CoreComparisonExpression.md)
 - [CoreCompiledTask](docs/CoreCompiledTask.md)
 - [CoreCompiledWorkflow](docs/CoreCompiledWorkflow.md)
 - [CoreCompiledWorkflowClosure](docs/CoreCompiledWorkflowClosure.md)
 - [CoreConjunctionExpression](docs/CoreConjunctionExpression.md)
 - [CoreConnectionSet](docs/CoreConnectionSet.md)
 - [CoreContainer](docs/CoreContainer.md)
 - [CoreContainerPort](docs/CoreContainerPort.md)
 - [CoreError](docs/CoreError.md)
 - [CoreExecutionError](docs/CoreExecutionError.md)
 - [CoreIdentifier](docs/CoreIdentifier.md)
 - [CoreIfBlock](docs/CoreIfBlock.md)
 - [CoreIfElseBlock](docs/CoreIfElseBlock.md)
 - [CoreKeyValuePair](docs/CoreKeyValuePair.md)
 - [CoreLiteral](docs/CoreLiteral.md)
 - [CoreLiteralCollection](docs/CoreLiteralCollection.md)
 - [CoreLiteralMap](docs/CoreLiteralMap.md)
 - [CoreLiteralType](docs/CoreLiteralType.md)
 - [CoreNode](docs/CoreNode.md)
 - [CoreNodeExecutionIdentifier](docs/CoreNodeExecutionIdentifier.md)
 - [CoreNodeExecutionPhase](docs/CoreNodeExecutionPhase.md)
 - [CoreNodeMetadata](docs/CoreNodeMetadata.md)
 - [CoreOperand](docs/CoreOperand.md)
 - [CoreOutputReference](docs/CoreOutputReference.md)
 - [CoreParameter](docs/CoreParameter.md)
 - [CoreParameterMap](docs/CoreParameterMap.md)
 - [CorePrimitive](docs/CorePrimitive.md)
 - [CoreResourceType](docs/CoreResourceType.md)
 - [CoreResources](docs/CoreResources.md)
 - [CoreRetryStrategy](docs/CoreRetryStrategy.md)
 - [CoreRuntimeMetadata](docs/CoreRuntimeMetadata.md)
 - [CoreScalar](docs/CoreScalar.md)
 - [CoreSchemaType](docs/CoreSchemaType.md)
 - [CoreSimpleType](docs/CoreSimpleType.md)
 - [CoreTaskExecutionIdentifier](docs/CoreTaskExecutionIdentifier.md)
 - [CoreTaskExecutionPhase](docs/CoreTaskExecutionPhase.md)
 - [CoreTaskLog](docs/CoreTaskLog.md)
 - [CoreTaskMetadata](docs/CoreTaskMetadata.md)
 - [CoreTaskNode](docs/CoreTaskNode.md)
 - [CoreTaskTemplate](docs/CoreTaskTemplate.md)
 - [CoreTypedInterface](docs/CoreTypedInterface.md)
 - [CoreVariable](docs/CoreVariable.md)
 - [CoreVariableMap](docs/CoreVariableMap.md)
 - [CoreVoid](docs/CoreVoid.md)
 - [CoreWorkflowExecutionIdentifier](docs/CoreWorkflowExecutionIdentifier.md)
 - [CoreWorkflowExecutionPhase](docs/CoreWorkflowExecutionPhase.md)
 - [CoreWorkflowMetadata](docs/CoreWorkflowMetadata.md)
 - [CoreWorkflowNode](docs/CoreWorkflowNode.md)
 - [CoreWorkflowTemplate](docs/CoreWorkflowTemplate.md)
 - [EventNodeExecutionEvent](docs/EventNodeExecutionEvent.md)
 - [EventParentTaskExecutionMetadata](docs/EventParentTaskExecutionMetadata.md)
 - [EventTaskExecutionEvent](docs/EventTaskExecutionEvent.md)
 - [EventWorkflowExecutionEvent](docs/EventWorkflowExecutionEvent.md)
 - [ExecutionMetadataExecutionMode](docs/ExecutionMetadataExecutionMode.md)
 - [FlyteidladminNodeExecution](docs/FlyteidladminNodeExecution.md)
 - [FlyteidladminTaskExecution](docs/FlyteidladminTaskExecution.md)
 - [FlyteidladminWorkflowNodeMetadata](docs/FlyteidladminWorkflowNodeMetadata.md)
 - [FlyteidlcoreSchema](docs/FlyteidlcoreSchema.md)
 - [FlyteidleventWorkflowNodeMetadata](docs/FlyteidleventWorkflowNodeMetadata.md)
 - [ProtobufListValue](docs/ProtobufListValue.md)
 - [ProtobufNullValue](docs/ProtobufNullValue.md)
 - [ProtobufStruct](docs/ProtobufStruct.md)
 - [ProtobufValue](docs/ProtobufValue.md)
 - [ResourcesResourceEntry](docs/ResourcesResourceEntry.md)
 - [ResourcesResourceName](docs/ResourcesResourceName.md)
 - [RuntimeMetadataRuntimeType](docs/RuntimeMetadataRuntimeType.md)
 - [SchemaColumnSchemaColumnType](docs/SchemaColumnSchemaColumnType.md)
 - [SchemaTypeSchemaColumn](docs/SchemaTypeSchemaColumn.md)
 - [SortDirection](docs/SortDirection.md)
 - [TaskLogMessageFormat](docs/TaskLogMessageFormat.md)


## Documentation For Authorization
 Endpoints do not require authorization.


## Author



