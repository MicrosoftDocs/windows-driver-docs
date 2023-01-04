---
title: CreateVirtualDisk method of the MSFT\_StoragePool class
description: Creates a virtual disk using the resources of the storage pool.
ms.assetid: 1a5bf78d-356c-44a7-8f76-2cad85d3c171
keywords:
- CreateVirtualDisk method Windows Storage Management API
- CreateVirtualDisk method Windows Storage Management API , MSFT_StoragePool class
- MSFT_StoragePool class Windows Storage Management API , CreateVirtualDisk method
topic_type:
- apiref
api_name:
- MSFT_StoragePool.CreateVirtualDisk
api_location:
- vdssys.h
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CreateVirtualDisk method of the MSFT\_StoragePool class

Creates a virtual disk using the resources of the storage pool.

## Syntax


```mof
UInt32 CreateVirtualDisk(
  [in]  String              FriendlyName,
  [in]  UInt64              Size,
  [in]  Boolean             UseMaximumSize,
  [in]  UInt16              ProvisioningType,
  [in]  String              ResiliencySettingName,
  [in]  UInt16              Usage,
  [in]  String              OtherUsageDescription,
  [in]  UInt16              NumberOfDataCopies,
  [in]  UInt16              PhysicalDiskRedundancy,
  [in]  UInt16              NumberOfColumns,
  [in]  Boolean             AutoNumberOfColumns,
  [in]  UInt64              Interleave,
  [in]  Boolean             IsEnclosureAware,
  [in]  String              PhysicalDisksToUse[],
  [in]  String              StorageTiers[],
  [in]  UInt64              StorageTierSizes[],
  [in]  UInt64              WriteCacheSize,
  [in]  Boolean             AutoWriteCacheSize,
  [in]  Boolean             RunAsJob,
  [out] String              CreatedVirtualDisk,
  [out] MSFT_StorageJob REF CreatedStorageJob,
  [out] String              ExtendedStatus
);
```



## Parameters

 

*FriendlyName* \[in\]
 

The friendly name for the virtual disk.

Friendly names are expected to be descriptive, but they are not required to be unique. Note that some storage pools do not allow setting a friendly name during virtual disk creation. If a storage pool doesn't support this, virtual disk creation should still succeed, however the virtual disk may have a different name assigned to it.

This parameter is required and cannot be **NULL**.

 

*Size* \[in\]
 

Indicates the desired size, in bytes, of the virtual disk. Note that some storage subsystems will round the size up or down to a multiple of its allocation unit size. On output, this parameter indicates the actual size of the virtual disk that was created. This parameter cannot be used if *UseMaximumSize* is set to **TRUE**.

 

*UseMaximumSize* \[in\]
 

If **TRUE**, this parameter instructs the storage array to create the largest possible virtual disk given the available resources of this storage pool. This parameter cannot be used if the *Size* parameter is set.

 

*ProvisioningType* \[in\]
 

Specifies the provisioning type for the virtual disk.



| Value                                                                                                                                                                                                                       | Meaning                                                                                                                                                                   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  **Unknown** 0  | The provisioning type is unknown. This could mean that this information is unavailable, or that the storage subsystem uses a proprietary method of allocation. |
|  **Thin** 1              | The storage for the virtual disk is allocated on demand.                                                                                                       |
|  **Fixed** 2          | The storage for the virtual disk is allocated when the disk is created.                                                                                        |



 

 

*ResiliencySettingName* \[in\]
 

The desired resiliency setting to use as a template for this virtual disk. This parameter's value should correspond to the particular [**MSFT\_ResiliencySetting**](msft-resiliencysetting.md) object's **Name** property. Only resiliency settings associated with this storage pool may be used.

 

*Usage* \[in\]
 

Specifies the intended usage for the virtual disk.

You can specify a predefined description or a custom description. To specify a predefined description, use a value other than **Other**.

