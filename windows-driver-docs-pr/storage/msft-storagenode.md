---
title: MSFT\_StorageNode class
description: Represents a storage node in a cluster.
ms.assetid: EAEDDC82-F170-48C4-BA93-A414C96C00D1
keywords:
- MSFT_StorageNode class Windows Storage Management API
- MSFT_StorageNode class Windows Storage Management API , described
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_StorageNode
- MSFT_StorageNode.Name
- MSFT_StorageNode.NameFormat
- MSFT_StorageNode.OtherIdentifyingInfo
- MSFT_StorageNode.OtherIdentifyingInfoDescription
- MSFT_StorageNode.OperationalStatus
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# MSFT\_StorageNode class

Represents a storage node in a cluster.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class MSFT_StorageNode : MSFT_StorageObject
{
  String Name;
  UInt16 NameFormat;
  String OtherIdentifyingInfo[];
  String OtherIdentifyingInfoDescription[];
  UInt16 OperationalStatus;
};
```

## Members

The **MSFT\_StorageNode** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageNode** class has these properties.

 

**Name**
   

Data type: **String**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

Human-readable identifier of a storage node.

 

**NameFormat**
   

Data type: **UInt16**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

The format of **Name**.



| Value                                                                                                  | Meaning            |
|--------------------------------------------------------------------------------------------------------|--------------------|
|  **1**    | Other   |
|  **2**    | IP      |
|  **3**    | Dial    |
|  **4**    | HID     |
|  **5**    | NWA     |
|  **6**    | HWA     |
|  **7**    | X25     |
|  **8**    | ISDN    |
|  **9**    | IPX     |
|  **10**  | DCC     |
|  **11**  | ICD     |
|  **12**  | E.164   |
|  **13**  | SNA     |
|  **14**  | OID/OSI |
|  **15**  | WWN     |
|  **16**  | NAA     |



 

 

**OperationalStatus**
   

Data type: **UInt16**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

The current status of the node.



| Value                                                                                                  | Meaning            |
|--------------------------------------------------------------------------------------------------------|--------------------|
|  **0**    | Unknown |
|  **2**    | Up      |
|  **6**    | Down    |
|  **8**    | Joining |
|  **10**  | Paused  |



 

 

**OtherIdentifyingInfo**
   

Data type: **String** array
 

Access type: Read-only
 

Custom identifiers for the node. If this field is set, **OtherIdentifyingInfoDescription** must also be set.

 

**OtherIdentifyingInfoDescription**
   

Data type: **String** array
 

Access type: Read-only
 

Descriptions of the format used in the custom identifiers in **OtherIdentifyingInfo**. There must be a 1:1 mapping between this array and **OtherIdentifyingInfo**.

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8.1 \[desktop apps only\]                                              |
| Minimum supported server | Windows Server 2012 R2 \[desktop apps only\]                                   |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_StorageObject**](msft-storageobject.md)
 

 

