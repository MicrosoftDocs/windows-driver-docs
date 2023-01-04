---
title: MSFT\_VirtualDisk class
description: Represents a subsystem storage volume.
ms.assetid: 4f0d6967-ab9c-494f-a991-f62fda8c2fa8
keywords:
- MSFT_VirtualDisk class Windows Storage Management API
- MSFT_VirtualDisk class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_VirtualDisk
- MSFT_VirtualDisk.FriendlyName
- MSFT_VirtualDisk.Name
- MSFT_VirtualDisk.NameFormat
- MSFT_VirtualDisk.UniqueIdFormat
- MSFT_VirtualDisk.UniqueIdFormatDescription
- MSFT_VirtualDisk.Usage
- MSFT_VirtualDisk.OtherUsageDescription
- MSFT_VirtualDisk.HealthStatus
- MSFT_VirtualDisk.OperationalStatus
- MSFT_VirtualDisk.OtherOperationalStatusDescription
- MSFT_VirtualDisk.ResiliencySettingName
- MSFT_VirtualDisk.Size
- MSFT_VirtualDisk.AllocatedSize
- MSFT_VirtualDisk.LogicalSectorSize
- MSFT_VirtualDisk.PhysicalSectorSize
- MSFT_VirtualDisk.FootprintOnPool
- MSFT_VirtualDisk.ProvisioningType
- MSFT_VirtualDisk.NumberOfDataCopies
- MSFT_VirtualDisk.PhysicalDiskRedundancy
- MSFT_VirtualDisk.ParityLayout
- MSFT_VirtualDisk.NumberOfColumns
- MSFT_VirtualDisk.Interleave
- MSFT_VirtualDisk.RequestNoSinglePointOfFailure
- MSFT_VirtualDisk.Access
- MSFT_VirtualDisk.IsSnapshot
- MSFT_VirtualDisk.IsManualAttach
- MSFT_VirtualDisk.IsDeduplicationEnabled
- MSFT_VirtualDisk.IsEnclosureAware
- MSFT_VirtualDisk.NumberOfAvailableCopies
- MSFT_VirtualDisk.DetachedReason
- MSFT_VirtualDisk.WriteCacheSize
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_VirtualDisk class

