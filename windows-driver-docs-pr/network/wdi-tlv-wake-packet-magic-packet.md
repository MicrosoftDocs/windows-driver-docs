---
title: WDI_TLV_WAKE_PACKET_MAGIC_PACKET
author: windows-driver-content
description: WDI_TLV_WAKE_PACKET_MAGIC_PACKET is a TLV that contains a pattern ID of a magic packet for OID_WDI_SET_ADD_WOL_PATTERN.
ms.assetid: F1DEB65B-8DD4-4D4A-9DCB-950C3B562F0A
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - WDI_TLV_WAKE_PACKET_MAGIC_PACKET Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_WAKE\_PACKET\_MAGIC\_PACKET


WDI\_TLV\_WAKE\_PACKET\_MAGIC\_PACKET is a TLV that contains a pattern ID of a magic packet for [OID\_WDI\_SET\_ADD\_WOL\_PATTERN](https://msdn.microsoft.com/library/windows/hardware/dn925858).

## TLV Type


0x5C

## Length


The size (in bytes) of a UINT32.

## Values


| Type   | Description                                        |
|--------|----------------------------------------------------|
| UINT32 | Specifies the wake-on-LAN magic packet pattern ID. |

 

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
<td>Wditypes.hpp</td>
</tr>
</tbody>
</table>

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20WDI_TLV_WAKE_PACKET_MAGIC_PACKET%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


