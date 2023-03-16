---
title: MSFT\_ReplicaPeer class
description: An enumerable object that represents an object in a target subsystem for which there is a replication relationship.
ms.assetid: 5DE51AC0-E84A-4DD9-9F9B-E8A3F6948E9F
keywords:
- MSFT_ReplicaPeer class Windows Storage Management API
- MSFT_ReplicaPeer class Windows Storage Management API , described
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_ReplicaPeer
- MSFT_ReplicaPeer.PeerObjectType
- MSFT_ReplicaPeer.PeerObjectId
- MSFT_ReplicaPeer.PeerObjectName
- MSFT_ReplicaPeer.PeerUniqueId
- MSFT_ReplicaPeer.PeerSubsystemName
- MSFT_ReplicaPeer.PeerProviderURI
- MSFT_ReplicaPeer.IsPrimary
- MSFT_ReplicaPeer.PeerObject
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# MSFT\_ReplicaPeer class

An enumerable object that represents an object in a target subsystem for which there is a replication relationship.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class MSFT_ReplicaPeer : MSFT_StorageObject
{
  UInt16  PeerObjectType;
  String  PeerObjectId;
  String  PeerObjectName;
  String  PeerUniqueId;
  String  PeerSubsystemName;
  String  PeerProviderURI;
  Boolean IsPrimary;
  String  PeerObject;
};
```

## Members

The **MSFT\_ReplicaPeer** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_ReplicaPeer** class has these properties.

 

**IsPrimary**
   

Data type: **Boolean**
 

Access type: Read-only
 

If **TRUE**, the replica peer is primary; that is, it is a System Element and not a Synced Element.

 

**PeerObject**
   

Data type: **String**
 

Access type: Write-only
 

A string that contains an embedded [**MSFT\_StorageObject**](msft-storageobject.md) object, populated when *PeerObjectType* has the value of "EmbeddedInstance".

 

**PeerObjectId**
   

Data type: **String**
 

Access type: Read-only
 

The object Id of the replica peer within the replica's storage subsystem.

 

**PeerObjectName**
   

Data type: **String**
 

Access type: Read-only
 

The name of the replica peer within the replica's storage subsystem.

 

**PeerObjectType**
   

Data type: **UInt16**
 

Access type: Read-only
 

The object type of this replica peer.

 

**VirtualDisk** (4)
 

**Volume** (5)
 

**Microsoft Reserved** (..)
 

**Partition** (0x8000)
 

**ReplicationGroup** (0x8001)
 

**StorageSubSystem** (0x8002)
 

 

**PeerProviderURI**
   

Data type: **String**
 

Access type: Read-only
 

If the [**MSFT\_StorageProvider**](msft-storageprovider.md) is of type 2 ("SMI-S"), this field contains the protocol, computer host name, and port of the SMI-S server. Otherwise, this field will be NULL.

 

**PeerSubsystemName**
   

Data type: **String**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

The subsystem name of the replica peer within the replica's storage subsystem.

 

**PeerUniqueId**
   

Data type: **String**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

The unique Id of the replica peer within the replica's storage subsystem.

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 10 \[desktop apps only\]                                               |
| Minimum supported server | Windows Server 2016 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_StorageObject**](msft-storageobject.md)
 

 

