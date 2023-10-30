---
title: DeleteObject method of the MSFT\_Partition class
description: Deletes the partition and corresponding volume.
ms.assetid: 4B1C92EE-4835-428E-BF52-4C816A60B418
keywords:
- DeleteObject method Windows Storage Management API
- DeleteObject method Windows Storage Management API , MSFT_Partition class
- MSFT_Partition class Windows Storage Management API , DeleteObject method
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_Partition.DeleteObject
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# DeleteObject method of the MSFT\_Partition class

Deletes the partition and corresponding volume.

## Syntax


```mof
UInt32 DeleteObject(
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
 

**In use** (6)
 

**Access denied** (40001)
 

**There are not enough resources to complete the operation.** (40002)
 

**The partition was deleted, although its access paths were not.** (42000)
 

**The extended partition still contains other partitions.** (42001)
 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_Partition**](msft-partition.md)
 

 

 





