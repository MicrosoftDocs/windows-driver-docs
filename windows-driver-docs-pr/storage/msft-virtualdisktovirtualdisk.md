---
title: MSFT\_VirtualDiskToVirtualDisk class
description: Association between a source VirtualDisk and a target VirtualDisk.
ms.assetid: 6C0F1564-E5C0-42D9-94DA-EFE0B32815B7
keywords:
- MSFT_VirtualDiskToVirtualDisk class Windows Storage Management API
- MSFT_VirtualDiskToVirtualDisk class Windows Storage Management API , described
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_VirtualDiskToVirtualDisk
- MSFT_VirtualDiskToVirtualDisk.SourceVirtualDisk
- MSFT_VirtualDiskToVirtualDisk.TargetVirtualDisk
- MSFT_VirtualDiskToVirtualDisk.SyncTime
- MSFT_VirtualDiskToVirtualDisk.SyncMaintained
- MSFT_VirtualDiskToVirtualDisk.CopyState
- MSFT_VirtualDiskToVirtualDisk.RequestedCopyState
- MSFT_VirtualDiskToVirtualDisk.SyncType
- MSFT_VirtualDiskToVirtualDisk.SyncMode
- MSFT_VirtualDiskToVirtualDisk.ProgressStatus
- MSFT_VirtualDiskToVirtualDisk.PercentSynced
- MSFT_VirtualDiskToVirtualDisk.CopyType
- MSFT_VirtualDiskToVirtualDisk.ReplicaType
- MSFT_VirtualDiskToVirtualDisk.SyncState
- MSFT_VirtualDiskToVirtualDisk.CopyPriority
- MSFT_VirtualDiskToVirtualDisk.CopyMethodology
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# MSFT\_VirtualDiskToVirtualDisk class

Association between a source [**VirtualDisk**](msft-virtualdisk.md) and a target **VirtualDisk**.

