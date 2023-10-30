---
title: Repair method of the MSFT\_Volume class
description: Repairs the volume.
ms.assetid: ee445db1-1afe-45ce-88f5-44fe8a13e002
keywords:
- Repair method Windows Storage Management API
- Repair method Windows Storage Management API , MSFT_Volume class
- MSFT_Volume class Windows Storage Management API , Repair method
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_Volume.Repair
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# Repair method of the MSFT\_Volume class

Repairs the volume.

## Syntax


```mof
UInt32 Repair(
  [in]  Boolean             OfflineScanAndFix,
  [in]  Boolean             Scan,
  [in]  Boolean             SpotFix,
  [out] UInt32              Output,
  [out] MSFT_StorageJob REF CreatedStorageJob,
  [out] String              ExtendedStatus
);
```



## Parameters

 

*OfflineScanAndFix* \[in\]
 

Set to TRUE to perform an offline scan and fix.

 

*Scan* \[in\]
 

Set to TRUE to scan the volume.

 

*SpotFix* \[in\]
 

Set to TRUE to perform spot fixes on the volume.

 

*Output* \[out\]
 

The output of the repair operation.

 

*CreatedStorageJob* \[out\]
 

Returns a reference to the storage job object used to track the long-running operation.

 

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
 

**This command is not supported on x86 running in x64 environment.** (7)
 

**Access Denied** (40001)
 

**An unexpected I/O error has occured** (40004)
 

**The specified file system is not supported** (43001)
 

**Cannot perform the requested operation when the drive is read only** (43006)
 

**The repair failed** (43007)
 

**The scan failed** (43008)
 

**A snapshot error occured while scanning this drive. You can try again, but if this problem persists, run an offline scan and fix.** (43009)
 

**A scan is already running on this drive. Chkdsk can not run more than one scan on a drive at a time.** (43010)
 

**A snapshot error occured while scanning this drive. You can try again, but if this problem persists, run an offline scan and fix.** (43011)
 

**A snapshot error occured while scanning this drive. Run an offline scan and fix.** (43012)
 

**Cannot open drive for direct access** (43013)
 

**Cannot determine the file system of the drive** (43014)
 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_Volume**](msft-volume.md)
 

 

 





