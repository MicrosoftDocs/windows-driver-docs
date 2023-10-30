---
title: MSFT\_SoftError class
description: Represents a soft error.
ms.assetid: 95810BD7-A582-4B4A-A878-35CDDD949599
keywords:
- MSFT_SoftError class Windows Storage Management API
- MSFT_SoftError class Windows Storage Management API , described
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_SoftError
- MSFT_SoftError.ErrorType
- MSFT_SoftError.OwningEntity
- MSFT_SoftError.MessageID
- MSFT_SoftError.Message
- MSFT_SoftError.PerceivedSeverity
- MSFT_SoftError.ErrorSource
- MSFT_SoftError.ErrorSourceFormat
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# MSFT\_SoftError class

Represents a soft error.

Soft errors can be returned by intrinsic methods (such as **EnumerateInstances** and **GetInstance**) to help distinguish between a query with no results (no error) and a query that fails for a specific reason.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
class MSFT_SoftError : CIM_Error
{
  UInt16 ErrorType;
  String OwningEntity;
  String MessageID;
  String Message;
  UInt16 PerceivedSeverity;
  String ErrorSource;
  UInt16 ErrorSourceFormat;
};
```

## Members

The **MSFT\_SoftError** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SoftError** class has these properties.

 

**ErrorSource**
   

Data type: **String**
 

Access type: Read-only
 

The CIM Object Path to the storage management provider's [**MSFT\_StorageProvider**](msft-storageprovider.md) object.

 

**ErrorSourceFormat**
   

Data type: **UInt16**
 

Access type: Read-only
 

Qualifiers: **Values** ( "CIMObjectPath" ), **ValueMap** ("2")
 

The CIM object path.

 

**ErrorType**
   

Data type: **UInt16**
 

Access type: Read-only
 

Qualifiers: **Values** ( "Software Error" ), **ValueMap** ("4")
 

This error is of the type **Software Error**.

 

**Message**
   

Data type: **String**
 

Access type: Read-only
 

The message displayed to the user. The value of this property is "%1: %2".

"%1" should be replaced with the storage management provider's [**MSFT\_StorageProvider**](msft-storageprovider.md).**Name** property. "%2" should be replaced with the error message.

 

**MessageID**
   

Data type: **String**
 

Access type: Read-only
 

The message identifier.

 

**OwningEntity**
   

Data type: **String**
 

Access type: Read-only
 

Corresponds to the storage management provider's [**MSFT\_StorageProvider**](msft-storageprovider.md).**Name** property.

 

**PerceivedSeverity**
   

Data type: **UInt16**
 

Access type: Read-only
 

Qualifiers: **Values** ( "Information" ), **ValueMap** ("2")
 

This error is informative only.

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**CIM\_Error**](/previous-versions//cc150671(v=vs.85))
 

 

