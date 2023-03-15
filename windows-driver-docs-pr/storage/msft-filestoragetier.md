---
title: MSFT\_FileStorageTier class
description: This class provides methods to manually pin a file onto a storage tier and to unpin it.
ms.assetid: 002FE1D2-A54F-45DB-B511-F7776A39FAD4
keywords:
- MSFT_FileStorageTier class Windows Storage Management API
- MSFT_FileStorageTier class Windows Storage Management API , described
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_FileStorageTier
- MSFT_FileStorageTier.FilePath
- MSFT_FileStorageTier.State
- MSFT_FileStorageTier.PlacementStatus
- MSFT_FileStorageTier.DesiredStorageTierName
- MSFT_FileStorageTier.FileSizeOnDesiredStorageTier
- MSFT_FileStorageTier.FileSize
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# MSFT\_FileStorageTier class

This class provides methods to manually pin a file onto a storage tier and to unpin it.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class MSFT_FileStorageTier
{
  String FilePath;
  UInt16 State;
  UInt16 PlacementStatus;
  String DesiredStorageTierName;
  UInt64 FileSizeOnDesiredStorageTier;
  UInt64 FileSize;
};
```

## Members

The **MSFT\_FileStorageTier** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_FileStorageTier** class has these methods.



| Method                                      | Description                                        |
|:--------------------------------------------|:---------------------------------------------------|
| [**Clear**](msft-filestoragetier-clear.md) | Unpins a file from a storage tier.      |
| [**Get**](msft-filestoragetier-get.md)     | Gets tier information for pinned files. |
| [**Set**](msft-filestoragetier-set.md)     | Pins a file to a storage tier.          |



 

### Properties

The **MSFT\_FileStorageTier** class has these properties.

 

**DesiredStorageTierName**
   

Data type: **String**
 

Access type: Read-only
 

The desired name of the storage tier.

 

**FilePath**
   

Data type: **String**
 

Access type: Read-only
 

Qualifiers: Key
 

The path of the file.

 

**FileSize**
   

Data type: **UInt64**
 

Access type: Read-only
 

The file size.

 

**FileSizeOnDesiredStorageTier**
   

Data type: **UInt64**
 

Access type: Read-only
 

The file size on the desired storage tier.

 

**PlacementStatus**
   

Data type: **UInt16**
 

Access type: Read-only
 

The placement status of the file.



| Value                                                                                                | Meaning                       |
|------------------------------------------------------------------------------------------------------|-------------------------------|
|  **0**  | Unknown            |
|  **1**  | Completely on tier |
|  **2**  | Partially on tier  |
|  **3**  | Not on tier        |



 

 

**State**
   

Data type: **UInt16**
 

Access type: Read-only
 

The state of the attempt to pin the file.



| Value                                                                                                | Meaning                          |
|------------------------------------------------------------------------------------------------------|----------------------------------|
|  **0**  | Unknown               |
|  **1**  | OK                    |
|  **2**  | Insufficient Capacity |
|  **3**  | In Process            |
|  **4**  | Pending               |



 

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8.1 \[desktop apps only\]                                              |
| Minimum supported server | Windows Server 2012 R2 \[desktop apps only\]                                   |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



 

 





