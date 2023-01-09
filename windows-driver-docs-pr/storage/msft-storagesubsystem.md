---
title: MSFT\_StorageSubSystem class
description: Represents a storage array subsystem that exposes virtual disks and/or a computer system that exposes file server capabilities.
ms.assetid: 3fa2f78f-be75-42c0-baba-b08f4959af8c
keywords:
- MSFT_StorageSubSystem class Windows Storage Management API
- MSFT_StorageSubSystem class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_StorageSubSystem
- MSFT_StorageSubSystem.FriendlyName
- MSFT_StorageSubSystem.Description
- MSFT_StorageSubSystem.Name
- MSFT_StorageSubSystem.NameFormat
- MSFT_StorageSubSystem.OtherIdentifyingInfo
- MSFT_StorageSubSystem.OtherIdentifyingInfoDescription
- MSFT_StorageSubSystem.HealthStatus
- MSFT_StorageSubSystem.OperationalStatus
- MSFT_StorageSubSystem.OtherOperationalStatusDescription
- MSFT_StorageSubSystem.CurrentCacheLevel
- MSFT_StorageSubSystem.Manufacturer
- MSFT_StorageSubSystem.Model
- MSFT_StorageSubSystem.SerialNumber
- MSFT_StorageSubSystem.FirmwareVersion
- MSFT_StorageSubSystem.Tag
- MSFT_StorageSubSystem.AutomaticClusteringEnabled
- MSFT_StorageSubSystem.PhysicalDisksPerStoragePoolMin
- MSFT_StorageSubSystem.SupportsMirrorLocal
- MSFT_StorageSubSystem.SupportsMirrorRemote
- MSFT_StorageSubSystem.SupportsSnapshotLocal
- MSFT_StorageSubSystem.SupportsSnapshotRemote
- MSFT_StorageSubSystem.SupportsCloneLocal
- MSFT_StorageSubSystem.SupportsCloneRemote
- MSFT_StorageSubSystem.SupportsVirtualDiskCreation
- MSFT_StorageSubSystem.SupportsVirtualDiskModification
- MSFT_StorageSubSystem.SupportsVirtualDiskDeletion
- MSFT_StorageSubSystem.SupportsVirtualDiskCapacityExpansion
- MSFT_StorageSubSystem.SupportsVirtualDiskCapacityReduction
- MSFT_StorageSubSystem.SupportsVirtualDiskRepair
- MSFT_StorageSubSystem.SupportsVolumeCreation
- MSFT_StorageSubSystem.SupportsStoragePoolCreation
- MSFT_StorageSubSystem.SupportsStoragePoolDeletion
- MSFT_StorageSubSystem.SupportsStoragePoolFriendlyNameModification
- MSFT_StorageSubSystem.SupportsStoragePoolAddPhysicalDisk
- MSFT_StorageSubSystem.SupportsStoragePoolRemovePhysicalDisk
- MSFT_StorageSubSystem.SupportsAutomaticStoragePoolSelection
- MSFT_StorageSubSystem.SupportsMultipleResiliencySettingsPerStoragePool
- MSFT_StorageSubSystem.SupportsStorageTierCreation
- MSFT_StorageSubSystem.SupportsStorageTierDeletion
- MSFT_StorageSubSystem.SupportsStorageTierResize
- MSFT_StorageSubSystem.SupportsStorageTierFriendlyNameModification
- MSFT_StorageSubSystem.SupportsStorageTieredVirtualDiskCreation
- MSFT_StorageSubSystem.ReplicasPerSourceSnapshotMax
- MSFT_StorageSubSystem.ReplicasPerSourceCloneMax
- MSFT_StorageSubSystem.ReplicasPerSourceMirrorMax
- MSFT_StorageSubSystem.SupportsMaskingVirtualDiskToHosts
- MSFT_StorageSubSystem.MaskingValidInitiatorIdTypes
- MSFT_StorageSubSystem.MaskingOtherValidInitiatorIdTypes
- MSFT_StorageSubSystem.MaskingPortsPerView
- MSFT_StorageSubSystem.MaskingClientSelectableDeviceNumbers
- MSFT_StorageSubSystem.MaskingOneInitiatorIdPerView
- MSFT_StorageSubSystem.MaskingMapCountMax
- MSFT_StorageSubSystem.DataTieringType
- MSFT_StorageSubSystem.iSCSITargetCreationScheme
- MSFT_StorageSubSystem.NumberOfSlots
- MSFT_StorageSubSystem.SupportedHostType
- MSFT_StorageSubSystem.OtherHostTypeDescription
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_StorageSubSystem class

