---
title: MSFT\_SoftError\_NotInCache class
description: Represents a not-in-cache error.
ms.assetid: EF2B4036-008A-49D2-A784-4089F62BEB3F
keywords:
- MSFT_SoftError_NotInCache class Windows Storage Management API
- MSFT_SoftError_NotInCache class Windows Storage Management API , described
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_SoftError_NotInCache
- MSFT_SoftError_NotInCache.MessageID
- MSFT_SoftError_NotInCache.Message
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# MSFT\_SoftError\_NotInCache class

Represents a not-in-cache error.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
class MSFT_SoftError_NotInCache : MSFT_SoftError
{
  String MessageID;
  String Message;
};
```

## Members

The **MSFT\_SoftError\_NotInCache** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SoftError\_NotInCache** class has these properties.

 

**Message**
   

Data type: **String**
 

Access type: Read-only
 

The message displayed to the user. The value of this property is "%1: The storage management provider's cache does not contain the requested object or object type.%2"

"%1" should be replaced with the corresponding storage provider's [**MSFT\_StorageProvider**](msft-storageprovider.md).**Name** property. "%2" can be replaced with extra error information.

 

**MessageID**
   

Data type: **String**
 

Access type: Read-only
 

The message identifier. The value of this property is "40006". This is the specific error code for 'Not in Cache'.

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_SoftError**](msft-softerror.md)
 

 

 





