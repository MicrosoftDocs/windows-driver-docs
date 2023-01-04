---
title: MSFT\_DiskImageToVolume class
description: Association between DiskImage and Volume.
ms.assetid: A8E35879-C5E8-4FEA-A34E-397A0D99D6B9
keywords:
- MSFT_DiskImageToVolume class Windows Storage Management API
- MSFT_DiskImageToVolume class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_DiskImageToVolume
- MSFT_DiskImageToVolume.DiskImage
- MSFT_DiskImageToVolume.Volume
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_DiskImageToVolume class

Association between [**DiskImage**](msft-diskimage.md) and [**Volume**](msft-volume.md).

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_DiskImageToVolume
{
  MSFT_DiskImage REF DiskImage;
  MSFT_Volume    REF Volume;
};
```

## Members

The **MSFT\_DiskImageToVolume** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_DiskImageToVolume** class has these properties.

 

**DiskImage**
   

Data type: **[**MSFT\_DiskImage**](msft-diskimage.md)**
 

Access type: Read-only
 

Qualifiers: [**Key**](/windows/win32/wmisdk/standard-qualifiers)
 

 

**Volume**
   

Data type: **[**MSFT\_Volume**](msft-volume.md)**
 

Access type: Read-only
 

Qualifiers: [**Key**](/windows/win32/wmisdk/standard-qualifiers)
 

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_DiskImage**](msft-diskimage.md)
 

[**MSFT\_Volume**](msft-volume.md)
 

 

