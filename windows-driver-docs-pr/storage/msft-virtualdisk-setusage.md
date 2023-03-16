---
title: SetUsage method of the MSFT\_VirtualDisk class
description: Sets or changes the intended usage for the virtual disk.
ms.assetid: 232159C8-51D3-423A-8868-4BD1056E536A
keywords:
- SetUsage method Windows Storage Management API
- SetUsage method Windows Storage Management API , MSFT_VirtualDisk class
- MSFT_VirtualDisk class Windows Storage Management API , SetUsage method
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_VirtualDisk.SetUsage
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# SetUsage method of the MSFT\_VirtualDisk class

Sets or changes the intended usage for the virtual disk.

## Syntax


```mof
UInt32 SetUsage(
  [in]  UInt16 Usage,
  [in]  String OtherUsageDescription,
  [out] String ExtendedStatus
);
```



## Parameters

 

*Usage* \[in\]
 

The new intended usage for the virtual disk.

This parameter is required and cannot be **NULL**.

 

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
 

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)
 

<span id="Unrestricted"></span><span id="unrestricted"></span><span id="UNRESTRICTED"></span>**Unrestricted** (2)
 

<span id="Reserved_for_ComputerSystem__the_block_server_"></span><span id="reserved_for_computersystem__the_block_server_"></span><span id="RESERVED_FOR_COMPUTERSYSTEM__THE_BLOCK_SERVER_"></span>**Reserved for ComputerSystem (the block server)** (3)
 

<span id="Reserved_by_Replication_Services"></span><span id="reserved_by_replication_services"></span><span id="RESERVED_BY_REPLICATION_SERVICES"></span>**Reserved by Replication Services** (4)
 

<span id="Reserved_by_Migration_Services"></span><span id="reserved_by_migration_services"></span><span id="RESERVED_BY_MIGRATION_SERVICES"></span>**Reserved by Migration Services** (5)
 

<span id="Local_Replica_Source"></span><span id="local_replica_source"></span><span id="LOCAL_REPLICA_SOURCE"></span>**Local Replica Source** (6)
 

<span id="Remote_Replica_Source"></span><span id="remote_replica_source"></span><span id="REMOTE_REPLICA_SOURCE"></span>**Remote Replica Source** (7)
 

<span id="Local_Replica_Target"></span><span id="local_replica_target"></span><span id="LOCAL_REPLICA_TARGET"></span>**Local Replica Target** (8)
 

<span id="Remote_Replica_Target"></span><span id="remote_replica_target"></span><span id="REMOTE_REPLICA_TARGET"></span>**Remote Replica Target** (9)
 

<span id="Local_Replica_Source_or_Target"></span><span id="local_replica_source_or_target"></span><span id="LOCAL_REPLICA_SOURCE_OR_TARGET"></span>**Local Replica Source or Target** (10)
 

<span id="Remote_Replica_Source_or_Target"></span><span id="remote_replica_source_or_target"></span><span id="REMOTE_REPLICA_SOURCE_OR_TARGET"></span>**Remote Replica Source or Target** (11)
 

<span id="Delta_Replica_Target"></span><span id="delta_replica_target"></span><span id="DELTA_REPLICA_TARGET"></span>**Delta Replica Target** (12)
 

<span id="Element_Component"></span><span id="element_component"></span><span id="ELEMENT_COMPONENT"></span>**Element Component** (13)
 

<span id="Reserved_as_Pool_Contributor"></span><span id="reserved_as_pool_contributor"></span><span id="RESERVED_AS_POOL_CONTRIBUTOR"></span>**Reserved as Pool Contributor** (14)
 

<span id="Composite_Volume_Member"></span><span id="composite_volume_member"></span><span id="COMPOSITE_VOLUME_MEMBER"></span>**Composite Volume Member** (15)
 

<span id="Composite_VirtualDisk_Member"></span><span id="composite_virtualdisk_member"></span><span id="COMPOSITE_VIRTUALDISK_MEMBER"></span>**Composite VirtualDisk Member** (16)
 

<span id="Reserved_for_Sparing"></span><span id="reserved_for_sparing"></span><span id="RESERVED_FOR_SPARING"></span>**Reserved for Sparing** (17)
   

*OtherUsageDescription* \[in\]
 

If *Usage* is set to **Other**, this parameter is the string representation of a vendor-defined usage for this virtual disk. This parameter must be **NULL** if *Usage* is not **Other**.

 

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
 

**Access denied** (40001)
 

**There are not enough resources to complete the operation.** (40002)
 

**Cannot connect to the storage provider.** (46000)
 

**The storage provider cannot connect to the storage subsystem.** (46001)
 

**The storage pool could not complete the operation because its health or operational status does not permit it.** (48006)
 

**The storage pool could not complete the operation because its configuration is read-only.** (48007)
 

**The virtual disk could not complete the operation because another computer controls its configuration.** (50002)
 

**The virtual disk could not complete the operation because its health or operational status does not permit it.** (50003)
 

## Remarks

Not all virtual disks may allow this method. Those that do not will cause this method to return **Not Supported**.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_VirtualDisk**](msft-virtualdisk.md)
 

 

 





