---
title: Mount method of the MSFT\_DiskImage class
description: Mounts the disk image.
ms.assetid: CD233786-8087-4093-834B-096FE2ADBEB1
keywords:
- Mount method Windows Storage Management API
- Mount method Windows Storage Management API , MSFT_DiskImage class
- MSFT_DiskImage class Windows Storage Management API , Mount method
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_DiskImage.Mount
api_location:
- vds.h
api_type:
- COM
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# Mount method of the MSFT\_DiskImage class

Mounts the disk image.

## Syntax


```mof
UInt32 Mount(
  [in] UInt16  Access,
  [in] Boolean NoDriveLetter
);
```



## Parameters

 

*Access* \[in\]
 

The access for the disk image.

 

**Unknown** (0)
 

**Read Write** (2)
 

**Read-Only** (3)
   

*NoDriveLetter* \[in\]
 

If **TRUE**, the disk image shouldn't be assigned a drive letter.

 

## Return value

If *Access* is not **DEVICE\_ACCESS\_READ\_ONLY** or **DEVICE\_ACCESS\_READ\_WRITE**, this method returns **E\_INVALIDARG**.

Otherwise, this method returns [**OpenVirtualDisk**](/windows/win32/api/virtdisk/nf-virtdisk-openvirtualdisk) and [**AttachVirtualDisk**](/windows/win32/api/virtdisk/nf-virtdisk-attachvirtualdisk) error codes converted to **HRESULT** codes.

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
 

 

