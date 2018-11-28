---
title: OID_WDI_SET_ADD_WOL_PATTERN
description: OID_WDI_SET_ADD_WOL_PATTERN adds a wake-on-LAN (WOL) pattern to the firmware.
ms.assetid: 96fb71fd-412b-4013-b3bc-c31a43516f55
ms.date: 07/18/2017
keywords:
 - OID_WDI_SET_ADD_WOL_PATTERN Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
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
| [**WDI\_TLV\_WAKE\_PACKET\_BITMAP\_PATTERN**](https://msdn.microsoft.com/library/windows/hardware/dn898084)                       | X                              | X        | WOL pattern information.                      |
| [**WDI\_TLV\_WAKE\_PACKET\_MAGIC\_PACKET**](https://msdn.microsoft.com/library/windows/hardware/dn898185)                           |                                | X        | Pattern ID of the magic packet.               |
| [**WDI\_TLV\_WAKE\_PACKET\_IPv4\_TCP\_SYNC**](https://msdn.microsoft.com/library/windows/hardware/dn898089)                        | X                              | X        | WOL IPv4 TCP sync packet information.         |
| [**WDI\_TLV\_WAKE\_PACKET\_IPv6\_TCP\_SYNC**](https://msdn.microsoft.com/library/windows/hardware/dn898091)                        | X                              | X        | WOL IPv4 TCP sync packet information.         |
| [**WDI\_TLV\_WAKE\_PACKET\_EAPOL\_REQUEST\_ID\_MESSAGE**](https://msdn.microsoft.com/library/windows/hardware/dn898087) |                                | X        | WOL pattern ID of a EAPOL request ID message. |

 

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

 

 




