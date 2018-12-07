---
title: NDIS_STATUS_WDI_INDICATION_WAKE_REASON
description: Miniport drivers use NDIS_STATUS_WDI_INDICATION_WAKE_REASON to indicate the reason for a wake when the NIC wakes the host. The wake reason is used for debugging purposes and has no functional effect.
ms.assetid: 5f2eb569-be1e-4f24-92f5-8405ffc7b061
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_WDI_INDICATION_WAKE_REASON Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
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

 

 




