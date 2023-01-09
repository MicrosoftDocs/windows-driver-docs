---
title: MSFT\_ReplicationCapabilities class
description: Represents the replication capabilities of a storage subsystem.
ms.assetid: EBD8AB73-BE3C-4AD8-9541-9853D3851900
keywords:
- MSFT_ReplicationCapabilities class Windows Storage Management API
- MSFT_ReplicationCapabilities class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_ReplicationCapabilities
- MSFT_ReplicationCapabilities.SupportedObjectTypes
- MSFT_ReplicationCapabilities.SupportedReplicationTypes
- MSFT_ReplicationCapabilities.DefaultRecoveryPointObjective
- MSFT_ReplicationCapabilities.SupportsReplicationGroup
- MSFT_ReplicationCapabilities.SupportsEmptyReplicationGroup
- MSFT_ReplicationCapabilities.SupportsFullDiscovery
- MSFT_ReplicationCapabilities.SupportsCreateReplicationRelationshipMethod
- MSFT_ReplicationCapabilities.SupportedAsynchronousActions
- MSFT_ReplicationCapabilities.SupportedSynchronousActions
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_ReplicationCapabilities class

Represents the replication capabilities of a storage subsystem.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class MSFT_ReplicationCapabilities : MSFT_StorageObject
{
  UInt16  SupportedObjectTypes[];
  UInt16  SupportedReplicationTypes[];
  UInt32  DefaultRecoveryPointObjective;
  Boolean SupportsReplicationGroup;
  Boolean SupportsEmptyReplicationGroup;
  Boolean SupportsFullDiscovery;
  Boolean SupportsCreateReplicationRelationshipMethod;
  Uint16  SupportedAsynchronousActions[];
  Uint16  SupportedSynchronousActions[];
};
```

## Members

The **MSFT\_ReplicationCapabilities** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_ReplicationCapabilities** class has these methods.



| Method                                                                                          | Description                                                                                                                                                                             |
|:------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetRecoveryPointData**](msft-replicationcapabilities-getrecoverypointdata.md)               | Returns, for a given *ReplicationType*, recovery point data.                                                                                                                 |
| [**GetSupportedCopyStates**](msft-replicationcapabilities-getsupportedcopystates.md)           | Returns, for a given *ReplicationType*, the supported copy states.                                                                                                           |
| [**GetSupportedFeatures**](msft-replicationcapabilities-getsupportedfeatures.md)               | Returns, for a given *ReplicationType*, the supported features.                                                                                                              |
| [**GetSupportedGroupCopyStates**](msft-replicationcapabilities-getsupportedgroupcopystates.md) | Returns, for a given *ReplicationType*, the supported replication group copy states.                                                                                         |
| [**GetSupportedGroupFeatures**](msft-replicationcapabilities-getsupportedgroupfeatures.md)     | Returns, for a given *ReplicationType*, the supported group features.                                                                                                        |
| [**GetSupportedGroupOperations**](msft-replicationcapabilities-getsupportedgroupoperations.md) | Returns, for a given *ReplicationType*, the supported operations on a group synchronized association that can be supplied to the **ModifyReplicaSynchronization** operation. |
| [**GetSupportedOperations**](msft-replicationcapabilities-getsupportedoperations.md)           | Returns, for a given ReplicationType, the supported Operations on a StorageSynchronized association that can be supplied to the **ModifyReplicaSynchronization** operation.  |



 

### Properties

The **MSFT\_ReplicationCapabilities** class has these properties.

 

**DefaultRecoveryPointObjective**
   

Data type: **UInt32**
 

Access type: Read-only
 

Default value for recovery point.

 

**SupportedAsynchronousActions**
   

Data type: **Uint16** array
 

Access type: Read-only
 

An enumeration indicating what operations will be executed as asynchronous jobs. If an operation is included in both this and *SupportedSynchronousActions* then the underlying implementation is indicating that it may or may not create a job.

> [!Note]  
> The following methods are not supported asynchronously:
>
> -   AddMembers
> -   AddReplicationEntity
> -   AddServiceAccessPoint
> -   AddSharedSecret
> -   CreateGroup
> -   DeleteGroup
> -   RemoveMembers

 

 

**CreateElementReplica** (2)
 

**CreateGroupReplica** (3)
 

**CreateSynchronizationAspect** (4)
 

**ModifyReplicaSynchronization** (5)
 

**ModifyListSynchronization** (6)
 

**ModifySettingsDefineState** (7)
 

**GetAvailableTargetElements** (8)
 

**GetPeerSystems** (9)
 

**GetReplicationRelationships** (10)
 

**GetServiceAccessPoints** (11)
 

**CreateListReplica** (19)
 

**CreateGroupReplicaFromElements** (20)
 

**GetReplicationRelationshipInstances** (21)
 

**ModifyListSettingsDefineState** (22)
 

**CreateRemoteReplicationCollection** (23)
 

**AddToRemoteReplicationCollection** (24)
 

**RemoveFromRemoteReplicationCollection** (25)
 

**GetSynchronizationAspects** (26)
 

**GetSynchronizationAspectInstances** (27)
 

**CreateGroupReplicaFromElementSynchronizations** (28)
 

**AddElementsToGroupSynchronized** (29)
 

**ConfirmTargetData** (30)
 

**CreateListSynchronizationAspect** (31)
 

**DMTF Reserved** ("..)
 

**Vendor Specific** (0x8000..)
 

 

**SupportedObjectTypes**
   

Data type: **UInt16** array
 

Access type: Read-only
 

An enumeration indicating the supported object types associated with these replication capabilities.

 

**VirtualDisk** (2)
 

**Volume** (3)
 

**ReplicaPeer** (4)
 

**Partition** (..)
 

**ReplicationGroup** (0x8000)
 

**StorageSubSystem** (0x8001)
 

 (0x8002)
 

 

**SupportedReplicationTypes**
   

Data type: **UInt16** array
 

Access type: Write-only
 

An enumeration indicating the supported SyncType/Mode/Local-or-Remote combinations.

 

**Synchronous Mirror Local** (2)
 

**Asynchronous Mirror Local** (3)
 

**Synchronous Mirror Remote** (4)
 

**Asynchronous Mirror Remote** (5)
 

**Synchronous Snapshot Local** (6)
 

**Asynchronous Snapshot Local** (7)
 

**Synchronous Snapshot Remote** (8)
 

**Asynchronous Snapshot Remote** (9)
 

**Synchronous Clone Local** (10)
 

**Asynchronous Clone Local** (11)
 

**Synchronous Clone Remote** (12)
 

**Asynchronous Clone Remote** (13)
 

**Synchronous TokenizedClone Local** (14)
 

**Asynchronous TokenizedClone Local** (15)
 

**Synchronous TokenizedClone Remote** (16)
 

**Asynchronous TokenizedClone Remote** (17)
 

**Adaptive Mirror Local** (18)
 

**Adaptive Mirror Remote** (19)
 

**Adaptive Snapshot Local** (20)
 

**Adaptive Snapshot Remote** (21)
 

**Adaptive Clone Local** (22)
 

**Adaptive Clone Remote** (23)
 

**Adaptive TokenizedClone Local** (24)
 

**Adaptive TokenizedClone Remote** (25)
 

**DMTF Reserved** (..)
 

**Vendor Specific** (0x8000..)
 

 

**SupportedSynchronousActions**
   

Data type: **Uint16** array
 

Access type: Read-only
 

An enumeration indicating what operations will be executed synchronously without the creation of a job. If an operation is included in both this and *SupportedAsynchronousActions* then the underlying implementation is indicating that it may or may not create a job.

> [!Note]  
> The following methods are not supported asynchronously:
>
> -   AddMembers
> -   AddReplicationEntity
> -   AddServiceAccessPoint
> -   AddSharedSecret
> -   CreateGroup
> -   DeleteGroup
> -   RemoveMembers

 

 

**CreateElementReplica** (2)
 

**CreateGroupReplica** (3)
 

**CreateSynchronizationAspect** (4)
 

**ModifyReplicaSynchronization** (5)
 

**ModifyListSynchronization** (6)
 

**ModifySettingsDefineState** (7)
 

**GetAvailableTargetElements** (8)
 

**GetPeerSystems** (9)
 

**GetReplicationRelationships** (10)
 

**GetServiceAccessPoints** (11)
 

**CreateGroup** (12)
 

**DeleteGroup** (13)
 

**AddMembers** (14)
 

**RemoveMembers** (15)
 

**AddReplicationEntity** (16)
 

**AddServiceAccessPoint** (17)
 

**AddSharedSecret** (18)
 

**CreateListReplica** (19)
 

**CreateGroupReplicaFromElements** (20)
 

**GetReplicationRelationshipInstances** (21)
 

**ModifyListSettingsDefineState** (22)
 

**CreateRemoteReplicationCollection** (23)
 

**AddToRemoteReplicationCollection** (24)
 

**RemoveFromRemoteReplicationCollection** (25)
 

**GetSynchronizationAspects** (26)
 

**GetSynchronizationAspectInstances** (27)
 

**CreateGroupReplicaFromElementSynchronizations** (28)
 

**AddElementsToGroupSynchronized** (29)
 

**ConfirmTargetData** (30)
 

**CreateListSynchronizationAspect** (31)
 

**DMTF Reserved** ("..)
 

**Vendor Specific** (0x8000..)
 

 

**SupportsCreateReplicationRelationshipMethod**
   

Data type: **Boolean**
 

Access type: Read-only
 

If **TRUE**, then the [**CreateReplicationRelationship**](msft-storagesubsystem-createreplicationrelationship.md) operation is supported.

 

**SupportsEmptyReplicationGroup**
   

Data type: **Boolean**
 

Access type: Read-only
 

If **TRUE**, then empty replication groups are allowed.

 

**SupportsFullDiscovery**
   

Data type: **Boolean**
 

Access type: Read-only
 

If **TRUE**, then this is a fully discovered model.

 

**SupportsReplicationGroup**
   

Data type: **Boolean**
 

Access type: Read-only
 

If **TRUE**, then replication groups are supported.

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 10 \[desktop apps only\]                                               |
| Minimum supported server | Windows Server 2016 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_StorageObject**](msft-storageobject.md)
 

 

 





