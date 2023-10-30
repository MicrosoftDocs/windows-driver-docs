---
title: CreateMaskingSet method of the MSFT\_StorageSubSystem class
description: Creates a new masking set.
ms.assetid: 479E1710-0101-4791-9936-07B1F1644454
keywords:
- CreateMaskingSet method Windows Storage Management API
- CreateMaskingSet method Windows Storage Management API , MSFT_StorageSubSystem class
- MSFT_StorageSubSystem class Windows Storage Management API , CreateMaskingSet method
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_StorageSubSystem.CreateMaskingSet
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# CreateMaskingSet method of the MSFT\_StorageSubSystem class

Creates a new masking set.

A masking set is a logical grouping of virtual disks, target ports, and initiators for the purpose of showing virtual disks to host computers

## Syntax


```mof
UInt32 CreateMaskingSet(
  [in]  String              FriendlyName,
  [in]  String              VirtualDiskNames[],
  [in]  UInt16              DeviceAccesses[],
  [in]  String              DeviceNumbers[],
  [in]  String              TargetPortAddresses[],
  [in]  String              InitiatorAddresses[],
  [in]  UInt16              HostType,
  [in]  Boolean             RunAsJob,
  [out] MSFT_StorageJob REF CreatedStorageJob,
  [out] String              CreatedMaskingSet,
  [out] String              ExtendedStatus
);
```



## Parameters

 

*FriendlyName* \[in\]
 

The friendly name for the masking set.

Friendly names are expected to be descriptive, but they are not required to be unique.

This parameter is required and cannot be **NULL**.

 

*VirtualDiskNames* \[in\]
 

The list of virtual disks to show to the initiators in the masking set. Each disk must be specified by the identifier that is stored in the **Name** property of its [**MSFT\_VirtualDisk**](msft-virtualdisk.md) object

This parameter has a 1:1 mapping with the *DeviceAccesses* parameter. Both arrays must be the same length, and the elements must be arranged in the same order.

 

*DeviceAccesses* \[in\]
 

The level of access that the initiator should have to each virtual disk specified in the *VirtualDiskNames* parameter. This parameter has a 1:1 mapping with the *VirtualDiskNames* parameter. Both arrays must be the same length, and the elements must be arranged in the same order.

 

**Unknown** (0)
 

**Read Write** (2)
 

**Read-Only** (3)
 

**No Access** (4)
   

*DeviceNumbers* \[in\]
 

Specifies the order in which the virtual disks should be shown to initiators. This capability is only available if the storage subsystem's **MaskingClientSelectableDeviceNumbers** property is **TRUE**. If specified, this parameter must have a 1:1 mapping with the *VirtualDiskNames* parameter.

 

*TargetPortAddresses* \[in\]
 

The target ports to use when showing the virtual disks to initiators. The number of target ports that can be specified depends on the subsystem's **MaskingPortsPerView** property. If **MaskingPortsPerView** is **All target ports share the same view**, this parameter is ignored, and all target ports on the system are associated with this masking set.

 

*InitiatorAddresses* \[in\]
 

The initiators to which the virtual disks should be shown. If the subsystem's **MaskingOneInitiatorIdPerView** property is **TRUE**, only one initiator can be specified for this masking set. The list of valid initiator address formats is specified by the subsystem's **MaskingValidInitiatorIdTypes** property.

 

*HostType* \[in\]
 

The host operating system or other host environmental factors that may influence the behavior that the storage system should have when showing a virtual disk to an initiator.

Values between 22 and 32767 (inclusive) are reserved for DMTF. Values between 32768 to 65535 (inclusive) are reserved for vendors.

 

**Unknown** (0)
 

**Other** (1)
 

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
 

**DMTF Reserved** (22..32767)
 

**Vendor Specific** (32768..65535)
   

*RunAsJob* \[in\]
 

If **TRUE**, this method uses the *CreatedStorageJob* parameter when the request is taking a long time to service. If a storage job has been created to track the operation, this method will return **Method Parameters Checked - Job Started**.

> [!Note]  
> Even if *RunAsJob* is **TRUE**, this method can still return a result if it has finished in sufficient time.

 

If **FALSE** or **NULL**, this method will follow default WMI asynchronous behavior as determined by the client's method for invocation. In other words, it is synchronous unless requested otherwise.

 

*CreatedStorageJob* \[out\]
 

If *RunAsJob* is set to **TRUE** and this method takes a long time to execute, this parameter receives a reference to the storage job object that is used to track the long-running operation.

 

*CreatedMaskingSet* \[out\]
 

If the masking set is created successfully, this parameter receives a string that contains an embedded [**MSFT\_MaskingSet**](msft-maskingset.md) object.

 

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
 

**Method Parameters Checked - Job Started** (4096)
 

**Access denied** (40001)
 

**There are not enough resources to complete the operation.** (40002)
 

**Cannot connect to the storage provider.** (46000)
 

**The storage provider cannot connect to the storage subsystem.** (46001)
 

**The specified virtual disk could not be found.** (50000)
 

**The device number specified is not valid.** (52000)
 

**The HostType requested is not supported.** (52001)
 

**DeviceAccess must be specified for each virtual disk.** (52002)
 

**The initiator address specified is not valid** (53000)
 

**Only one initiator address is acceptable for this operation.** (53001)
 

**The target port address specified is not valid.** (54000)
 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)
 

 

 





