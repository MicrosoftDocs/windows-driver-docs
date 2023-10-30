---
title: GetRecoveryPointData method of the MSFT\_ReplicationCapabilities class
description: Returns, for a given ReplicationType, recovery point data.
ms.assetid: F14F4AFE-F554-4DFA-8E45-2B953676E357
keywords:
- GetRecoveryPointData method Windows Storage Management API
- GetRecoveryPointData method Windows Storage Management API , MSFT_ReplicationCapabilities class
- MSFT_ReplicationCapabilities class Windows Storage Management API , GetRecoveryPointData method
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_ReplicationCapabilities.GetRecoveryPointData
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# GetRecoveryPointData method of the MSFT\_ReplicationCapabilities class

Returns, for a given *ReplicationType*, recovery point data.

## Syntax


```mof
UInt32 GetRecoveryPointData(
  [in]  UInt16 ReplicationType,
  [in]  UInt16 DefaultRecoveryPoint,
  [out] UInt16 RecoveryPointValues[],
  [out] UInt16 RecoveryPointIndicator,
  [out] String ExtendedStatus
);
```



## Parameters

 

*ReplicationType* \[in\]
 

A value representing the replication type. This must be in the enumeration [**MSFT\_ReplicationCapabilities**](msft-replicationcapabilities.md).SupportedReplicationTypes.

 

*DefaultRecoveryPoint* \[in\]
 

Default recovery point value.

 

*RecoveryPointValues* \[out\]
  

*RecoveryPointIndicator* \[out\]
 

Indicates the semantics of the supported values.

 

**Range** (1)
 

**Discrete** (2)
   

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
 

**In Use** (6)
 

**Property Is Not Supported** (7)
 

**DMTF Reserved** (..)
 

**Vendor Specific** (0x8000..)
 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 10 \[desktop apps only\]                                               |
| Minimum supported server | Windows Server 2016 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_ReplicationCapabilities**](msft-replicationcapabilities.md)
 

 

 





