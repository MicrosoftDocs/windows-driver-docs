---
title: NET_TXQUEUE_CONFIG_INIT method
description: Initializes the NET\_TXQUEUE\_CONFIG structure.
ms.assetid: 73e0c295-8324-4fb9-b845-1ab26981f215
keywords: ["NET_TXQUEUE_CONFIG_INIT method Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NET_TXQUEUE_CONFIG_INIT
api_location:
- nettxqueue.h
api_type:
- HeaderDef
---

# NET\_TXQUEUE\_CONFIG\_INIT method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Initializes the [NET\_TXQUEUE\_CONFIG](net-txqueue-config.md) structure.

Syntax
------

```ManagedCPlusPlus
__inline
void NET_TXQUEUE_CONFIG_INIT(
  _Out_ PNET_TXQUEUE_CONFIG                  NetTxQueueConfig,
  _In_  PFN_TXQUEUE_ADVANCE                  EvtTxQueueAdvance,
  _In_  PFN_TXQUEUE_SET_NOTIFICATION_ENABLED EvtTxQueueSetNotificationEnabled,
  _In_  PFN_TXQUEUE_CANCEL                   EvtTxQueueCancel
);
```

Parameters
----------

*NetTxQueueConfig* \[out\]  
A pointer to the driver-allocated [**NET\_TXQUEUE\_CONFIG**](net-txqueue-config.md) structure.

*EvtTxQueueAdvance* \[in\]  
A pointer to the driver's [*EVT\_TXQUEUE\_ADVANCE*](evt-txqueue-advance.md) callback function.

*EvtTxQueueSetNotificationEnabled* \[in\]  
A pointer to the driver's [*EVT\_TXQUEUE\_SET\_NOTIFICATION\_ENABLED*](evt-txqueue-set-notification-enabled.md) callback function.

*EvtTxQueueCancel* \[in\]  
A pointer to the driver's [*EVT\_TXQUEUE\_CANCEL*](evt-txqueue-cancel.md) callback function.

Return value
------------

This method does not return a value.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Minimum supported client</p></td>
<td align="left"><p>Windows 10</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum supported server</p></td>
<td align="left"><p>Windows Server 2016</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Nettxqueue.h</td>
</tr>
<tr class="even">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

 

 





