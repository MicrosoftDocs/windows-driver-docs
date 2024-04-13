---
title: MSFT_StorageModificationEvent Class
description: Represents a storage modification event. Storage modification events are used when the underlying state of an object has changed.
ms.assetid: 7AD4584D-09DA-40BB-B686-AD704119A78B
keywords:
- MSFT_StorageModificationEvent class Windows Storage Management API
- MSFT_StorageModificationEvent class Windows Storage Management API , described
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_StorageModificationEvent
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# MSFT\_StorageModificationEvent class

Represents a storage modification event. Storage modification events are used when the underlying state of an object has changed.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Indication]
class MSFT_StorageModificationEvent : MSFT_StorageEvent
{
};
```

## Members

The **MSFT\_StorageModificationEvent** class does not define any members.

## Remarks

Not all properties should be tracked (for example, **AllocatedSize** may change so frequently that sending events would be impractical). At a minimum, an event should be sent any time an object's **HealthStatus** or **OperationalStatus** properties change.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_StorageEvent**](msft-storageevent.md)
 

 

 





