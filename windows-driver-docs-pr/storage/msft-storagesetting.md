---
title: MSFT\_StorageSetting class
description: Represents various operating system-wide settings related to storage management.
ms.assetid: 5F956BBF-8FAB-44B2-A2C0-F234813D979B
keywords:
- MSFT_StorageSetting class Windows Storage Management API
- MSFT_StorageSetting class Windows Storage Management API , described
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_StorageSetting
- MSFT_StorageSetting.NewDiskPolicy
- MSFT_StorageSetting.ScrubPolicy
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# MSFT\_StorageSetting class

Represents various operating system-wide settings related to storage management.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
class MSFT_StorageSetting
{
  UInt16 NewDiskPolicy;
  UInt32 ScrubPolicy;
};
```

## Members

The **MSFT\_StorageSetting** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_StorageSetting** class has these methods.



| Method                                                                       | Description                                                                                                              |
|:-----------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------|
| [**Get**](msft-storagesetting-get.md)                                       | Retrieves the current state of all storage settings for the computer.                                         |
| [**Set**](msft-storagesetting-set.md)                                       | Sets the state of various storage settings on this computer.                                                  |
| [**UpdateHostStorageCache**](msft-storagesetting-updatehoststoragecache.md) | Updates the internal cache of software objects (that is, Disks, Partitions, Volumes) for the storage setting. |



 

### Properties

The **MSFT\_StorageSetting** class has these properties.

 

**NewDiskPolicy**
   

Data type: **UInt16**
 

Access type: Read-only
 

Describes the action the operating system will take when a new disk is discovered on the system. When a disk is offline, the disk layout can be read, but no volume devices are surfaced through Plug and Play (PnP). This means that no file system can be mounted on the disk. When a disk is online, one or more volume devices are installed for the disk.



| Value                                                                                                                                                                                                                                                           | Meaning                                                                                                          |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| <span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span> **Unknown** 0                                      | The disk policy is not specified.                                                                     |
| <span id="Online_All"></span><span id="online_all"></span><span id="ONLINE_ALL"></span> **Online All** 1                          | All newly discovered disks are brought online and made read/write.                                    |
| <span id="Offline_Shared"></span><span id="offline_shared"></span><span id="OFFLINE_SHARED"></span> **Offline Shared** 2          | All newly discovered disks that do not reside on a shared bus are brought online and made read/write. |
| <span id="Offline_All"></span><span id="offline_all"></span><span id="OFFLINE_ALL"></span> **Offline All** 3                      | All newly discovered disks remain offline and read-only.                                              |
| <span id="Offline_Internal"></span><span id="offline_internal"></span><span id="OFFLINE_INTERNAL"></span> **Offline Internal** 4  | All newly discovered disks that do not reside on a shared bus remain offline and read-only.           |



 

 

**ScrubPolicy**
   

Data type: **UInt32**
 

Access type: Read-only
 

Describes the policy for the files that the automatic data integrity scanner will scrub.

 

<span id="Off"></span><span id="off"></span><span id="OFF"></span>**Off** (0)
 

<span id="Integrity_Streams"></span><span id="integrity_streams"></span><span id="INTEGRITY_STREAMS"></span>**Integrity Streams** (1)
 

<span id="All"></span><span id="all"></span><span id="ALL"></span>**All** (2)
 

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



 

 





