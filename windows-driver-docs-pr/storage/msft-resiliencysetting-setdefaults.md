---
title: SetDefaults method of the MSFT\_ResiliencySetting class
description: Allows a user to modify the default property values of the MSFT\_ResiliencySetting object.
ms.assetid: E568F70B-3492-4D17-BF77-657E091046C6
keywords:
- SetDefaults method Windows Storage Management API
- SetDefaults method Windows Storage Management API , MSFT_ResiliencySetting class
- MSFT_ResiliencySetting class Windows Storage Management API , SetDefaults method
topic_type:
- apiref
api_name:
- MSFT_ResiliencySetting.SetDefaults
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetDefaults method of the MSFT\_ResiliencySetting class

Allows a user to modify the default property values of the [**MSFT\_ResiliencySetting**](msft-resiliencysetting.md) object.

The updated values will only take effect for subsequent virtual disk creations and are not retroactively applied.

## Syntax


```mof
UInt32 SetDefaults(
  [in]  UInt16  NumberOfDataCopiesDefault,
  [in]  UInt16  PhysicalDiskRedundancyDefault,
  [in]  UInt16  NumberOfColumnsDefault,
  [in]  Boolean AutoNumberOfColumns,
  [in]  UInt64  InterleaveDefault,
  [out] String  ExtendedStatus
);
```



## Parameters

 

*NumberOfDataCopiesDefault* \[in\]
 

The desired number of full data copies to maintain. This value must be between the values of the **NumberofDataCopiesMin** and **NumberofDataCopiesMax** properties of the [**MSFT\_ResiliencySetting**](msft-resiliencysetting.md) object.

 

*PhysicalDiskRedundancyDefault* \[in\]
 

The desired level of physical disk failure tolerance. This value must be between the values of the **PhysicalDiskRedundancyMin** and **PhysicalDiskRedundancyMax** properties of the [**MSFT\_ResiliencySetting**](msft-resiliencysetting.md) object.

 

*NumberOfColumnsDefault* \[in\]
 

The desired number of physical disks to stripe data across. This value must be between the values of the **NumberOfColumnsMin** and **NumberofColumnsMax** properties of the [**MSFT\_ResiliencySetting**](msft-resiliencysetting.md) object.

 

*AutoNumberOfColumns* \[in\]
 

If **TRUE**, the storage provider (or subsystem) should automatically choose what it determines to be the best number of columns for this resiliency setting. If this parameter is **TRUE**, then the *NumberOfColumnsDefault* parameter must be **NULL**.

 

*InterleaveDefault* \[in\]
 

The desired size of a data strip on a single physical disk in a striping based resiliency setting. This value must be between the values of the **InterleaveMin** and **InterleaveMax** properties of the [**MSFT\_ResiliencySetting**](msft-resiliencysetting.md) object.

 

*ExtendedStatus* \[out\]
 

A string that contains an embedded [**MSFT\_StorageExtendedStatus**](msft-storageextendedstatus.md) object.

This parameter allows the storage provider to return extended (implementation-specific) error information.

 

## Return value



| Return code/value                                                                                                                                                                                                                                        | Description                                              |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
|  **Success** 0                                                                                                             | The method completed successfully.            |
|  **Not Supported** 1                                                                                                       | This method is not supported for this object. |
|  **Unspecified Error** 2                                                                                                   | An unspecified error has occurred.            |
|  **Timeout** 3                                                                                                             | The method has timed out.                     |
|  **Failed** 4                                                                                                              | The method failed.                            |
|  **Invalid Parameter** 5                                                                                                   | One or more parameter values were not valid.  |
|  **Access denied** 40001                                                                                                   |                                                          |
|  **There are not enough resources to complete the operation.** 40002                                                       |                                                          |
|  **Cannot connect to the storage provider.** 46000                                                                         |                                                          |
|  **The storage provider cannot connect to the storage subsystem.** 46001                                                   |                                                          |
|  **This operation is not supported on primordial storage pools.** 48000                                                    |                                                          |
|  **The storage pool could not complete the operation because its health or operational status does not permit it.** 48006  |                                                          |
|  **The storage pool could not complete the operation because its configuration is read-only.** 48007                       |                                                          |
|  **The value for PhysicalDiskRedundancy is outside of the supported range of values.** 49002                               |                                                          |
|  **The value for NumberOfDataCopies is outside of the supported range of values.** 49003                                   |                                                          |
|  **The value for Interleave is outside of the supported range of values.** 49005                                           |                                                          |
|  **The value for NumberOfColumns is outside of the supported range of values.** 49006                                      |                                                          |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_ResiliencySetting**](msft-resiliencysetting.md)
 

 

 





