---
title: MSFT\_VolumeToFileShare class
description: Association between a MSFT\_Volume and its MSFT\_FileShare objects.
ms.assetid: 50CF46C1-F67C-436C-9E71-7C7DFE18BDA1
keywords:
- MSFT_VolumeToFileShare class Windows Storage Management API
- MSFT_VolumeToFileShare class Windows Storage Management API , described
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_VolumeToFileShare
- MSFT_VolumeToFileShare.Volume
- MSFT_VolumeToFileShare.FileShare
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# MSFT\_VolumeToFileShare class

Association between a [**MSFT\_Volume**](msft-volume.md) and its [**MSFT\_FileShare**](msft-fileshare.md) objects.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_VolumeToFileShare
{
  MSFT_Volume    REF Volume;
  MSFT_FileShare REF FileShare;
};
```

## Members

The **MSFT\_VolumeToFileShare** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_VolumeToFileShare** class has these properties.

 

**FileShare**
   

Data type: **[**MSFT\_FileShare**](msft-fileshareaccesscontrolentry.md)**
 

Access type: Read-only
 

Qualifiers: **Key**
 

 

**Volume**
   

Data type: **[**MSFT\_Volume**](msft-volume.md)**
 

Access type: Read-only
 

Qualifiers: **Key**
 

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 10 \[desktop apps only\]                                               |
| Minimum supported server | Windows Server 2016 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_FileShare**](msft-fileshare.md)
 

[**MSFT\_Volume**](msft-volume.md)
 

 

 





