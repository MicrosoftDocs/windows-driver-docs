---
title: Optimize method of the MSFT\_Volume class
description: Optimizes the volume.
ms.assetid: ef56d743-1b6b-421c-8ffc-82c08cc9dee1
keywords:
- Optimize method Windows Storage Management API
- Optimize method Windows Storage Management API , MSFT_Volume class
- MSFT_Volume class Windows Storage Management API , Optimize method
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_Volume.Optimize
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# Optimize method of the MSFT\_Volume class

Optimizes the volume.

## Syntax


```mof
UInt32 Optimize(
  [in]  Boolean ReTrim,
  [in]  Boolean Analyze,
  [in]  Boolean Defrag,
  [in]  Boolean SlabConsolidate,
  [in]  Boolean TierOptimize,
  [out] String  ExtendedStatus
);
```



## Parameters

 

*ReTrim* \[in\]
 

Set to TRUE to retrim the volume.

 

*Analyze* \[in\]
 

Set to TRUE to analyze the volume.

 

*Defrag* \[in\]
 

Set to TRUE to defragment the volume.

 

*SlabConsolidate* \[in\]
 

Set to TRUE to slab-consolidate the volume.

 

*TierOptimize* \[in\]
 

Set to TRUE to optimize the volume tiers.

 

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
 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_Volume**](msft-volume.md)
 

 

 