To specify a custom description, use **Other** and specify a non-NULL value for the **OtherUsageDescription** property.

 

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
 

A vendor specific usage for the new virtual disk. This parameter can only be specified if the **Usage** property is set to **Other**.

 

*NumberOfDataCopies* \[in\]
 

Specifies the number of complete data copies to maintain for the virtual disk.

If specified, this value will override the **NumberOfDataCopiesDefault** which would have been inherited from the resiliency setting specified by *ResiliencySettingName*.

 

*PhysicalDiskRedundancy* \[in\]
 

Specifies how many physical disk failures the virtual disk should be able to withstand before data loss occurs. If specified, this value will override the **PhysicalDiskRedundancyDefault** which would have been inherited from the resiliency setting specified by *ResiliencySettingName*.

 

*NumberOfColumns* \[in\]
 

Specifies the number of underlying physical disks across which data should be striped. If specified, this value will override the **NumberOfColumnsDefault** which would have been inherited from the resiliency setting specified by *ResiliencySettingName*.

 

*AutoNumberOfColumns* \[in\]
 

If **TRUE**, this field instructs the storage provider (or subsystem) to automatically choose what it determines to be the best number of columns for the virtual disk. If this field is **TRUE**, the *NumberOfColumns* parameter must be **NULL**.

 

*Interleave* \[in\]
 

Specifies the number of bytes that should for a strip in the common striping-based resiliency settings. The strip is defined as the size of the portion of a stripe that lies on one physical disk. Thus *Interleave* \* *NumberOfColumns* will yield the size of one stripe of user data.

If this parameter is specified, this value will override the **InterleaveDefault** which would have been inherited from the resiliency setting specified by *ResiliencySettingName*.

 

*IsEnclosureAware* \[in\]
 

Determines the allocation behavior for this virtual disk. Enclosure aware virtual disks will intelligently pick the physical disks to use for their redundancy. If **TRUE**, the virtual disk will attempt to use physical disks from different enclosures to balance the fault tolerance between two or more physical enclosures.

 

*PhysicalDisksToUse* \[in\]
 

If this parameter contains a list of physical disks, allocation of this virtual disk's storage is limited to the physical disks in the list. These physical disks must already be added to this storage pool.

 

*StorageTiers* \[in\]
 

Storage tiers on this virtual disk. Each element of the array is an [**MSFT\_StorageTier**](msft-storagetier.md) object.

 

*StorageTierSizes* \[in\]
 

Sizes of the storage tiers.

 

*WriteCacheSize* \[in\]
 

Size of write cache on the virtual disk.

 

*AutoWriteCacheSize* \[in\]
 

**TRUE** if the provider should pick up the auto write cache size; otherwise, **FALSE**.

 

*RunAsJob* \[in\]
 

If **TRUE**, this method uses the *CreatedStorageJob* parameter when the request is taking a long time to service. If a storage job has been created to track the operation, this method will return **Method Parameters Checked - Job Started**.

> [!Note]  
> Even if *RunAsJob* is **TRUE**, this method can still return a result if it has finished in sufficient time.

 

If **FALSE** or **NULL**, this method will follow default WMI asynchronous behavior as determined by the client's method for invocation. In other words, it is synchronous unless requested otherwise.

 

*CreatedVirtualDisk* \[out\]
 

Receives a [**MSFT\_VirtualDisk**](msft-virtualdisk.md) object if this method is run normally (with *RunAsJob* set to **FALSE**) and the virtual disk is successfully created.

 

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
 

**You must specify a size by using either the Size or the UseMaximumSize parameter. You can specify only one of these parameters at a time.** (40005)
 

**Cannot connect to the storage provider.** (46000)
 

**The storage provider cannot connect to the storage subsystem.** (46001)
 

**Failover clustering could not be enabled for this storage object.** (46008)
 

**This subsystem does not support creation of virtual disks with the specified provisioning type.** (47001)
 

**This operation is not supported on primordial storage pools.** (48000)
 

