---
title: MSFT\_StorageNodeToPhysicalDisk class
description: Association between a MSFT\_StorageNode and a MSFT\_PhysicalDisk.
ms.assetid: B9C7B6DA-2BBC-4D67-95FF-635458A60FCF
keywords:
- MSFT_StorageNodeToPhysicalDisk class Windows Storage Management API
- MSFT_StorageNodeToPhysicalDisk class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_StorageNodeToPhysicalDisk
- MSFT_StorageNodeToPhysicalDisk.StorageNode
- MSFT_StorageNodeToPhysicalDisk.PhysicalDisk
- MSFT_StorageNodeToPhysicalDisk.OperationalStatus
- MSFT_StorageNodeToPhysicalDisk.HealthStatus
- MSFT_StorageNodeToPhysicalDisk.DiskNumber
- MSFT_StorageNodeToPhysicalDisk.IsMpioEnabled
- MSFT_StorageNodeToPhysicalDisk.LoadBalancePolicy
- MSFT_StorageNodeToPhysicalDisk.PathId
- MSFT_StorageNodeToPhysicalDisk.PathState
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_StorageNodeToPhysicalDisk class

Association between a [**MSFT\_StorageNode**](msft-storagenode.md) and a [**MSFT\_PhysicalDisk**](msft-physicaldisk.md).

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Association]
class MSFT_StorageNodeToPhysicalDisk
{
  MSFT_StorageNode  REF StorageNode;
  MSFT_PhysicalDisk REF PhysicalDisk;
  UInt16                OperationalStatus[];
  UInt16                HealthStatus;
  UInt32                DiskNumber;
  Boolean               IsMpioEnabled;
  UInt16                LoadBalancePolicy;
  String                PathId[];
  UInt16                PathState[];
};
```

## Members

The **MSFT\_StorageNodeToPhysicalDisk** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageNodeToPhysicalDisk** class has these properties.

 

**DiskNumber**
   

Data type: **UInt32**
 

Access type: Read-only
 

The operating system's number for the disk on this storage node. Disk 0 is typically the boot device. Disk numbers may not necessarily remain the same across reboot, and are not necessarily the same on different nodes.

 

**HealthStatus**
   

Data type: **UInt16**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

Denotes the health status of the physical disk on this storage node.

 

**Healthy** (0)
 

**Warning** (1)
 

**Unhealthy** (2)
 

**Unknown** (5)
 

 

**IsMpioEnabled**
   

Data type: **Boolean**
 

Access type: Read-only
 

Indicates whether the physical disk uses MPIO.

 

**LoadBalancePolicy**
   

Data type: **UInt16**
 

Access type: Read-only
 

The MPIO load balance policy being used by the disk.

 

**Unknown** (0)
 

**Fail Over** (1)
 

**Round Robin** (2)
 

**Round Robin with Subset** (3)
 

**Least Queue Depth** (4)
 

**Weighted Paths** (5)
 

**Least Blocks** (6)
 

**Vendor Specific** (7)
 

 

**OperationalStatus**
   

Data type: **UInt16** array
 

Access type: Read-only
 

**Starting in Windows 10:** Denotes the operational status of the physical disk:

 

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
 

**Failed Media** (0xD004)
 

**Split** (0xD005)
 

**Stale Metadata** (0xD006)
 

**IO Error** (0xD007)
 

**Unrecognized Metadata** (0xD008)
 

**Microsoft Reserved** (0xD009..)
 

 

**PathId**
   

Data type: **String** array
 

Access type: Read-only
 

Collection of MPIO path IDs, reported by the MPIO DSM, when applicable.

 

**PathState**
   

Data type: **UInt16** array
 

Access type: Read-only
 

The current state of MPIO paths between the node and physical disk.

 

**Unavailable** (0)
 

**Active/Unoptimized** (1)
 

**Standby** (2)
 

**Active/Optimized** (3)
 

 

**PhysicalDisk**
   

Data type: **[**MSFT\_PhysicalDisk**](msft-physicaldisk.md)**
 

Access type: Read-only
 

Qualifiers: **Key**
 

 

**StorageNode**
   

Data type: **[**MSFT\_StorageNode**](msft-storagenode.md)**
 

Access type: Read-only
 

Qualifiers: **Key**
 

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8.1 \[desktop apps only\]                                              |
| Minimum supported server | Windows Server 2012 R2 \[desktop apps only\]                                   |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_PhysicalDisk**](msft-physicaldisk.md)
 

[**MSFT\_StorageNode**](msft-storagenode.md)
 

 

