---
title: Clear method of the MSFT\_Disk class
description: Removes partition information and uninitializes a disk, returning it to a RAW state.
ms.assetid: a3703b30-5e32-4bcf-9abd-fd3fb67fa6b6
keywords:
- Clear method Windows Storage Management API
- Clear method Windows Storage Management API , MSFT_Disk class
- MSFT_Disk class Windows Storage Management API , Clear method
topic_type:
- apiref
api_name:
- MSFT_Disk.Clear
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Clear method of the MSFT\_Disk class

Removes partition information and uninitializes a disk, returning it to a RAW state.

## Syntax


```mof
UInt32 Clear(
  [in]  Boolean RemoveData,
  [in]  Boolean RemoveOEM,
  [in]  Boolean ZeroOutEntireDisk,
  [out] String  ExtendedStatus
);
```



## Parameters

 

*RemoveData* \[in\]
 

**TRUE** if it is okay to remove data partitions from the disk. If this parameter is **FALSE** or **NULL**, this method will fail in the presence of a data partition.

 

*RemoveOEM* \[in\]
 

**TRUE** if it is okay to remove OEM and other special partitions. If this parameter is **FALSE** or not specified, this method will fail in the presence of these types of partitions.

 

*ZeroOutEntireDisk* \[in\]
 

**TRUE** if this parameter instructs this method to zero out the entire disk in addition to removing all partition information. If this parameter is **FALSE** or **NULL**, only the first and last megabytes of the disk are zeroed.

 

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
 

**Cannot clear with OEM partitions present. To clear OEM partitions, use the RemoveOEM flag.** (41007)
 

**Cannot clear with data partitions present. To clear data partitions, use the RemoveData flag.** (41008)
 

**Operation not supported on a critical disk.** (41009)
 

**There is no media in the device.** (41015)
 

**The specified object is managed by the Microsoft Failover Clustering component. The disk must be removed from the cluster to perform this operation.** (41019)
 

## Remarks

The caller must specify *RemoveData*, *RemoveOEM*, or both, unless it first deletes all data partitions, known OEM partitions, and ESP partitions on the disk. This requirement excludes metadata partitions such as the MSR, the LDM metadata partition, and unknown OEM partitions.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_Disk**](msft-disk.md)
 

 

 