Represents a subsystem storage volume.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
class MSFT_VirtualDisk : MSFT_StorageObject
{
  String  FriendlyName;
  String  Name;
  UInt16  NameFormat;
  UInt16  UniqueIdFormat;
  String  UniqueIdFormatDescription;
  UInt16  Usage;
  String  OtherUsageDescription;
  UInt16  HealthStatus;
  UInt16  OperationalStatus[];
  String  OtherOperationalStatusDescription;
  String  ResiliencySettingName;
  UInt64  Size;
  UInt64  AllocatedSize;
  UInt64  LogicalSectorSize;
  UInt64  PhysicalSectorSize;
  UInt64  FootprintOnPool;
  UInt16  ProvisioningType;
  UInt16  NumberOfDataCopies;
  UInt16  PhysicalDiskRedundancy;
  UInt16  ParityLayout;
  UInt16  NumberOfColumns;
  UInt64  Interleave;
  Boolean RequestNoSinglePointOfFailure;
  UInt16  Access;
  Boolean IsSnapshot;
  Boolean IsManualAttach;
  Boolean IsDeduplicationEnabled;
  Boolean IsEnclosureAware;
  UInt16  NumberOfAvailableCopies;
  UInt16  DetachedReason;
  UInt64  WriteCacheSize;
};
```

## Members

The **MSFT\_VirtualDisk** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_VirtualDisk** class has these methods.



| Method                                                                            | Description                                                                                                                                    |
|:----------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddPhysicalDisk**](msft-virtualdisk-addphysicaldisk.md)                       | Adds one or more physical disks for manual allocation.                                                                              |
| [**Attach**](msft-virtualdisk-attach.md)                                         | Attaches the virtual disk.                                                                                                          |
| [**CreateClone**](msft-virtualdisk-createclone.md)                               | Creates a new virtual disk that is a clone of the existing virtual disk.                                                            |
| [**CreateReplica**](msft-virtualdisk-createremotereplica.md)                     | Creates a replication relationship between virtual disks.                                                                           |
| [**CreateSnapshot**](msft-virtualdisk-createsnapshot.md)                         | Creates a clone of a virtual disk, resulting in a new virtual disk whose data is identical to that of the original virtual disk.    |
| [**DeleteObject**](msft-virtualdisk-deleteobject.md)                             | Deletes the virtual disk.                                                                                                           |
| [**Detach**](msft-virtualdisk-detach.md)                                         | Detaches the virtual disk.                                                                                                          |
| [**GetSecurityDescriptor**](msft-virtualdisk-getsecuritydescriptor.md)           | Retrieves the security descriptor that controls access to the virtual disk object instance.                                         |
| [**Hide**](msft-virtualdisk-hide.md)                                             | Hides the virtual disk.                                                                                                             |
| [**RemovePhysicalDisk**](msft-virtualdisk-removephysicaldisk.md)                 | Removes one or more physical disks from manual allocation.                                                                          |
| [**Repair**](msft-virtualdisk-repair.md)                                         | Initiates a repair of the virtual disk, restoring data and redundancy to different (or new) physical disks within the storage pool. |
| [**Resize**](msft-virtualdisk-resize.md)                                         | Resizes the virtual disk.                                                                                                           |
| [**SetAttributes**](msft-virtualdisk-setattributes.md)                           | Sets or updates various attributes for the virtual disk.                                                                            |
| [**SetFriendlyName**](msft-virtualdisk-setfriendlyname.md)                       | Sets the friendly name for the virtual disk.                                                                                        |
| [**SetReplicationRelationship**](msft-virtualdisk-setreplicationrelationship.md) | Sets the replication relationship between virtual disks.                                                                            |
| [**SetSecurityDescriptor**](msft-virtualdisk-setsecuritydescriptor.md)           | Sets the security descriptor that controls access to the virtual disk object instance.                                              |
| [**SetUsage**](msft-virtualdisk-setusage.md)                                     | Sets the intended usage for the virtual disk.                                                                                       |
| [**Show**](msft-virtualdisk-show.md)                                             | Exposes the virtual disk.                                                                                                           |



 

### Properties

The **MSFT\_VirtualDisk** class has these properties.

 

**Access**
   

Data type: **UInt16**
 

Access type: Read-only
 

Indicates whether the virtual disk is available for read and write access.

 

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
 

<span id="Readable"></span><span id="readable"></span><span id="READABLE"></span>**Readable** (1)
 

<span id="Writeable"></span><span id="writeable"></span><span id="WRITEABLE"></span>**Writeable** (2)
 

<span id="Read_Write"></span><span id="read_write"></span><span id="READ_WRITE"></span>**Read/Write** (3)
 

<span id="Write_Once"></span><span id="write_once"></span><span id="WRITE_ONCE"></span>**Write Once** (4)
 

 

**AllocatedSize**
   

Data type: **UInt64**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers), [**Units**](/windows/win32/wmisdk/standard-qualifiers) ("Bytes")
 

The currently allocated size of the virtual disk. If the virtual disk's **ProvisioningType** is **Fixed**, **AllocatedSize** should equal **Size**. If the **ProvisioningType** is **Thin**, this value is the amount of space actually allocated (which must be less than **Size**).

 

**DetachedReason**
   

Data type: **UInt16**
 

Access type: Read-only
 

The reason why this virtual disk is detached. This property will only be set when the virtual disk's **OperationalStatus** includes **Detached**. Note that this field is specific to storage spaces.

 

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
 

<span id="None"></span><span id="none"></span><span id="NONE"></span>**None** (1)
 

<span id="By_Policy"></span><span id="by_policy"></span><span id="BY_POLICY"></span>**By Policy** (2)
 

<span id="Majority_Disks_Unhealthy"></span><span id="majority_disks_unhealthy"></span><span id="MAJORITY_DISKS_UNHEALTHY"></span>**Majority Disks Unhealthy** (3)
 

<span id="Incomplete"></span><span id="incomplete"></span><span id="INCOMPLETE"></span>**Incomplete** (4)
 

 

**FootprintOnPool**
   

Data type: **UInt64**
 

Access type: Read-only
 

Qualifiers: [**Units**](/windows/win32/wmisdk/standard-qualifiers) ("Bytes")
 

The total storage pool capacity, in bytes, that is being consumed by this virtual disk. For example, in the case of a 2-way mirrored virtual disk whose size is 1 GB, the footprint in the pool would be approximately 2 GB.

 

**FriendlyName**
   

Data type: **String**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

A user-settable, display oriented string containing the name of the virtual disk.

 

**HealthStatus**
   

Data type: **UInt16**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

The health status of the virtual disk.

Health of a virtual disk is derived from the health of the backing physical disks, and whether or not the virtual disk can maintain the required levels of resiliency.



| Value                                                                                                                                                                                                                                | Meaning                                                                                                                          |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| <span id="Healthy"></span><span id="healthy"></span><span id="HEALTHY"></span> **Healthy** 0           | All physical disks are present and in a healthy state.                                                                |
| <span id="Warning"></span><span id="warning"></span><span id="WARNING"></span> **Warning** 1           | The majority of physical disks are healthy, but one or more may be failing I/O requests.                              |
| <span id="Unhealthy"></span><span id="unhealthy"></span><span id="UNHEALTHY"></span> **Unhealthy** 2   | The majority of physical disks are unhealthy or in a failed state, and the virtual disk no longer has data integrity. |
| <span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span> **Unknown** 5           | The health status is unknown.                                                                                         |



 

 

**Interleave**
   

Data type: **UInt64**
 

Access type: Read-only
 

The number of bytes that will form a strip in common striping-based resiliency settings. The strip is defined as the size of the portion of a stripe that lies on one physical disk. Thus **Interleave** \* **NumberOfColumns** will yield the size of one stripe of user data.

 

**IsDeduplicationEnabled**
   

Data type: **Boolean**
 

Access type: Read/write
 

**TRUE** if data deduplication is enabled for the virtual disk.

 

**IsEnclosureAware**
   

Data type: **Boolean**
 

Access type: Read-only
 

The current allocation behavior for this virtual disk. Enclosure-aware virtual disks will intelligently pick the physical disks to use for their redundancy. If **TRUE**, the virtual disk will attempt to use physical disks from different enclosures to balance the fault tolerance between two or more physical enclosures.

 

**IsManualAttach**
   

Data type: **Boolean**
 

Access type: Read/write
 

**TRUE** if this virtual disk will only be attached to the system if an explicit call is made to the [**Attach**](msft-virtualdisk-attach.md) method. Note that this property is specific to storage spaces.

 

**IsSnapshot**
   

Data type: **Boolean**
 

Access type: Read-only
 

**TRUE** if this virtual disk is a shadow copy of another virtual disk.

 

**LogicalSectorSize**
   

Data type: **UInt64**
 

Access type: Read-only
 

Qualifiers: [**Units**](/windows/win32/wmisdk/standard-qualifiers) ("Bytes")
 

The logical sector size of the virtual disk, in bytes.

 

**Name**
   

Data type: **String**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

A semi-unique (scoped to the owning storage subsystem), human-readable string that is used to identify the virtual disk.

 

**NameFormat**
   

Data type: **UInt16**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

The format of the **Name** property.

 

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
 

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)
 

<span id="VPD83NAA6"></span><span id="vpd83naa6"></span>**VPD83NAA6** (2)
 

<span id="VPD83NAA5"></span><span id="vpd83naa5"></span>**VPD83NAA5** (3)
 

<span id="VPD83Type2"></span><span id="vpd83type2"></span><span id="VPD83TYPE2"></span>**VPD83Type2** (4)
 

<span id="VPD83Type1"></span><span id="vpd83type1"></span><span id="VPD83TYPE1"></span>**VPD83Type1** (5)
 

<span id="VPD83Type0"></span><span id="vpd83type0"></span><span id="VPD83TYPE0"></span>**VPD83Type0** (6)
 

<span id="SNVM"></span><span id="snvm"></span>**SNVM** (7)
 

<span id="NodeWWN"></span><span id="nodewwn"></span><span id="NODEWWN"></span>**NodeWWN** (8)
 

<span id="NAA"></span><span id="naa"></span>**NAA** (9)
 

<span id="EUI64"></span><span id="eui64"></span>**EUI64** (10)
 

<span id="T10VID"></span><span id="t10vid"></span>**T10VID** (11)
 

 

**NumberOfAvailableCopies**
   

Data type: **UInt16**
 

Access type: Read-only
 

The number of consistent copies of data that are available.

 

**NumberOfColumns**
   

Data type: **UInt16**
 

Access type: Read-only
 

The number of underlying physical disks across which the data for this virtual disk is striped.

 

**NumberOfDataCopies**
   

Data type: **UInt16**
 

Access type: Read-only
 

The number of complete data copies that are being maintained for the virtual disk. For example, RAID 5 maintains one copy of data, while RAID 1 maintains at least two copies.

 

**OperationalStatus**
   

Data type: **UInt16** array
 

Access type: Read-only
 

An array of values that indicate the current operating conditions of the virtual disk. Unlike **HealthStatus**, this property indicates the status of hardware, software, and infrastructure issues related to this virtual disk, and can contain multiple values.



| Value                                                                                                                                                                                                                                                                                                    | Meaning                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span> **Unknown** 0                                                                               | The operational status is unknown.                                                                                              |
| <span id="Other"></span><span id="other"></span><span id="OTHER"></span> **Other** 1                                                                                       | A vendor-specific **OperationalStatus** has been specified by setting the **OtherOperationalStatusDescription** property.       |
| <span id="OK"></span><span id="ok"></span> **OK** 2                                                                                                                        | The virtual disk is responding to commands and is in a normal operating state.                                                  |
| <span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span> **Degraded** 3                                                                           | The virtual disk is responding to commands, but is not running in an optimal operating state.                                   |
| <span id="Stressed"></span><span id="stressed"></span><span id="STRESSED"></span> **Stressed** 4                                                                           |                                                                                                                                            |
| <span id="Predictive_Failure"></span><span id="predictive_failure"></span><span id="PREDICTIVE_FAILURE"></span> **Predictive Failure** 5                                   |                                                                                                                                            |
| <span id="Error"></span><span id="error"></span><span id="ERROR"></span> **Error** 6                                                                                       |                                                                                                                                            |
| <span id="Non-Recoverable_Error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span> **Non-Recoverable Error** 7                       |                                                                                                                                            |
| <span id="Starting"></span><span id="starting"></span><span id="STARTING"></span> **Starting** 8                                                                           |                                                                                                                                            |
| <span id="Stopping"></span><span id="stopping"></span><span id="STOPPING"></span> **Stopping** 9                                                                           |                                                                                                                                            |
| <span id="Stopped"></span><span id="stopped"></span><span id="STOPPED"></span> **Stopped** 10                                                                              | The virtual disk is responding to commands, but is not running in an optimal operating state.                                   |
| <span id="In_Service"></span><span id="in_service"></span><span id="IN_SERVICE"></span> **In Service** 11                                                                  | The virtual disk is being configured, maintained, cleaned, or otherwise administered.                                           |
| <span id="No_Contact"></span><span id="no_contact"></span><span id="NO_CONTACT"></span> **No Contact** 12                                                                  |                                                                                                                                            |
| <span id="Lost_Communication"></span><span id="lost_communication"></span><span id="LOST_COMMUNICATION"></span> **Lost Communication** 13                                  |                                                                                                                                            |
| <span id="Aborted"></span><span id="aborted"></span><span id="ABORTED"></span> **Aborted** 14                                                                              |                                                                                                                                            |
| <span id="Dormant"></span><span id="dormant"></span><span id="DORMANT"></span> **Dormant** 15                                                                              |                                                                                                                                            |
| <span id="Supporting_Entity_in_Error"></span><span id="supporting_entity_in_error"></span><span id="SUPPORTING_ENTITY_IN_ERROR"></span> **Supporting Entity in Error** 16  |                                                                                                                                            |
| <span id="Completed"></span><span id="completed"></span><span id="COMPLETED"></span> **Completed** 17                                                                      |                                                                                                                                            |
| <span id="Power_Mode"></span><span id="power_mode"></span><span id="POWER_MODE"></span> **Power Mode** 18                                                                  |                                                                                                                                            |
| <span id="Relocating"></span><span id="relocating"></span><span id="RELOCATING"></span> **Relocating** 19                                                                  |                                                                                                                                            |
| <span id="Detached"></span><span id="detached"></span><span id="DETACHED"></span> **Detached** 0xD002                                                                      | This value is reserved for Windows. The virtual disk that is visible to the host system but does not have a disk device object. |
| <span id="Incomplete"></span><span id="incomplete"></span><span id="INCOMPLETE"></span> **Incomplete** 0xD003                                                              | The virtual disk does not have enough redundancy remaining to successfully repair or regenerate its data.                       |



 

 

**OtherOperationalStatusDescription**
   

Data type: **String**
 

Access type: Read-only
 

If **OperationalStatus** contains **Other**, this property is a string containing the vendor defined operational status. This property must be **NULL** if **OperationalStatus** does not contain **Other**.

 

**OtherUsageDescription**
   

Data type: **String**
 

Access type: Read-only
 

If the virtual disk's **Usage** property is set to **Other**, this property must contain a description of the vendor- or user-defined usage. If **Usage** is not set to **Other**, this property must be **NULL**.

 

**ParityLayout**
   

Data type: **UInt16**
 

Access type: Read-only
 

The type of parity layout that is being used for parity-based resiliency settings. This property should be **NULL** if the virtual disk does not use a parity-based resiliency setting.

 

<span id="Non-rotated_Parity"></span><span id="non-rotated_parity"></span><span id="NON-ROTATED_PARITY"></span>**Non-rotated Parity** (1)
 

<span id="Rotated_Parity"></span><span id="rotated_parity"></span><span id="ROTATED_PARITY"></span>**Rotated Parity** (2)
 

 

**PhysicalDiskRedundancy**
   

Data type: **UInt16**
 

Access type: Read-only
 

The number of backing physical disks that can fail without compromising data redundancy. For example: RAID 0 cannot tolerate any failures, RAID 5 can tolerate a single drive failure, and RAID 6 can tolerate two failures.

 

**PhysicalSectorSize**
   

Data type: **UInt64**
 

Access type: Read-only
 

Qualifiers: [**Units**](/windows/win32/wmisdk/standard-qualifiers) ("Bytes")
 

The physical sector size of the virtual disk, in bytes.

 

**ProvisioningType**
   

Data type: **UInt16**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

The provisioning scheme for the virtual disk.



| Value                                                                                                                                                                                                                       | Meaning                                                                     |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| <span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span> **Unknown** 0  | The provisioning scheme is unknown.                              |
| <span id="Thin"></span><span id="thin"></span><span id="THIN"></span> **Thin** 1              | The virtual disk's capacity is allocated on demand.              |
| <span id="Fixed"></span><span id="fixed"></span><span id="FIXED"></span> **Fixed** 2          | The virtual disk's capacity is fully allocated at creation time. |



 

 

**RequestNoSinglePointOfFailure**
   

Data type: **Boolean**
 

Access type: Read-only
 

Set to **TRUE** to request no single point of failure.

 

**ResiliencySettingName**
   

Data type: **String**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers), [**ModelCorrespondence {"MSFT\_ResiliencySetting.Name"}**](/windows/win32/wmisdk/standard-qualifiers)
 

The name of the resiliency setting for the virtual disk.

 

**Size**
   

Data type: **UInt64**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers), [**Units**](/windows/win32/wmisdk/standard-qualifiers) ("Bytes")
 

The logical size, in bytes, of the virtual disk.

 

**UniqueIdFormat**
   

Data type: **UInt16**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers), [**Values**](/windows/win32/wmisdk/standard-qualifiers) ( "Vendor Specific", "Vendor Id", "EUI64", "FCPH Name", "SCSI Name String" ), [**ValueMap**](/windows/win32/wmisdk/standard-qualifiers) ("0", "1", "2", "3", "8"), [**ModelCorrespondence {"MSFT\_StorageObject.UniqueId"}**](/windows/win32/wmisdk/standard-qualifiers)
 

The type of identifier used in the **UniqueId** property that this class inherits from the [**MSFT\_StorageObject**](msft-storageobject.md) class. This identifier must be the highest available identifier using the following order of preference: 8 (highest), 3, 2, 1, 0 (lowest).

For example, if the virtual disk device exposes identifiers of type 0, 1, and 3, **UniqueId** must be the type 3 identifier, and **UniqueIdFormat** should be set to 3.

 

**UniqueIdFormatDescription**
   

Data type: **String**
 

Access type: Read-only
 

Qualifiers: [**ModelCorrespondence {"MSFT\_StorageObject.UniqueId"}**](/windows/win32/wmisdk/standard-qualifiers), [**ModelCorrespondence {"MSFT\_VirtualDisk.UniqueIdFormat"}**](/windows/win32/wmisdk/standard-qualifiers)
 

Certain values for **UniqueIdFormat** may include various sub-formats. This property is a free-form string used to describe the specific format used in **UniqueId**.

 

**Usage**
   

Data type: **UInt16**
 

Access type: Read/write
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

The intended usage for this virtual disk.

 

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
 

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)
 

<span id="Unrestricted"></span><span id="unrestricted"></span><span id="UNRESTRICTED"></span>**Unrestricted** (2)
 

<span id="Reserved_for_ComputerSystem__the_block_server_"></span><span id="reserved_for_computersystem__the_block_server_"></span><span id="RESERVED_FOR_COMPUTERSYSTEM__THE_BLOCK_SERVER_"></span>**Reserved for ComputerSystem (the block server)** (3)
 

<span id="Reserved_by_Replication_Services"></span><span id="reserved_by_replication_services"></span><span id="RESERVED_BY_REPLICATION_SERVICES"></span>**Reserved by Replication Services** (4)
 

<span id="Reserved_by_Migration_Services"></span><span id="reserved_by_migration_services"></span><span id="RESERVED_BY_MIGRATION_SERVICES"></span>**Reserved by Migration Services** (5)
 

<span id="Local_Replica_Source"></span><span id="local_replica_source"></span><span id="LOCAL_REPLICA_SOURCE"></span>**Local Replica Source** (6)
 

<span id="Remote_Replica_Source"></span><span id="remote_replica_source"></span><span id="REMOTE_REPLICA_SOURCE"></span>**Remote Replica Source** (7)
 

<span id="Local_Replica_Target"></span><span id="local_replica_target"></span><span id="LOCAL_REPLICA_TARGET"></span>**Local Replica Target** (8)
 

<span id="Remote_Replica_Target"></span><span id="remote_replica_target"></span><span id="REMOTE_REPLICA_TARGET"></span>**Remote Replica Target** (9)
 

<span id="Local_Replica_Source_or_Target"></span><span id="local_replica_source_or_target"></span><span id="LOCAL_REPLICA_SOURCE_OR_TARGET"></span>**Local Replica Source or Target** (10)
 

<span id="Remote_Replica_Source_or_Target"></span><span id="remote_replica_source_or_target"></span><span id="REMOTE_REPLICA_SOURCE_OR_TARGET"></span>**Remote Replica Source or Target** (11)
 

<span id="Delta_Replica_Target"></span><span id="delta_replica_target"></span><span id="DELTA_REPLICA_TARGET"></span>**Delta Replica Target** (12)
 

<span id="Element_Component"></span><span id="element_component"></span><span id="ELEMENT_COMPONENT"></span>**Element Component** (13)
 

<span id="Reserved_as_Pool_Contributor"></span><span id="reserved_as_pool_contributor"></span><span id="RESERVED_AS_POOL_CONTRIBUTOR"></span>**Reserved as Pool Contributor** (14)
 

<span id="Composite_Volume_Member"></span><span id="composite_volume_member"></span><span id="COMPOSITE_VOLUME_MEMBER"></span>**Composite Volume Member** (15)
 

<span id="Composite_VirtualDisk_Member"></span><span id="composite_virtualdisk_member"></span><span id="COMPOSITE_VIRTUALDISK_MEMBER"></span>**Composite VirtualDisk Member** (16)
 

<span id="Reserved_for_Sparing"></span><span id="reserved_for_sparing"></span><span id="RESERVED_FOR_SPARING"></span>**Reserved for Sparing** (17)
 

 

**WriteCacheSize**
   

Data type: **UInt64**
 

Access type: Read-only
 

The size of the write cache for the virtual disk.

 

## Remarks

Virtual disks are units of usable storage with an expanded set of attributes as compared to physical disks. Examples of the additional attributes include resiliency and dynamic capacity extension.

LUNs and storage spaces are examples of virtual disks.

Virtual disks, when exposed to Windows, appear as (Windows) disks to the rest of the Windows stack.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



 

