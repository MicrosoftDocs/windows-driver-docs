---
title: WDI_TLV_INDICATION_WAKE_REASON
author: windows-driver-content
description: WDI_TLV_INDICATION_WAKE_REASON is a TLV that contains a wake reason for NDIS_STATUS_WDI_INDICATION_WAKE_REASON.
ms.assetid: 3D3F93EA-4733-44FC-9CB3-721F0552F3E2
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - WDI_TLV_INDICATION_WAKE_REASON Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_INDICATION\_WAKE\_REASON


WDI\_TLV\_INDICATION\_WAKE\_REASON is a TLV that contains a wake reason for [NDIS\_STATUS\_WDI\_INDICATION\_WAKE\_REASON](https://msdn.microsoft.com/library/windows/hardware/dn925669).

## TLV Type


0x9C

## Length


The size (in bytes) of a UINT32.

## Values


| Type   | Description                |
|--------|----------------------------|
| UINT32 | Specifies the wake reason. |

 

Valid wake reason values are:

| Wake reason                                       | Value  | Description                                                                                                          |
|---------------------------------------------------|--------|----------------------------------------------------------------------------------------------------------------------|
| WDI\_WAKE\_REASON\_CODE\_PACKET                   | 0x0001 | A received packet matches the wake pattern.                                                                          |
| WDI\_WAKE\_REASON\_CODE\_MEDIA\_DISCONNECT        | 0x0002 | Media disconnection.                                                                                                 |
| WDI\_WAKE\_REASON\_CODE\_MEDIA\_CONNECT           | 0x0003 | Media connection.                                                                                                    |
| WDI\_WAKE\_REASON\_CODE\_NLO\_DISCOVERY           | 0x1000 | NLO discovery.                                                                                                       |
| WDI\_WAKE\_REASON\_CODE\_AP\_ASSOCIATION\_LOST    | 0x1001 | Access point association lost.                                                                                       |
| WDI\_WAKE\_REASON\_CODE\_GTK\_HANDSHAKE\_ERROR    | 0x1002 | GTK handshake error.                                                                                                 |
| WDI\_WAKE\_REASON\_CODE\_4WAY\_HANDSHAKE\_REQUEST | 0x1003 | 4-Way Handshake request.                                                                                             |
| WDI\_WAKE\_REASON\_CODE\_EAPID\_REQUEST           | 0x1004 | Reserved for future use.                                                                                             |
| WDI\_WAKE\_ REASON \_CODE\_INCOMING\_M1           | 0x1005 | Use WDI\_WAKE\_REASON\_CODE\_4WAY\_HANDSHAKE\_REQUEST instead.                                                       |
| WDI\_WAKE\_REASON\_CODE\_FIRMWARE\_STALLED        | 0x1010 | Firmware hang is detected (for example, by the watchdog timer) and wake logic is still functioning to wake the host. |
| WDI\_WAKE\_REASON\_CODE\_GTK\_HANDSHAKE\_REQUEST  | 0x1020 | Group Key rekey request.                                                                                             |

 

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
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20WDI_TLV_INDICATION_WAKE_REASON%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


