---
title: NET_RXQUEUE_CONFIG_INIT method
topic_type:
- apiref
api_name:
- NET_RXQUEUE_CONFIG_INIT
api_location:
- netrxqueue.h
api_type:
- HeaderDef
---

# NET_RXQUEUE_CONFIG_INIT method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Initializes the [NET_RXQUEUE_CONFIG](net-rxqueue-config.md) structure.

Syntax
------

```cpp
__inline
void NET_RXQUEUE_CONFIG_INIT(
  _Out_ PNET_RXQUEUE_CONFIG                  NetRxQueueConfig,
  _In_  PFN_RXQUEUE_ADVANCE                  EvtRxQueueAdvance,
  _In_  PFN_RXQUEUE_SET_NOTIFICATION_ENABLED EvtRxQueueSetNotificationEnabled,
  _In_  PFN_RXQUEUE_CANCEL                   EvtRxQueueCancel
);
```

Parameters
----------

*NetRxQueueConfig* [out]  
A pointer to the driver-allocated [**NET_RXQUEUE_CONFIG**](net-rxqueue-config.md) structure.

*EvtRxQueueAdvance* [in]  
A pointer to the driver's [*EVT_RXQUEUE_ADVANCE*](evt-rxqueue-advance.md) callback function.

*EvtRxQueueSetNotificationEnabled* [in]  
A pointer to the driver's [*EVT_RXQUEUE_SET_NOTIFICATION_ENABLED*](evt-rxqueue-set-notification-enabled.md) callback function.

*EvtRxQueueCancel* [in]  
A pointer to the driver's [*EVT_RXQUEUE_CANCEL*](evt-rxqueue-cancel.md) callback function.

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
<td align="left">Netrxqueue.h</td>
</tr>
<tr class="even">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

 

 





