---
title: MSFT\_StoragePool class
description: Represents a logical grouping of physical disks that may be used to create virtual disks.
ms.assetid: 5b6c5566-7a3f-4bc4-b69e-53664920c9b2
keywords:
- MSFT_StoragePool class Windows Storage Management API
- MSFT_StoragePool class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_StoragePool
- MSFT_StoragePool.FriendlyName
- MSFT_StoragePool.Name
- MSFT_StoragePool.Usage
- MSFT_StoragePool.OtherUsageDescription
- MSFT_StoragePool.IsPrimordial
- MSFT_StoragePool.HealthStatus
- MSFT_StoragePool.OperationalStatus
- MSFT_StoragePool.OtherOperationalStatusDescription
- MSFT_StoragePool.Size
- MSFT_StoragePool.AllocatedSize
- MSFT_StoragePool.LogicalSectorSize
- MSFT_StoragePool.PhysicalSectorSize
- MSFT_StoragePool.ProvisioningTypeDefault
- MSFT_StoragePool.SupportedProvisioningTypes
- MSFT_StoragePool.ResiliencySettingNameDefault
- MSFT_StoragePool.IsReadOnly
- MSFT_StoragePool.ReadOnlyReason
- MSFT_StoragePool.IsClustered
- MSFT_StoragePool.SupportsDeduplication
- MSFT_StoragePool.ThinProvisioningAlertThresholds
- MSFT_StoragePool.ClearOnDeallocate
- MSFT_StoragePool.IsPowerProtected
- MSFT_StoragePool.RepairPolicy
- MSFT_StoragePool.EnclosureAwareDefault
- MSFT_StoragePool.FaultDomainAwarenessDefault
- MSFT_StoragePool.RetireMissingPhysicalDisks
- MSFT_StoragePool.Version
- MSFT_StoragePool.WriteCacheSizeDefault
- MSFT_StoragePool.WriteCacheSizeMin
- MSFT_StoragePool.WriteCacheSizeMax
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_StoragePool class

Represents a logical grouping of physical disks that may be used to create virtual disks.

