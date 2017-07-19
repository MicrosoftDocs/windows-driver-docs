---
title: WDI\_TLV\_ADDITIONAL\_IES
author: windows-driver-content
description: WDI\_TLV\_ADDITIONAL\_IES is a TLV that contains additional Information Element (IE) settings.
ms.assetid: B9094E9D-894F-4B23-B4DA-126F87E908C9
ms.author: windowsdriverdev 
ms.date: 0718/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - WDI_TLV_ADDITIONAL_IES Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_ADDITIONAL\_IES


WDI\_TLV\_ADDITIONAL\_IES is a TLV that contains additional Information Element (IE) settings.

## TLV Type


0x8A

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                                                       | Multiple TLV instances allowed | Optional | Description                                                                                                                                                                                                                                                                                                          |
|------------------------------------------------------------------------------------------------------------|--------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_ADDITIONAL\_BEACON\_IES**](wdi-tlv-additional-beacon-ies.md)                                 |                                | X        | An array of beacon IEs. The Wi-Fi Direct port must add these additional IEs to the beacon packets when it is acting as a Group Owner. This is ignored when the Wi-Fi Direct port is operating in device or client mode.                                                                                              |
| [**WDI\_TLV\_ADDITIONAL\_PROBE\_RESPONSE\_IES**](wdi-tlv-additional-probe-response-ies.md)                |                                | X        | An array of probe response IEs. The Wi-Fi Direct port must add these additional IEs to the probe response packets when it is acting as a Wi-Fi Direct device or Group Owner. This is ignored when the Wi-Fi Direct port is operating in client mode.                                                                 |
| [**WDI\_TLV\_ADDITIONAL\_PROBE\_REQUEST\_DEFAULT\_IES**](wdi-tlv-additional-probe-request-default-ies.md) |                                | X        | An array of additional probe request IEs. This offset is relative to the start of the buffer that contains this structure. The Wi-Fi Direct port must add these additional IEs to the probe request packets that it transmits. Note that a Wi-Fi Direct discover request may override the default probe request IEs. |

 

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
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20WDI_TLV_ADDITIONAL_IES%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


