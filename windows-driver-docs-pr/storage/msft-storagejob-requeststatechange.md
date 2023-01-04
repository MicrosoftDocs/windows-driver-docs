---
title: RequestStateChange method of the MSFT\_StorageJob class
description: Requests that the state of the job be changed to the value specified in the RequestedState parameter.
ms.assetid: 5259BE29-2B3C-4FED-9D99-14264751D898
keywords:
- RequestStateChange method Windows Storage Management API
- RequestStateChange method Windows Storage Management API , MSFT_StorageJob class
- MSFT_StorageJob class Windows Storage Management API , RequestStateChange method
topic_type:
- apiref
api_name:
- MSFT_StorageJob.RequestStateChange
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RequestStateChange method of the MSFT\_StorageJob class

Requests that the state of the job be changed to the value specified in the *RequestedState* parameter.

## Syntax


```mof
UInt32 RequestStateChange(
  [in]  UInt16 RequestedState,
  [out] String ExtendedStatus
);
```



## Parameters

 

*RequestedState* \[in\]
 

The new state.



| Value                                                                                                                                                                                                                                                                  | Meaning                                                                                                                                                                                                                                                                                                             |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  **Start** 2                                                     | This value changes the value of the **JobState** property to **Running**.                                                                                                                                                                                                                                |
|  **Suspend** 3                                             | This value stops the job temporarily. The intention is to subsequently restart the job with a second call to **RequestStateChange** with the *RequestedState* parameter set to **Start**. It might be possible for the job to enter the **Service** state while it is suspended. (This is job-specific.) |
|  **Terminate** 4                                     | This value stops the job cleanly, saving data, preserving the state, and shutting down all underlying processes in an orderly manner.                                                                                                                                                                    |
|  **Kill** 5                                                         | This value terminates the job immediately with no requirement to save data or preserve the state.                                                                                                                                                                                                        |
|  **Service** 6                                             | This value puts the job into a vendor-specific service state. It might be possible to restart the job.                                                                                                                                                                                                   |
|  **DMTF Reserved** 7..32767              | Values between 7 and 32767 (inclusive) are reserved for DMTF.                                                                                                                                                                                                                                            |
|  **Vendor Reserved** 32768..65535  | Values between 32768 and 65535 (inclusive) are reserved for vendors.                                                                                                                                                                                                                                     |



 

 

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
 

**Access denied** (40001)
 

**There are not enough resources to complete the operation.** (40002)
 

**Cannot connect to the storage provider.** (46000)
 

**The storage provider cannot connect to the storage subsystem.** (46001)
 

## Remarks

If you call this method multiple times, earlier requests could be overwritten or lost.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_StorageJob**](msft-storagejob.md)
 

 

 





