---
title: Online method of the MSFT\_Partition class
description: Brings the partition online by mounting the associated volume (if one exists).
ms.assetid: BC790184-88EE-4A45-A9E8-C520E26F991D
keywords:
- Online method Windows Storage Management API
- Online method Windows Storage Management API , MSFT_Partition class
- MSFT_Partition class Windows Storage Management API , Online method
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_Partition.Online
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# Online method of the MSFT\_Partition class

Brings the partition online by mounting the associated volume (if one exists).

## Syntax


```mof
UInt32 Online(
  [out] String ExtendedStatus
);
```



## Parameters

 

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
 

**In Use** (6)
 

**Access denied** (40001)
 

**There are not enough resources to complete the operation.** (40002)
 

**This operation is only supported on data partitions.** (42011)
 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_Partition**](msft-partition.md)
 

 

 