**The storage pool is reserved for special usage only.** (48001)
 

**The specified resiliency setting is not supported by this storage pool.** (48002)
 

**There are not enough physical disks in the storage pool to create the specified virtual disk configuration.** (48004)
 

**The storage pool could not complete the operation because its health or operational status does not permit it.** (48006)
 

**The storage pool could not complete the operation because its configuration is read-only.** (48007)
 

**You must specify the size info (either the Size or UseMaximumSize parameter) or the tier info (the StorageTiers and StorageTierSizes parameters), but not both size info and tier info.** (48010)
 

**No auto-allocation drives found in storage pool.** (48011)
 

**No resiliency setting with that name exists.** (49000)
 

**The value for NoSinglePointOfFailure is not supported.** (49001)
 

**The value for PhysicalDiskRedundancy is outside of the supported range of values.** (49002)
 

**The value for NumberOfDataCopies is outside of the supported range of values.** (49003)
 

**The value for ParityLayout is outside of the supported range of values.** (49004)
 

**The value for Interleave is outside of the supported range of values.** (49005)
 

**The value for NumberOfColumns is outside of the supported range of values.** (49006)
 

**The value for WriteCacheSize is outside of the supported range of values.** (50005)
 

**One of the physical disks specified is not supported by this operation.** (51000)
 

**Not enough physical disks were specified to successfully complete the operation.** (51001)
 

## Remarks

This method is only available when the **SupportsVirtualDiskCreation** property on the storage subsystem is set to **TRUE**. If it is set to **FALSE**, this method will fail with **MI\_RESULT\_NOT\_SUPPORTED**.

This method is not supported for primordial pools.

This method only requires a *FriendlyName* and *Size* to be specified. Sizes can be specified explicitly through the *Size* parameter, or told to use the maximum available space from the storage pool by using the *UseMaximumSize* parameter. Both *FriendlyName* and *Size* are treated as goals rather than hard requirements. For example, not all SMI-S based arrays may support custom friendly names, however the virtual disk creation will still succeed. If the size specified is not achieved, then the actual size used for the virtual disk will be returned in the out parameter structure.

The usage of this virtual disk can be set using the *Usage* and *OtherUsageDescription* parameters. If a value for *OtherUsageDescription* is given, *Usage* must be set to 1 - 'Other', otherwise an error will be returned.

By default, the resiliency setting applied to this virtual disk will be whatever is specified in the storage pool's **ResiliencySettingNameDefault** property. This can be overridden using the *ResiliencySettingName* parameter. Note that the name given here must correspond to a resiliency setting associated with this storage pool. Any other value will result in an error.

Individual settings of the resiliency setting can be overridden using the *NumberOfDataCopies*, *PhysicalDiskRedundancy*, *NumberOfColumns*, and *Interleave* parameters. If these parameters are not used, the defaults from the resiliency setting will be used. These overrides will not persist back to the particular resiliency setting instance; however some storage providers may choose to create a new resiliency setting instance to capture this new configuration. If any of the goals specified in the override parameters are out of range, or are not supported by the storage pool, an error will be returned.

The provisioning policy for the virtual disk is determined in a similar way to the resiliency setting. If no preference is specified in the *ProvisioningType* parameter, the policy is determined by the storage pool's **ProvisioningTypeDefault** property. If the *ProvisioningType* parameter is specified, the default is ignored and the value specified will be used instead.

Allocation can be further controlled by the *PhysicalDisksToUse* parameter. There may be certain scenarios where a storage administrator wants to manually choose which physical disks should back the virtual disk. When this parameter is specified, data for the virtual disk will only be stored on the physical disks in this array and not on any others.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8.1 \[desktop apps only\]                                              |
| Minimum supported server | Windows Server 2012 R2 \[desktop apps only\]                                   |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| Header                   |  Vdssys.h        |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_StoragePool**](msft-storagepool.md)
 

 

 





