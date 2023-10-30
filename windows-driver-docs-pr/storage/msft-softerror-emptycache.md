---
title: MSFT\_SoftError\_EmptyCache class
description: Represents an empty-cache error.
ms.assetid: 9B5449D1-C89A-4087-B2C0-FA66BD8E6D6E
keywords:
- MSFT_SoftError_EmptyCache class Windows Storage Management API
- MSFT_SoftError_EmptyCache class Windows Storage Management API , described
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_SoftError_EmptyCache
- MSFT_SoftError_EmptyCache.MessageID
- MSFT_SoftError_EmptyCache.Message
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# MSFT\_SoftError\_EmptyCache class

Represents an empty-cache error.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
class MSFT_SoftError_EmptyCache : MSFT_SoftError
{
  String MessageID;
  String Message;
};
```

## Members

The **MSFT\_SoftError\_EmptyCache** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SoftError\_EmptyCache** class has these properties.

 

**Message**
   

Data type: **String**
 

Access type: Read-only
 

The message displayed to the user. The value of this property is "%1: The storage management provider's cache is empty.%2".

"%1" should be replaced with the corresponding storage provider's [**MSFT\_StorageProvider**](msft-storageprovider.md).**Name** property. "%2" can be replaced with extra error information.

 

**MessageID**
   

Data type: **String**
 

Access type: Read-only
 

The message identifier. The value of this property is "40003". This is the specific error code for 'Cache out of date'.

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_SoftError**](msft-softerror.md)
 

 

 





