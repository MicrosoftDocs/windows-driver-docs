---
title: MSFT\_FileIntegrity class
description: Represents the file integrity state for a file.
ms.assetid: 1CDF98E4-3E19-4324-AE61-15F2FEF94BBA
keywords:
- MSFT_FileIntegrity class Windows Storage Management API
- MSFT_FileIntegrity class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_FileIntegrity
- MSFT_FileIntegrity.FileName
- MSFT_FileIntegrity.Enabled
- MSFT_FileIntegrity.Enforced
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_FileIntegrity class

Represents the file integrity state for a file.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
class MSFT_FileIntegrity
{
  String  FileName;
  Boolean Enabled;
  Boolean Enforced;
};
```

## Members

The **MSFT\_FileIntegrity** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_FileIntegrity** class has these methods.



| Method                                      | Description                                                                 |
|:--------------------------------------------|:----------------------------------------------------------------------------|
| [**Get**](msft-fileintegrity-get.md)       | Retrieves the file integrity information for the specified file. |
| [**Repair**](msft-fileintegrity-repair.md) | Scrubs the data for the specified file.                          |
| [**Set**](msft-fileintegrity-set.md)       | Sets the file integrity state for the specified file.            |



 

### Properties

The **MSFT\_FileIntegrity** class has these properties.

 

**Enabled**
   

Data type: **Boolean**
 

Access type: Read-only
 

Specifies whether integrity streams are enabled for this file.

 

**Enforced**
   

Data type: **Boolean**
 

Access type: Read-only
 

Specifies whether integrity streams are enforced for this file.

 

**FileName**
   

Data type: **String**
 

Access type: Read-only
 

The name of the file.

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



 

 





