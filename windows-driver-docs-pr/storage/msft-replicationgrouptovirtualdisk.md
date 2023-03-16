---
title: MSFT\_ReplicationGroupToVirtualDisk class
description: Association between an MSFT\_ReplicationGroup and its MSFT\_VirtualDisk objects.
ms.assetid: 21D7BD95-14EC-4869-80A9-50238B32BC27
keywords:
- MSFT_ReplicationGroupToVirtualDisk class Windows Storage Management API
- MSFT_ReplicationGroupToVirtualDisk class Windows Storage Management API , described
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_ReplicationGroupToVirtualDisk
- MSFT_ReplicationGroupToVirtualDisk.ReplicationGroup
- MSFT_ReplicationGroupToVirtualDisk.VirtualDisk
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# MSFT\_ReplicationGroupToVirtualDisk class

Association between an [**MSFT\_ReplicationGroup**](msft-replicationgroup.md) and its [**MSFT\_VirtualDisk**](msft-virtualdisk.md) objects.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_ReplicationGroupToVirtualDisk
{
  MSFT_ReplicationGroup REF ReplicationGroup;
  MSFT_VirtualDisk      REF VirtualDisk;
};
```

## Members

The **MSFT\_ReplicationGroupToVirtualDisk** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_ReplicationGroupToVirtualDisk** class has these properties.

 

**ReplicationGroup**
   

Data type: **[**MSFT\_ReplicationGroup**](msft-replicationgroup.md)**
 

Access type: Read-only
 

Qualifiers: **Key**
 

 

**VirtualDisk**
   

Data type: **[**MSFT\_VirtualDisk**](msft-virtualdisk.md)**
 

Access type: Read-only
 

Qualifiers: **Key**
 

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 10 \[desktop apps only\]                                               |
| Minimum supported server | Windows Server 2016 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_ReplicationGroup**](msft-replicationgroup.md)
 

[**MSFT\_VirtualDisk**](msft-virtualdisk.md)
 

 

 





