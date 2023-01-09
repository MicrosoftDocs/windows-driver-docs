---
title: Show method of the MSFT\_VirtualDisk class
description: Shows a virtual disk to an initiator.
ms.assetid: 6B2649E0-669B-4E8A-9DC5-78287ECE5625
keywords:
- Show method Windows Storage Management API
- Show method Windows Storage Management API , MSFT_VirtualDisk class
- MSFT_VirtualDisk class Windows Storage Management API , Show method
topic_type:
- apiref
api_name:
- MSFT_VirtualDisk.Show
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Show method of the MSFT\_VirtualDisk class

Shows a virtual disk to an initiator.

This operation is also known as "exposing" or "unmasking" a virtual disk.

## Syntax


```mof
UInt32 Show(
  [in]  String              TargetPortAddresses[],
  [in]  String              InitiatorAddress,
  [in]  UInt16              HostType,
  [in]  Boolean             RunAsJob,
  [out] MSFT_StorageJob REF CreatedStorageJob,
  [out] String              ExtendedStatus
);
```



## Parameters

 

*TargetPortAddresses* \[in\]
 

An array of target port addresses from which the virtual disk should be shown.

This parameter is required and cannot be **NULL**.

 

*InitiatorAddress* \[in\]
 

The address of the initiator to which the virtual disk should be shown.

This parameter is required and cannot be **NULL**.

 

*HostType* \[in\]
 

The host operating system or other host environmental factors that may influence the behavior that the storage system should have when showing a virtual disk to an initiator.

 

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
 

<span id="Standard"></span><span id="standard"></span><span id="STANDARD"></span>**Standard** (2)
 

<span id="Solaris"></span><span id="solaris"></span><span id="SOLARIS"></span>**Solaris** (3)
 

<span id="HPUX"></span><span id="hpux"></span>**HPUX** (4)
 

<span id="OpenVMS"></span><span id="openvms"></span><span id="OPENVMS"></span>**OpenVMS** (5)
 

<span id="Tru64"></span><span id="tru64"></span><span id="TRU64"></span>**Tru64** (6)
 

<span id="Netware"></span><span id="netware"></span><span id="NETWARE"></span>**Netware** (7)
 

<span id="Sequent"></span><span id="sequent"></span><span id="SEQUENT"></span>**Sequent** (8)
 

<span id="AIX"></span><span id="aix"></span>**AIX** (9)
 

<span id="DGUX"></span><span id="dgux"></span>**DGUX** (10)
 

<span id="Dynix"></span><span id="dynix"></span><span id="DYNIX"></span>**Dynix** (11)
 

<span id="Irix"></span><span id="irix"></span><span id="IRIX"></span>**Irix** (12)
 

<span id="Cisco_iSCSI_Storage_Router"></span><span id="cisco_iscsi_storage_router"></span><span id="CISCO_ISCSI_STORAGE_ROUTER"></span>**Cisco iSCSI Storage Router** (13)
 

<span id="Linux"></span><span id="linux"></span><span id="LINUX"></span>**Linux** (14)
 

<span id="Microsoft_Windows"></span><span id="microsoft_windows"></span><span id="MICROSOFT_WINDOWS"></span>**Microsoft Windows** (15)
 

<span id="OS400"></span><span id="os400"></span>**OS400** (16)
 

<span id="TRESPASS"></span><span id="trespass"></span>**TRESPASS** (17)
 

<span id="HI-UX"></span><span id="hi-ux"></span>**HI-UX** (18)
 

<span id="VMware_ESXi"></span><span id="vmware_esxi"></span><span id="VMWARE_ESXI"></span>**VMware ESXi** (19)
 

<span id="Microsoft_Windows_Server_2008"></span><span id="microsoft_windows_server_2008"></span><span id="MICROSOFT_WINDOWS_SERVER_2008"></span>**Microsoft Windows Server 2008** (20)
 

<span id="Microsoft_Windows_Server_2003"></span><span id="microsoft_windows_server_2003"></span><span id="MICROSOFT_WINDOWS_SERVER_2003"></span>**Microsoft Windows Server 2003** (21)
 

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved** (22..32767)
 

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>**Vendor Specific** (32768..65535)
   

*RunAsJob* \[in\]
 

If **TRUE**, this method uses the *CreatedStorageJob* parameter when the request is taking a long time to service. If a storage job has been created to track the operation, this method will return **Method Parameters Checked - Job Started**.

> [!Note]  
> Even if *RunAsJob* is **TRUE**, this method can still return a result if it has finished in sufficient time.

 

If **FALSE** or **NULL**, this method will follow default WMI asynchronous behavior as determined by the client's method for invocation. In other words, it is synchronous unless requested otherwise.

 

*CreatedStorageJob* \[out\]
 

If *RunAsJob* is set to **TRUE** and this method takes a long time to execute, this parameter receives a reference to the storage job object that is used to track the long-running operation.

 

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
 

**Cache out of date** (40003)
 

**Cannot connect to the storage provider.** (46000)
 

**The storage provider cannot connect to the storage subsystem.** (46001)
 

**The HostType requested is not supported.** (52001)
 

**The initiator address specified is not valid** (53000)
 

**The target port address specified is not valid.** (54000)
 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_VirtualDisk**](msft-virtualdisk.md)
 

 

 