The target virtual disk is a mirror, snapshot, or clone of the source virtual disk.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_VirtualDiskToVirtualDisk
{
  MSFT_VirtualDisk REF SourceVirtualDisk;
  MSFT_VirtualDisk REF TargetVirtualDisk;
  Datetime             SyncTime;
  Boolean              SyncMaintained;
  UInt16               CopyState;
  UInt16               RequestedCopyState;
  UInt16               SyncType;
  UInt16               SyncMode;
  UInt16               ProgressStatus;
  UInt16               PercentSynced;
  UInt16               CopyType;
  UInt16               ReplicaType;
  UInt16               SyncState;
  UInt16               CopyPriority;
  UInt16               CopyMethodology;
};
```

## Members

The **MSFT\_VirtualDiskToVirtualDisk** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_VirtualDiskToVirtualDisk** class has these properties.

 

**CopyMethodology**
   

Data type: **UInt16**
 

Access type: Read-only
 

Specifies the copy methodology that the copy engine uses to create and maintain the target.

One of the following values.



| Value                                                                                                                                                                                                                                                                                   | Meaning                                                                                                                                        |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Not_Specified"></span><span id="not_specified"></span><span id="NOT_SPECIFIED"></span> **Not Specified** 0                                      | The method of maintaining the copy is not specified.                                                                                |
| <span id="Other"></span><span id="other"></span><span id="OTHER"></span> **Other** 1                                                                      | The copy engine uses a vendor-specific copy methodology to create and maintain the target.                                          |
| <span id="Implementation_decides"></span><span id="implementation_decides"></span><span id="IMPLEMENTATION_DECIDES"></span> **Implementation decides** 2  | The implementation chooses the copy methodology.                                                                                    |
| <span id="Full_Copy"></span><span id="full_copy"></span><span id="FULL_COPY"></span> **Full Copy** 3                                                      | A full copy of the source is generated.                                                                                             |
| <span id="Incremental-Copy"></span><span id="incremental-copy"></span><span id="INCREMENTAL-COPY"></span> **Incremental-Copy** 4                          | Only changed data from the source is copied to the target.                                                                          |
| <span id="Differential-Copy"></span><span id="differential-copy"></span><span id="DIFFERENTIAL-COPY"></span> **Differential-Copy** 5                      | Only the new writes to the source are copied to the target.                                                                         |
| <span id="Copy-On-Write"></span><span id="copy-on-write"></span><span id="COPY-ON-WRITE"></span> **Copy-On-Write** 6                                      | On the first write to the source, the affected data is copied to the target.                                                        |
| <span id="Copy-On-Access"></span><span id="copy-on-access"></span><span id="COPY-ON-ACCESS"></span> **Copy-On-Access** 7                                  | On the first access to the source, the affected data is copied to the target.                                                       |
| <span id="Delta-Update"></span><span id="delta-update"></span><span id="DELTA-UPDATE"></span> **Delta-Update** 8                                          | Difference-based replication where, after the initial copy, only updates to the source are copied to the target.                    |
| <span id="Snap-And-Clone"></span><span id="snap-and-clone"></span><span id="SNAP-AND-CLONE"></span> **Snap-And-Clone** 9                                  | The service creates a shadow copy of the source first, then uses the shadow copy as the source of the copy operation to the target. |
| <span id="Microsoft_Reserved"></span><span id="microsoft_reserved"></span><span id="MICROSOFT_RESERVED"></span> **Microsoft Reserved** ..                 | This value is reserved for system use.                                                                                              |
| <span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span> **Vendor Specific** 0x8000..                       | These values are reserved for vendors.                                                                                              |



 

 

**CopyPriority**
   

Data type: **UInt16**
 

Access type: Read-only
 

Allows the priority of background copy engine I/O to be managed relative to host I/O operations during a sequential background copy operation.

One of the following values.



| Value                                                                                                                                                                                                                                                                    | Meaning                                                                |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| <span id="Not_Managed"></span><span id="not_managed"></span><span id="NOT_MANAGED"></span> **Not Managed** 0                               | The priority of copy engine I/O to host I/O is not managed. |
| <span id="Low"></span><span id="low"></span><span id="LOW"></span> **Low** 1                                                               | Copy engine I/O is lower priority than host I/O.            |
| <span id="Same"></span><span id="same"></span><span id="SAME"></span> **Same** 2                                                           | Copy engine I/O has the same priority as host I/O.          |
| <span id="High"></span><span id="high"></span><span id="HIGH"></span> **High** 3                                                           | Copy engine I/O has higher priority than host I/O.          |
| <span id="Microsoft_Reserved"></span><span id="microsoft_reserved"></span><span id="MICROSOFT_RESERVED"></span> **Microsoft Reserved** ..  | This value is reserved for system use.                      |
| <span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span> **Vendor Specific** 0x8000..        | These values are reserved for vendors.                      |



 

 

**CopyState**
   

Data type: **UInt16**
 

Access type: Read-only
 

The replication state of the association. One of the following values.



| Value                                                                                                                                                                                                                                                                    | Meaning                                                                                                                                                                                 |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Initialized"></span><span id="initialized"></span><span id="INITIALIZED"></span> **Initialized** 2                               | The link to enable replication is established, and the source and target have been associated. However, the copy operation has not started.                                  |
| <span id="Unsynchronized"></span><span id="unsynchronized"></span><span id="UNSYNCHRONIZED"></span> **Unsynchronized** 3                   | Not all of the source data has been copied to the target.                                                                                                                    |
| <span id="Synchronized"></span><span id="synchronized"></span><span id="SYNCHRONIZED"></span> **Synchronized** 4                           | All of the source data has been copied to the target.                                                                                                                        |
| <span id="Broken"></span><span id="broken"></span><span id="BROKEN"></span> **Broken** 5                                                   | The relationship is nonfunctional due to errors in the source, the target, the path between the two, or space constraints.                                                   |
| <span id="Fractured"></span><span id="fractured"></span><span id="FRACTURED"></span> **Fractured** 6                                       | The target is split from the source.                                                                                                                                         |
| <span id="Split"></span><span id="split"></span><span id="SPLIT"></span> **Split** 7                                                       | The target was gracefully (or systematically) split from the source in a way that ensures consistency.                                                                       |
| <span id="Inactive"></span><span id="inactive"></span><span id="INACTIVE"></span> **Inactive** 8                                           | The copy operation has stopped. Writes to the source will not be sent to the target.                                                                                         |
| <span id="Suspended"></span><span id="suspended"></span><span id="SUSPENDED"></span> **Suspended** 9                                       | Data flow between the source and target has stopped. Writes to the source are held until the association is resumed.                                                         |
| <span id="Failedover"></span><span id="failedover"></span><span id="FAILEDOVER"></span> **Failedover** 10                                  | Reads from and writes to the target have failed. The source is not reachable.                                                                                                |
| <span id="Prepared"></span><span id="prepared"></span><span id="PREPARED"></span> **Prepared** 11                                          | Initialization is completed, and the copy operation has started. However, the data flow has not started.                                                                     |
| <span id="Aborted"></span><span id="aborted"></span><span id="ABORTED"></span> **Aborted** 12                                              | The copy operation was aborted. Use the Resync Replica operation to restart the copy operation.                                                                              |
| <span id="Skewed"></span><span id="skewed"></span><span id="SKEWED"></span> **Skewed** 13                                                  | The target has been modified and is no longer synchronized with the source or the point-in-time view.                                                                        |
| <span id="Mixed"></span><span id="mixed"></span><span id="MIXED"></span> **Mixed** 14                                                      | Applies to the *CopyState* of *GroupSynchronized*. It indicates that the *StorageSynchronized* associations of the elements in the groups have different *CopyState* values. |
| <span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span> **Not Applicable** 15                  | The target does not have a replication state.                                                                                                                                |
| <span id="Microsoft_Reserved"></span><span id="microsoft_reserved"></span><span id="MICROSOFT_RESERVED"></span> **Microsoft Reserved** ..  | This value is reserved for system use.                                                                                                                                       |
| <span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span> **Vendor Specific** 0x8000..        | These values are reserved for vendors.                                                                                                                                       |



 

 

**CopyType**
   

Data type: **UInt16**
 

Access type: Read-only
 

The replication policy for the association.

One of the following values.



| Value                                                                                                                                                                                                                                                                    | Meaning                                                                                                                      |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| <span id="Async"></span><span id="async"></span><span id="ASYNC"></span> **Async** 2                                                       | Create and maintain an asynchronous copy of the source.                                                           |
| <span id="Sync"></span><span id="sync"></span><span id="SYNC"></span> **Sync** 3                                                           | Create and maintain a synchronized copy of the source.                                                            |
| <span id="UnSyncAssoc"></span><span id="unsyncassoc"></span><span id="UNSYNCASSOC"></span> **UnSyncAssoc** 4                               | Create an unsynchronized copy and maintain an association to the source.                                          |
| <span id="UnSyncUnAssoc"></span><span id="unsyncunassoc"></span><span id="UNSYNCUNASSOC"></span> **UnSyncUnAssoc** 5                       | Create an unsynchronized copy with a temporary association that is deleted upon completion of the copy operation. |
| <span id="Microsoft_Reserved"></span><span id="microsoft_reserved"></span><span id="MICROSOFT_RESERVED"></span> **Microsoft Reserved** ..  | This value is reserved for system use.                                                                            |
| <span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span> **Vendor Specific** 0x8000..        | These values are reserved for vendors.                                                                            |



 

 

**PercentSynced**
   

Data type: **UInt16**
 

Access type: Read-only
 

The percentage of the work completed to reach synchronization. Must be set to NULL if implementation is not capable of providing this information.

 

**ProgressStatus**
   

Data type: **UInt16**
 

Access type: Read-only
 

The status of the association with respect to replication activity.

One of the following values.



| Value                                                                                                                                                                                                                                                                    | Meaning                                                                                                                                                               |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span> **Unknown** 0                                               | The status of the association is unknown.                                                                                                                  |
| <span id="Completed"></span><span id="completed"></span><span id="COMPLETED"></span> **Completed** 2                                       | The request has been completed. The copy operation is idle.                                                                                                |
| <span id="Dormant"></span><span id="dormant"></span><span id="DORMANT"></span> **Dormant** 3                                               | The copy operation is inactive, suspended, or quiesced.                                                                                                    |
| <span id="Initializing"></span><span id="initializing"></span><span id="INITIALIZING"></span> **Initializing** 4                           | The source-to-target association is in the process of being initialized, and the copy operation has not started.                                           |
| <span id="Preparing"></span><span id="preparing"></span><span id="PREPARING"></span> **Preparing** 5                                       | The copy operation is in the process of being prepared.                                                                                                    |
| <span id="Synchronizing"></span><span id="synchronizing"></span><span id="SYNCHRONIZING"></span> **Synchronizing** 6                       | The source and target are in the process of being synchronized.                                                                                            |
| <span id="Resyncing"></span><span id="resyncing"></span><span id="RESYNCING"></span> **Resyncing** 7                                       | The source and target are in the process of being resynchronized.                                                                                          |
| <span id="Restoring"></span><span id="restoring"></span><span id="RESTORING"></span> **Restoring** 8                                       | The source is in the process of being restored from the target.                                                                                            |
| <span id="Fracturing"></span><span id="fracturing"></span><span id="FRACTURING"></span> **Fracturing** 9                                   | A fracture is in progress.                                                                                                                                 |
| <span id="Splitting"></span><span id="splitting"></span><span id="SPLITTING"></span> **Splitting** 10                                      | A split is in progress.                                                                                                                                    |
| <span id="Failing_over"></span><span id="failing_over"></span><span id="FAILING_OVER"></span> **Failing over** 11                          | A failover is in progress. This means that the source and target are being switched.                                                                       |
| <span id="Failing_back"></span><span id="failing_back"></span><span id="FAILING_BACK"></span> **Failing back** 12                          | The result of failover is being undone.                                                                                                                    |
| <span id="Aborting"></span><span id="aborting"></span><span id="ABORTING"></span> **Aborting** 13                                          | The operation is in the process of being aborted.                                                                                                          |
| <span id="Mixed"></span><span id="mixed"></span><span id="MIXED"></span> **Mixed** 14                                                      | This value applies to groups with element pairs with different statuses. Generally, the individual statuses need to examined.                              |
| <span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span> **Not Applicable** 15                  | The target does not have a progress status.                                                                                                                |
| <span id="Suspending"></span><span id="suspending"></span><span id="SUSPENDING"></span> **Suspending** 16                                  | The copy operation is in the process of being suspended.                                                                                                   |
| <span id="Requires_fracture"></span><span id="requires_fracture"></span><span id="REQUIRES_FRACTURE"></span> **Requires fracture** 17      | The requested operation has completed. However, the synchronization relationship needs to be fractured before further copy operations can be issued.       |
| <span id="Requires_resync"></span><span id="requires_resync"></span><span id="REQUIRES_RESYNC"></span> **Requires resync** 18              | The requested operation has completed, however, the synchronization relationship needs to be resynchronized before further copy operations can be started. |
| <span id="Requires_activate"></span><span id="requires_activate"></span><span id="REQUIRES_ACTIVATE"></span> **Requires activate** 19      | The requested operation has completed, however, the synchronization relationship needs to be activated before further copy operations can be started.      |
| <span id="Pending"></span><span id="pending"></span><span id="PENDING"></span> **Pending** 20                                              | The flow of data has stopped momentarily due to limited bandwidth or busy system.                                                                          |
| <span id="Detaching"></span><span id="detaching"></span><span id="DETACHING"></span> **Detaching** 21                                      | The target is being detached from the source.                                                                                                              |
| <span id="Microsoft_Reserved"></span><span id="microsoft_reserved"></span><span id="MICROSOFT_RESERVED"></span> **Microsoft Reserved** ..  | This value is reserved for system use.                                                                                                                     |
| <span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span> **Vendor Specific** 0x8000..        | These values are reserved for vendors.                                                                                                                     |



 

 

**ReplicaType**
   

Data type: **UInt16**
 

Access type: Read-only
 

Provides information on how the replica is being maintained.

One of the following values.



| Value                                                                                                                                                                                                                                                                    | Meaning                                                                      |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| <span id="Not_Specified"></span><span id="not_specified"></span><span id="NOT_SPECIFIED"></span> **Not Specified** 0                       | The method of maintaining the copy is not specified.              |
| <span id="Full_Copy"></span><span id="full_copy"></span><span id="FULL_COPY"></span> **Full Copy** 2                                       | A full copy of the source will be created.                        |
| <span id="Before_Delta"></span><span id="before_delta"></span><span id="BEFORE_DELTA"></span> **Before Delta** 3                           | The source will be maintained as delta data from the target.      |
| <span id="After_Delta"></span><span id="after_delta"></span><span id="AFTER_DELTA"></span> **After Delta** 4                               | The target will be maintained as delta data from the source.      |
| <span id="Log"></span><span id="log"></span><span id="LOG"></span> **Log** 5                                                               | The target is being maintained as a log of changes to the source. |
| <span id="Microsoft_Reserved"></span><span id="microsoft_reserved"></span><span id="MICROSOFT_RESERVED"></span> **Microsoft Reserved** ..  | This value is reserved for system use.                            |
| <span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span> **Vendor Specific** 0x8000..        | These value are reserved for vendors.                             |



 

 

**RequestedCopyState**
   

Data type: **UInt16**
 

Access type: Read-only
 

The last requested or desired state for the association. The actual state of the association is represented by the **CopyState** property. Note that when **CopyState** reaches the requested state, this property will be set to **Not Applicable**.

The default value of this property is **Not Applicable**.

 

**SourceVirtualDisk**
   

Data type: **[**MSFT\_VirtualDisk**](msft-virtualdisk.md)**
 

Access type: Read-only
 

Qualifiers: [**Key**](/windows/win32/wmisdk/standard-qualifiers)
 

The source virtual disk.

 

**SyncMaintained**
   

Data type: **Boolean**
 

Access type: Read-only
 

**TRUE** if synchronization is maintained.

 

**SyncMode**
   

Data type: **UInt16**
 

Access type: Read-only
 

Describes whether the target will be updated synchronously or asynchronously. If **NULL**, the implementation chooses the mode.

One of the following values.

 

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
 

<span id="Synchronous"></span><span id="synchronous"></span><span id="SYNCHRONOUS"></span>**Synchronous** (2)
 

<span id="Asynchronous"></span><span id="asynchronous"></span><span id="ASYNCHRONOUS"></span>**Asynchronous** (3)
 

<span id="Microsoft_Reserved"></span><span id="microsoft_reserved"></span><span id="MICROSOFT_RESERVED"></span>**Microsoft Reserved** (..)
 

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>**Vendor Specific** (32768..65535)
 

 

**SyncState**
   

Data type: **UInt16**
 

Access type: Read-only
 

The state of the association with respect to replication activity.

One of the following values.



| Value                                                                                                                                                                                                                                                                            | Meaning                                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Initialized"></span><span id="initialized"></span><span id="INITIALIZED"></span> **Initialized** 2                                       | The link to enable replication is established, and the source and target are associated, but the copy engine has not started.                                       |
| <span id="PrepareInProgress"></span><span id="prepareinprogress"></span><span id="PREPAREINPROGRESS"></span> **PrepareInProgress** 3               | Preparation for replication is in progress and the copy engine has started.                                                                                         |
| <span id="Prepared"></span><span id="prepared"></span><span id="PREPARED"></span> **Prepared** 4                                                   | All necessary preparation has completed.                                                                                                                            |
| <span id="ResyncInProgress"></span><span id="resyncinprogress"></span><span id="RESYNCINPROGRESS"></span> **ResyncInProgress** 5                   | Synchronization or resynchronization is in progress. This may be the initial copy or subsequent changes being copied.                                               |
| <span id="Synchronized"></span><span id="synchronized"></span><span id="SYNCHRONIZED"></span> **Synchronized** 6                                   | An asynchronous or synchronous replication is currently synchronized. When this value is set, the **SyncMaintained** property will be **TRUE**.                     |
| <span id="Fracture_In_Progress"></span><span id="fracture_in_progress"></span><span id="FRACTURE_IN_PROGRESS"></span> **Fracture In Progress** 7   | An operation to fracture an asynchronous or synchronous replication is in progress.                                                                                 |
| <span id="QuiesceInProgress"></span><span id="quiesceinprogress"></span><span id="QUIESCEINPROGRESS"></span> **QuiesceInProgress** 8               | A quiesce operation is in progress.                                                                                                                                 |
| <span id="Quiesced"></span><span id="quiesced"></span><span id="QUIESCED"></span> **Quiesced** 9                                                   | The replication has been quiesced and is ready for a change.                                                                                                        |
| <span id="Restore_In_Progresss"></span><span id="restore_in_progresss"></span><span id="RESTORE_IN_PROGRESSS"></span> **Restore In Progresss** 10  | An operation is in progress to copy the synchronized object to the System object.                                                                                   |
| <span id="Idle"></span><span id="idle"></span><span id="IDLE"></span> **Idle** 11                                                                  | The normal state for the replica if the **CopyType** property is **UnSyncAssoc**.                                                                                   |
| <span id="Broken"></span><span id="broken"></span><span id="BROKEN"></span> **Broken** 12                                                          | The relationship is nonfunctional due to errors in the source, the target, the path between the two or space constraints.                                           |
| <span id="Fractured"></span><span id="fractured"></span><span id="FRACTURED"></span> **Fractured** 13                                              | The replication is fractured.                                                                                                                                       |
| <span id="Frozen"></span><span id="frozen"></span><span id="FROZEN"></span> **Frozen** 14                                                          | All blocks copied from source to an UnSyncAssoc replica and the copy engine is stopped.                                                                             |
| <span id="Copy_In_Progress"></span><span id="copy_in_progress"></span><span id="COPY_IN_PROGRESS"></span> **Copy In Progress** 15                  | A deferred background copy operation is in progress to copy the source to the replica target. This will only occur if the **CopyType** property is **UnSyncAssoc**. |
| <span id="Microsoft_Reserved"></span><span id="microsoft_reserved"></span><span id="MICROSOFT_RESERVED"></span> **Microsoft Reserved** ..          | This value is reserved for system use.                                                                                                                              |
| <span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span> **Vendor Specific** 0x8000..                | These values are reserved for vendors.                                                                                                                              |



 

 

**SyncTime**
   

Data type: **Datetime**
 

Access type: Read-only
 

The last time when the source and target virtual disks were synchronized.

 

**SyncType**
   

Data type: **UInt16**
 

Access type: Read-only
 

The intended outcome of the replication. One of the following values.



| Value                                                                                                                                                                                                                                                                    | Meaning                                                     |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| <span id="Microsoft_Reserved"></span><span id="microsoft_reserved"></span><span id="MICROSOFT_RESERVED"></span> **Microsoft Reserved** ..  | This value is reserved for system use.           |
| <span id="Mirror"></span><span id="mirror"></span><span id="MIRROR"></span> **Mirror** 6                                                   | Create and maintain a copy of the source.        |
| <span id="Snapshot"></span><span id="snapshot"></span><span id="SNAPSHOT"></span> **Snapshot** 7                                           | Create a volume shadow copy of the source.       |
| <span id="Clone"></span><span id="clone"></span><span id="CLONE"></span> **Clone** 8                                                       | Create a point-in-time, full copy of the source. |
| <span id="Microsoft_Reserved"></span><span id="microsoft_reserved"></span><span id="MICROSOFT_RESERVED"></span> **Microsoft Reserved** ..  | This value is reserved for system use.           |
| <span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span> **Vendor Specific** 0x8000..        | These values are reserved for vendors.           |



 

 

**TargetVirtualDisk**
   

Data type: **MSFT\_VirtualDisk**
 

Access type: Read-only
 

Qualifiers: [**Key**](/windows/win32/wmisdk/standard-qualifiers)
 

The target virtual disk.

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_VirtualDisk**](msft-virtualdisk.md)
 

 

