---
title: NET_TXQUEUE_CONFIG_INIT method
topic_type:
- apiref
api_name:
- NET_TXQUEUE_CONFIG_INIT
api_location:
- nettxqueue.h
api_type:
- HeaderDef
---

# NET_TXQUEUE_CONFIG_INIT method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Initializes the [NET_TXQUEUE_CONFIG](net-txqueue-config.md) structure.

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

*NetTxQueueConfig* [out]  
A pointer to the driver-allocated [**NET_TXQUEUE_CONFIG**](net-txqueue-config.md) structure.

*EvtTxQueueAdvance* [in]  
A pointer to the driver's [*EVT_TXQUEUE_ADVANCE*](evt-txqueue-advance.md) callback function.

*EvtTxQueueSetNotificationEnabled* [in]  
A pointer to the driver's [*EVT_TXQUEUE_SET_NOTIFICATION_ENABLED*](evt-txqueue-set-notification-enabled.md) callback function.

*EvtTxQueueCancel* [in]  
A pointer to the driver's [*EVT_TXQUEUE_CANCEL*](evt-txqueue-cancel.md) callback function.

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

 

 





