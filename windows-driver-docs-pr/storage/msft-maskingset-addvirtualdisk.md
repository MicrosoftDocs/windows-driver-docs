---
title: AddVirtualDisk method of the MSFT\_MaskingSet class
description: Adds one or more virtual disks to the masking set.
ms.assetid: D81ED854-CF77-4C55-9A2D-D17D7E64FD3B
keywords:
- AddVirtualDisk method Windows Storage Management API
- AddVirtualDisk method Windows Storage Management API , MSFT_MaskingSet class
- MSFT_MaskingSet class Windows Storage Management API , AddVirtualDisk method
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_MaskingSet.AddVirtualDisk
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# AddVirtualDisk method of the MSFT\_MaskingSet class

Adds one or more virtual disks to the masking set.

Adding a virtual disk allows the disk to be shown to the initiators contained in the set.

## Syntax


```mof
UInt32 AddVirtualDisk(
  [in]  String                  VirtualDiskNames[],
  [in]  UInt16                  DeviceNumbers[],
  [in]  UInt16                  DeviceAccesses[],
  [in]  Boolean                 RunAsJob,
  [out] MSFT_StorageJob REF CreatedStorageJob,
  [out] String                  ExtendedStatus
);
```



## Parameters

 

*VirtualDiskNames* \[in\]
 

Array of strings containing virtual disk names. This parameter is required and cannot be NULL.

 

*DeviceNumbers* \[in\]
 

Array of device numbers for the virtual disks. This parameter is required.

 

*DeviceAccesses* \[in\]
 

Array of device accesses for the virtual disks.

 

**Read Write** (2)
 

**Read-Only** (3)
 

**No Access** (4)
   

*RunAsJob* \[in\]
 

This parameter controls the asynchronous behavior the method will follow.

**TRUE** to use the *CreatedStorageJob* out parameter when the request takes a long time to service; otherwise **FALSE**.

If a storage job has been created to track the operation, this method will return 4096 - 'Method Parameters Checked - Job Started'. Note, even if *RunAsJob* is **TRUE**, the method can still return a result if it finishes in sufficient time.

If **FALSE** or **NULL**, this method will follow default WMI asynchronous behavior as determined by the client's method for invocation (i.e. synchronous unless requested otherwise).

 

*CreatedStorageJob* \[out\]
 

If *RunAsJob* is set to **TRUE** and this method takes a while to execute, this parameter returns a reference to the storage job used to track the long running operation.

 

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
 

**The specified virtual disk could not be found.** (50000)
 

**The device number specified is not valid.** (52000)
 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_MaskingSet**](msft-maskingset.md)
 

 

 





