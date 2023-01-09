---
title: SetAttributes method of the MSFT\_StoragePool class
description: Sets or changes attribute values for the storage pool object.
ms.assetid: 01D081C7-349A-4344-AF11-123872887AE4
keywords:
- SetAttributes method Windows Storage Management API
- SetAttributes method Windows Storage Management API , MSFT_StoragePool class
- MSFT_StoragePool class Windows Storage Management API , SetAttributes method
topic_type:
- apiref
api_name:
- MSFT_StoragePool.SetAttributes
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetAttributes method of the MSFT\_StoragePool class

Sets or changes attribute values for the storage pool object.

## Syntax


```mof
UInt32 SetAttributes(
  [in]  Boolean IsReadOnly,
  [in]  Boolean ClearOnDeallocate,
  [in]  Boolean IsPowerProtected,
  [in]  UInt16  RepairPolicy,
  [in]  UInt16  RetireMissingPhysicalDisks,
  [in]  UInt16  ThinProvisioningAlertThresholds[],
  [out] String  ExtendedStatus
);
```



## Parameters

 

*IsReadOnly* \[in\]
 

Indicates whether or not the storage pool's configuration is read only. If **TRUE**, the storage pool will not allow modification to its properties or any of its associated elements.

 

*ClearOnDeallocate* \[in\]
 

If **TRUE**, physical disks should be zeroed (cleared of all data) when unmapped or removed from the storage pool. If **FALSE**, the behavior is subsystem defined.

 

*IsPowerProtected* \[in\]
 

If **TRUE**, the disks in this pool are able to tolerate power loss without data loss. For example, they automatically flush volatile buffers to non-volatile media after external power is disconnected.

 

*RepairPolicy* \[in\]
 

How the operating system repairs virtual disks for this storage pool.



| Value                                                                                                | Meaning                                                                                                                                                |
|------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
|  **2**  | Sequential - processes one allocation slab at a time. Repairs take longer, but with less impact on the I/O load.                            |
|  **3**  | Parallel - processes as many allocation slabs as it can in parallel. Repair time is minimized, but with significant impact on the I/O load. |



 

 

*RetireMissingPhysicalDisks* \[in\]
 

Specifies whether the storage subsystem will automatically retire physical disks that are missing from this storage pool and replace them with hot spares or other physical disks that are available in the storage pool.

 

**Auto** (1)
 

**Always** (2)
 

**Never** (3)
   

*ThinProvisioningAlertThresholds* \[in\]
 

An array of percentage values that represent various sparse (thin provisioning) thresholds. The minimum value for each value is 1; the maximum value is 100. When the virtual disk space usage crosses one of these thresholds, a notification will be broadcasted to all subscribed clients.

 

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
 

**The number of thin provisioning alert thresholds specified exceeds the limit for this storage pool.** (48009)
 

## Remarks

Not all parameters must be specified, and only those that are specified will be updated.

When you set the **IsReadOnly** property to **TRUE**, it must be set alone and must be the last attribute set.

If you want to set the **IsReadOnly**, **ClearOnDeallocate**, and **IsPowerProtected** properties:

1.  Call this method and specify appropriate values for the *ClearOnDeallocate* and *IsPowerProtected* parameter and **FALSE** for the *IsReadOnly* parameter.
2.  If the **IsReadOnly** property should be **TRUE**, call this method again and specify **TRUE** for the *IsReadOnly* parameter.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_StoragePool**](msft-storagepool.md)
 

 

 





