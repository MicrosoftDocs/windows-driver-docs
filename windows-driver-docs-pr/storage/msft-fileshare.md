---
title: MSFT\_FileShare class
description: Models the Windows operating system's concept of a file share.
ms.assetid: 064B4DA4-5879-4758-A7D1-683DB77F909D
keywords:
- MSFT_FileShare class Windows Storage Management API
- MSFT_FileShare class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_FileShare
- MSFT_FileShare.Name
- MSFT_FileShare.Description
- MSFT_FileShare.VolumeRelativePath
- MSFT_FileShare.ContinuouslyAvailable
- MSFT_FileShare.EncryptData
- MSFT_FileShare.FileSharingProtocol
- MSFT_FileShare.ShareState
- MSFT_FileShare.HealthStatus
- MSFT_FileShare.OperationalStatus
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_FileShare class

Models the Windows operating system's concept of a file share.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class MSFT_FileShare : MSFT_StorageObject
{
  String  Name;
  String  Description;
  String  VolumeRelativePath;
  Boolean ContinuouslyAvailable;
  Boolean EncryptData;
  UInt16  FileSharingProtocol;
  UInt16  ShareState;
  UInt16  HealthStatus;
  UInt16  OperationalStatus[];
};
```

## Members

The **MSFT\_FileShare** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_FileShare** class has these methods.



| Method                                                             | Description                                                                              |
|:-------------------------------------------------------------------|:-----------------------------------------------------------------------------------------|
| [**BlockAccess**](msft-fileshare-blockaccess.md)                  | Denies specified users access to the file share.                              |
| [**DeleteObject**](msft-fileshare-deleteobject.md)                | Deletes the file share.                                                       |
| [**Diagnose**](msft-fileshare-diagnose.md)                        | Performs a diagnostic on the file share, returning any actionable results.    |
| [**GetAccessControlEntries**](msft-fileshare-getaccesscontrol.md) | Gets the access control entries for specified accounts.                       |
| [**GrantAccess**](msft-fileshare-grantaccess.md)                  | Grants to the specified user accounts the specified access to the file share. |
| [**RevokeAccess**](msft-fileshare-revokeaccess.md)                | Revokes access to the file share for specified users.                         |
| [**SetAttributes**](msft-fileshare-setattributes.md)              | Allows the user to update or set various attributes on the file share.        |
| [**SetDescription**](msft-fileshare-setdescription.md)            | Allows a user to set the description field of the file share.                 |
| [**UnblockAccess**](msft-fileshare-unblockaccess.md)              | Removes specified users from the denied access list for the file share.       |



 

### Properties

The **MSFT\_FileShare** class has these properties.

 

**ContinuouslyAvailable**
   

Data type: **Boolean**
 

Access type: Read-only
 

If **TRUE**, the share is continuously available.

 

**Description**
   

Data type: **String**
 

Access type: Read-only
 

A user settable description of the file share. This field can be used to store extra free-form information, such as notes or details about the intended usage. Some shares do not allow setting a description and will either support a default description or will not support any description.

 

**EncryptData**
   

Data type: **Boolean**
 

Access type: Read-only
 

If **TRUE**, the share data is encrypted during transport.

 

**FileSharingProtocol**
   

Data type: **UInt16**
 

Access type: Read-only
 

The file sharing protocol used by the share.

 

**NFS** (2)
 

**CIFS(SMB)** (3)
 

 

**HealthStatus**
   

Data type: **UInt16**
 

Access type: Read-only
 

The current health status of the file share.

 

**Healthy** (0)
 

**Warning** (1)
 

**Unhealthy** (2)
 

**Unknown** (5)
 

 

**Name**
   

Data type: **String**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

A semi-unique (scoped to the owning file server), human-readable string used to identify and access a file share.

 

**OperationalStatus**
   

Data type: **UInt16** array
 

Access type: Read-only
 

An array of values that denote the current operational status of the file share. Unlike *HealthStatus*, this field indicates the status of hardware, software, and infrastructure issues related to this share, and can contain multiple values.

 

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
 

**Power Mode** (18 )
 

**Relocating** (19 )
 

**Microsoft Reserved** (..)
 

**Read-only** (0xD000)
 

**Incomplete** (0xD001)
 

**Microsoft Reserved** (0xD001..)
 

 

**ShareState**
   

Data type: **UInt16**
 

Access type: Read-only
 

The current state of the file share.

 

**Pending** (0)
 

**Online** (1)
 

**Offline** (2)
 

 

**VolumeRelativePath**
   

Data type: **String**
 

Access type: Read-only
 

The volume relative path to the directory that is being shared.

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 10 \[desktop apps only\]                                               |
| Minimum supported server | Windows Server 2016 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_StorageObject**](msft-storageobject.md)
 

 

