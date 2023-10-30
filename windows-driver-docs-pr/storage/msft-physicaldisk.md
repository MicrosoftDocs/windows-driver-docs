---
title: MSFT\_PhysicalDisk class
description: Represents a subsystem drive or spindle.
ms.assetid: 01eeb68b-c8b0-4f91-9072-3a03b20b9636
keywords:
- MSFT_PhysicalDisk class Windows Storage Management API
- MSFT_PhysicalDisk class Windows Storage Management API , described
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_PhysicalDisk
- MSFT_PhysicalDisk.UniqueIdFormat
- MSFT_PhysicalDisk.DeviceId
- MSFT_PhysicalDisk.FriendlyName
- MSFT_PhysicalDisk.HealthStatus
- MSFT_PhysicalDisk.OperationalStatus
- MSFT_PhysicalDisk.OperationalDetails
- MSFT_PhysicalDisk.PhysicalLocation
- MSFT_PhysicalDisk.VirtualDiskFootprint
- MSFT_PhysicalDisk.Usage
- MSFT_PhysicalDisk.SupportedUsages
- MSFT_PhysicalDisk.Description
- MSFT_PhysicalDisk.PartNumber
- MSFT_PhysicalDisk.FirmwareVersion
- MSFT_PhysicalDisk.SoftwareVersion
- MSFT_PhysicalDisk.Size
- MSFT_PhysicalDisk.AllocatedSize
- MSFT_PhysicalDisk.BusType
- MSFT_PhysicalDisk.IsWriteCacheEnabled
- MSFT_PhysicalDisk.IsPowerProtected
- MSFT_PhysicalDisk.PhysicalSectorSize
- MSFT_PhysicalDisk.LogicalSectorSize
- MSFT_PhysicalDisk.SpindleSpeed
- MSFT_PhysicalDisk.IsIndicationEnabled
- MSFT_PhysicalDisk.EnclosureNumber
- MSFT_PhysicalDisk.SlotNumber
- MSFT_PhysicalDisk.CanPool
- MSFT_PhysicalDisk.CannotPoolReason
- MSFT_PhysicalDisk.OtherCannotPoolReasonDescription
- MSFT_PhysicalDisk.IsPartial
- MSFT_PhysicalDisk.MediaType
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# MSFT\_PhysicalDisk class

