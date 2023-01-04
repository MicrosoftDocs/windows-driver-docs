---
title: MSFT\_FileServer class
description: Models the Windows operating system's concept of a file server.
ms.assetid: 1AF4536E-8B51-46A5-856F-9BE2482312F6
keywords:
- MSFT_FileServer class Windows Storage Management API
- MSFT_FileServer class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_FileServer
- MSFT_FileServer.FriendlyName
- MSFT_FileServer.HostNames
- MSFT_FileServer.HealthStatus
- MSFT_FileServer.OperationalStatus
- MSFT_FileServer.OtherOperationalStatusDescription
- MSFT_FileServer.SupportsFileShareCreation
- MSFT_FileServer.SupportsContinuouslyAvailableFileShare
- MSFT_FileServer.FileSharingProtocols
- MSFT_FileServer.FileSharingProtocolVersions
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_FileServer class

Models the Windows operating system's concept of a file server.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class MSFT_FileServer : MSFT_StorageObject
{
  String  FriendlyName;
  String  HostNames[];
  UInt16  HealthStatus;
  UInt16  OperationalStatus[];
  String  OtherOperationalStatusDescription;
  Boolean SupportsFileShareCreation;
  Boolean SupportsContinuouslyAvailableFileShare;
  UInt16  FileSharingProtocols[];
  String  FileSharingProtocolVersions[];
};
```

## Members

The **MSFT\_FileServer** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_FileServer** class has these methods.



| Method                                                     | Description                                         |
|:-----------------------------------------------------------|:----------------------------------------------------|
| [**CreateFileShare**](msft-fileserver-createfileshare.md) | Creates a file share on the file server. |
| [**DeleteObject**](msft-fileserver-deleteobject.md)       | Deletes the file server.                 |
| [**SetFriendlyName**](msft-fileserver-setproperties.md)   | Allows the file server to be renamed.    |



 

### Properties

The **MSFT\_FileServer** class has these properties.

 

**FileSharingProtocols**
   

Data type: **UInt16** array
 

Access type: Read-only
 

The file sharing protocols supported by the file server.

 

**NFS** (2)
 

**SMB** (3)
 

 

**FileSharingProtocolVersions**
   

Data type: **String** array
 

Access type: Read-only
 

Specifies the file sharing protocol versions supported.

 

**FriendlyName**
   

Data type: **String**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

A user-friendly string representing the name of the file server. Some servers may assign a default friendly name which cannot be modified by the user.

 

**HealthStatus**
   

Data type: **UInt16**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

Denotes the current health status of the file server.

 

**Healthy** (0)
 

**Warning** (1)
 

**Unhealthy** (2)
 

**Unknown** (5)
 

 

**HostNames**
   

Data type: **String** array
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

Host names are semi-unique (scoped to the owning storage subsystem), human-readable strings used to identify a file server. There is a separate host name element per file sharing protocol.

 

**OperationalStatus**
   

Data type: **UInt16** array
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

An array of values that denote the current operational status of the file server. Unlike *HealthStatus*, this field indicates the status of hardware, software, and infrastructure issues related to this server, and can contain multiple values.

 

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
 

 

**OtherOperationalStatusDescription**
   

Data type: **String**
 

Access type: Read-only
 

A string representation of the vendor-defined operational status. This field should only be set if the *OperationalStatus* array contains 1 ("Other").

 

**SupportsContinuouslyAvailableFileShare**
   

Data type: **Boolean**
 

Access type: Read-only
 

If **TRUE**, the file server will support continuously available file shares.

 

**SupportsFileShareCreation**
   

Data type: **Boolean**
 

Access type: Read-only
 

If **TRUE**, the server supports file share creation.

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 10 \[desktop apps only\]                                               |
| Minimum supported server | Windows Server 2016 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_StorageObject**](msft-storageobject.md)
 

 

