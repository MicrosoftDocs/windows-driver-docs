---
title: CreateVolume method of the MSFT\_StoragePool class
description: Creates a virtual disk and single volume using the resources of the storage pool.
ms.assetid: 35FFE851-F9A4-43D6-BBB6-975836E79105
keywords:
- CreateVolume method Windows Storage Management API
- CreateVolume method Windows Storage Management API , MSFT_StoragePool class
- MSFT_StoragePool class Windows Storage Management API , CreateVolume method
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_StoragePool.CreateVolume
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# CreateVolume method of the MSFT\_StoragePool class

Creates a virtual disk and single volume using the resources of the storage pool.

## Syntax


```mof
UInt32 CreateVolume(
  [in]  String              FriendlyName,
  [in]  UInt64              Size,
  [in]  String              StorageTiers[],
  [in]  UInt64              StorageTierSizes[],
  [in]  UInt16              ProvisioningType,
  [in]  String              ResiliencySettingName,
  [in]  UInt16              PhysicalDiskRedundancy,
  [in]  UInt16              NumberOfColumns,
  [in]  UInt16              FileSystem,
  [in]  String              AccessPath,
  [in]  String              FileServer,
  [out] String              CreatedVolume,
  [out] MSFT_StorageJob REF CreatedStorageJob,
  [out] String              ExtendedStatus
);
```



## Parameters

 

*FriendlyName* \[in\]
 

The friendly name of the volume. The friendly name should describe the volume. It need not be unique. The label of the file system will also be set to this name.

This parameter is required and cannot be **NULL**.

 

*Size* \[in\]
 

The size of the virtual disk. Note that some storage subsystems will round the size up or down to a multiple of its allocation unit size. The size of the created volume will be as large as this virtual disk size allows.

 

*StorageTiers* \[in\]
 

The storage tiers on the virtual disk. Each array element is an [**MSFT\_StorageTier**](msft-storagetier.md) object.

 

*StorageTierSizes* \[in\]
 

The sizes of the tiers.

 

*ProvisioningType* \[in\]
 

The provisioning type of the volume.



| Value                                                                                                | Meaning                                                                                             |
|------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
|  **1**  | Thin provisioning - the storage for the volume is allocated on-demand.                   |
|  **2**  | Fixed provisioning - the storage for the volume is allocated when the volume is created. |



 

 

*ResiliencySettingName* \[in\]
 

The name of the resiliency setting to use as a template for this the volume. It is the same as the **Name** property of the resiliency setting instance. Only resiliency settings associated with this storage pool may be used.

 

*PhysicalDiskRedundancy* \[in\]
 

The number of physical disk failures that the virtual disk can withstand without data loss. If not specified, the value used is the **PhysicalDiskRedundancyDefault** member of the resiliency setting specified by *ResiliencySettingName*.

 

*NumberOfColumns* \[in\]
 

The number of physical disks to use to stripe the data. If not specified, the value used is the **NumberOfColumnsDefault** member of the resiliency setting specified by *ResiliencySettingName*.

 

*FileSystem* \[in\]
 

The type of file system to use on the created volume. A CSV file system is only supported on a storage spaces subsystem. For CSV the pool must be clusterable and the volume created will be a cluster shared volume.

This parameter is required and cannot be **NULL**.



| Value                                                                                                                                   | Meaning                |
|-----------------------------------------------------------------------------------------------------------------------------------------|------------------------|
|  **14**                                   | NTFS        |
|  **15**                                   | ReFS        |
|  **0x8000**  | CSVFS\_NTFS |
|  **0x8001**  | CSVFS\_ReFS |



 

 

*AccessPath* \[in\]
 

A local access path to the volume. If the access path could not be set, or this parameter is **NULL**, a new access path will be assigned.

 

*FileServer* \[in\]
 

**Starting in Windows 10:** A string that contains an embedded [**MSFT\_FileServer**](msft-fileserver.md) object, representing the file server that will own this volume.

 

*CreatedVolume* \[out\]
 

The created volume, a [**MSFT\_Volume**](msft-volume.md) object.

 

*CreatedStorageJob* \[out\]
 

Returns a reference to the storage job object used to track the long-running operation.

 

*ExtendedStatus* \[out\]
 

Extended error information in a [**MSFT\_StorageExtendedStatus**](msft-storageextendedstatus.md) object. The information is implementation-specific.

 

## Return value

 

**Success** (0)
 

**Not Supported** (1)
 

**Unspecified Error** (2)
 

**Timeout** (3)
 

**Failed** (4)
 

**Invalid Parameter** (5)
 

**Method Parameters Checked - Job Started** (4096)
 

**Size Not Supported** (4097)
 

**Not enough free space** (40000)
 

**Access denied** (40001)
 

**There are not enough resources to complete the operation.** (40002)
 

**An unexpected I/O error has occurred.** (40004)
 

**You must specify a size by using either the *Size* or the *UseMaximumSize* parameter. You can specify only one of these parameters at a time.** (40005)
 

**The requested access path is already in use.** (42002)
 

**The access path is not valid.** (42007)
 

**The specified file system is not supported.** (43001)
 

**The volume cannot be quick formatted.** (43002)
 

**Cannot perform the requested operation when the drive is read only.** (43006)
 

**You must specify a name for this volume.** (43017)
 

**You must specify a file server to expose this volume to.** (43018)
 

**The volume is not exposed to the specified file server.** (43019)
 

**Cannot connect to the storage provider.** (46000)
 

**The storage provider cannot connect to the storage subsystem.** (46001)
 

**Failover clustering could not be enabled for this storage object.** (46008)
 

**This operation is not supported on primordial storage pools.** (48000)
 

**The storage pool is reserved for special usage only.** (48001)
 

**The specified resiliency setting is not supported by this storage pool.** (48002)
 

**There are not enough physical disks in the storage pool to create the specified virtual disk configuration.** (48004)
 

**The storage pool could not complete the operation because its health or operational status does not permit it.** (48006)
 

**The storage pool could not complete the operation because its configuration is read-only.** (48007)
 

**You must specify the size info (either the *Size* or *UseMaximumSize* parameter) or the tier info (the *StorageTiers* and *StorageTierSizes* parameters), but not both size info and tier info.** (48010)
 

**No resiliency setting with that name exists.** (49000)
 

**The value for *NoSinglePointOfFailure* is not supported.** (49001)
 

**The value for *PhysicalDiskRedundancy* is outside of the supported range of values.** (49002)
 

**The value for *NumberOfDataCopies* is outside of the supported range of values.** (49003)
 

**The value for *ParityLayout* is outside of the supported range of values.** (49004)
 

**The value for *Interleave* is outside of the supported range of values.** (49005)
 

**The value for *NumberOfColumns* is outside of the supported range of values.** (49006)
 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8.1 \[desktop apps only\]                                              |
| Minimum supported server | Windows Server 2012 R2 \[desktop apps only\]                                   |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_StoragePool**](msft-storagepool.md)
 

 

 





