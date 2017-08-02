---
title: NDIS_STATUS_WDI_INDICATION_WAKE_REASON
author: windows-driver-content
description: Miniport drivers use NDIS_STATUS_WDI_INDICATION_WAKE_REASON to indicate the reason for a wake when the NIC wakes the host. The wake reason is used for debugging purposes and has no functional effect.
ms.assetid: 5f2eb569-be1e-4f24-92f5-8405ffc7b061
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NDIS_STATUS_WDI_INDICATION_WAKE_REASON Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_WDI\_INDICATION\_WAKE\_REASON


Miniport drivers use NDIS\_STATUS\_WDI\_INDICATION\_WAKE\_REASON to indicate the reason for a wake when the NIC wakes the host. The wake reason is used for debugging purposes and has no functional effect.

| Object |
|--------|
| Port   |

 

When the host goes to low power state, it offloads a few functions to the NIC and arms the NIC for wake. When a wake event occurs, the NIC asserts the wake interrupt line to wake the host. The host then brings the NIC into D0 (running power state). The NIC must indicate the wake reason once it enters D0.

If the wake reason is a wake packet, the NIC should also include the wake packet and the wake pattern ID that matches the packet. The packet is encapsulated as [**WDI\_TLV\_INDICATION\_WAKE\_PACKET**](https://msdn.microsoft.com/library/windows/hardware/dn897833). The wake reason should also include [**WDI\_TLV\_INDICATION\_WAKE\_PACKET\_PATTERN\_ID**](https://msdn.microsoft.com/library/windows/hardware/dn897832) to specify the pattern ID which matches the packet.

## Payload data


| Type                                                                                                      | Multiple TLV instances allowed | Optional | Description                                                                                                 |
|-----------------------------------------------------------------------------------------------------------|--------------------------------|----------|-------------------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_INDICATION\_WAKE\_REASON**](https://msdn.microsoft.com/library/windows/hardware/dn897834)                         |                                |          | The wake reason.                                                                                            |
| [**WDI\_TLV\_INDICATION\_WAKE\_PACKET**](https://msdn.microsoft.com/library/windows/hardware/dn897833)                         |                                | X        | The wake packet.                                                                                            |
| [**WDI\_TLV\_INDICATION\_WAKE\_PACKET\_PATTERN\_ID**](https://msdn.microsoft.com/library/windows/hardware/dn897832) |                                | X        | The ID of the pattern that matches the wake packet. The ID is obtained from the Add command of the pattern. |

 

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
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_STATUS_WDI_INDICATION_WAKE_REASON%20%20RELEASE:%20%286/30/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


