---
title: SetAttributes method of the MSFT\_Disk class
description: Sets the disk's attributes and properties.
ms.assetid: 71D7E14B-8E03-479A-BA80-821EE019B8CB
keywords:
- SetAttributes method Windows Storage Management API
- SetAttributes method Windows Storage Management API , MSFT_Disk class
- MSFT_Disk class Windows Storage Management API , SetAttributes method
topic_type:
- apiref
api_name:
- MSFT_Disk.SetAttributes
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetAttributes method of the MSFT\_Disk class

Sets the disk's attributes and properties. The disk must be online for most attributes to be set.

## Syntax


```mof
UInt32 SetAttributes(
  [in]  Boolean IsReadOnly,
  [in]  UInt32  Signature,
  [in]  String  Guid,
  [out] String  ExtendedStatus
);
```



## Parameters

 

*IsReadOnly* \[in\]
 

If **TRUE**, the disk will be made read-only. If **FALSE**, the disk will become writable.

 

*Signature* \[in\]
 

Sets the MBR signature of the disk. This parameter is only valid when the disk's **PartitionStyle** property is **MBR**. An error will be returned if the disk is any other partition style.

 

*Guid* \[in\]
 

Sets the GPT GUID of the disk. This parameter is only valid when the disk's **PartitionStyle** property is **GPT**. An error will be returned if the disk is any other partition style.

 

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
 

**Disk is in use** (6)
 

**Access denied** (40001)
 

**There are not enough resources to complete the operation.** (40002)
 

**Cache out of date** (40003)
 

**The disk has not been initialized.** (41000)
 

**The disk is offline.** (41003)
 

**A parameter is not valid for this type of partition.** (41006)
 

**Operation not supported on a critical disk.** (41009)
 

**The specified object is managed by the Microsoft Failover Clustering component. The disk must be in cluster maintenance mode and the cluster resource status must be online to perform this operation.** (41018)
 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_Disk**](msft-disk.md)
 

 

 





