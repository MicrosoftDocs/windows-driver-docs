---
title: MSFT\_FileShareAccessControlEntry class
description: Models the subsystem's concept of an access control entry for a file share.
ms.assetid: 0F2A94A2-BFA9-4895-B93F-71A502850F1E
keywords:
- MSFT_FileShareAccessControlEntry class Windows Storage Management API
- MSFT_FileShareAccessControlEntry class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_FileShareAccessControlEntry
- MSFT_FileShareAccessControlEntry.AccountName
- MSFT_FileShareAccessControlEntry.AccessControlType
- MSFT_FileShareAccessControlEntry.AccessRight
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_FileShareAccessControlEntry class

Models the subsystem's concept of an access control entry for a file share.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class MSFT_FileShareAccessControlEntry
{
  String AccountName;
  UInt16 AccessControlType;
  UInt16 AccessRight;
};
```

## Members

The **MSFT\_FileShareAccessControlEntry** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_FileShareAccessControlEntry** class has these properties.

 

**AccessControlType**
   

Data type: **UInt16**
 

Access type: Read-only
 

Denotes the access type:

 

**Allow** (0)
 

**Deny** (1)
 

 

**AccessRight**
   

Data type: **UInt16**
 

Access type: Read-only
 

Denotes the access right:

 

**Full** (0)
 

**Modify** (1)
 

**Read** (2)
 

**Custom** (3)
 

 

**AccountName**
   

Data type: **String**
 

Access type: Read-only
 

The name of the account to which the access right is granted.

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 10 \[desktop apps only\]                                               |
| Minimum supported server | Windows Server 2016 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



 

 





