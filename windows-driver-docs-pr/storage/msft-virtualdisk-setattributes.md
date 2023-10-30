---
title: SetAttributes method of the MSFT\_VirtualDisk class
description: Sets or updates various attributes for the virtual disk.
ms.assetid: AC57C471-7424-4F01-9C1E-44E523BBC8F2
keywords:
- SetAttributes method Windows Storage Management API
- SetAttributes method Windows Storage Management API , MSFT_VirtualDisk class
- MSFT_VirtualDisk class Windows Storage Management API , SetAttributes method
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_VirtualDisk.SetAttributes
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# SetAttributes method of the MSFT\_VirtualDisk class

Sets or updates various attributes for the virtual disk.

## Syntax


```mof
UInt32 SetAttributes(
  [in]  Boolean IsManualAttach,
  [in]  UInt16  Access,
  [out] String  ExtendedStatus
);
```



## Parameters

 

*IsManualAttach* \[in\]
 

If **TRUE**, this virtual disk will only be attached to the system if an explicit call is made to the [**Attach**](msft-virtualdisk-attach.md) method. Note that this property is specific to storage spaces.

 

*Access* \[in\]
 

Indicates whether the virtual disk is available for read and write access.

 

<span id="Readable"></span><span id="readable"></span><span id="READABLE"></span>**Readable** (1)
 

<span id="Writeable"></span><span id="writeable"></span><span id="WRITEABLE"></span>**Writeable** (2)
 

<span id="Read_Write"></span><span id="read_write"></span><span id="READ_WRITE"></span>**Read/Write** (3)
 

<span id="Write_Once"></span><span id="write_once"></span><span id="WRITE_ONCE"></span>**Write Once** (4)
   

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
 

**The storage pool could not complete the operation because its health or operational status does not permit it.** (48006)
 

**The storage pool could not complete the operation because its configuration is read-only.** (48007)
 

**The virtual disk could not complete the operation because another computer controls its configuration.** (50002)
 

**The virtual disk could not complete the operation because its health or operational status does not permit it.** (50003)
 

## Remarks

Not all parameters must be specified, and only those that are specified will be updated.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_VirtualDisk**](msft-virtualdisk.md)
 

 

 





