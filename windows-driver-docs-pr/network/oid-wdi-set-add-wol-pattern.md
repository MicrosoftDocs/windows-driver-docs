---
title: OID_WDI_SET_ADD_WOL_PATTERN
author: windows-driver-content
description: OID_WDI_SET_ADD_WOL_PATTERN adds a wake-on-LAN (WOL) pattern to the firmware.
ms.assetid: 96fb71fd-412b-4013-b3bc-c31a43516f55
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - OID_WDI_SET_ADD_WOL_PATTERN Network Drivers Starting with Windows Vista
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WDI_SET_ADD_WOL_PATTERN%20%20RELEASE:%20%286/30/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


