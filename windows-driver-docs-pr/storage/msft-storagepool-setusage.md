---
title: SetUsage method of the MSFT\_StoragePool class
description: Sets or changes the intended usage for the storage pool object.
ms.assetid: CC133913-C19A-4565-8D91-45679B7C709A
keywords:
- SetUsage method Windows Storage Management API
- SetUsage method Windows Storage Management API , MSFT_StoragePool class
- MSFT_StoragePool class Windows Storage Management API , SetUsage method
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_StoragePool.SetUsage
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# SetUsage method of the MSFT\_StoragePool class

Sets or changes the intended usage for the storage pool object.

## Syntax


```mof
UInt32 SetUsage(
  [in]  UInt16 Usage,
  [in]  String OtherUsageDescription,
  [out] String ExtendedStatus
);
```



## Parameters

 

*Usage* \[in\]
 

The new usage for the storage pool. This parameter is required and cannot be NULL.

 

**Other** (1)
 

**Unrestricted** (2)
 

**Reserved for ComputerSystem (the block server)** (3)
 

**Reserved as a Delta Replica Container** (4)
 

**Reserved by Migration Services** (5)
 

**Reserved for Local Replication Services** (6)
 

**Reserved for Remote Replication Services** (7)
 

**Reserved for Sparing** (8)
   

*OtherUsageDescription* \[in\]
 

If *Usage* is set to **Other**, this parameter is the string representation of a vendor defined usage for this storage pool. This parameter must not be set if *Usage* is not **Other**.

 

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
 

**The storage pool could not complete the operation because its health or operational status does not permit it.** (48006)
 

**The storage pool could not complete the operation because its configuration is read-only.** (48007)
 

## Remarks

Not all storage pools may allow this method. Those that do not will cause this method to return **Not Supported**.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_StoragePool**](msft-storagepool.md)
 

 

 





