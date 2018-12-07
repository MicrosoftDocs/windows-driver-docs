---
title: WDI_TLV_ADDITIONAL_IES
description: WDI_TLV_ADDITIONAL_IES is a TLV that contains additional Information Element (IE) settings.
ms.assetid: B9094E9D-894F-4B23-B4DA-126F87E908C9
ms.date: 07/18/2017
keywords:
 - WDI_TLV_ADDITIONAL_IES Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
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

 

 




