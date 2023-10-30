---
title: MSFT\_StorageEnclosureToPhysicalDisk class
description: Association between StorageEnclosure and PhysicalDisk.
ms.assetid: B2FDB260-CD0D-4481-B002-572D58D0CF84
keywords:
- MSFT_StorageEnclosureToPhysicalDisk class Windows Storage Management API
- MSFT_StorageEnclosureToPhysicalDisk class Windows Storage Management API , described
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_StorageEnclosureToPhysicalDisk
- MSFT_StorageEnclosureToPhysicalDisk.StorageEnclosure
- MSFT_StorageEnclosureToPhysicalDisk.PhysicalDisk
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# MSFT\_StorageEnclosureToPhysicalDisk class

Association between [**StorageEnclosure**](msft-storageenclosure.md) and [**PhysicalDisk**](msft-physicaldisk.md).

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Association]
class MSFT_StorageEnclosureToPhysicalDisk
{
  MSFT_StorageEnclosure REF StorageEnclosure;
  MSFT_PhysicalDisk     REF PhysicalDisk;
};
```

## Members

The **MSFT\_StorageEnclosureToPhysicalDisk** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageEnclosureToPhysicalDisk** class has these properties.

 

**PhysicalDisk**
   

Data type: **[**MSFT\_PhysicalDisk**](msft-physicaldisk.md)**
 

Access type: Read-only
 

Qualifiers: [**Key**](/windows/win32/wmisdk/standard-qualifiers)
 

 

**StorageEnclosure**
   

Data type: **[**MSFT\_StorageEnclosure**](msft-storageenclosure.md)**
 

Access type: Read-only
 

Qualifiers: [**Key**](/windows/win32/wmisdk/standard-qualifiers)
 

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8.1 \[desktop apps only\]                                              |
| Minimum supported server | Windows Server 2012 R2 \[desktop apps only\]                                   |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_StorageEnclosure**](msft-storageenclosure.md)
 

[**MSFT\_PhysicalDisk**](msft-physicaldisk.md)
 

 

