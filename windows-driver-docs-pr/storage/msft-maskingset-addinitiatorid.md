---
title: AddInitiatorId method of the MSFT\_MaskingSet class
description: Adds one or more initiator identifiers to the masking set.
ms.assetid: 2B0B1B65-01B5-459D-957F-FFEA7FD57DE5
keywords:
- AddInitiatorId method Windows Storage Management API
- AddInitiatorId method Windows Storage Management API , MSFT_MaskingSet class
- MSFT_MaskingSet class Windows Storage Management API , AddInitiatorId method
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_MaskingSet.AddInitiatorId
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# AddInitiatorId method of the MSFT\_MaskingSet class

Adds one or more initiator identifiers to the masking set.

All virtual disks in the masking set will be accessible (shown) to these initiators.

## Syntax


```mof
UInt32 AddInitiatorId(
  [in]  String                  InitiatorIds[],
  [in]  UInt16                  HostType,
  [in]  Boolean                 RunAsJob,
  [out] MSFT_StorageJob REF CreatedStorageJob,
  [out] String                  ExtendedStatus
);
```



## Parameters

 

*InitiatorIds* \[in\]
 

Array of strings containing initiator addresses. For each address contained in this array, a corresponding [**MSFT\_InitiatorId**](msft-initiatorid.md) instance should be created and then associated with this masking set using the [**MSFT\_MaskingSetToInitiatorId**](msft-maskingsettoinitiatorid.md) class.

This parameter is required and cannot be NULL.

 

*HostType* \[in\]
 

The host operating system or other host environmental factors that may influence the behavior that the storage system should have when showing a virtual disk to an initiator.

 

**Unknown** (0)
 

**Standard** (2)
 

**Solaris** (3)
 

**HPUX** (4)
 

**OpenVMS** (5)
 

**Tru64** (6)
 

**Netware** (7)
 

**Sequent** (8)
 

**AIX** (9)
 

**DGUX** (10)
 

**Dynix** (11)
 

**Irix** (12)
 

**Cisco iSCSI Storage Router** (13)
 

**Linux** (14)
 

**Microsoft Windows** (15)
 

**OS400** (16)
 

**TRESPASS** (17)
 

**HI-UX** (18)
 

**VMware ESXi** (19)
 

**Microsoft Windows Server 2008** (20)
 

**Microsoft Windows Server 2003** (21)
 

**Microsoft Reserved** (22..32767)
 

**Vendor Specific** (32768..65535)
   

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
 

**The initiator address specified is not valid** (53000)
 

**Only one initiator address is acceptable for this operation.** (53001)
 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_MaskingSet**](msft-maskingset.md)
 

 

 





