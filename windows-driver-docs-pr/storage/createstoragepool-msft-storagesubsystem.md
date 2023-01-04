---
title: CreateStoragePool method of the MSFT\_StorageSubSystem class
description: Creates a storage pool from available physical disks contained within a common primordial pool.
ms.assetid: 3fa2f78f-be75-42c0-baba-b08f4959af8c
keywords:
- CreateStoragePool method Windows Storage Management API
- CreateStoragePool method Windows Storage Management API , MSFT_StorageSubSystem class
- MSFT_StorageSubSystem class Windows Storage Management API , CreateStoragePool method
topic_type:
- apiref
api_name:
- MSFT_StorageSubSystem.CreateStoragePool
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CreateStoragePool method of the MSFT\_StorageSubSystem class

Creates a storage pool from available physical disks contained within a common primordial pool.

A physical disk is available for storage pool creation if the **CanPool** property of its [**MSFT\_PhysicalDisk**](msft-physicaldisk.md) object is **TRUE**.

Storage pool creation is only available when the **SupportsStoragePoolCreation** property of the storage subsystem's [**MSFT\_StorageSubSystem**](msft-storagesubsystem.md) object is **TRUE**.

## Syntax


```mof
UInt32 CreateStoragePool(
  [in]  String              FriendlyName,
  [in]  UInt16              Usage,
  [in]  String              OtherUsageDescription,
  [in]  String              PhysicalDisks[],
  [in]  String              ResiliencySettingNameDefault,
  [in]  UInt16              ProvisioningTypeDefault,
  [in]  UInt64              LogicalSectorSizeDefault,
  [in]  Boolean             EnclosureAwareDefault,
  [in]  UInt64              WriteCacheSizeDefault,
  [in]  Boolean             AutoWriteCacheSize,
  [in]  Boolean             RunAsJob,
  [out] String              CreatedStoragePool,
  [out] MSFT_StorageJob REF CreatedStorageJob,
  [out] String              ExtendedStatus
);
```



## Parameters

 

*FriendlyName* \[in\]
 

Specifies the friendly name for the new storage pool.

Friendly names are expected to be descriptive, but they are not required to be unique. Note that some storage subsystems do not allow setting a friendly name during pool creation.

If a subsystem doesn't support this, storage pool creation should still succeed. However, the pool may have a different name assigned to it.

This parameter is required and cannot be NULL.

 

*Usage* \[in\]
 

Specifies the intended usage for the storage pool.

You can specify a predefined description or a custom description. To specify a predefined description, use a value other than **Other**.

To specify a custom description, use **Other** and specify a non-NULL value for the *OtherUsageDescription* parameter.

 

**Other** (1)
 

**Unrestricted** (2)
 

**Reserved for ComputerSystem (the block server)** (3)
 

**Reserved as a Delta Replica Container** (4)
 

**Reserved for Migration Services** (5)
 

**Reserved for Local Replication Services** (6)
 

**Reserved for Remote Replication Services** (7)
 

**Reserved for Sparing** (8)
   

*OtherUsageDescription* \[in\]
 

Allows a user to set a custom usage type for the new [**MSFT\_StoragePool**](msft-storagepool.md) object. This parameter can only be specified if the *Usage* parameter is set to **Other**.

 

*PhysicalDisks* \[in\]
 

An array of strings, each of which contains an embedded instance of the [**MSFT\_PhysicalDisk**](msft-physicaldisk.md) class.

This parameter is used to specify an array of [**MSFT\_PhysicalDisk**](msft-physicaldisk.md) objects that will be used as the backing data storage for the newly created storage pool. The physical disks must come from a primordial pool in the subsystem in which you are creating this pool. All of the physical disks must come from the same primordial pool.

This parameter is required and cannot be NULL.

 

*ResiliencySettingNameDefault* \[in\]
 

The desired resiliency setting to be used by default when creating a new virtual disk in this storage pool. If the subsystem's **SupportsMultipleResiliencySettingsPerStoragePool** property is set to **FALSE**, this parameter also acts as a hint to the storage management provider on which resiliency setting should be inherited by this storage pool. If no value is given, the storage management provider is responsible for choosing the most appropriate resiliency setting.

 

*ProvisioningTypeDefault* \[in\]
 

The desired provisioning type to be used by default when creating a new virtual disk on this storage pool. If this parameter is zero, the default provisioning type is inherited from the primordial pool.

 

