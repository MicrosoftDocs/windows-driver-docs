---
title: Discover method of the MSFT\_StorageProvider class
description: Discovers the objects that are owned by the storage provider.
ms.assetid: afafd4d5-c0c1-4461-814d-bf00de403b3f
keywords:
- Discover method Windows Storage Management API
- Discover method Windows Storage Management API , MSFT_StorageProvider class
- MSFT_StorageProvider class Windows Storage Management API , Discover method
topic_type:
- apiref
api_name:
- MSFT_StorageProvider.Discover
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Discover method of the MSFT\_StorageProvider class

Discovers the objects that are owned by the storage provider.

This method is used when a user needs to explicitly discover or re-enumerate objects owned by the storage provider. A call to this method will result in full or partial cache invalidation and over-the-wire calls to the storage subsystem to discover new or updated objects. Because this is an expensive task, this method should be used sparingly.

The scope of the discovery operation is controlled by the *DiscoveryLevel* and *RootObject* parameters. *DiscoveryLevel* controls the depth of the object discovery. *RootObject* defines the starting point from which discovery will happen.

## Syntax


```mof
UInt32 Discover(
  [in]  UInt16                 DiscoveryLevel,
  [in]  MSFT_StorageObject REF RootObject,
  [in]  Boolean                RunAsJob,
  [out] MSFT_StorageJob    REF CreatedStorageJob,
  [out] String                 ExtendedStatus
);
```



## Parameters

 

*DiscoveryLevel* \[in\]
 

The level (or depth) of discovery that should be performed. This parameter can only be specified if the root object is a storage provider, storage subsystem, or **NULL**. When specified, the storage provider will discover objects starting from **Level 0** and continuing until the specified level is reached. Associations between objects (within the discovered levels) will also be discovered.

| Value | Meaning |
|:----- |:------- |
| **Level 0** 0 |The storage provider, storage subsystem, and fileserver objects will be discovered. Note: **Starting in Windows 10:** Discovery of fileserver objects has been added. |
| **Level 1** 1 | Storage pools, file shares, resiliency settings, target ports, target portals, and initiator identifiers will be discovered. Note: **Starting in Windows 10:** Discovery of file shares has been added. |
| **Level 2** 2 | Virtual disks, volumes, partitions, disks, and masking sets will be discovered. Note: **Starting in Windows 10:** Discovery of volumes, partitions, and disks has been added. |
| **Level 3** 3 | Physical disks will be discovered. |

*RootObject* \[in\]
 

If this parameter is set, discovery will begin from this object. When *DiscoveryLevel* is **NULL**, well-defined actions will be taken depending on the type of object specified by *RootObject*:

-   Storage subsystem: All associated objects will be discovered.
-   Storage pool: The pool, along with any associated resiliency settings, virtual disks, and physical disks will be discovered.
-   Masking set: The masking set, along with any associated target ports, initiator identifiers, and virtual disks will be discovered.
-   For all other objects, only that object will be discovered or refreshed.

 

*RunAsJob* \[in\]
 

If **TRUE**, this method uses the *CreatedStorageJob* parameter when the request is taking a long time to service. If a storage job has been created to track the operation, this method will return **Method Parameters Checked - Job Started**.

> [!Note]  
> Even if *RunAsJob* is **TRUE**, this method can still return a result if it has finished in sufficient time.

 

If **FALSE** or **NULL**, this method will follow default WMI asynchronous behavior as determined by the client's method for invocation. In other words, it is synchronous unless requested otherwise.

 

*CreatedStorageJob* \[out\]
 

If *RunAsJob* is set to **TRUE** and this method takes a long time to execute, this parameter receives a reference to the storage job object that is used to track the long-running operation.

 

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
 

**Method Parameters Checked - Job Started** (4096)
 

**Access denied** (40001)
 

**There are not enough resources to complete the operation.** (40002)
 

**Cannot connect to the storage provider.** (46000)
 

**The storage provider cannot connect to the storage subsystem.** (46001)
 

**The storage provider does not support a required profile.** (46002)
 

**The storage provider does not support a required association.** (46003)
 

**Discover failed for the root object.** (46009 )
 

**Discover failed on one or more subsystems.** (46010)
 

## Remarks

Storage providers should complete **Level 0** discovery at start-up. The [**MSFT\_StorageProvider**](msft-storageprovider.md) and [**MSFT\_StorageSubSystem**](msft-storagesubsystem.md) objects should be loaded into cache.

For better performance, storage subsystems that have the **iSCSITargetCreationScheme** property set to **Auto** should do their discovery of target ports along with the virtual disks in **Level 2**. Note that target portals should still be discovered in **Level 1**.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_StorageProvider**](msft-storageprovider.md)
 

[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)
 

 

 





