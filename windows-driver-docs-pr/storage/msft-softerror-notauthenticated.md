---
title: MSFT\_SoftError\_NotAuthenticated class
description: Represents an access-denied error.
ms.assetid: EC170B07-05EA-46F7-A910-559C96DFAD7B
keywords:
- MSFT_SoftError_NotAuthenticated class Windows Storage Management API
- MSFT_SoftError_NotAuthenticated class Windows Storage Management API , described
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_SoftError_NotAuthenticated
- MSFT_SoftError_NotAuthenticated.MessageID
- MSFT_SoftError_NotAuthenticated.Message
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# MSFT\_SoftError\_NotAuthenticated class

Represents an access-denied error.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
class MSFT_SoftError_NotAuthenticated : MSFT_SoftError
{
  String MessageID;
  String Message;
};
```

## Members

The **MSFT\_SoftError\_NotAuthenticated** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SoftError\_NotAuthenticated** class has these properties.

 

**Message**
   

Data type: **String**
 

Access type: Read-only
 

The message displayed to the user. The value of this property is "%1: The storage management provider has not been authenticated with the storage subsystem \\"%2\\". Extra configuration may be required.%3"

"%1" should be replaced with the corresponding storage provider's [**MSFT\_StorageProvider**](msft-storageprovider.md).**Name** property. "%2" should be replaced with the subsystem's [**MSFT\_StorageSubSystem**](msft-storagesubsystem.md).**FriendlyName** property. "%3" can be replaced with extra error information.

 

**MessageID**
   

Data type: **String**
 

Access type: Read-only
 

The message identifier. The value of this property is "40001". This is the specific error code for 'Access Denied'.

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_SoftError**](msft-softerror.md)
 

 

 





