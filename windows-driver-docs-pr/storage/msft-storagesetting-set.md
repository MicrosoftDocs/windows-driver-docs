---
title: Set method of the MSFT\_StorageSetting class
description: Sets the state of various storage settings on this computer.
ms.assetid: 94F98CA7-795B-481C-BE97-B65FF015B761
keywords:
- Set method Windows Storage Management API
- Set method Windows Storage Management API , MSFT_StorageSetting class
- MSFT_StorageSetting class Windows Storage Management API , Set method
topic_type:
- apiref
api_name:
- MSFT_StorageSetting.Set
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Set method of the MSFT\_StorageSetting class

Sets the state of various storage settings on this computer.

Only the parameters specified will be set on the system.

## Syntax


```mof
UInt32 Set(
  [in] UInt16 NewDiskPolicy,
  [in] UInt32 ScrubPolicy
);
```



## Parameters

 

*NewDiskPolicy* \[in\]
 

The new disk policy.



| Value                                                                                                                                                                                                                                                           | Meaning                                                                                                          |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| <span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span> **Unknown** 0                                      | The disk policy is not specified.                                                                     |
| <span id="Online_All"></span><span id="online_all"></span><span id="ONLINE_ALL"></span> **Online All** 1                          | All newly discovered disks are brought online and made read/write.                                    |
| <span id="Offline_Shared"></span><span id="offline_shared"></span><span id="OFFLINE_SHARED"></span> **Offline Shared** 2          | All newly discovered disks that do not reside on a shared bus are brought online and made read/write. |
| <span id="Offline_All"></span><span id="offline_all"></span><span id="OFFLINE_ALL"></span> **Offline All** 3                      | All newly discovered disks remain offline and read-only.                                              |
| <span id="Offline_Internal"></span><span id="offline_internal"></span><span id="OFFLINE_INTERNAL"></span> **Offline Internal** 4  | All newly discovered disks that do not reside on a shared bus remain offline and read-only.           |



 

 

*ScrubPolicy* \[in\]
 

The file scrub policy of the automatic data integrity scanner.



| Value                                                                        | Meaning                      |
|------------------------------------------------------------------------------|------------------------------|
|  0  | Off               |
|  1  | Integrity Streams |
|  2  | All               |



 

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8.1 \[desktop apps only\]                                              |
| Minimum supported server | Windows Server 2012 R2 \[desktop apps only\]                                   |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_StorageSetting**](msft-storagesetting.md)
 

 

 