Represents a subsystem drive or spindle.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
class MSFT_PhysicalDisk : MSFT_StorageFaultDomain
{
  UInt16  UniqueIdFormat;
  String  DeviceId;
  String  FriendlyName;
  UInt16  HealthStatus;
  UInt16  OperationalStatus[];
  String  OperationalDetails[];
  String  PhysicalLocation;
  UInt16  VirtualDiskFootprint;
  UInt16  Usage;
  UInt16  SupportedUsages[];
  String  Description;
  String  PartNumber;
  String  FirmwareVersion;
  String  SoftwareVersion;
  UInt64  Size;
  UInt64  AllocatedSize;
  UInt16  BusType;
  Boolean IsWriteCacheEnabled;
  Boolean IsPowerProtected;
  UInt64  PhysicalSectorSize;
  UInt64  LogicalSectorSize;
  UInt32  SpindleSpeed;
  Boolean IsIndicationEnabled;
  UInt16  EnclosureNumber;
  UInt16  SlotNumber;
  Boolean CanPool;
  UInt16  CannotPoolReason[];
  String  OtherCannotPoolReasonDescription;
  Boolean IsPartial;
  UInt16  MediaType;
};
```

## Members

The **MSFT\_PhysicalDisk** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_PhysicalDisk** class has these methods.



| Method                                                       | Description                                                                                                                       |
|:-------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------|
| [**Maintenance**](msft-physicaldisk-maintenance.md)         | Allows maintenance operations to be performed on the physical disk while in a concrete pool, such as firmware updates. |
| [**Reset**](msft-physicaldisk-reset.md)                     | Resets the physical disk.                                                                                              |
| [**SetAttributes**](msft-physicaldisk-setattributes.md)     | Updates the attributes of the physical disk.                                                                           |
| [**SetDescription**](msft-physicaldisk-setdescription.md)   | Sets or changes the description for the physical disk.                                                                 |
| [**SetFriendlyName**](msft-physicaldisk-setfriendlyname.md) | Sets or changes the friendly name for the physical disk.                                                               |
| [**SetUsage**](msft-physicaldisk-setusage.md)               | Sets or changes the intended usage for the physical disk within a concrete pool.                                       |
| [**SetWriteCache**](msft-physicaldisk-setwritecache.md)     | Allows the physical disk's write cache to be enabled or disabled.                                                      |



 

### Properties

The **MSFT\_PhysicalDisk** class has these properties.

 

**AllocatedSize**
   

Data type: **UInt64**
 

Access type: Read-only
 

Qualifiers: [**Units**](/windows/win32/wmisdk/standard-qualifiers) ("Bytes")
 

The total amount of used space on this physical disk. This should include usage from all storage pools and other data stored on the disk.

 

**BusType**
   

Data type: **UInt16**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

The storage bus type of the physical disk.



| Value                                                                                                                                                                                                                                                                        | Meaning                                           |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
|  **Unknown** 0                                                   | The bus type is unknown.               |
|  **SCSI** 1                                                                                      | SCSI                                   |
|  **ATAPI** 2                                                                                   | ATAPI                                  |
|  **ATA** 3                                                                                         | ATA                                    |
|  **1394** 4                                                                                                             | IEEE 1394                              |
|  **SSA** 5                                                                                         | SSA                                    |
|  **Fibre Channel** 6                           | Fibre Channel                          |
|  **USB** 7                                                                                         | USB                                    |
|  **RAID** 8                                                                                      | RAID                                   |
|  **iSCSI** 9                                                           | iSCSI                                  |
|  **SAS** 10                                                                                        | Serial Attached SCSI (SAS)             |
|  **SATA** 11                                                                                     | Serial ATA (SATA)                      |
|  **SD** 12                                                                                           | Secure Digital (SD)                    |
|  **MMC** 13                                                                                        | Multimedia Card (MMC)                  |
|  **MAX** 14                                                                                        | This value is reserved for system use. |
|  **File Backed Virtual** 15  | File-Backed Virtual                    |
|  **Storage Spaces** 16                      | Storage Spaces                         |
|  **NVMe** 17                                                              |                                                   |
|  **Microsoft Reserved** 18..    | This value is reserved for system use. |



 

 

**CannotPoolReason**
   

Data type: **UInt16** array
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

An array of values specifying the reasons why this physical disk cannot be added to a concrete pool. This property is valid only if the **CanPool** property is **FALSE**.

 

**Unknown** (0)
 

**Other** (1)
 

**In a Pool** (2)
 

**Not Healthy** (3)
 

**Removable Media** (4)
 

**In Use by Cluster** (5)
 

**Offline** (6)
 

**Insufficient Capacity** (7)
 

**Spare Disk** (8)
 

**Reserved by subsystem** (9)
 

**Starting** (10)
 

**Microsoft Reserved** (..)
 

**Vendor Reserved** (0x8000..)
 

 

**CanPool**
   

Data type: **Boolean**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

**TRUE** if this physical disk can be added to a concrete pool.

 

**Description**
   

Data type: **String**
 

Access type: Read-only
 

A user-settable description of the physical disk.

 

**DeviceId**
   

Data type: **String**
 

Access type: Read-only
 

An address or other identifier that uniquely names the physical disk.

 

**EnclosureNumber**
   

Data type: **UInt16**
 

Access type: Read-only
 

The number of the enclosure in which the disk physically resides.

 

**FirmwareVersion**
   

Data type: **String**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

A string representation of the firmware revision.

 

**FriendlyName**
   

Data type: **String**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

A user-friendly display name for the physical disk. The initial value should be set by the storage provider or subsystem, and can be modified by the user at any point in the object's lifetime.

 

**HealthStatus**
   

Data type: **UInt16**
 

Access type: Read-only
 

A high-level indication of device health.



| Value                                                                        | Meaning              |
|------------------------------------------------------------------------------|----------------------|
|  0  | Healthy   |
|  1  | Warning   |
|  2  | Unhealthy |
|  5  | Unknown   |



 

 

**IsIndicationEnabled**
   

Data type: **Boolean**
 

Access type: Read-only
 

Indicates whether the physical disk's identification LEDs are active or not. This is typically used in maintenance operations.

 

**IsPartial**
   

Data type: **Boolean**
 

Access type: Read-only
 

**TRUE** if this physical disk is partially consumed by a system or service outside of normal storage pool operations.

 

**IsPowerProtected**
   

Data type: **Boolean**
 

Access type: Read-only
 

Indicates whether this physical disk is equipped to tolerate a power loss without loss of data.

 

**IsWriteCacheEnabled**
   

Data type: **Boolean**
 

Access type: Read-only
 

Indicates whether write caching is enabled on this physical disk or not.

 

**LogicalSectorSize**
   

Data type: **UInt64**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers), [**Units**](/windows/win32/wmisdk/standard-qualifiers) ("Bytes")
 

The logical sector size of the physical disk, in bytes. For example: a 4K native disk should report 4096, while a 512-byte emulated disk should report 512.

 

**MediaType**
   

Data type: **UInt16**
 

Access type: Read-only
 

The media type of the physical disk.



| Value                                                                                                | Meaning                |
|------------------------------------------------------------------------------------------------------|------------------------|
|  **0**  | Unspecified |
|  **3**  | HDD         |
|  **4**  | SSD         |
|  **5**  | SCM         |



 

 

**OperationalDetails**
   

Data type: **String** array
 

Access type: Read-only
 

An array of strings providing further information on a given operational status.

 

**OperationalStatus**
   

Data type: **UInt16** array
 

Access type: Read-only
 

An array of operational status values further explaining a given health status.

 

**OtherCannotPoolReasonDescription**
   

Data type: **String**
 

Access type: Read-only
 

A string containing the vendor-defined reason why this physical disk cannot be added to a concrete pool. This property must be **NULL** if the value of the **CannotPoolReason** property is not **Other**.

 

**PartNumber**
   

Data type: **String**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

A string representation of the physical disk's part number or SKU.

 

**PhysicalLocation**
   

Data type: **String**
 

Access type: Read-only
 

This field is a free-form string indicating where the hardware is located.

 

**PhysicalSectorSize**
   

Data type: **UInt64**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers), [**Units**](/windows/win32/wmisdk/standard-qualifiers) ("Bytes")
 

The physical sector size of the physical disk, in bytes. For example: for 4K native and 512-byte emulated disks, the value of this property should be 4096.

 

**Size**
   

Data type: **UInt64**
 

Access type: Read-only
 

Qualifiers: [**Units**](/windows/win32/wmisdk/standard-qualifiers) ("Bytes")
 

Total physical storage size of the disk, in bytes.

 

**SlotNumber**
   

Data type: **UInt16**
 

Access type: Read-only
 

The number of the enclosure slot in which the disk physically resides.

 

**SoftwareVersion**
   

Data type: **String**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

A string representation of the software version number.

 

**SpindleSpeed**
   

Data type: **UInt32**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers), [**Units**](/windows/win32/wmisdk/standard-qualifiers) ("RPM")
 

The rotational speed of spindle-based physical disks. For solid state devices (SSDs) or other non-rotational media, this member should be set to 0. For rotating media that has an unknown speed, this member should be set to 0xFFFFFFFF (**UINT32\_MAX**).

 

**SupportedUsages**
   

Data type: **UInt16** array
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

An array of values that specify the supported usages for this physical disk.



| Value                                                                                                                                                                                                                                               | Meaning                                                                                                                                                                                                                                                                        |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  **Unknown** 0                          | The intended usage is not specified.                                                                                                                                                                                                                                |
|  **Auto-Select** 1          | This physical disk should only be used for data storage.                                                                                                                                                                                                            |
|  **Manual-Select** 2  | This physical disk should only be used if manually selected by an administrator at the time of virtual disk creation. A manual-select disk is selected using the *PhysicalDisksToUse* parameter to [**CreateVirtualDisk**](createvirtualdisk-msft-storagepool.md). |
|  **Hot Spare** 3                  | This physical disk should be used as a hot spare.                                                                                                                                                                                                                   |
|  **Retired** 4                          | This physical disk should be retired from use. At a minimum, no new allocations should go to this disk. If the virtual disks that reside on this disk are repaired, the data should be moved to another active physical disk.                                       |
|  **Journal** 5                          | This physical disk should be used as a cache for other devices comprising a virtual disk. It will back a virtual disk s write-back cache, if configured.                                                                                                            |



 

 

**UniqueIdFormat**
   

Data type: **UInt16**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

Indicates the type of identifier used in the *UniqueId* field (inherited from [**MSFT\_StorageObject**](msft-storageobject.md)). The identifier used in *UniqueId* must be the highest available identifier using the following order of preference: 8 (highest), 3, 2, 1, 0 (lowest). For example, if the physical disk device exposes identifiers of type 0, 1, and 3, *UniqueId* must be the identifier of type 3, and *UniqueIdFormat* should be set to 3.

 

**Vendor Specific** (0)
 

**Vendor Id** (1)
 

**EUI64** (2)
 

**FCPH Name** (3)
 

**SCSI Name String** (8)
 

 

**Usage**
   

Data type: **UInt16**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

The intended usage of this physical disk within a concrete pool.

Storage pools are required to follow the assigned policy for a physical disk.



| Value                                                                                                                                                                                                                                               | Meaning                                                                                                                                                                                                                                                                        |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  **Unknown** 0                          | The intended usage is not specified.                                                                                                                                                                                                                                |
|  **Auto-Select** 1          | This physical disk should only be used for data storage.                                                                                                                                                                                                            |
|  **Manual-Select** 2  | This physical disk should only be used if manually selected by an administrator at the time of virtual disk creation. A manual-select disk is selected using the *PhysicalDisksToUse* parameter to [**CreateVirtualDisk**](createvirtualdisk-msft-storagepool.md). |
|  **Hot Spare** 3                  | This physical disk should be used as a hot spare.                                                                                                                                                                                                                   |
|  **Retired** 4                          | This physical disk should be retired from use. At a minimum, no new allocations should go to this disk. If the virtual disks that reside on this disk are repaired, the data should be moved to another active physical disk.                                       |
|  **Journal** 5                          | This physical disk should be used as a cache for other devices comprising a virtual disk. It will back a virtual disk s write-back cache, if configured.                                                                                                            |



 

 

**VirtualDiskFootprint**
   

Data type: **UInt16**
 

Access type: Read-only
 

This field indicates the size in bytes of the user data footprint from virtual disks on this physical disk.

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



 