**Thin** (1)
 

**Fixed** (2)
   

*LogicalSectorSizeDefault* \[in\]
 

The default logical sector size, in bytes. This is useful when a storage pool may contain a mix of 512-byte emulated and either 4K-byte native or 512-byte native physical disks.

 

*EnclosureAwareDefault* \[in\]
 

The default allocation policy for virtual disks created in an enclosure aware storage pool. For example, an enclosure-aware subsystem could balance each data copy of the virtual disk across multiple physical enclosures such that each enclosure contains a full data copy of the virtual disk.

 

*WriteCacheSizeDefault* \[in\]
 

The default size of the write cache for virtual disk creation.

 

*AutoWriteCacheSize* \[in\]
 

If **TRUE**, the provider should pick up the auto write cache size.

 

*RunAsJob* \[in\]
 

If **TRUE**, this method uses the *CreatedStorageJob* parameter when the request is taking a long time to service. If a storage job has been created to track the operation, this method will return **Method Parameters Checked - Job Started**.

> [!Note]  
> Even if *RunAsJob* is **TRUE**, this method can still return a result if it has finished in sufficient time.

 

If **FALSE** or **NULL**, this method will follow default WMI asynchronous behavior as determined by the client's method for invocation. In other words, it is synchronous unless requested otherwise.

 

*CreatedStoragePool* \[out\]
 

If the storage pool is successfully created, this parameter receives a string that contains an embedded [**MSFT\_StoragePool**](msft-storagepool.md) object.

 

*CreatedStorageJob* \[out\]
 

If *RunAsJob* is set to **TRUE** and this method takes a long time to execute, this parameter receives a reference to the storage job object that is used to track the long-running operation.

 

*ExtendedStatus* \[out\]
 

A string that contains an embedded [**MSFT\_StorageExtendedStatus**](msft-storageextendedstatus.md) object.

This parameter allows the storage provider to return extended (implementation-specific) error information.

 

## Return value

 

**Success** (0)
 

**Not Supported** (1)
 

**Unspecified Error** (2)
 

**Timeout** (3)
 

**Failed** (4)
 

**Invalid Parameter** (5)
 

**Object Not Found** (8)
 

**Method Parameters Checked - Job Started** (4096)
 

**Access denied** (40001)
 

**There are not enough resources to complete the operation.** (40002)
 

**Cache out of date** (40003)
 

**An unexpected I/O error has occurred** (40004)
 

**The request failed due to a fatal device hardware error.** (40007)
 

**Cannot connect to the storage provider.** (46000)
 

**The storage provider cannot connect to the storage subsystem.** (46001)
 

**Failover clustering could not be enabled for this storage object.** (46008)
 

**No resiliency setting with that name exists.** (49000)
 

**The value for WriteCacheSize is outside of the supported range of values.** (50005)
 

**One of the physical disks specified is not supported by this operation.** (51000)
 

**Not enough physical disks were specified to successfully complete the operation.** (51001)
 

**One of the physical disks specified is already in use.** (51002)
 

**One of the physical disks specified uses a sector size that is not supported by this storage pool.** (51003)
 

**One or more physical disks are not connected to the nodes on which the pool is being created.** (51005)
 

## Remarks

Subsystems that don't support storage pools should implement this method as follows:

-   The **SupportsAutomaticStoragePoolSelection** property of the [**MSFT\_StorageSubSystem**](msft-storagesubsystem.md) object should be set to **TRUE**.
-   The **SupportsStoragePoolCreation**, **SupportsStoragePoolModification**, and **SupportsStoragePoolDeletion** properties of the [**MSFT\_StorageSubSystem**](msft-storagesubsystem.md) object should be set to **FALSE**.
-   The [**MSFT\_VirtualDisk**](msft-virtualdisk.md) object should be created in the subsystem by calling [**MSFT\_StorageSubSystem.CreateVirtualDisk**](msft-storagesubsystem-createvirtualdisk.md). Support for this method is mandatory in this case.
-   Support for the [**MSFT\_StoragePool**](msft-storagepool.md) and [**MSFT\_ResiliencySetting**](msft-resiliencysetting.md) classes is not required.
-   Support for the [**MSFT\_StoragePool.CreateVirtualDisk**](createvirtualdisk-msft-storagepool.md) method is not required.

