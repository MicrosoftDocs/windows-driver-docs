---
title: Initialize method of the MSFT\_Disk class
description: Initializes a RAW disk with a particular partition style.
ms.assetid: 70782a94-406f-4c28-9562-8df554b65463
keywords:
- Initialize method Windows Storage Management API
- Initialize method Windows Storage Management API , MSFT_Disk class
- MSFT_Disk class Windows Storage Management API , Initialize method
topic_type:
- apiref
api_name:
- MSFT_Disk.Initialize
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Initialize method of the MSFT\_Disk class

Initializes a RAW disk with a particular partition style.

## Syntax


```mof
UInt32 Initialize(
  [in]  UInt16 PartitionStyle,
  [out] String ExtendedStatus
);
```



## Parameters

 

*PartitionStyle* \[in\]
 

The desired partition style for the disk. The default value for this parameter is **GPT**.

 

**MBR** (1)
 

**GPT** (2 )
   

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
 

**The disk has already been initialized.** (41001)
 

**The specified partition type is not valid.** (41010)
 

**The disk is not large enough to support a GPT partition style.** (41014)
 

**The specified object is managed by the Microsoft Failover Clustering component. The disk must be in cluster maintenance mode and the cluster resource status must be online to perform this operation.** (41018)
 

## Remarks

If no partition style is specified, GPT will be selected by default. If the disk is already initialized, this method will fail with a well-defined error code.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_Disk**](msft-disk.md)
 

 

 





