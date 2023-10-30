---
title: MSFT\_ReplicationSettings class
description: Represents the settings to be configured on a group or sync pair.
ms.assetid: 0C78E4F9-C420-47B3-9E4E-7EAADCF21A06
keywords:
- MSFT_ReplicationSettings class Windows Storage Management API
- MSFT_ReplicationSettings class Windows Storage Management API , described
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_ReplicationSettings
- MSFT_ReplicationSettings.TargetElementSupplier
- MSFT_ReplicationSettings.ThinProvisioningPolicy
- MSFT_ReplicationSettings.LogDevices
- MSFT_ReplicationSettings.LogSizeInBytes
- MSFT_ReplicationSettings.ReplicationQuorum
- MSFT_ReplicationSettings.SyncMode
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# MSFT\_ReplicationSettings class

Represents the settings to be configured on a group or sync pair.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class MSFT_ReplicationSettings
{
  UInt16 TargetElementSupplier;
  UInt16 ThinProvisioningPolicy;
  String LogDevices[];
  UInt64 LogSizeInBytes;
  UInt16 ReplicationQuorum;
  UInt16 SyncMode;
};
```

## Members

The **MSFT\_ReplicationSettings** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_ReplicationSettings** class has these properties.

 

**LogDevices**
   

Data type: **String** array
 

Access type: Read-only
 

An array of strings that contain embedded [**MSFT\_Volume**](msft-volume.md) objects representing a set of volumes where the replication journal for the replication group is hosted.

 

**LogSizeInBytes**
   

Data type: **UInt64**
 

Access type: Read-only
 

Qualifiers: [**Units**](/windows/win32/wmisdk/standard-qualifiers) (Bytes)
 

Size of the replication journal in units of bytes. The size must be in multiples of gigabytes.

 

**ReplicationQuorum**
   

Data type: **UInt16**
 

Access type: Read-only
 

Minimum number of synchronous replication partnerships that are in synchronous replication state for I/O to continue on the source replication group.

 

**SyncMode**
   

Data type: **UInt16**
 

Access type: Read-only
 

Describes whether the target elements will be updated synchronously or asynchronously. If **NULL**, the implementation decides the mode.

 

**Unknown** (0)
 

**Synchronous** (2)
 

**Asynchronous** (3)
 

**Microsoft Reserved** (..)
 

**Vendor Specific** (32768..65535)
 

 

**TargetElementSupplier**
   

Data type: **UInt16**
 

Access type: Read-only
 

 

**ThinProvisioningPolicy**
   

Data type: **UInt16**
 

Access type: Read-only
 

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 10 \[desktop apps only\]                                               |
| Minimum supported server | Windows Server 2016 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



 