Subsystems that support storage pools but don't allow storage pool selection (administrator selection of the pool in which the virtual disk is created), creation, modification, or deletion should implement this method as follows:

-   The **SupportsAutomaticStoragePoolSelection** property of the [**MSFT\_StorageSubSystem**](msft-storagesubsystem.md) object should be set to **TRUE**.
-   The **SupportsStoragePoolCreation**, **SupportsStoragePoolModification**, and **SupportsStoragePoolDeletion** properties of the [**MSFT\_StorageSubSystem**](msft-storagesubsystem.md) object should be set to **FALSE**.
-   The [**MSFT\_VirtualDisk**](msft-virtualdisk.md) object should be created in the subsystem by calling [**MSFT\_StorageSubSystem.CreateVirtualDisk**](msft-storagesubsystem-createvirtualdisk.md). Support for this method is mandatory in this case.
-   The storage pool in which the [**MSFT\_VirtualDisk**](msft-virtualdisk.md) object will be created needs to be automatically selected by the SMP.
-   Support for the [**MSFT\_StoragePool**](msft-storagepool.md) and [**MSFT\_ResiliencySetting**](msft-resiliencysetting.md) classes is not required.
-   Support for the [**MSFT\_StoragePool.CreateVirtualDisk**](createvirtualdisk-msft-storagepool.md) method is not required.

Subsystems that support storage pools and storage pool selection but do not support storage pool creation, modification, or deletion should implement this method as follows:

-   The **SupportsAutomaticStoragePoolSelection** property of the [**MSFT\_StorageSubSystem**](msft-storagesubsystem.md) object should be set to **TRUE** only if the [**MSFT\_StoragePool.CreateVirtualDisk**](createvirtualdisk-msft-storagepool.md) method is implemented.
-   The **SupportsStoragePoolCreation**, **SupportsStoragePoolModification**, and **SupportsStoragePoolDeletion** properties of the [**MSFT\_StorageSubSystem**](msft-storagesubsystem.md) object should be set to **FALSE**.
-   The [**MSFT\_VirtualDisk**](msft-virtualdisk.md) object should be created in the subsystem by calling [**MSFT\_StorageSubSystem.CreateVirtualDisk**](msft-storagesubsystem-createvirtualdisk.md). Support for this method is mandatory in this case.
-   The storage pool in which the [**MSFT\_VirtualDisk**](msft-virtualdisk.md) object will be created needs to be automatically selected by the user.
-   Support for the [**MSFT\_StoragePool**](msft-storagepool.md) and [**MSFT\_ResiliencySetting**](msft-resiliencysetting.md) classes is required. Support for at least one concrete pool and one type of resiliency setting is required.
-   Support for the [**MSFT\_StoragePool.CreateVirtualDisk**](createvirtualdisk-msft-storagepool.md) method is optional.

Subsystems that support storage pools and storage pool selection and also support storage pool creation, modification, or deletion should implement this method as follows:

-   The **SupportsAutomaticStoragePoolSelection** property of the [**MSFT\_StorageSubSystem**](msft-storagesubsystem.md) object should be set to **TRUE** only if the [**MSFT\_StoragePool.CreateVirtualDisk**](createvirtualdisk-msft-storagepool.md) method is implemented.
-   The **SupportsStoragePoolCreation**, **SupportsStoragePoolModification**, and **SupportsStoragePoolDeletion** properties of the [**MSFT\_StorageSubSystem**](msft-storagesubsystem.md) object should be set to **TRUE**.
-   The [**MSFT\_VirtualDisk**](msft-virtualdisk.md) object should be created in the subsystem by calling [**MSFT\_StorageSubSystem.CreateVirtualDisk**](msft-storagesubsystem-createvirtualdisk.md). Support for this method is mandatory in this case.
-   The storage pool in which the [**MSFT\_VirtualDisk**](msft-virtualdisk.md) object will be created needs to be automatically selected by the user.
-   Support for the [**MSFT\_StoragePool**](msft-storagepool.md) and [**MSFT\_ResiliencySetting**](msft-resiliencysetting.md) classes is required. Support for at least one concrete pool and one type of resiliency setting is required.
-   Support for the [**MSFT\_StoragePool.CreateVirtualDisk**](createvirtualdisk-msft-storagepool.md) method is optional.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)
 

 

 





