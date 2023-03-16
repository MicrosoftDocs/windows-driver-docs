---
title: Dismount method of the MSFT\_DiskImage class
description: Dismounts the disk image.
ms.assetid: 67E66529-1B2C-4F53-A7C5-03FC4E671D7A
keywords:
- Dismount method Windows Storage Management API
- Dismount method Windows Storage Management API , MSFT_DiskImage class
- MSFT_DiskImage class Windows Storage Management API , Dismount method
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_DiskImage.Dismount
api_location:
- vds.h
api_type:
- COM
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# Dismount method of the MSFT\_DiskImage class

Dismounts the disk image.

## Syntax


```mof
UInt32 Dismount();
```



## Parameters

This method has no parameters.

## Return value

This method returns [**OpenVirtualDisk**](/windows/win32/api/virtdisk/nf-virtdisk-openvirtualdisk) and [**DetachVirtualDisk**](/windows/win32/api/virtdisk/nf-virtdisk-detachvirtualdisk) error codes converted to **HRESULT** codes.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| Header                   |  Vds.h           |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_DiskImage**](msft-diskimage.md)
 

 

