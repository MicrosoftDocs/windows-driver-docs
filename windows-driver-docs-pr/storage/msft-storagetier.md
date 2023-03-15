---
title: MSFT\_StorageTier class
description: Represents a storage tier.
ms.assetid: 0E049D07-DD37-4F64-8483-3ECF32211567
keywords:
- MSFT_StorageTier class Windows Storage Management API
- MSFT_StorageTier class Windows Storage Management API , described
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_StorageTier
- MSFT_StorageTier.FriendlyName
- MSFT_StorageTier.MediaType
- MSFT_StorageTier.Size
- MSFT_StorageTier.Description
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# MSFT\_StorageTier class

Represents a storage tier.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class MSFT_StorageTier : MSFT_StorageObject
{
  String FriendlyName;
  UInt16 MediaType;
  UInt64 Size;
  String Description;
};
```

## Members

The **MSFT\_StorageTier** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_StorageTier** class has these methods.



| Method                                                        | Description                                                        |
|:--------------------------------------------------------------|:-------------------------------------------------------------------|
| [**DeleteObject**](msft-storagetier-deleteobject.md)         | Deletes the storage tier.                               |
| [**GetSupportedSize**](msft-storagetier-getsupportedsize.md) | Returns the supported sizes for a new storage tier.     |
| [**Resize**](msft-storagetier-resize.md)                     | Resizes the storage tier on the virtual disk.           |
| [**SetAttributes**](msft-storagetier-setattributes.md)       | Updates or sets various attributes on the storage tier. |
| [**SetDescription**](msft-storagetier-setdescription.md)     | Updates the description of the storage tier.            |
| [**SetFriendlyName**](msft-storagetier-setfriendlyname.md)   | Renames the storage tier.                               |



 

### Properties

The **MSFT\_StorageTier** class has these properties.

 

**Description**
   

Data type: **String**
 

Access type: Read-only
 

A description of the storage tier, provided by the user.

 

**FriendlyName**
   

Data type: **String**
 

Access type: Read-only
 

The friendly name of the storage tier, defined by the user.

 

**MediaType**
   

Data type: **UInt16**
 

Access type: Read-only
 

The media type of the storage tier.



| Value                                                                                                | Meaning                |
|------------------------------------------------------------------------------------------------------|------------------------|
| <span id="0"></span> **0**  | Unspecified |
| <span id="3"></span> **3**  | HDD         |
| <span id="4"></span> **4**  | SSD         |



 

 

**Size**
   

Data type: **UInt64**
 

Access type: Read-only
 

The size of the tier on the virtual disk. This property is available only when the storage tier is part of a virtual disk. The property is unspecified for pool-level storage tiers.

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8.1 \[desktop apps only\]                                              |
| Minimum supported server | Windows Server 2012 R2 \[desktop apps only\]                                   |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_StorageObject**](msft-storageobject.md)
 

 

 





