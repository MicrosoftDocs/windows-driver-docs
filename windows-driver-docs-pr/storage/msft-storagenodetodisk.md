---
title: MSFT\_StorageNodeToDisk class
description: Association between MSFT\_StorageNode and MSFT\_Disk.
ms.assetid: B892198B-F423-4F6A-8A43-99917D98B78F
keywords:
- MSFT_StorageNodeToDisk class Windows Storage Management API
- MSFT_StorageNodeToDisk class Windows Storage Management API , described
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_StorageNodeToDisk
- MSFT_StorageNodeToDisk.DiskNumber
- MSFT_StorageNodeToDisk.OperationalStatus
- MSFT_StorageNodeToDisk.HealthStatus
- MSFT_StorageNodeToDisk.IsOffline
- MSFT_StorageNodeToDisk.OfflineReason
- MSFT_StorageNodeToDisk.IsReadOnly
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# MSFT\_StorageNodeToDisk class

Association between [**MSFT\_StorageNode**](msft-storagenode.md) and [**MSFT\_Disk**](msft-disk.md).

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Association]
class MSFT_StorageNodeToDisk
{
  UInt32  DiskNumber;
  UInt16  OperationalStatus;
  UInt16  HealthStatus;
  Boolean IsOffline;
  UInt16  OfflineReason;
  Boolean IsReadOnly;
};
```

## Members

The **MSFT\_StorageNodeToDisk** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageNodeToDisk** class has these properties.

 

**DiskNumber**
   

Data type: **UInt32**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

The operating system's number for the disk. Disk 0 is typically the boot device. Disk numbers may not necessarily remain the same across reboots.

 

**HealthStatus**
   

Data type: **UInt16**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

Denotes the health status of the disk.

 

**Unknown** (0)
 

**Healthy** (1)
 

**Failing** (4)
 

**Failed** (8)
 

 

**IsOffline**
   

Data type: **Boolean**
 

Access type: Read-only
 

Indicates whether the disk is offline.

 

**IsReadOnly**
   

Data type: **Boolean**
 

Access type: Read-only
 

Indicates whether the disk is read only.

 

**OfflineReason**
   

Data type: **UInt16**
 

Access type: Read-only
 

If *IsOffline* is **TRUE**, this property denotes the specific reason for the disk being offline.



| Value                                                                                                                                                                                                                                                                                                           | Meaning                                                                     |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
|  **Policy** 1                                                                                          | The user requested the disk to be offline.                       |
|  **Redundant Path** 2                                                          | The disk is used for multi-path I/O.                             |
|  **Snapshot** 3                                                                                  | The disk is a snapshot disk.                                     |
|  **Collision** 4                                                                              | There was a signature or identifier collision with another disk. |
|  **Resource Exhaustion** 5                                      | There were insufficient resources to bring the disk online.      |
|  **Critical Write Failures** 6                      | There were critical write failures on the disk.                  |
|  **Data Integrity Scan Required** 7  | A data integrity scan is required.                               |



 

 

**OperationalStatus**
   

Data type: **UInt16**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

Denotes the operational status of the disk:

 

**Unknown** (0)
 

**Online** (1)
 

**Not Ready** (2)
 

**No Media** (3)
 

**Offline** (4)
 

**Failed** (5)
 

**Missing** (6)
 

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8.1 \[desktop apps only\]                                              |
| Minimum supported server | Windows Server 2012 R2 \[desktop apps only\]                                   |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_Disk**](msft-disk.md)
 

[**MSFT\_StorageNode**](msft-storagenode.md)
 

 

