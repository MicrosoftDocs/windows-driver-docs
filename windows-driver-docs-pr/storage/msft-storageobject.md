---
title: MSFT\_StorageObject class
description: MSFT\_StorageObject is the base class for all storage object classes.
ms.assetid: 0B9FF9B2-98AE-49C7-AD19-501FE30DE723
keywords:
- MSFT_StorageObject class Windows Storage Management API
- MSFT_StorageObject class Windows Storage Management API , described
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_StorageObject
- MSFT_StorageObject.ObjectId
- MSFT_StorageObject.UniqueId
- MSFT_StorageObject.PassThroughIds
- MSFT_StorageObject.PassThroughServer
- MSFT_StorageObject.PassThroughNamespace
- MSFT_StorageObject.PassThroughClass
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# MSFT\_StorageObject class

**MSFT\_StorageObject** is the base class for all storage object classes.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
class MSFT_StorageObject
{
  String ObjectId;
  String UniqueId;
  String PassThroughIds;
  String PassThroughServer;
  String PassThroughNamespace;
  String PassThroughClass;
};
```

## Members

The **MSFT\_StorageObject** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageObject** class has these properties.

 

**ObjectId**
   

Data type: **String**
 

Access type: Read-only
 

Qualifiers: [**Key**](/windows/win32/wmisdk/standard-qualifiers), [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

**ObjectId** is a mandatory property that is used to opaquely and uniquely identify an instance of a class. **ObjectId** values are required to be globally unique. That is, no two objects should ever have the same **ObjectId**, even if they are managed by separate storage management providers, or are on different storage subsystems.

The **ObjectId** is created and maintained for use of the Storage Management Providers and their clients to track instances of objects. If an object is visible through two different paths for example, if there are two separate storage management providers that point to the same storage subsystem then the same object may appear with two different **ObjectId** values. For determining if two object instances are the same object, refer to the **UniqueId** property.

 

**PassThroughClass**
   

Data type: **String**
 

Access type: Read-only
 

The WMI class name of the proprietary storage provider object.

 

**PassThroughIds**
   

Data type: **String**
 

Access type: Read-only
 

A comma-separated list of all implementation specific keys. This list is used by storage management applications to access the vendor proprietary object model. The list should be in the form: `key1='value1', key2='value2'`.

 

**PassThroughNamespace**
   

Data type: **String**
 

Access type: Read-only
 

The WMI namespace that contains the proprietary storage provider classes.

 

**PassThroughServer**
   

Data type: **String**
 

Access type: Read-only
 

The computer that is hosting the proprietary storage provider classes.

 

**UniqueId**
   

Data type: **String**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

**UniqueId** is a mandatory property that is used to uniquely identify a logical instance of a storage subsystem's object. This value must be the same for an object viewed by two or more provider instances, even if they are running on separate management servers. **UniqueId** can be any globally unique, opaque value, unless otherwise specified by a derived class.

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



 

