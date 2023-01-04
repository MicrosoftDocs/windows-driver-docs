---
title: SetDedupMode method of the MSFT\_Volume class
description: Enables or disables deduplication on the volume.
ms.assetid: A37E60BA-914A-4876-B411-138B8D9335B3
keywords:
- SetDedupMode method Windows Storage Management API
- SetDedupMode method Windows Storage Management API , MSFT_Volume class
- MSFT_Volume class Windows Storage Management API , SetDedupMode method
topic_type:
- apiref
api_name:
- MSFT_Volume.SetDedupMode
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetDedupMode method of the MSFT\_Volume class

Enables or disables deduplication on the volume.

## Syntax


```mof
UInt32 SetDedupMode(
  [in]  UInt32 SetDedupMode,
  [out] String ExtendedStatus
);
```



## Parameters

 

*SetDedupMode* \[in\]
 

New deduplication mode of the volume.

 

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>**Disabled** (0)
 

<span id="GeneralPurpose"></span><span id="generalpurpose"></span><span id="GENERALPURPOSE"></span>**GeneralPurpose** (1)
 

<span id="HyperV"></span><span id="hyperv"></span><span id="HYPERV"></span>**HyperV** (2)
 

<span id="Backup"></span><span id="backup"></span><span id="BACKUP"></span>**Backup** (3)
 

<span id="NotAvailable"></span><span id="notavailable"></span><span id="NOTAVAILABLE"></span>**NotAvailable** (4)
   

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
 

**Object Not Found** (8)
 

**Access denied** (40001)
 

**Deduplication feature is not available** (43020)
 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 10 \[desktop apps only\]                                               |
| Minimum supported server | Windows Server 2016 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_Volume**](msft-volume.md)
 

 

 





