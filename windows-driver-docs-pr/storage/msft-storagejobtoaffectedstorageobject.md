---
title: MSFT_StorageJobToAffectedStorageObject Class
description: Association between a MSFT\_StorageJob and MSFT\_StorageObject objects that are affected by the job operation.
ms.assetid: 86056850-8918-4AD4-BAFC-EE73DEFF8958
keywords:
- MSFT_StorageJobToAffectedStorageObject class Windows Storage Management API
- MSFT_StorageJobToAffectedStorageObject class Windows Storage Management API , described
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_StorageJobToAffectedStorageObject
- MSFT_StorageJobToAffectedStorageObject.StorageJob
- MSFT_StorageJobToAffectedStorageObject.AffectedStorageObject
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# MSFT\_StorageJobToAffectedStorageObject class

Association between a [**MSFT\_StorageJob**](msft-storagejob.md) and [**MSFT\_StorageObject**](msft-storageobject.md) objects that are affected by the job operation.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_StorageJobToAffectedStorageObject
{
  MSFT_StorageJob    REF StorageJob;
  MSFT_StorageObject REF AffectedStorageObject;
};
```

## Members

The **MSFT\_StorageJobToAffectedStorageObject** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageJobToAffectedStorageObject** class has these properties.

 

**AffectedStorageObject**
   

Data type: **[**MSFT\_StorageObject**](msft-storageobject.md)**
 

Access type: Read-only
 

Qualifiers: **Key**
 

The storage object that is affected by the job operation.

 

**StorageJob**
   

Data type: **[**MSFT\_StorageJob**](msft-storagejob.md)**
 

Access type: Read-only
 

Qualifiers: **Key**
 

The job object for the storage job.

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_StorageJob**](msft-storagejob.md)
 

[**MSFT\_StorageObject**](msft-storageobject.md)
 

 

 





