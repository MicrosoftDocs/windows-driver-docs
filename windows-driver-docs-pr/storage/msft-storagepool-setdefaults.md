---
title: SetDefaults method of the MSFT\_StoragePool class
description: Sets or changes the default values for properties of the storage pool object.
ms.assetid: F9435AA1-B102-4628-B664-251D35AD40F1
keywords:
- SetDefaults method Windows Storage Management API
- SetDefaults method Windows Storage Management API , MSFT_StoragePool class
- MSFT_StoragePool class Windows Storage Management API , SetDefaults method
topic_type:
- apiref
api_name:
- MSFT_StoragePool.SetDefaults
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetDefaults method of the MSFT\_StoragePool class

Sets or changes the default values for properties of the storage pool object.

Note that not all parameters must be specified, and only those that are specified will be updated.

## Syntax


```mof
UInt32 SetDefaults(
  [in]  UInt16  ProvisioningTypeDefault,
  [in]  String  ResiliencySettingNameDefault,
  [in]  Boolean EnclosureAwareDefault,
  [in]  UInt64  WriteCacheSizeDefault,
  [in]  Boolean AutoWriteCacheSize,
  [out] String  ExtendedStatus
);
```



## Parameters

 

*ProvisioningTypeDefault* \[in\]
 

The default provisioning type for virtual disks in the storage pool.



| Value                                                                                                                                                                                                               | Meaning                                                                                    |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
|  **Thin** 1      | Storage for the virtual disk is allocated on demand.                            |
|  **Fixed** 2  | Storage for the virtual disk is allocated at the time of virtual disk creation. |



 

 

*ResiliencySettingNameDefault* \[in\]
 

The new default resiliency setting for the storage pool. The resiliency setting specified must already be associated with this storage pool.

 

*EnclosureAwareDefault* \[in\]
 

**TRUE** if the storage pool is enclosure aware by default. This parameter determines the default allocation policy for virtual disks created in an enclosure aware storage pool. For example, an enclosure aware subsystem could balance each data copy of the virtual disk across multiple physical enclosures such that each enclosure contains a full data copy of the virtual disk.

 

*WriteCacheSizeDefault* \[in\]
 

The new default size of the write cache for virtual disk creation.

 

*AutoWriteCacheSize* \[in\]
 

**TRUE** if the provider should pick up the auto write cache size; otherwise, **FALSE**.

 

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
 

**Access denied** (40001)
 

**There are not enough resources to complete the operation.** (40002)
 

**Cannot connect to the storage provider.** (46000)
 

**The storage provider cannot connect to the storage subsystem.** (46001)
 

**This operation is not supported on primordial storage pools.** (48000)
 

**The specified resiliency setting is not supported by this storage pool.** (48002)
 

**The storage pool could not complete the operation because its health or operational status does not permit it.** (48006)
 

**The storage pool could not complete the operation because its configuration is read-only.** (48007)
 

**No resiliency setting with that name exists.** (49000)
 

**The value for WriteCacheSize is outside of the supported range of values.** (50005)
 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_StoragePool**](msft-storagepool.md)
 

 

 





