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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NET_TXQUEUE_CONFIG_INIT%20method%20%20RELEASE:%20%281/19/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