The virtual disks can be created with different characteristics and levels of resiliency based on the number of available physical disks and the capabilities of the storage pool.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
class MSFT_StoragePool : MSFT_StorageObject
{
  String  FriendlyName;
  String  Name;
  UInt16  Usage;
  String  OtherUsageDescription;
  Boolean IsPrimordial;
  UInt16  HealthStatus;
  UInt16  OperationalStatus[];
  String  OtherOperationalStatusDescription;
  UInt64  Size;
  UInt64  AllocatedSize;
  UInt64  LogicalSectorSize;
  UInt64  PhysicalSectorSize;
  UInt16  ProvisioningTypeDefault;
  UInt16  SupportedProvisioningTypes[];
  String  ResiliencySettingNameDefault;
  Boolean IsReadOnly;
  UInt16  ReadOnlyReason;
  Boolean IsClustered;
  Boolean SupportsDeduplication;
  UInt16  ThinProvisioningAlertThresholds[];
  Boolean ClearOnDeallocate;
  Boolean IsPowerProtected;
  UInt16  RepairPolicy;
  Boolean EnclosureAwareDefault;
  UInt16  FaultDomainAwarenessDefault;
  UInt16  RetireMissingPhysicalDisks;
  UInt16  Version;
  UInt64  WriteCacheSizeDefault;
  UInt64  WriteCacheSizeMin;
  UInt64  WriteCacheSizeMax;
};
```

## Members

The **MSFT\_StoragePool** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_StoragePool** class has these methods.



| Method                                                                  | Description                                                                                    |
|:------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------|
| [**AddPhysicalDisk**](addphysicaldisk-msft-storagepool.md)             | Adds physical disks to a storage pool.                                              |
| [**CreateStorageTier**](msft-storagepool-createstoragetier.md)         | Creates a storage tier template on the storage pool.                                |
| [**CreateVirtualDisk**](createvirtualdisk-msft-storagepool.md)         | Creates a virtual disk within the storage pool.                                     |
| [**CreateVolume**](msft-storagepool-createvolume.md)                   | Creates a virtual disk and single volume using the resources of the storage pool.   |
| [**DeleteObject**](msft-storagepool-deleteobject.md)                   | Deletes an empty storage pool.                                                      |
| [**GetSecurityDescriptor**](getsecuritydescriptor-msft-storagepool.md) | Retrieves the security descriptor for the storage pool object instance.             |
| [**GetSupportedSize**](msft-storagepool-getsupportedsize.md)           | Retrieves the supported virtual disk sizes that can be created in the storage pool. |
| [**Optimize**](msft-storagepool-optimize.md)                           | Optimizes the storage pool.                                                         |
| [**RemovePhysicalDisk**](removephysicaldisk-msft-storagepool.md)       | Removes physical disks from a storage pool.                                         |
| [**SetAttributes**](msft-storagepool-setattributes.md)                 | Sets or changes the attribute values for the storage pool object.                   |
| [**SetDefaults**](msft-storagepool-setdefaults.md)                     | Sets or changes the default values for properties of the storage pool object.       |
| [**SetFriendlyName**](msft-storagepool-setfriendlyname.md)             | Sets or changes the friendly name for the storage pool object.                      |
| [**SetSecurityDescriptor**](setsecuritydescriptor-msft-storagepool.md) | Sets or changes the security descriptor for the storage pool object.                |
| [**SetUsage**](msft-storagepool-setusage.md)                           | Sets or changes the intended usage for the storage pool object.                     |
| [**Upgrade**](msft-storagepool-upgrade.md)                             | Upgrades the metadata on the storage pool.                                          |



 

### Properties

The **MSFT\_StoragePool** class has these properties.

 

**AllocatedSize**
   

Data type: **UInt64**
 

Access type: Read-only
 

Qualifiers: [**Units**](/windows/win32/wmisdk/standard-qualifiers) ("Bytes")
 

The total capacity used by this storage pool. If the pool is primordial, this will be the sum of all capacity currently allocated to concrete storage pools. If the pool is concrete, this value should be the sum of all capacity currently allocated to virtual disks and other pool metadata.

 

**ClearOnDeallocate**
   

Data type: **Boolean**
 

Access type: Read-only
 

**TRUE** if physical disks should be zeroed (cleared of all data) when unmapped or removed from the storage pool.

 

**EnclosureAwareDefault**
   

Data type: **Boolean**
 

Access type: Read-only
 

The default allocation behavior for virtual disks created in this pool. Enclosure aware virtual disks will intelligently pick the physical disks to use for their redundancy. If **TRUE**, the virtual disk will use physical disks from different enclosures to balance the fault tolerance between two or more physical enclosures.

 

**FaultDomainAwarenessDefault**
   

Data type: **UInt16**
 

Access type: Read-only
 

Determines the default allocation behavior for virtual disks created in this pool. Fault domain-aware virtual disks intelligently pick the physical disks to use for their redundancy to balance the fault tolerance between two (or more) fault domain units of the specified type.

 

**PhysicalDisk** (1)
 

**StorageEnclosure** (2)
 

**StorageScaleUnit** (3)
 

**StorageChassis** (4)
 

**StorageRack** (5)
 

 

**FriendlyName**
   

Data type: **String**
 

Access type: Read/write
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

A user-friendly name for the storage pool. This name can be set by calling the [**SetFriendlyName**](msft-storagepool-setfriendlyname.md) method.

 

**HealthStatus**
   

Data type: **UInt16**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

The health status of the storage pool.

Health of a storage pool is derived from the health of the backing physical disks, and whether or not the storage pool can maintain the required redundancy levels.



| Value                                                                                                                                                                                                                                    | Meaning                                                                                                                          |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
|  **Healthy** 0               | All physical disks are present and in a healthy state.                                                                |
|  **Warning** 1               | The majority of physical disks are healthy, but one or more may be failing I/O requests.                              |
|  **Unhealthy**  2   | The majority of physical disks are unhealthy or in a failed state, and the storage pool no longer has data integrity. |
|  **Unknown**  5           | The health status of the storage pool is unknown.                                                                     |



 

 

**IsClustered**
   

Data type: **Boolean**
 

Access type: Read-only
 

**TRUE** if the storage pool is used in a clustered environment.

 

**IsPowerProtected**
   

Data type: **Boolean**
 

Access type: Read-only
 

**TRUE** if the disks in this pool are able to tolerate power loss without data loss. For example, they automatically flush volatile buffers to non-volatile media after external power is disconnected.

 

**IsPrimordial**
   

Data type: **Boolean**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

If this field is set to **TRUE**, the storage pool is primordial. A primordial pool, also known as the 'available storage' pool is where storage capacity is drawn and returned in the creation and deletion of concrete storage pools. Primordial pools cannot be created or deleted.

If this field is set to **FALSE**, the storage pool is a concrete pool. These pools are subject to all of the management operations defined on the storage pool class, including creation and deletion of virtual disks.

 

**IsReadOnly**
   

Data type: **Boolean**
 

Access type: Read-only
 

Indicates whether or not the storage pool's configuration is read only. If **TRUE**, the storage pool will not allow modification to itself or any of its virtual and physical disks. Note that the data on the virtual disk may still be writable, even if this property is **TRUE**.

 

**LogicalSectorSize**
   

Data type: **UInt64**
 

Access type: Read-only
 

Qualifiers: [**Units**](/windows/win32/wmisdk/standard-qualifiers) ("Bytes")
 

Logical sector size, in bytes, of the storage pool. This value should be derived from the backing physical disks, as well as the preference specified at the time this storage pool was created.

 

**Name**
   

Data type: **String**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

A semi-unique (scoped to the owning storage subsystem), human-readable string used to identify the storage pool.

 

**OperationalStatus**
   

Data type: **UInt16** array
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

The operational status of the storage pool. Unlike **HealthStatus**, this property indicates the status of hardware, software, and infrastructure issues related to the storage pool, and can contain multiple values.



| Value                                                                                                                                                                                                                                                                                                    | Meaning                                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  **Unknown** 0                                                                               | The operational status is unknown.                                                                                                                                                         |
|  **Other** 1                                                                                       | A vendor-specific **OperationalStatus** has been specified by setting the **OtherOperationalStatusDescription** property.                                                                  |
|  **OK** 2                                                                                                                        | The storage pool is responding to commands and is in a normal operating state.                                                                                                             |
|  **Degraded** 3                                                                           | The storage pool is responding to commands, but is not running in an optimal operating state.                                                                                              |
|  **Stressed** 4                                                                           | The storage pool is functioning, but needs attention. For example, the storage subsystem may be overloaded or overheated.                                                                  |
|  **Predictive Failure** 5                                   | The storage pool is functioning, but predicting a failure in the near future.                                                                                                              |
|  **Error** 6                                                                                       | An error has occurred.                                                                                                                                                                     |
|  **Non-Recoverable Error** 7                       | An nonrecoverable error has occurred.                                                                                                                                                      |
|  **Starting** 8                                                                           | The storage pool is in the process of starting.                                                                                                                                            |
|  **Stopping** 9                                                                           | The storage pool is in the process of stopping.                                                                                                                                            |
|  **Stopped** 10                                                                              | The storage pool was stopped in a clean and orderly fashion.                                                                                                                               |
|  **In Service** 11                                                                  | The storage pool is being configured, maintained, cleaned, or otherwise administered.                                                                                                      |
|  **No Contact** 12                                                                  | The storage provider has knowledge of the storage pool, but has never been able to establish communication with it.                                                                        |
|  **Lost Communication** 13                                  | The storage provider has knowledge of the storage pool and has contacted it successfully in the past, but is the storage subsystem is currently unreachable.                               |
|  **Aborted** 14                                                                              | Similar to **Stopped**, except that the storage pool stopped abruptly and may require configuration or maintenance.                                                                        |
|  **Dormant** 15                                                                              | The storage pool is reachable, but it is inactive.                                                                                                                                         |
|  **Supporting Entity in Error** 16  | This status value does not necessarily indicate trouble with the storage pool, but it does indicate that another device or connection that the storage pool depends on may need attention. |
|  **Completed** 17                                                                      | The storage pool has completed an operation. This status value should be combined with **OK**, **Error**, or **Degraded**, depending on the outcome of the operation                       |
|  **Power Mode** 18                                                                  | This value is reserved for system use.                                                                                                                                                     |
|  **Relocating** 19                                                                  | The storage pool is in the process of relocating.                                                                                                                                          |
|  **Microsoft Reserved** ..                                  | This value is reserved for system use.                                                                                                                                                     |
|  **Majority Disks Unhealthy** 0x8000      | This value is reserved for system use.                                                                                                                                                     |
|  **Minority Disks Unhealthy** 0x8001      | This value is reserved for system use.                                                                                                                                                     |
|  **Microsoft Reserved** 0x8002..                            | This value is reserved for system use.                                                                                                                                                     |



 

 

**OtherOperationalStatusDescription**
   

Data type: **String**
 

Access type: Read-only
 

A string representation of the vendor-defined status. This property should only be set if the value of the **OperationalStatus** property is **Other**.

 

**OtherUsageDescription**
   

Data type: **String**
 

Access type: Read-only
 

A string representation of the vendor defined usage for the storage pool. This property can only be specified if the **Usage** property is set to **Other**.

 

**PhysicalSectorSize**
   

Data type: **UInt64**
 

Access type: Read-only
 

Qualifiers: [**Units**](/windows/win32/wmisdk/standard-qualifiers) ("Bytes")
 

Physical sector size, in bytes. This value is derived from the backing physical disks that belong to the storage pool.

 

**ProvisioningTypeDefault**
   

Data type: **UInt16**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

The default provisioning scheme to use when creating new virtual disks in the storage pool.



| Value                                                                                                                                                                                                                       | Meaning                                                                                                                                                         |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  **Unknown** 0  | The allocation policy is unknown. This could mean that this information is unavailable, or the storage pool uses a proprietary method of allocation. |
|  **Thin** 1              | Storage for the virtual disk is allocated on demand.                                                                                                 |
|  **Fixed** 2          | Storage for the virtual disk is allocated at the time of virtual disk creation.                                                                      |



 

 

**ReadOnlyReason**
   

Data type: **UInt16**
 

Access type: Read-only
 

The reason why the storage pool is read-only.



| Value                                                                                                                                                                                                                                                                                           | Meaning                                                                                                                                           |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
|  **Unknown** 0                                                                      | The reason is unknown.                                                                                                                 |
|  **None** 1                                                                                  | The pool is not read-only.                                                                                                             |
|  **By Policy** 2                                                              | The administrator has requested the pool to be read-only or has enacted a policy on the system that requires the pool to be read-only. |
|  **Majority Disks Unhealthy** 3  | The majority of the supporting physical disks are in an unhealthy state, which has forced the storage pool into a read-only state.     |



 

 

**RepairPolicy**
   

Data type: **UInt16**
 

Access type: Read-only
 

How the operating system repairs virtual disks for this storage pool.



| Value                                                                                                | Meaning                                                                                                                                                |
|------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
|  **2**  | Sequential - processes one allocation slab at a time. Repairs take longer, but with less impact on the I/O load.                            |
|  **3**  | Parallel - processes as many allocation slabs as it can in parallel. Repair time is minimized, but with significant impact on the I/O load. |



 

 

**ResiliencySettingNameDefault**
   

Data type: **String**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers), [**ModelCorrespondence {"MSFT\_ResiliencySetting.Name"}**](/windows/win32/wmisdk/standard-qualifiers)
 

The desired resiliency setting to be used by default when creating new virtual disks on the storage pool. This default value can be overridden at the time of virtual disk creation. This property's value should correspond to the [**MSFT\_ResiliencySetting**](msft-resiliencysetting.md) object's **Name** property.

 

**RetireMissingPhysicalDisks**
   

Data type: **UInt16**
 

Access type: Read-only
 

Qualifiers: **Values** ( "Auto", "Always", "Never" ), **ValueMap** ("1", "2", "3")
 

Specifies whether the storage subsystem will automatically retire physical disks that are missing from this storage pool and replace them with hot spares or other physical disks that are available in the storage pool.

 

**Size**
   

Data type: **UInt64**
 

Access type: Read-only
 

Qualifiers: [**Units**](/windows/win32/wmisdk/standard-qualifiers) ("Bytes")
 

The capacity of the storage pool. If the pool is primordial, this is the sum of all the healthy physical disk sizes. If the pool is concrete, this is the sum of all associated physical disks (except hot spares, and including failed drives).

 

**SupportedProvisioningTypes**
   

Data type: **UInt16** array
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

The provisioning schemes that the storage pool supports for creating virtual disks.



| Value                                                                                                                                                                                                                       | Meaning                                                                                                                                                         |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  **Unknown** 0  | The allocation policy is unknown. This could mean that this information is unavailable, or the storage pool uses a proprietary method of allocation. |
|  **Thin** 1              | Storage for the virtual disk is allocated on demand.                                                                                                 |
|  **Fixed** 2          | Storage for the virtual disk is allocated at the time of virtual disk creation.                                                                      |



 

 

**SupportsDeduplication**
   

Data type: **Boolean**
 

Access type: Read-only
 

**TRUE** if the storage pool supports data deduplication.

 

**ThinProvisioningAlertThresholds**
   

Data type: **UInt16** array
 

Access type: Read-only
 

Qualifiers: [**Units**](/windows/win32/wmisdk/standard-qualifiers) ("Percentage"), [**MinValue**](/windows/win32/wmisdk/standard-qualifiers) (0), [**MaxValue**](/windows/win32/wmisdk/standard-qualifiers) (100)
 

An array of percentage values that represent various sparse (thin provisioning) thresholds. When the virtual disk space usage crosses one of these thresholds, a notification will be broadcasted to all subscribed clients.

 

**Usage**
   

Data type: **UInt16**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

The intended use of the storage pool.

You can specify a predefined description or a custom description. To specify a predefined description, use a value other than **Other**.

To specify a custom description, use **Other** and specify a non-NULL value for the **OtherUsageDescription** property.

 

**Unknown** (0)
 

**Other** (1)
 

**Unrestricted** (2)
 

**Reserved for ComputerSystem (the block server)** (3)
 

**Reserved as a Delta Replica Container** (4)
 

**Reserved for Migration Services** (5)
 

**Reserved for Local Replication Services** (6)
 

**Reserved for Remote Replication Services** (7)
 

**Reserved for Sparing** (8)
 

 

**Version**
   

Data type: **UInt16**
 

Access type: Read-only
 

The minimum OS version that supports this storage pool.



| Value                                                                                                | Meaning                                   |
|------------------------------------------------------------------------------------------------------|-------------------------------------------|
|  **1**  | Windows Server 2012            |
|  **2**  | Windows Server 2012 R2 Preview |
|  **3**  | Windows Server 2012 R2         |



 

 

**WriteCacheSizeDefault**
   

Data type: **UInt64**
 

Access type: Read-only
 

Default size of write cache for virtual disk creation.

 

**WriteCacheSizeMax**
   

Data type: **UInt64**
 

Access type: Read-only
 

Maximum size of write cache for virtual disk creation.

 

**WriteCacheSizeMin**
   

Data type: **UInt64**
 

Access type: Read-only
 

Minimum size of write cache for virtual disk creation.

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



 

