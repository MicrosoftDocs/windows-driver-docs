---
title: MSFT\_DiskImage class
description: Represents a disk image.
ms.assetid: A895A5DB-39C7-4633-9C8C-3DA8AE8BD81A
keywords:
- MSFT_DiskImage class Windows Storage Management API
- MSFT_DiskImage class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_DiskImage
- MSFT_DiskImage.ImagePath
- MSFT_DiskImage.StorageType
- MSFT_DiskImage.DevicePath
- MSFT_DiskImage.FileSize
- MSFT_DiskImage.Size
- MSFT_DiskImage.LogicalSectorSize
- MSFT_DiskImage.BlockSize
- MSFT_DiskImage.Attached
- MSFT_DiskImage.Number
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_DiskImage class

Represents a disk image.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
class MSFT_DiskImage
{
  String  ImagePath;
  UInt32  StorageType;
  String  DevicePath;
  UInt64  FileSize;
  UInt64  Size;
  UInt64  LogicalSectorSize;
  UInt64  BlockSize;
  Boolean Attached;
  UInt32  Number;
};
```

## Members

The **MSFT\_DiskImage** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_DiskImage** class has these methods.



| Method                                      | Description                          |
|:--------------------------------------------|:-------------------------------------|
| [**Dismount**](msft-diskimage-dismount.md) | Dismounts the disk image. |
| [**Mount**](msft-diskimage-mount.md)       | Mounts the disk image.    |



 

### Properties

The **MSFT\_DiskImage** class has these properties.

 

**Attached**
   

Data type: **Boolean**
 

Access type: Read-only
 

**TRUE** if the disk image is attached.

 

**BlockSize**
   

Data type: **UInt64**
 

Access type: Read-only
 

Qualifiers: **Units** (Bytes)
 

Block size of the disk image, in bytes.

 

**DevicePath**
   

Data type: **String**
 

Access type: Read-only
 

The device path for the disk image.

 

**FileSize**
   

Data type: **UInt64**
 

Access type: Read-only
 

Qualifiers: **Units** (Bytes)
 

The file size, in bytes, of the disk image.

 

**ImagePath**
   

Data type: **String**
 

Access type: Read-only
 

Qualifiers: **Key**
 

The path to the disk image.

 

**LogicalSectorSize**
   

Data type: **UInt64**
 

Access type: Read-only
 

Qualifiers: **Units** (Bytes)
 

Logical sector size of the disk image, in bytes.

 

**Number**
   

Data type: **UInt32**
 

Access type: Read-only
 

The disk number of the disk image.

 

**Size**
   

Data type: **UInt64**
 

Access type: Read-only
 

Qualifiers: **Units** (Bytes)
 

The size, in bytes, of the disk image.

 

**StorageType**
   

Data type: **UInt32**
 

Access type: Read-only
 

Qualifiers: **Key**, **Values** ( "Unknown", "ISO", "VHD", "VHDX" ), **ValueMap** ("0", "1", "2", "3")
 

The type of the disk image.

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



 

 





