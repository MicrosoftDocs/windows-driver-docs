---
title: SetReplicationSettings method of the MSFT\_ReplicationGroup class
description: Specifies the replication settings for this replication group.
ms.assetid: D7D6E175-A067-4EAF-99A6-0A394D3679AD
keywords:
- SetReplicationSettings method Windows Storage Management API
- SetReplicationSettings method Windows Storage Management API , MSFT_ReplicationGroup class
- MSFT_ReplicationGroup class Windows Storage Management API , SetReplicationSettings method
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_ReplicationGroup.SetReplicationSettings
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# SetReplicationSettings method of the MSFT\_ReplicationGroup class

Specifies the replication settings for this replication group.

## Syntax


```mof
UInt32 SetReplicationSettings(
  [in]  String ReplicationSettings,
  [out] String ExtendedStatus
);
```



## Parameters

 

*ReplicationSettings* \[in\]
 

A string that contains an embedded [**MSFT\_ReplicationSettings**](msft-replicationsettings.md) object specifying the replication settings.

 

*ExtendedStatus* \[out\]
 

A string that contains an embedded [**MSFT\_StorageExtendedStatus**](msft-storageextendedstatus.md) object.

This parameter allows the storage provider to return extended (implementation-specific) error information.

 

## Return value

 

**Success** (0)
 

**Not Supported** (1)
 

**Unspecified Error** (2)
 

**Timeout** (3)
 

**Failed** (4)
 

**Invalid Parameter** (5)
 

**Object Not Found** (8)
 

**Access denied** (40001)
 

**There are not enough resources to complete the operation.** (40002)
 

**Cache out of date** (40003)
 

**The operation is not supported while the cluster is being upgraded.** (40009)
 

**Cannot connect to the storage provider.** (46000)
 

**The storage provider cannot connect to the storage subsystem.** (46001)
 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 10 \[desktop apps only\]                                               |
| Minimum supported server | Windows Server 2016 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_ReplicationGroup**](msft-replicationgroup.md)
 

 

 





