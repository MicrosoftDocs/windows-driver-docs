---
title: CreateStorageTier method of the MSFT\_StoragePool class
description: Creates a storage tier template on the storage pool.
ms.assetid: F559AE08-E9E8-4BEF-9E54-C5F8E3E9A9A0
keywords:
- CreateStorageTier method Windows Storage Management API
- CreateStorageTier method Windows Storage Management API , MSFT_StoragePool class
- MSFT_StoragePool class Windows Storage Management API , CreateStorageTier method
topic_type:
- apiref
api_name:
- MSFT_StoragePool.CreateStorageTier
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CreateStorageTier method of the MSFT\_StoragePool class

Creates a storage tier template on the storage pool. This method is available only when the **SupportsStorageTierCreation** property on the storage subsystem is set to **TRUE**. If it is set to **FALSE**, this method will fail with **MI\_RESULT\_NOT\_SUPPORTED**. This method is not supported for primordial pools.

## Syntax


```mof
UInt32 CreateStorageTier(
  [in]  String              FriendlyName,
  [in]  UInt16              MediaType,
  [in]  String              Description,
  [in]  Boolean             RunAsJob,
  [out] String              CreatedStorageTier,
  [out] MSFT_StorageJob REF CreatedStorageJob,
  [out] String              ExtendedStatus
);
```



## Parameters

 

*FriendlyName* \[in\]
 

The friendly name of the storage tier.

 

*MediaType* \[in\]
 

The media type of the storage tier.



| Value                                                                                                | Meaning        |
|------------------------------------------------------------------------------------------------------|----------------|
|  **3**  | HDD |
|  **4**  | SSD |



 

 

*Description* \[in\]
 

The description of the storage tier.

 

*RunAsJob* \[in\]
 

If **TRUE**, this method uses the *CreatedStorageJob* parameter when the request is taking a long time to service. If a storage job has been created to track the operation, this method will return **Method Parameters Checked - Job Started**.

> [!Note]  
> Even if *RunAsJob* is **TRUE**, this method can still return a result if it has finished in sufficient time.

 

If **FALSE** or **NULL**, this method will follow default WMI asynchronous behavior as determined by the client's method for invocation. In other words, it is synchronous unless requested otherwise.

 

*CreatedStorageTier* \[out\]
 

The created storage tier, an [**MSFT\_StorageTier**](msft-storagetier.md) object.

 

*CreatedStorageJob* \[out\]
 

If *RunAsJob* is set to **TRUE** and this method takes a long time to execute, this parameter receives a reference to the storage job object that is used to track the long-running operation.

 

*ExtendedStatus* \[out\]
 

Extended error information in a [**MSFT\_StorageExtendedStatus**](msft-storageextendedstatus.md) object. This information is implementation-specific.

 

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
 

**The storage pool could not complete the operation because its configuration is read-only.** (48007)
 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8.1 \[desktop apps only\]                                              |
| Minimum supported server | Windows Server 2012 R2 \[desktop apps only\]                                   |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_StoragePool**](msft-storagepool.md)
 

 

 





