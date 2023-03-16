---
title: MSFT\_Synchronized class
description: Synchronized status of a storage object and its snapshots, clones, or mirrors.
ms.assetid: 460FAAB4-9DB2-4B02-9E2B-07791E93E728
keywords:
- MSFT_Synchronized class Windows Storage Management API
- MSFT_Synchronized class Windows Storage Management API , described
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_Synchronized
- MSFT_Synchronized.SyncTime
- MSFT_Synchronized.SyncMaintained
- MSFT_Synchronized.CopyState
- MSFT_Synchronized.RequestedCopyState
- MSFT_Synchronized.SyncType
- MSFT_Synchronized.SyncMode
- MSFT_Synchronized.ProgressStatus
- MSFT_Synchronized.PercentSynced
- MSFT_Synchronized.CopyType
- MSFT_Synchronized.ReplicaType
- MSFT_Synchronized.SyncState
- MSFT_Synchronized.CopyPriority
- MSFT_Synchronized.CopyMethodology
- MSFT_Synchronized.RecoveryPointObjective
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# MSFT\_Synchronized class

Synchronized status of a storage object and its snapshots, clones, or mirrors.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class MSFT_Synchronized
{
  DateTime SyncTime;
  Boolean  SyncMaintained;
  UInt16   CopyState;
  UInt16   RequestedCopyState;
  UInt16   SyncType;
  UInt16   SyncMode;
  UInt16   ProgressStatus;
  UInt16   PercentSynced;
  UInt16   CopyType;
  UInt16   ReplicaType;
  UInt16   SyncState;
  UInt16   CopyPriority;
  UInt16   CopyMethodology;
  UInt16   RecoveryPointObjective[];
};
```

## Members

The **MSFT\_Synchronized** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_Synchronized** class has these properties.

 

**CopyMethodology**
   

Data type: **UInt16**
 

Access type: Read-only
 

Specifies the copy methodology that the copy engine uses to create and/or maintain the target element.



| Value                                                                                                                                                                                                                                                                                   | Meaning                                                                                                                                                  |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Not_Specified"></span><span id="not_specified"></span><span id="NOT_SPECIFIED"></span> **Not Specified** 0                                      | The method of maintaining the copy is not specified.                                                                                          |
| <span id="Other"></span><span id="other"></span><span id="OTHER"></span> **Other** 1                                                                      |                                                                                                                                                          |
| <span id="Implementation_decides"></span><span id="implementation_decides"></span><span id="IMPLEMENTATION_DECIDES"></span> **Implementation decides** 2  |                                                                                                                                                          |
| <span id="Full_Copy"></span><span id="full_copy"></span><span id="FULL_COPY"></span> **Full Copy** 3                                                      | A full copy of the source object is (or will be) generated.                                                                                   |
| <span id="Incremental_Copy"></span><span id="incremental_copy"></span><span id="INCREMENTAL_COPY"></span> **Incremental Copy** 4                          | Only changed data from the source element is copied to the target element.                                                                    |
| <span id="Differential_Copy"></span><span id="differential_copy"></span><span id="DIFFERENTIAL_COPY"></span> **Differential Copy** 5                      | Only the new writes to the source element are copied to the target element.                                                                   |
| <span id="Copy_On_Write"></span><span id="copy_on_write"></span><span id="COPY_ON_WRITE"></span> **Copy On Write** 6                                      | Affected data is copied on the first write to the source or to the target elements.                                                           |
| <span id="Copy_On_Access"></span><span id="copy_on_access"></span><span id="COPY_ON_ACCESS"></span> **Copy On Access** 7                                  | Affected data is copied on the first access to the source element.                                                                            |
| <span id="Delta_Update"></span><span id="delta_update"></span><span id="DELTA_UPDATE"></span> **Delta Update** 8                                          | Difference-based replication where, after the initial copy, only updates to the source are copied to the target.                              |
| <span id="Snap_And______Clone"></span><span id="snap_and______clone"></span><span id="SNAP_AND______CLONE"></span> **Snap And Clone** 9                   | The service creates a snapshot of the source element first, then uses the snapshot as the source of the copy operation to the target element. |
| <span id="Microsoft_Reserved"></span><span id="microsoft_reserved"></span><span id="MICROSOFT_RESERVED"></span> **Microsoft Reserved** ..                 |                                                                                                                                                          |
| <span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span> **Vendor Specific** 0x8000..                       |                                                                                                                                                          |



 

 

**CopyPriority**
   

Data type: **UInt16**
 

Access type: Read-only
 

Allows the priority of background copy engine I/O to be managed relative to host I/O operations during a sequential background copy operation.



| Value                                                                                                                                                                                                                                                                    | Meaning                                                       |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| <span id="Not_Managed"></span><span id="not_managed"></span><span id="NOT_MANAGED"></span> **Not Managed** 0                               |                                                               |
| <span id="Low"></span><span id="low"></span><span id="LOW"></span> **Low** 1                                                               | Copy engine I/O has lower priority than host I/O.  |
| <span id="Same"></span><span id="same"></span><span id="SAME"></span> **Same** 2                                                           | Copy engine I/O has the same priority as host I/O. |
| <span id="High"></span><span id="high"></span><span id="HIGH"></span> **High** 3                                                           | copy engine I/O has higher priority as host I/O.   |
| <span id="Microsoft_Reserved"></span><span id="microsoft_reserved"></span><span id="MICROSOFT_RESERVED"></span> **Microsoft Reserved** ..  |                                                               |
| <span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span> **Vendor Specific** 0x8000..        |                                                               |



 

 

**CopyState**
   

Data type: **UInt16**
 

Access type: Read-only
 

Describes the state of the association with respect to replication activity.



| Value                                                                                                                                                                                                                                                                    | Meaning                                                                                                                                                                                 |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Initialized"></span><span id="initialized"></span><span id="INITIALIZED"></span> **Initialized** 2                               | The link to enable replication is established, and source and replica elements are associated, but the copy operation has not started.                                       |
| <span id="Unsynchronized"></span><span id="unsynchronized"></span><span id="UNSYNCHRONIZED"></span> **Unsynchronized** 3                   | Not all the source element data has been copied to the target element.                                                                                                       |
| <span id="Synchronized"></span><span id="synchronized"></span><span id="SYNCHRONIZED"></span> **Synchronized** 4                           | For mirror, snapshot, or clone replication, the target represents a copy of the source.                                                                                      |
| <span id="Broken"></span><span id="broken"></span><span id="BROKEN"></span> **Broken** 5                                                   | The relationship is non-functional due to errors in the source, the target, the path between the two, or space constraints.                                                  |
| <span id="Fractured"></span><span id="fractured"></span><span id="FRACTURED"></span> **Fractured** 6                                       | The target is split from the source.                                                                                                                                         |
| <span id="Split"></span><span id="split"></span><span id="SPLIT"></span> **Split** 7                                                       | The target element was gracefully (or systematically) split from its source element. Consistency is guaranteed.                                                              |
| <span id="Inactive"></span><span id="inactive"></span><span id="INACTIVE"></span> **Inactive** 8                                           | The copy operation has stopped. Writes to the source element will not be sent to target element.                                                                             |
| <span id="Suspended"></span><span id="suspended"></span><span id="SUSPENDED"></span> **Suspended** 9                                       | Data flow between the source and target elements has stopped. Writes to the source element are held until the association is resumed.                                        |
| <span id="Failedover"></span><span id="failedover"></span><span id="FAILEDOVER"></span> **Failedover** 10                                  | Reads and writes to and from the target element have failed. The source element is not reachable.                                                                            |
| <span id="Prepared"></span><span id="prepared"></span><span id="PREPARED"></span> **Prepared** 11                                          | Initialization has completed and the copy operation started. However, the data flow has not started.                                                                         |
| <span id="Aborted"></span><span id="aborted"></span><span id="ABORTED"></span> **Aborted** 12                                              | The copy operation is aborted with the Abort operation. Use the Resync Replica operation to restart the copy operation.                                                      |
| <span id="Skewed"></span><span id="skewed"></span><span id="SKEWED"></span> **Skewed** 13                                                  | The target has been modified and is no longer synchronized with the source element or the point-in-time view.                                                                |
| <span id="Mixed"></span><span id="mixed"></span><span id="MIXED"></span> **Mixed** 14                                                      | Applies to the *CopyState* of *GroupSynchronized*. It indicates that the *StorageSynchronized* associations of the elements in the groups have different *CopyState* values. |
| <span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span> **Not Applicable** 15                  | The target does not have a replication state.                                                                                                                                |
| <span id="Microsoft_Reserved"></span><span id="microsoft_reserved"></span><span id="MICROSOFT_RESERVED"></span> **Microsoft Reserved** ..  | This value is reserved for system use.                                                                                                                                       |
| <span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span> **Vendor Specific** 0x8000..        | These values are reserved for vendors.                                                                                                                                       |



 

 

**CopyType**
   

Data type: **UInt16**
 

Access type: Read-only
 

Describes the replication policy.



| Value                                                                                                                                                                                                                                                                    | Meaning                                                                                                                      |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| <span id="Async"></span><span id="async"></span><span id="ASYNC"></span> **Async** 2                                                       | Create and maintain an asynchronous copy of the source.                                                           |
| <span id="Sync"></span><span id="sync"></span><span id="SYNC"></span> **Sync** 3                                                           | Create and maintain a synchronized copy of the source.                                                            |
| <span id="UnSyncAssoc"></span><span id="unsyncassoc"></span><span id="UNSYNCASSOC"></span> **UnSyncAssoc** 4                               | Create an unsynchronized copy and maintain an association to the source.                                          |
| <span id="UnSyncUnAssoc"></span><span id="unsyncunassoc"></span><span id="UNSYNCUNASSOC"></span> **UnSyncUnAssoc** 5                       | Create an unsynchronized copy with a temporary association that is deleted upon completion of the copy operation. |
| <span id="Microsoft_Reserved"></span><span id="microsoft_reserved"></span><span id="MICROSOFT_RESERVED"></span> **Microsoft Reserved** ..  |                                                                                                                              |
| <span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span> **Vendor Specific** 0x8000..        |                                                                                                                              |



 

 

**PercentSynced**
   

Data type: **UInt16**
 

Access type: Read-only
 

Specifies the percent of the work completed to reach synchronization. Must be set to **NULL** if the implementation is not capable of providing this information.

 

**ProgressStatus**
   

Data type: **UInt16**
 

Access type: Read-only
 

Describes the status of the association with respect to replication activity.



| Value                                                                                                                                                                                                                                                                    | Meaning                                                                                                                                                         |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span> **Unknown** 0                                               |                                                                                                                                                                 |
| <span id="Completed"></span><span id="completed"></span><span id="COMPLETED"></span> **Completed** 2                                       | The request is completed. Copy operation is idle.                                                                                                    |
| <span id="Dormant"></span><span id="dormant"></span><span id="DORMANT"></span> **Dormant** 3                                               | The copy operation is inactive, suspended, or quiesced.                                                                                              |
| <span id="Initializing"></span><span id="initializing"></span><span id="INITIALIZING"></span> **Initializing** 4                           | In the process of establishing the source/replica association. The copy operation has not started.                                                   |
| <span id="Preparing"></span><span id="preparing"></span><span id="PREPARING"></span> **Preparing** 5                                       | Preparation is in progress.                                                                                                                          |
| <span id="Synchronizing"></span><span id="synchronizing"></span><span id="SYNCHRONIZING"></span> **Synchronizing** 6                       | Sync is in progress.                                                                                                                                 |
| <span id="Resyncing"></span><span id="resyncing"></span><span id="RESYNCING"></span> **Resyncing** 7                                       | Resync is in progress.                                                                                                                               |
| <span id="Restoring"></span><span id="restoring"></span><span id="RESTORING"></span> **Restoring** 8                                       | Restore is in progress.                                                                                                                              |
| <span id="Fracturing"></span><span id="fracturing"></span><span id="FRACTURING"></span> **Fracturing** 9                                   | Fracture is in progress.                                                                                                                             |
| <span id="Splitting"></span><span id="splitting"></span><span id="SPLITTING"></span> **Splitting** 10                                      | Split is in progress.                                                                                                                                |
| <span id="Failing_over"></span><span id="failing_over"></span><span id="FAILING_OVER"></span> **Failing over** 11                          | In the process of switching source and target.                                                                                                       |
| <span id="Failing_back"></span><span id="failing_back"></span><span id="FAILING_BACK"></span> **Failing back** 12                          | Undoing the result of failover.                                                                                                                      |
| <span id="Detaching"></span><span id="detaching"></span><span id="DETACHING"></span> **Detaching** 13                                      | Detach in progress.                                                                                                                                  |
| <span id="Aborting"></span><span id="aborting"></span><span id="ABORTING"></span> **Aborting** 14                                          | Abort in progress.                                                                                                                                   |
| <span id="Mixed"></span><span id="mixed"></span><span id="MIXED"></span> **Mixed** 15                                                      | Applies to groups with element pairs with different statuses. Generally, the individual statuses need to be examined.                                |
| <span id="Suspending"></span><span id="suspending"></span><span id="SUSPENDING"></span> **Suspending** 16                                  | The copy operation is in the process of being suspended.                                                                                             |
| <span id="Requires_fracture"></span><span id="requires_fracture"></span><span id="REQUIRES_FRACTURE"></span> **Requires fracture** 17      | The requested operation has completed. However, the synchronization relationship needs to be fractured before further copy operations can be issued. |
| <span id="Requires_resync"></span><span id="requires_resync"></span><span id="REQUIRES_RESYNC"></span> **Requires resync** 18              | The requested operation has completed. However, the synchronization relationship needs to be resynced before further copy operations can be issued.  |
| <span id="Requires_activate"></span><span id="requires_activate"></span><span id="REQUIRES_ACTIVATE"></span> **Requires activate** 19      | The requested operation has completed. However, the synchronization relationship needs to be activated before further copy operations can be issued. |
| <span id="Pending"></span><span id="pending"></span><span id="PENDING"></span> **Pending** 20                                              | The flow of data has stopped momentarily due to limited bandwidth or a busy system.                                                                  |
| <span id="Microsoft_Reserved"></span><span id="microsoft_reserved"></span><span id="MICROSOFT_RESERVED"></span> **Microsoft Reserved** ..  |                                                                                                                                                                 |
| <span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span> **Vendor Specific** 0x8000..        |                                                                                                                                                                 |



 

 

**RecoveryPointObjective**
   

Data type: **UInt16** array
 

Access type: Read-only
 

Indicates the maximum interval in which data might be lost. For synchronous copy operations, *RecoveryPointObjective* is 0. For asynchronous copy operations *RecoveryPointObjective* represents the interval since the most recent transmission of data to the target element.

 

**ReplicaType**
   

Data type: **UInt16**
 

Access type: Read-only
 

Provides information on how the replica is being maintained.



| Value                                                                                                                                                                                                                                                                    | Meaning                                                                              |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| <span id="Not_Specified"></span><span id="not_specified"></span><span id="NOT_SPECIFIED"></span> **Not Specified** 0                       | The method of maintaining the copy is not specified.                      |
| <span id="Full_Copy"></span><span id="full_copy"></span><span id="FULL_COPY"></span> **Full Copy** 2                                       | A full copy of the source object is (or will be) generated.               |
| <span id="Before_Delta"></span><span id="before_delta"></span><span id="BEFORE_DELTA"></span> **Before Delta** 3                           | The source object will be maintained as a delta data from the replica.    |
| <span id="After_Delta"></span><span id="after_delta"></span><span id="AFTER_DELTA"></span> **After Delta** 4                               | The replica will be maintained as delta data from the source object.      |
| <span id="Log"></span><span id="log"></span><span id="LOG"></span> **Log** 5                                                               | The replica object is being maintained as a log of changes to the source. |
| <span id="Microsoft_Reserved"></span><span id="microsoft_reserved"></span><span id="MICROSOFT_RESERVED"></span> **Microsoft Reserved** ..  |                                                                                      |
| <span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span> **Vendor Specific** 0x8000..        |                                                                                      |



 

 

**RequestedCopyState**
   

Data type: **UInt16**
 

Access type: Read-only
 

An integer enumeration that indicates the last requested or desired state for the association. The actual state of the association is represented by *CopyState*. Note that when *CopyState* reaches the requested state, his property will be set to "Not Applicable".

 

**SyncMaintained**
   

Data type: **Boolean**
 

Access type: Read-only
 

Indicates whether synchronization is maintained.

 

**SyncMode**
   

Data type: **UInt16**
 

Access type: Read-only
 

Describes whether the target elements will be updated synchronously or asynchronously. If **NULL**, the implementation decides the mode.

 

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
 

<span id="Synchronous"></span><span id="synchronous"></span><span id="SYNCHRONOUS"></span>**Synchronous** (2)
 

<span id="Asynchronous"></span><span id="asynchronous"></span><span id="ASYNCHRONOUS"></span>**Asynchronous** (3)
 

<span id="Microsoft_Reserved"></span><span id="microsoft_reserved"></span><span id="MICROSOFT_RESERVED"></span>**Microsoft Reserved** (..)
 

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>**Vendor Specific** (32768..65535)
 

 

**SyncState**
   

Data type: **UInt16**
 

Access type: Read-only
 

Describes the state of the association with respect to replication activity.



| Value                                                                                                                                                                                                                                                                           | Meaning                                                                                                                                     |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Initialized"></span><span id="initialized"></span><span id="INITIALIZED"></span> **Initialized** 2                                      | The link to enable replication is established and source/replica elements are associated, but the copy engine has not started.   |
| <span id="PrepareInProgress"></span><span id="prepareinprogress"></span><span id="PREPAREINPROGRESS"></span> **PrepareInProgress** 3              | Preparation for replication is in progress and the copy engine has started.                                                      |
| <span id="Prepared"></span><span id="prepared"></span><span id="PREPARED"></span> **Prepared** 4                                                  | All necessary preparation has completed.                                                                                         |
| <span id="ResyncInProgress"></span><span id="resyncinprogress"></span><span id="RESYNCINPROGRESS"></span> **ResyncInProgress** 5                  | Synchronization or resynchronization is in progress. This may be the initial copy or subsequent changes being copied.            |
| <span id="Synchronized"></span><span id="synchronized"></span><span id="SYNCHRONIZED"></span> **Synchronized** 6                                  | An async or sync replication is currently synchronized. When this value is set, *SyncMaintained* will be true.                   |
| <span id="Fracture_In_Progress"></span><span id="fracture_in_progress"></span><span id="FRACTURE_IN_PROGRESS"></span> **Fracture In Progress** 7  | An operation to fracture an async or sync replication is in progress.                                                            |
| <span id="QuiesceInProgress"></span><span id="quiesceinprogress"></span><span id="QUIESCEINPROGRESS"></span> **QuiesceInProgress** 8              | A quiesce operation is in progress.                                                                                              |
| <span id="Quiesced"></span><span id="quiesced"></span><span id="QUIESCED"></span> **Quiesced** 9                                                  | The replication has been quiesced and is ready for a change.                                                                     |
| <span id="Restore_In_Progress"></span><span id="restore_in_progress"></span><span id="RESTORE_IN_PROGRESS"></span> **Restore In Progress** 10     | Operation is in progress to copy the synced object to the system object.                                                         |
| <span id="Idle"></span><span id="idle"></span><span id="IDLE"></span> **Idle** 11                                                                 | The normal state for an **UnSyncAssoc** replica.                                                                                 |
| <span id="Broken"></span><span id="broken"></span><span id="BROKEN"></span> **Broken** 12                                                         | The relationship is non-functional due to errors in the source, the target, the path between the two, or space constraints.      |
| <span id="Fractured"></span><span id="fractured"></span><span id="FRACTURED"></span> **Fractured** 13                                             | An async or sync replication is fractured.                                                                                       |
| <span id="Frozen"></span><span id="frozen"></span><span id="FROZEN"></span> **Frozen** 14                                                         | All blocks are copied from the source to an **UnSyncAssoc** replica, and the copy engine is stopped.                             |
| <span id="Copy_In_Progress"></span><span id="copy_in_progress"></span><span id="COPY_IN_PROGRESS"></span> **Copy In Progress** 15                 | A deferred background copy operation is in progress to copy the source to the replica target for an **UnSyncAssoc** association. |
| <span id="Microsoft_Reserved"></span><span id="microsoft_reserved"></span><span id="MICROSOFT_RESERVED"></span> **Microsoft Reserved** ..         |                                                                                                                                             |
| <span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span> **Vendor Specific** 0x8000..               |                                                                                                                                             |



 

 

**SyncTime**
   

Data type: **DateTime**
 

Access type: Read-only
 

The point in time that the virtual disks were synchronized.

 

**SyncType**
   

Data type: **UInt16**
 

Access type: Read-only
 

Describes the intended outcome of the replication.



| Value                                                                                                                                                                                                                                                                    | Meaning                                                        |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| <span id="Microsoft_Reserved"></span><span id="microsoft_reserved"></span><span id="MICROSOFT_RESERVED"></span> **Microsoft Reserved** ..  |                                                                |
| <span id="Mirror"></span><span id="mirror"></span><span id="MIRROR"></span> **Mirror** 6                                                   | Create and maintain a copy of the source.           |
| <span id="Snapshot"></span><span id="snapshot"></span><span id="SNAPSHOT"></span> **Snapshot** 7                                           | Create a point-in-time, virtual copy of the source. |
| <span id="Clone"></span><span id="clone"></span><span id="CLONE"></span> **Clone** 8                                                       | Create a point-in-time, full copy the source.       |
| <span id="Microsoft_Reserved"></span><span id="microsoft_reserved"></span><span id="MICROSOFT_RESERVED"></span> **Microsoft Reserved** ..  |                                                                |
| <span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span> **Vendor Specific** 0x8000..        |                                                                |



 

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 10 \[desktop apps only\]                                               |
| Minimum supported server | Windows Server 2016 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



 

 





