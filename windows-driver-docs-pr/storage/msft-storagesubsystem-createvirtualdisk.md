---
title: CreateVirtualDisk method of the MSFT\_StorageSubSystem class
description: Creates a new virtual disk.
ms.assetid: D31EEC10-7DEA-4701-9025-FBD04A50E5F7
keywords:
- CreateVirtualDisk method Windows Storage Management API
- CreateVirtualDisk method Windows Storage Management API , MSFT_StorageSubSystem class
- MSFT_StorageSubSystem class Windows Storage Management API , CreateVirtualDisk method
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_StorageSubSystem.CreateVirtualDisk
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# CreateVirtualDisk method of the MSFT\_StorageSubSystem class

Creates a new virtual disk.

## Syntax


```mof
UInt32 CreateVirtualDisk(
  [in]      String              FriendlyName,
  [in]      UInt16              Usage,
  [in]      String              OtherUsageDescription,
  [in, out] UInt64              Size,
  [in]      Boolean             UseMaximumSize,
  [in]      UInt16              NumberOfDataCopies,
  [in]      UInt16              PhysicalDiskRedundancy,
  [in]      UInt16              NumberOfColumns,
  [in]      UInt64              Interleave,
  [in]      UInt16              ParityLayout,
  [in]      Boolean             RequestNoSinglePointOfFailure,
  [in]      Boolean             IsEnclosureAware,
  [in]      UInt16              ProvisioningType,
  [in]      Boolean             RunAsJob,
  [out]     String              CreatedVirtualDisk,
  [out]     MSFT_StorageJob REF CreatedStorageJob,
  [out]     String              ExtendedStatus
);
```



## Parameters

 

*FriendlyName* \[in\]
 

The friendly name for the virtual disk.

Friendly names are expected to be descriptive, but they are not required to be unique. Note that some storage subsystems do not allow setting a friendly name during virtual disk creation. If a subsystem doesn't support this, virtual disk creation should still succeed, however the disk may have a different name assigned to it.

This parameter is required and cannot be **NULL**.

 

*Usage* \[in\]
 

Specifies the intended usage for the virtual disk.

You can specify a predefined description or a custom description. To specify a predefined description, use a value other than **Other**.

To specify a custom description, use **Other** and specify a non-**NULL** value for the *OtherUsageDescription* parameter.

 

**Other** (1)
 

**Unrestricted** (2)
 

**Reserved for ComputerSystem (the block server)** (3)
 

**Reserved by Replication Services** (4)
 

**Reserved by Migration Services** (5)
 

**Local Replica Source** (6)
 

**Remote Replica Source** (7)
 

**Local Replica Target** (8)
 

**Remote Replica Target** (9)
 

**Local Replica Source or Target** (10)
 

**Remote Replica Source or Target** (11)
 

**Delta Replica Target** (12)
 

**Element Component** (13)
 

**Reserved as Pool Contributor** (14)
 

**Composite Volume Member** (15)
 

**Composite VirtualDisk Member** (16)
 

**Reserved for Sparing** (17)
   

*OtherUsageDescription* \[in\]
 

A vendor specific usage for the new virtual disk. This parameter can only be specified if the *Usage* parameter is set to **Other**.

 

*Size* \[in, out\]
 

Desired size, in bytes, of the virtual disk. Note that some storage subsystems will round the size up or down to a multiple of its allocation unit size.

The storage subsystem uses this parameter only if the *UseMaximumSize* parameter is **FALSE** or **NULL**.

If the *UseMaximumSize* parameter is **TRUE**, this parameter is ignored.

This parameter is required and cannot be zero.

 

*UseMaximumSize* \[in\]
 

If **TRUE**, use the maximum size available to create the virtual disk.

This parameter cannot be used together with the *Size* parameter.

 

*NumberOfDataCopies* \[in\]
 

The number of complete data copies to maintain for this virtual disk.

 

*PhysicalDiskRedundancy* \[in\]
 

The number of physical disk failures that the virtual disk should be able to withstand before data loss occurs.

 

*NumberOfColumns* \[in\]
 

The number of underlying physical disks across which data should be striped. This parameter is required.

 

*Interleave* \[in\]
 

The number of bytes that should for a strip in common striping-based resiliency settings. The strip is defined as the size of the portion of a stripe that lies on one physical disk. Thus *Interleave* \* *NumberOfColumns* will yield the size of one stripe. This parameter is required.

 

*ParityLayout* \[in\]
 

If a parity-based resiliency setting is desired, set this parameter to one of the following values.

If the desired resiliency setting is not parity-based, this property must be **NULL**.

 

**Non-rotated Parity** (1)
 

**Rotated Parity** (2)
   

*RequestNoSinglePointOfFailure* \[in\]
 

Set to **TRUE** to request no single point of failure.

 

*IsEnclosureAware* \[in\]
 

The allocation behavior for this virtual disk. Enclosure-aware virtual disks will intelligently pick the physical disks to use for their redundancy. If **TRUE**, the virtual disk will attempt to use physical disks from different enclosures to balance the fault tolerance between two or more physical enclosures.

 

*ProvisioningType* \[in\]
 

The provisioning type for the virtual disk.

 

**Thin** (1)
 

**Fixed** (2)
   

*RunAsJob* \[in\]
 

If **TRUE**, this method uses the *CreatedStorageJob* parameter when the request is taking a long time to service. If a storage job has been created to track the operation, this method will return **Method Parameters Checked - Job Started**.

> [!Note]  
> Even if *RunAsJob* is **TRUE**, this method can still return a result if it has finished in sufficient time.

 

If **FALSE** or **NULL**, this method will follow default WMI asynchronous behavior as determined by the client's method for invocation. In other words, it is synchronous unless requested otherwise.

 

*CreatedVirtualDisk* \[out\]
 

If the virtual disk is successfully created, this parameter receives a string that contains an embedded [**MSFT\_VirtualDisk**](msft-virtualdisk.md) object.

 

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
 

**Size Not Supported** (4097)
 

**Not enough free space** (40000)
 

**Access denied** (40001)
 

**There are not enough resources to complete the operation.** (40002)
 

**Cache out of date** (40003)
 

**You must specify a size by using either the Size or the UseMaximumSize parameter. You can specify only one of these parameters at a time.** (40005)
 

**Cannot connect to the storage provider.** (46000)
 

**The storage provider cannot connect to the storage subsystem.** (46001)
 

**No storage pools were found that can support this virtual disk configuration.** (47000)
 

**The value for NoSinglePointOfFailure is not supported.** (49001)
 

**The value for PhysicalDiskRedundancy is outside of the supported range of values.** (49002)
 

**The value for NumberOfDataCopies is outside of the supported range of values.** (49003)
 

**The value for ParityLayout is outside of the supported range of values.** (49004)
 

**The value for Interleave is outside of the supported range of values.** (49005)
 

**The value for NumberOfColumns is outside of the supported range of values.** (49006)
 

## Remarks

This method is typically used when one of the following is true:

-   The storage subsystem's storage pools do not allow virtual disk creation directly.
-   The storage subsystem doesn't support storage pools.

Storage management providers can also choose to implement this method to "intelligently" pick a storage pool for the user. If this method is supported, the subsystem's **SupportsAutomaticStoragePoolSelection** property should be set to **TRUE**.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)
 

 

 





