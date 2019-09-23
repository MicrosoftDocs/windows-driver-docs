---
title: OID_WDI_SET_ADD_WOL_PATTERN
description: OID_WDI_SET_ADD_WOL_PATTERN adds a wake-on-LAN (WOL) pattern to the firmware.
ms.assetid: 96fb71fd-412b-4013-b3bc-c31a43516f55
ms.date: 07/18/2017
keywords:
 - OID_WDI_SET_ADD_WOL_PATTERN Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
ms.custom: 19H1
---

# OID\_WDI\_SET\_ADD\_WOL\_PATTERN


OID\_WDI\_SET\_ADD\_WOL\_PATTERN adds a wake-on-LAN (WOL) pattern to the firmware.

| Scope | Set serialized with task | Normal execution time (seconds) |
|-------|--------------------------|---------------------------------|
| Port  | Yes                      | 1                               |

 

The host defines the packet pattern types to add to the firmware. The firmware detects matching packets that arrive in Dx. If detected, the firmware asserts the wake interrupt.

## Set property parameters


| TLV                                                                                                              | Multiple TLV instances allowed | Optional | Description                                   |
|------------------------------------------------------------------------------------------------------------------|--------------------------------|----------|-----------------------------------------------|
| [**WDI\_TLV\_WAKE\_PACKET\_BITMAP\_PATTERN**](https://docs.microsoft.com/windows-hardware/drivers/network/wdi-tlv-wake-packet-bitmap-pattern)                       | X                              | X        | WOL pattern information.                      |
| [**WDI\_TLV\_WAKE\_PACKET\_MAGIC\_PACKET**](https://docs.microsoft.com/windows-hardware/drivers/network/wdi-tlv-wake-packet-magic-packet)                           |                                | X        | Pattern ID of the magic packet.               |
| [**WDI\_TLV\_WAKE\_PACKET\_IPv4\_TCP\_SYNC**](https://docs.microsoft.com/windows-hardware/drivers/network/wdi-tlv-wake-packet-ipv4-tcp-sync)                        | X                              | X        | WOL IPv4 TCP sync packet information.         |
| [**WDI\_TLV\_WAKE\_PACKET\_IPv6\_TCP\_SYNC**](https://docs.microsoft.com/windows-hardware/drivers/network/wdi-tlv-wake-packet-ipv6-tcp-sync)                        | X                              | X        | WOL IPv4 TCP sync packet information.         |
| [**WDI\_TLV\_WAKE\_PACKET\_EAPOL\_REQUEST\_ID\_MESSAGE**](https://docs.microsoft.com/windows-hardware/drivers/network/wdi-tlv-wake-packet-eapol-request-id-message) |                                | X        | WOL pattern ID of a EAPOL request ID message. |

 

## Set property results


No additional data. The data in the header is sufficient.

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

## See also


[OID\_WDI\_SET\_REMOVE\_WOL\_PATTERN](oid-wdi-set-remove-wol-pattern.md)

 

 




