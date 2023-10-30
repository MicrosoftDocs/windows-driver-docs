---
title: Upgrade method of the MSFT\_StoragePool class
description: Upgrades the metadata on the storage pool.
ms.assetid: FE6ADA25-70F4-49EF-AC2B-799AFCECFBBC
keywords:
- Upgrade method Windows Storage Management API
- Upgrade method Windows Storage Management API , MSFT_StoragePool class
- MSFT_StoragePool class Windows Storage Management API , Upgrade method
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_StoragePool.Upgrade
api_location:
- netcfgn.h
api_type:
- COM
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# Upgrade method of the MSFT\_StoragePool class

Upgrades the metadata on the storage pool. On Windows 8.1 or later, if a Windows 8 pool is present then this method can be used to upgrade the pool metadata so that it now becomes a Windows 8.1 pool and has new Windows 8.1 features (such as tiering) available.

## Syntax


```mof
UInt32 Upgrade(
  [out] String ExtendedStatus
);
```



## Parameters

 

*ExtendedStatus* \[out\]
 

Extended error information from the storage provider in a [**MSFT\_StorageExtendedStatus**](msft-storageextendedstatus.md) object. The information is implementation-specific.

 

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
 

**The storage pool could not complete the operation because its configuration is read-only.** (48007)
 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8.1 \[desktop apps only\]                                              |
| Minimum supported server | Windows Server 2012 R2 \[desktop apps only\]                                   |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| Header                   |  Netcfgn.h       |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_StoragePool**](msft-storagepool.md)
 

 

 