Represents a storage array subsystem that exposes virtual disks and/or a computer system that exposes file server capabilities.

Storage subsystems expose virtual disks to Windows. Storage subsystems respond to administrative commands through corresponding storage providers.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
class MSFT_StorageSubSystem : MSFT_StorageObject
{
  String  FriendlyName;
  String  Description;
  String  Name;
  UInt16  NameFormat;
  String  OtherIdentifyingInfo[];
  String  OtherIdentifyingInfoDescription[];
  UInt16  HealthStatus;
  UInt16  OperationalStatus[];
  String  OtherOperationalStatusDescription;
  UInt16  CurrentCacheLevel;
  String  Manufacturer;
  String  Model;
  String  SerialNumber;
  String  FirmwareVersion;
  String  Tag;
  Boolean AutomaticClusteringEnabled;
  UInt16  PhysicalDisksPerStoragePoolMin;
  Boolean SupportsMirrorLocal;
  Boolean SupportsMirrorRemote;
  Boolean SupportsSnapshotLocal;
  Boolean SupportsSnapshotRemote;
  Boolean SupportsCloneLocal;
  Boolean SupportsCloneRemote;
  Boolean SupportsVirtualDiskCreation;
  Boolean SupportsVirtualDiskModification;
  Boolean SupportsVirtualDiskDeletion;
  Boolean SupportsVirtualDiskCapacityExpansion;
  Boolean SupportsVirtualDiskCapacityReduction;
  Boolean SupportsVirtualDiskRepair;
  Boolean SupportsVolumeCreation;
  Boolean SupportsStoragePoolCreation;
  Boolean SupportsStoragePoolDeletion;
  Boolean SupportsStoragePoolFriendlyNameModification;
  Boolean SupportsStoragePoolAddPhysicalDisk;
  Boolean SupportsStoragePoolRemovePhysicalDisk;
  Boolean SupportsAutomaticStoragePoolSelection;
  Boolean SupportsMultipleResiliencySettingsPerStoragePool;
  Boolean SupportsStorageTierCreation;
  Boolean SupportsStorageTierDeletion;
  Boolean SupportsStorageTierResize;
  Boolean SupportsStorageTierFriendlyNameModification;
  Boolean SupportsStorageTieredVirtualDiskCreation;
  Uint16  ReplicasPerSourceSnapshotMax;
  Uint16  ReplicasPerSourceCloneMax;
  Uint16  ReplicasPerSourceMirrorMax;
  Boolean SupportsMaskingVirtualDiskToHosts;
  Uint16  MaskingValidInitiatorIdTypes[];
  String  MaskingOtherValidInitiatorIdTypes[];
  Uint16  MaskingPortsPerView;
  Boolean MaskingClientSelectableDeviceNumbers;
  Boolean MaskingOneInitiatorIdPerView;
  Uint16  MaskingMapCountMax;
  Uint16  DataTieringType;
  Uint16  iSCSITargetCreationScheme;
  UInt32  NumberOfSlots;
  UInt16  SupportedHostType[];
  String  OtherHostTypeDescription[];
};
```

## Members

The **MSFT\_StorageSubSystem** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_StorageSubSystem** class has these methods.



| Method                                                                                       | Description                                                                                                              |
|:---------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------|
| [**CreateFileServer**](msft-storagesubsystem-createfileserver.md)                           | **Starting in Windows 10:** Creates a file server on a storage subsystem.                                     |
| [**CreateMaskingSet**](msft-storagesubsystem-createmaskingset.md)                           | Creates a new masking set.                                                                                    |
| [**CreateReplicationGroup**](msft-storagesubsystem-createreplicationgroup.md)               | **Starting in Windows 10:** Creates a replication group on a storage subsystem.                               |
| [**CreateReplicationRelationship**](msft-storagesubsystem-createreplicationrelationship.md) | **Starting in Windows 10:** Creates two replication groups and a replication relationship between them.       |
| [**CreateStoragePool**](createstoragepool-msft-storagesubsystem.md)                         | Creates a storage pool from available physical disks contained within a common primordial pool.               |
| [**CreateVirtualDisk**](msft-storagesubsystem-createvirtualdisk.md)                         | Creates a new virtual disk.                                                                                   |
| [**DeleteReplicationRelationship**](msft-storagesubsystem-deletereplicationrelationship.md) | **Starting in Windows 10:** Deletes a replication relationship between groups.                                |
| [**Diagnose**](msft-storagesubsystem-diagnose.md)                                           | **Starting in Windows 10:** Performs a diagnostic on the storage subsystem, returning any actionable results. |
| [**GetDiagnosticInfo**](msft-storagesubsystem-getdiagnosticinfo.md)                         | **Starting in Windows 10:** Gets the diagnostic information of the storage subsystem.                         |
| [**GetSecurityDescriptor**](msft-storagesubsystem-getsecuritydescriptor.md)                 | Retrieves the security descriptor that controls access to the storage subsystem object instance.              |
| [**SetAttributes**](msft-storagesubsystem-setattributes.md)                                 | Sets the **SupportsAutomaticObjectClustering** field of the storage subsystem object instance.                |
| [**SetDescription**](msft-storagesubsystem-setdescription.md)                               | Sets the **Description** property of the storage subsystem object instance.                                   |
| [**SetSecurityDescriptor**](msft-storagesubsystem-setsecuritydescriptor.md)                 | Sets the security descriptor that controls access to the storage subsystem object instance.                   |
| [**StartDiagnosticLog**](msft-storagesubsystem-startdiagnosticlog.md)                       | **Starting in Windows 10:** Starts a diagnostic log for the storage subsystem.                                |
| [**StopDiagnosticLog**](msft-storagesubsystem-stopdiagnosticlog.md)                         | **Starting in Windows 10:** Stops the diagnostic log for the storage subsystem.                               |



 

### Properties

The **MSFT\_StorageSubSystem** class has these properties.

 

**AutomaticClusteringEnabled**
   

Data type: **Boolean**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

**TRUE** if this subsystem supports automatic object clustering; otherwise, **FALSE**.

 

**CurrentCacheLevel**
   

Data type: **UInt16**
 

Access type: Read-only
 

The cache level that has been discovered. This corresponds to the storage provider's *DiscoveryLevel* parameter in the [**Discover**](discover-msft-storageprovider.md) method.



| Value                                                                                                                                                                                                                       | Meaning                                                                                                                                                  |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
|  **Level 0** 0  | The storage provider and storage subsystem objects have been discovered.                                                                      |
|  **Level 1** 1  | Storage pools, resiliency settings, target ports, target portals, and initiator identifiers belonging to this subsystem have been discovered. |
|  **Level 2** 2  | Virtual disks and masking sets belonging to this subsystem have been discovered.                                                              |
|  **Level 3** 3  | Physical disks belonging to this subsystem have been discovered.                                                                              |



 

 

**DataTieringType**
   

Data type: **Uint16**
 

Access type: Read-only
 

The type of data tiering, if any, that is supported by the storage subsystem.

 

**Unknown** (0)
 

**Not Supported** (1)
 

**Manual** (2)
 

**Auto** (3)
 

 

**Description**
   

Data type: **String**
 

Access type: Read-only
 

A user-settable description of the storage subsystem. This field can be used to store extra free-form information, such as notes or details about the subsystem's intended usage.

 

**FirmwareVersion**
   

Data type: **String**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

The firmware version of the storage subsystem array.

 

**FriendlyName**
   

Data type: **String**
 

Access type: Read-only
 

A user-settable string containing the name of the storage subsystem. The storage provider is expected to supply an initial value for this field.

 

**HealthStatus**
   

Data type: **UInt16**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

The health status of the subsystem.



| Value                                                                                                                                                                                                                                    | Meaning                                                                                                                                        |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
|  **Healthy** 0               | The storage subsystem is functioning normally.                                                                                      |
|  **Warning** 1               | The storage subsystem is still functioning, but has detected errors or issues that require administrator intervention.              |
|  **Unhealthy**  2   | The storage subsystem is not functioning, due to errors or failures. The subsystem needs immediate attention from an administrator. |



 

 

**iSCSITargetCreationScheme**
   

Data type: **Uint16**
 

Access type: Read-only
 

The iSCSI target creation scheme, if any, that is supported by the storage subsystem.



| Value                                                                                                                                                                                                                                                   | Meaning                                                       |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|
|  **Not Applicable** 0  | The subsystem is a non-iSCSI subsystem.            |
|  **Not Supported** 1      | The subsystem does not allow creation of a target. |
|  **Manual** 2                                  | The subsystem allows manual creation of a target.  |
|  **Auto** 3                                          | The subsystem automatically creates a target.      |



 

 

**Manufacturer**
   

Data type: **String**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

The name of the company responsible for creating the storage subsystem hardware.

 

**MaskingClientSelectableDeviceNumbers**
   

Data type: **Boolean**
 

Access type: Read-only
 

**TRUE** if this storage subsystem allows the client to specify the *DeviceNumber* parameter in methods such as [**MSFT\_StorageSubsystem::CreateMaskingSet**](msft-storagesubsystem-createmaskingset.md) and [**MSFT\_MaskingSet::AddVirtualDisk**](msft-maskingset-addvirtualdisk.md).

 

**MaskingMapCountMax**
   

Data type: **Uint16**
 

Access type: Read-only
 

The maximum number of masking sets that can be a particular virtual disk can be added to. If this property is zero, there is no limit.

 

**MaskingOneInitiatorIdPerView**
   

Data type: **Boolean**
 

Access type: Read-only
 

**TRUE** if this storage subsystem allows only one initiator identifier per masking set.

 

**MaskingOtherValidInitiatorIdTypes**
   

Data type: **String** array
 

Access type: Read-only
 

If one of the elements in the **MaskingValidInitiatorIdTypes** array is **Other**, this property is an array that contains the other valid [**MSFT\_InitiatorId**](msft-initiatorid.md) types.

 

**MaskingPortsPerView**
   

Data type: **Uint16**
 

Access type: Read-only
 

The number of target ports that can be used for masking a virtual disk. This applies to masking sets and to the [**MSFT\_VirtualDisk.Show**](msft-virtualdisk-show.md) method.



| Value                                                                        | Meaning                                              |
|------------------------------------------------------------------------------|------------------------------------------------------|
|  2  | There is only one target per view.        |
|  3  | There are multiple target ports per view. |
|  4  | All target ports share the same view.     |



 

 

**MaskingValidInitiatorIdTypes**
   

Data type: **Uint16** array
 

Access type: Read-only
 

An array that contains the address formats the storage provider and subsystem can expect when working with initiator identifiers.

 

**Other** (1)
 

**Port WWN** (2)
 

**Node WWN** (3)
 

**Host Name** (4)
 

**iSCSI Name** (5)
 

**Switch WWN** (6)
 

**SAS Address** (7)
 

 

**Model**
   

Data type: **String**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

The model number of the storage subsystem array.

 

**Name**
   

Data type: **String**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

A globally unique, human-readable string used to identify the storage subsystem.

 

**NameFormat**
   

Data type: **UInt16**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

The format of the string stored in the **Name** property.

 

**Other** (1)
 

**IP** (2)
 

**Dial** (3)
 

**HID** (4)
 

**NWA** (5)
 

**HWA** (6)
 

**X25** (7)
 

**ISDN** (8)
 

**IPX** (9)
 

**DCC** (10)
 

**ICD** (11)
 

**E.164** (12)
 

**SNA** (13)
 

**OID/OSI** (14)
 

**WWN** (15)
 

**NAA** (16)
 

 

**NumberOfSlots**
   

Data type: **UInt32**
 

Access type: Read-only
 

The maximum number of physical disk slots in the subsystem or enclosure.

 

**OperationalStatus**
   

Data type: **UInt16** array
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

An array of values that denote the current operational status of the subsystem.



| Value                                                                                                                                                                                                                                                                                                    | Meaning                                                                                                                                                                                                 |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  **Unknown** 0                                                                               | The operational status is unknown.                                                                                                                                                           |
|  **Other** 1                                                                                       | A vendor-specific **OperationalStatus** has been specified by setting the **OtherOperationalStatusDescription** property.                                                                    |
|  **OK** 2                                                                                                                        | The storage subsystem is responding to commands and is in a normal operating state.                                                                                                          |
|  **Degraded** 3                                                                           | The storage subsystem is responding to commands, but is not running in an optimal operating state.                                                                                           |
|  **Stressed** 4                                                                           | The storage subsystem is functioning, but needs attention. For example, the storage subsystem might be overloaded or overheated.                                                             |
|  **Predictive Failure** 5                                   | The storage subsystem is functioning, but a failure is likely to occur in the near future.                                                                                                   |
|  **Error** 6                                                                                       | An error has occurred.                                                                                                                                                                       |
|  **Non-Recoverable Error** 7                       | A nonrecoverable error has occurred.                                                                                                                                                         |
|  **Starting** 8                                                                           | The storage subsystem is in the process of starting.                                                                                                                                         |
|  **Stopping** 9                                                                           | The storage subsystem is in the process of stopping.                                                                                                                                         |
|  **Stopped** 10                                                                              | The storage subsystem was stopped or shut down in a clean and orderly fashion.                                                                                                               |
|  **In Service** 11                                                                  | The storage subsystem is being configured, maintained, cleaned, or otherwise administered.                                                                                                   |
|  **No Contact** 12                                                                  | The storage provider has knowledge of the storage subsystem, but has never been able to establish communication with it.                                                                     |
|  **Lost Communication** 13                                  | The storage provider has knowledge of the storage subsystem and has contacted it successfully in the past, but the storage subsystem is currently unreachable.                               |
|  **Aborted** 14                                                                              | Similar to **Stopped**, except that the storage subsystem stopped abruptly and may require configuration or maintenance.                                                                     |
|  **Dormant** 15                                                                              | The storage subsystem is reachable, but it is inactive.                                                                                                                                      |
|  **Supporting Entity in Error** 16  | This status value does not necessarily indicate trouble with the storage subsystem, but it does indicate that another device or connection that the subsystem depends on may need attention. |
|  **Completed** 17                                                                      | The storage subsystem has completed an operation. This status value should be combined with **OK**, **Error**, or **Degraded**, depending on the outcome of the operation                    |
|  **Power Mode**  18                                                              | This value is reserved for system use.                                                                                                                                                       |



 

 

**OtherHostTypeDescription**
   

Data type: **String** array
 

Access type: Read-only
 

Qualifiers: [**ArrayType**](/windows/win32/wmisdk/standard-qualifiers) ( "Indexed" ), [**ModelCorrespondence {"CIM\_StorageClientSettingData.ClientTypes"}**](/windows/win32/wmisdk/standard-qualifiers)
 

If the corresponding entry in the **SupportedHostType** array is **Other**, the entry in this property contains a string describing the manufacturer and operating system or environment.

If the corresponding entry in the **SupportedHostType** array is not **Other**, the entry in this property allows variations or qualifications of **ClientTypes** for example, different versions of Solaris.

 

**OtherIdentifyingInfo**
   

Data type: **String** array
 

Access type: Read-only
 

An array of strings, each containing a custom identifier for the subsystem. If this property is set, the **NameFormat** property must be set to **Other** and the **OtherIdentifyingInfoDescription** property must also be set.

 

**OtherIdentifyingInfoDescription**
   

Data type: **String** array
 

Access type: Read-only
 

An array containing string descriptions of the formats used in each of the custom identifiers in the **OtherIdentifyingInfo** array. There must be a 1:1 mapping between the elements in this array and the elements **OtherIdentifyingInfo** array.

 

**OtherOperationalStatusDescription**
   

Data type: **String**
 

Access type: Read-only
 

A string representation of the vendor-defined operational status. This property should only be set if the value of the **OperationalStatus** property is **Other**.

 

**PhysicalDisksPerStoragePoolMin**
   

Data type: **UInt16**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

The minimum number of physical disks needed for a storage pool on this subsystem.

 

**ReplicasPerSourceCloneMax**
   

Data type: **Uint16**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

Reserved for system use.

 

**ReplicasPerSourceMirrorMax**
   

Data type: **Uint16**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

Reserved for future use.

 

**ReplicasPerSourceSnapshotMax**
   

Data type: **Uint16**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

Reserved for system use.

 

**SerialNumber**
   

Data type: **String**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

The serial number of the storage subsystem array.

 

**SupportedHostType**
   

Data type: **UInt16** array
 

Access type: Read-only
 

An array of values that specify the supported host types.

 

**Unknown** (0)
 

**Other** (1)
 

**Standard** (2)
 

**Solaris** (3)
 

**HPUX** (4)
 

**OpenVMS** (5)
 

**Tru64** (6)
 

**Netware** (7)
 

**Sequent** (8)
 

**AIX** (9)
 

**DGUX** (10)
 

**Dynix** (11)
 

**Irix** (12)
 

**Cisco iSCSI Storage Router** (13)
 

**Linux** (14)
 

**Microsoft Windows** (15)
 

**OS400** (16)
 

**TRESPASS** (17)
 

**HI-UX** (18)
 

**VMware ESXi** (19)
 

**Microsoft Windows Server 2008** (20)
 

**Microsoft Windows Server 2003** (21)
 

**DMTF Reserved** (22..32767)
 

**Vendor Specific** (32768..65535)
 

 

**SupportsAutomaticStoragePoolSelection**
   

Data type: **Boolean**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

**TRUE** if automatic storage pool selection is supported.

 

**SupportsCloneLocal**
   

Data type: **Boolean**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

**TRUE** if this storage subsystem supports replication type **Clone Local**.

 

**SupportsCloneRemote**
   

Data type: **Boolean**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

**TRUE** if this storage subsystem supports replication type **Clone Remote**.

 

**SupportsMaskingVirtualDiskToHosts**
   

Data type: **Boolean**
 

Access type: Read-only
 

**TRUE** if the storage subsystem supports showing and hiding (masking) a virtual disk to a host initiator through the [**MSFT\_VirtualDisk.Show**](msft-virtualdisk-show.md)[**MSFT\_VirtualDisk.Hide**](msft-virtualdisk-hide.md) methods and by the use of masking sets.

 

**SupportsMirrorLocal**
   

Data type: **Boolean**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

**TRUE** if this storage subsystem supports replication type **Mirror Local**.

 

**SupportsMirrorRemote**
   

Data type: **Boolean**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

**TRUE** if this storage subsystem supports replication type **Mirror Remote**.

 

**SupportsMultipleResiliencySettingsPerStoragePool**
   

Data type: **Boolean**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

If **TRUE**, all resiliency settings will be copied from the primordial pool and added to a concrete pool upon its creation. If **FALSE**, the storage pool should copy the resiliency setting name specified in the *ResiliencySettingNameDefault* parameter of the [**MSFT\_StorageSubSystem.CreateStoragePool**](createstoragepool-msft-storagesubsystem.md) method. If no resiliency setting name was specified, the resiliency setting specified in the primordial pool's **ResiliencySettingNameDefault** property should be used.

 

**SupportsSnapshotLocal**
   

Data type: **Boolean**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

**TRUE** if this storage subsystem supports replication type **Snapshot Local**.

 

**SupportsSnapshotRemote**
   

Data type: **Boolean**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

**TRUE** if this storage subsystem supports replication type **Snapshot Remote**.

 

**SupportsStoragePoolAddPhysicalDisk**
   

Data type: **Boolean**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

**TRUE** if the storage pools in this storage subsystem support adding physical disks to expand capacity.

 

**SupportsStoragePoolCreation**
   

Data type: **Boolean**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

**TRUE** if the storage subsystem supports the ability to create new concrete storage pools from one or more physical disks. If **FALSE**, either the subsystem uses pre-created storage pools, or it does not support storage pools at all.

 

**SupportsStoragePoolDeletion**
   

Data type: **Boolean**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

**TRUE** if the storage subsystem supports the deletion of its storage pools.

 

**SupportsStoragePoolFriendlyNameModification**
   

Data type: **Boolean**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

**TRUE** if the storage subsystem supports storage pool friendly name modification.

 

**SupportsStoragePoolRemovePhysicalDisk**
   

Data type: **Boolean**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

**TRUE** if the storage pools in this subsystem support the replacement or removal of physical disks by use of the [**MSFT\_StoragePool.RemovePhysicalDisk**](removephysicaldisk-msft-storagepool.md) method.

 

**SupportsStorageTierCreation**
   

Data type: **Boolean**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

If **TRUE**, this subsystem supports the ability to create new storage tiers. If **FALSE**, either the subsystem uses pre-created storage tiers, or it does not support storage tiers.

 

**SupportsStorageTierDeletion**
   

Data type: **Boolean**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

If **TRUE**, this subsystem supports the deletion of storage tiers.

 

**SupportsStorageTieredVirtualDiskCreation**
   

Data type: **Boolean**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

If **TRUE**, this subsystem supports the creation of tiered virtual disks.

 

**SupportsStorageTierFriendlyNameModification**
   

Data type: **Boolean**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

If **TRUE**, this subsystem supports the modification of the storage tier friendly name.

 

**SupportsStorageTierResize**
   

Data type: **Boolean**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

If **TRUE**, this subsystem supports the resizing of storage tiers..

 

**SupportsVirtualDiskCapacityExpansion**
   

Data type: **Boolean**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

**TRUE** if a user can increase the size of a virtual disk by using the [**MSFT\_VirtualDisk.Resize**](msft-virtualdisk-resize.md) method.

 

**SupportsVirtualDiskCapacityReduction**
   

Data type: **Boolean**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

**TRUE** if a user can reduce the size of a virtual disk by using the [**MSFT\_VirtualDisk.Resize**](msft-virtualdisk-resize.md) method.

 

**SupportsVirtualDiskCreation**
   

Data type: **Boolean**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

**TRUE** if a user can create a virtual disk by using the [**MSFT\_StorageSubSystem.CreateVirtualDisk**](msft-storagesubsystem-createvirtualdisk.md) method or the [**MSFT\_StoragePool.CreateVirtualDisk**](createvirtualdisk-msft-storagepool.md) method.

 

**SupportsVirtualDiskDeletion**
   

Data type: **Boolean**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

**TRUE** if a user can delete a virtual disk by using the [**MSFT\_VirtualDisk.DeleteObject**](msft-virtualdisk-deleteobject.md) method.

 

**SupportsVirtualDiskModification**
   

Data type: **Boolean**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

**TRUE** if a user can modify attributes or other properties on a virtual disk by using methods such as [**MSFT\_VirtuDisk.SetFriendlyName**](msft-virtualdisk-setfriendlyname.md) and [**MSFT\_VirtuDisk.SetAttributes**](msft-virtualdisk-setattributes.md).

 

**SupportsVirtualDiskRepair**
   

Data type: **Boolean**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

**TRUE** if a user can repair a virtual disk by using the [**MSFT\_VirtualDisk.Repair**](msft-virtualdisk-repair.md) method.

 

**SupportsVolumeCreation**
   

Data type: **Boolean**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

**TRUE** if this subsystem supports direct creation of volumes on a storage pool.

 

**Tag**
   

Data type: **String**
 

Access type: Read-only
 

An identifier for the subsystem that is independent from any location-based information. For example, this property might contain the subsystem's serial number or asset tag number.

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



 

