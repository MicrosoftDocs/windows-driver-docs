---
title: MSFT\_ReplicationGroup class
description: Represents a consistency grouping of storage replicas.
ms.assetid: C828E13D-0AC5-4E83-9BEE-982B4BB1D729
keywords:
- MSFT_ReplicationGroup class Windows Storage Management API
- MSFT_ReplicationGroup class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_ReplicationGroup
- MSFT_ReplicationGroup.FriendlyName
- MSFT_ReplicationGroup.Description
- MSFT_ReplicationGroup.HealthStatus
- MSFT_ReplicationGroup.OperationalStatus
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_ReplicationGroup class

Represents a consistency grouping of storage replicas.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class MSFT_ReplicationGroup : MSFT_StorageObject
{
  String FriendlyName;
  String Description;
  UInt16 HealthStatus;
  UInt16 OperationalStatus[];
};
```

## Members

The **MSFT\_ReplicationGroup** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_ReplicationGroup** class has these methods.



| Method                                                                                 | Description                                                               |
|:---------------------------------------------------------------------------------------|:--------------------------------------------------------------------------|
| [**AddMember**](msft-replicationgroup-addmember.md)                                   | Adds members to this replication group.                        |
| [**CreateReplica**](msft-replicationgroup-createreplica.md)                           | Creates a replication relationship between replication groups. |
| [**DeleteObject**](msft-replicationgroup-deleteobject.md)                             | Deletes an empty replication group.                            |
| [**GetReplicationSettings**](msft-replicationgroup-getreplicationsettings.md)         | Returns the replication settings for this replication group.   |
| [**RemoveMember**](msft-replicationgroup-removemember.md)                             | Remove members from this replication group.                    |
| [**SetFriendlyName**](msft-replicationgroup-setfriendlyname.md)                       | Sets the friendly name for the replication group.              |
| [**SetReplicationRelationship**](msft-replicationgroup-setreplicationrelationship.md) | Modifies the relationship between replication groups.          |
| [**SetReplicationSettings**](msft-replicationgroup-setreplicationsettings.md)         | Specifies the replication settings for this replication group. |



 

### Properties

The **MSFT\_ReplicationGroup** class has these properties.

 

**Description**
   

Data type: **String**
 

Access type: Read-only
 

A user-friendly string representing the description of the replication group.

 

**FriendlyName**
   

Data type: **String**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

A user-friendly string representing the name of the replication group.

 

**HealthStatus**
   

Data type: **UInt16**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

Denotes the current health status of the replication group. The health of a group is derived from the health of the backing storage replicas.



| Value                                                                                                                                                                                                                               | Meaning                                                                                         |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
|  **Healthy** 0          | All replicas are in a healthy state.                                                 |
|  **Warning** 1          | The majority of replicas are healthy, but one or more may be not fully synchronized. |
|  **Unhealthy** 2  | The majority of replicas are unhealthy or in a failed state.                         |
|  **Unknown** 5          |                                                                                                 |



 

 

**OperationalStatus**
   

Data type: **UInt16** array
 

Access type: Read-only
 

Indicates the current operating conditions of the group. Unlike *HealthStatus*, this field indicates the status of hardware, software, and infrastructure issues related to this group, and can contain multiple values.

 

**Unknown** (0)
 

**Other** (1)
 

**OK** (2)
 

**Degraded** (3)
 

**Stressed** (4)
 

**Predictive Failure** (5)
 

**Error** (6)
 

**Non-Recoverable Error** (7)
 

**Starting** (8)
 

**Stopping** (9)
 

**Stopped** (10)
 

**In Service** (11)
 

**No Contact** (12)
 

**Lost Communication** (13)
 

**Aborted** (14)
 

**Dormant** (15)
 

**Supporting Entity in Error** (16)
 

**Completed** (17)
 

**Power Mode** (18)
 

**Relocating** (19)
 

**Microsoft Reserved** (..)
 

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 10 \[desktop apps only\]                                               |
| Minimum supported server | Windows Server 2016 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_StorageObject**](msft-storageobject.md)
 

 

