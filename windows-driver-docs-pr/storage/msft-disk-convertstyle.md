---
title: ConvertStyle method of the MSFT\_Disk class
description: Converts the partition style of an already initialized disk.
ms.assetid: 38C1C3A0-DAB0-490F-A308-D0966364B728
keywords:
- ConvertStyle method Windows Storage Management API
- ConvertStyle method Windows Storage Management API , MSFT_Disk class
- MSFT_Disk class Windows Storage Management API , ConvertStyle method
topic_type:
- apiref
api_name:
- MSFT_Disk.ConvertStyle
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ConvertStyle method of the MSFT\_Disk class

Converts the partition style of an already initialized disk.

## Syntax


```mof
UInt32 ConvertStyle(
  [in]  UInt16 PartitionStyle,
  [out] String ExtendedStatus
);
```



## Parameters

 

*PartitionStyle* \[in\]
 

The new partition style for the disk. This parameter is required.

 

**MBR** (1)
 

**GPT** (2)
   

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
 

**The disk is read only.** (41002)
 

**The disk is offline.** (41003)
 

**Operation not supported on a critical disk.** (41009)
 

**Cannot convert the style of a disk with data or other known partitions on it.** (41013)
 

**The disk is not large enough to support a GPT partition style.** (41014)
 

**The specified object is managed by the Microsoft Failover Clustering component. The disk must be removed from the cluster to perform this operation.** (41019)
 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_Disk**](msft-disk.md)
 

 

 





