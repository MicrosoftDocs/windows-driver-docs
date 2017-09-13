---
title: NDIS_STATUS_WDI_INDICATION_P2P_OPERATING_CHANNEL_ATTRIBUTES
author: windows-driver-content
description: Miniport drivers use NDIS_STATUS_WDI_INDICATION_P2P_OPERATING_CHANNEL_ATTRIBUTES to indicate the preferred operating channel to start a GO, the preferred listen channel if asked to enter listen state, and the full set of supported channels at any point of time. The indication is sent once when adapter initializes, and then sent each time one of these parameters changes due to events such as roaming or connecting or disconnecting from an access point.
ms.assetid: F7D27328-99B3-4EB5-9F48-864338EF8D8A
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NDIS_STATUS_WDI_INDICATION_P2P_OPERATING_CHANNEL_ATTRIBUTES Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_WDI\_INDICATION\_P2P\_OPERATING\_CHANNEL\_ATTRIBUTES


Miniport drivers use NDIS\_STATUS\_WDI\_INDICATION\_P2P\_OPERATING\_CHANNEL\_ATTRIBUTES to indicate the preferred operating channel to start a GO, the preferred listen channel if asked to enter listen state, and the full set of supported channels at any point of time. The indication is sent once when adapter initializes, and then sent each time one of these parameters changes due to events such as roaming or connecting or disconnecting from an access point.

| Object |
|--------|
| Port   |

 

The operating channel and channel list values are local settings and do not account for the actual channel negotiation during GO negotiation/invitation. The driver is still expected to negotiate the channel when GO negotiation/invitation is performed.

It is expected that the listen channel reported by the driver is honored if listen state is turned on. It is expected that this indication is fired if the host configured a listen channel that is different from the preferred listen channel reported earlier via this indication.

## Payload data


| Type                                                                                       | Multiple TLV instances allowed | Optional | Description                                              |
|--------------------------------------------------------------------------------------------|--------------------------------|----------|----------------------------------------------------------|
| [**WDI\_TLV\_P2P\_CHANNEL\_NUMBER**](https://msdn.microsoft.com/library/windows/hardware/dn897869)                  |                                |          | The Wi-Fi Direct Operating channel attribute.            |
| [**WDI\_TLV\_P2P\_CHANNEL\_LIST\_ATTRIBUTE**](https://msdn.microsoft.com/library/windows/hardware/dn897868) |                                |          | The full set of channels supported by the local adapter. |
| [**WDI\_TLV\_P2P\_LISTEN\_CHANNEL**](https://msdn.microsoft.com/library/windows/hardware/mt269138)                  |                                |          | The Wi-Fi Direct Listen channel attribute.               |

 

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Minimum supported client</p></td>
<td><p>Windows 10</p></td>
</tr>
<tr class="even">
<td><p>Minimum supported server</p></td>
<td><p>Windows Server 2016</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Dot11wdi.h</td>
</tr>
</tbody>
</table>

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_STATUS_WDI_INDICATION_P2P_OPERATING_CHANNEL_ATTRIBUTES%20%20RELEASE:%20%286/30/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


