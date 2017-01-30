---
title: NET_TXQUEUE_CONFIG structure
description: Call NET\_TXQUEUE\_CONFIG\_INIT to initialize this structure.
ms.assetid: ec5be68e-dcd7-4133-8d0a-3512a5d71653
keywords: ["NET_TXQUEUE_CONFIG structure Network Drivers Starting with Windows Vista", "PNET_TXQUEUE_CONFIG structure pointer Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NET_TXQUEUE_CONFIG
api_location:
- nettxqueue.h
api_type:
- HeaderDef
---

# NET\_TXQUEUE\_CONFIG structure


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Call [NET\_TXQUEUE\_CONFIG\_INIT](net-txqueue-config-init.md) to initialize this structure.

Syntax
------

```ManagedCPlusPlus
typedef struct _NET_TXQUEUE_CONFIG {
  ULONG                                Size;
  PFN_TXQUEUE_CANCEL                   EvtTxQueueCancel;
  PFN_TXQUEUE_SET_NOTIFICATION_ENABLED EvtTxQueueSetNotificationEnabled;
  PFN_TXQUEUE_ADVANCE                  EvtTxQueueAdvance;
  PCNET_CONTEXT_TYPE_INFO              ContextTypeInfo;
} NET_TXQUEUE_CONFIG, *PNET_TXQUEUE_CONFIG;
```

Members
-------

**Size**  

**EvtTxQueueCancel**  
A pointer to the client driver's [*EVT\_TXQUEUE\_CANCEL*](evt-txqueue-cancel.md) event callback function. This callback function is required.

**EvtTxQueueSetNotificationEnabled**  
A pointer to the client driver's [*EVT\_TXQUEUE\_SET\_NOTIFICATION\_ENABLED*](evt-txqueue-set-notification-enabled.md) event callback function. This callback function is required.

**EvtTxQueueAdvance**  
A pointer to the client driver's [*EVT\_TXQUEUE\_ADVANCE*](evt-txqueue-advance.md) event callback function. This callback function is required.

**ContextTypeInfo**  

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Minimum KMDF version</p></td>
<td align="left"><p>1.21</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum NetAdapterCx version</p></td>
<td align="left"><p>1.0</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Nettxqueue.h</td>
</tr>
</tbody>
</table>

 

 





