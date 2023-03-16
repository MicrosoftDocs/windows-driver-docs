---
title: GetReplicationSettings method of the MSFT\_ReplicationGroup class
description: Returns the replication settings for this replication group.
ms.assetid: 6A4144F4-C432-439C-B0F1-DAB8E8636ECC
keywords:
- GetReplicationSettings method Windows Storage Management API
- GetReplicationSettings method Windows Storage Management API , MSFT_ReplicationGroup class
- MSFT_ReplicationGroup class Windows Storage Management API , GetReplicationSettings method
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_ReplicationGroup.GetReplicationSettings
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# GetReplicationSettings method of the MSFT\_ReplicationGroup class

Returns the replication settings for this replication group.

## Syntax


```mof
UInt32 GetReplicationSettings(
  [out] String ReplicationSettings,
  [out] String ExtendedStatus
);
```



## Parameters

 

*ReplicationSettings* \[out\]
 

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
 

 

 





