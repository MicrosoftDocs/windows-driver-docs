---
title: MSFT\_VolumeToReplicaPeer class
description: Association between MSFT\_Volume and MSFT\_ReplicaPeer .
ms.assetid: FB7BF33C-21F1-4DAB-B45E-F2126ACC10BF
keywords:
- MSFT_VolumeToReplicaPeer class Windows Storage Management API
- MSFT_VolumeToReplicaPeer class Windows Storage Management API , described
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_VolumeToReplicaPeer
- MSFT_VolumeToReplicaPeer.Volume
- MSFT_VolumeToReplicaPeer.FileShare
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# MSFT\_VolumeToReplicaPeer class

Association between [**MSFT\_Volume**](msft-volume.md) and [**MSFT\_ReplicaPeer**](msft-replicapeer.md) .

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class MSFT_VolumeToReplicaPeer : MSFT_Synchronized
{
  MSFT_Volume      REF Volume;
  MSFT_ReplicaPeer REF FileShare;
};
```

## Members

The **MSFT\_VolumeToReplicaPeer** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_VolumeToReplicaPeer** class has these properties.

 

**FileShare**
   

Data type: **[**MSFT\_ReplicaPeer**](msft-replicapeer.md)**
 

Access type: Read-only
 

Qualifiers: **Key**
 

 

**Volume**
   

Data type: **[**MSFT\_Volume**](msft-volume.md)**
 

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

 

[**MSFT\_Synchronized**](https://www.bing.com/search?q=**MSFT\_Synchronized**)
 

[**MSFT\_ReplicaPeer**](msft-replicapeer.md)
 

[**MSFT\_Volume**](msft-volume.md)
 

 

 





