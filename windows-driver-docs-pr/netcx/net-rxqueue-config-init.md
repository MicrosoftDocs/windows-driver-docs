---
title: NET_RXQUEUE_CONFIG_INIT method
description: Initializes the NET\_RXQUEUE\_CONFIG structure.
ms.assetid: f1b07385-2f4c-4eb3-84b8-7331b21a1985
keywords: ["NET_RXQUEUE_CONFIG_INIT method Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NET_RXQUEUE_CONFIG_INIT
api_location:
- netrxqueue.h
api_type:
- HeaderDef
---

# NET\_RXQUEUE\_CONFIG\_INIT method


\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Initializes the [NET\_RXQUEUE\_CONFIG](net-rxqueue-config.md) structure.

Syntax
------

```ManagedCPlusPlus
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

*NetRxQueueConfig* \[out\]  
A pointer to the driver-allocated [**NET\_RXQUEUE\_CONFIG**](net-rxqueue-config.md) structure.

*EvtRxQueueAdvance* \[in\]  
A pointer to the driver's [*EVT\_RXQUEUE\_ADVANCE*](evt-rxqueue-advance.md) callback function.

*EvtRxQueueSetNotificationEnabled* \[in\]  
A pointer to the driver's [*EVT\_RXQUEUE\_SET\_NOTIFICATION\_ENABLED*](evt-rxqueue-set-notification-enabled.md) callback function.

*EvtRxQueueCancel* \[in\]  
A pointer to the driver's [*EVT\_RXQUEUE\_CANCEL*](evt-rxqueue-cancel.md) callback function.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NET_RXQUEUE_CONFIG_INIT%20method%20%20RELEASE:%20%281/19/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




