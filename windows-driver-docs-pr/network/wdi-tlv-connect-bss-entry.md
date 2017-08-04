---
title: WDI_TLV_CONNECT_BSS_ENTRY
author: windows-driver-content
description: WDI_TLV_CONNECT_BSS_ENTRY is a TLV that contains a list of candidate connect BSS entries.
ms.assetid: 0D74B2DE-9224-4FDF-8EA8-B22CEC0B5F26
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - WDI_TLV_CONNECT_BSS_ENTRY Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_CONNECT\_BSS\_ENTRY


WDI\_TLV\_CONNECT\_BSS\_ENTRY is a TLV that contains a list of candidate connect BSS entries.

## TLV Type


0x34

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                                        | Multiple TLV instances allowed | Optional | Description                                                                                                                                                   |
|---------------------------------------------------------------------------------------------|--------------------------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_BSSID**](wdi-tlv-bssid.md)                                                    |                                |          | The BSSID of the BSS.                                                                                                                                         |
| [**WDI\_TLV\_PROBE\_RESPONSE\_FRAME**](wdi-tlv-probe-response-frame.md)                    |                                | X        | The probe response frame. If no probe response has been received, this would be empty.                                                                        |
| [**WDI\_TLV\_BEACON\_FRAME**](wdi-tlv-beacon-frame.md)                                     |                                | X        | The beacon frame. If no beacon has been received, this would be empty.                                                                                        |
| [**WDI\_TLV\_BSS\_ENTRY\_SIGNAL\_INFO**](wdi-tlv-bss-entry-signal-info.md)                 |                                |          | The signal information for this BSS entry.                                                                                                                    |
| [**WDI\_TLV\_BSS\_ENTRY\_CHANNEL\_INFO**](wdi-tlv-bss-entry-channel-info.md)               |                                |          | The channel information for this BSS entry.                                                                                                                   |
| [**WDI\_TLV\_BSS\_ENTRY\_DEVICE\_CONTEXT**](wdi-tlv-bss-entry-device-context.md)           |                                | X        | The IHV provided context data about this peer.                                                                                                                |
| [**WDI\_TLV\_PMKID**](wdi-tlv-pmkid.md)                                                    |                                | X        | The 16 byte PMKID value for this BSS entry.                                                                                                                   |
| [**WDI\_TLV\_EXTRA\_ASSOCIATION\_REQUEST\_IES**](wdi-tlv-extra-association-request-ies.md) |                                | X        | The IE to be included in the (re)association request frame for this BSSID. If present, this should be included in addition to the common IE.                  |
| [**WDI\_TLV\_FT\_INITIAL\_ASSOC\_PARAMETERS**](wdi-tlv-ft-initial-assoc-parameters.md)     |                                | X        | The initial Mobility Domain association parameters.                                                                                                           |
| [**WDI\_TLV\_FT\_REASSOC\_PARAMETERS**](wdi-tlv-ft-reassoc-parameters.md)                  |                                | X        | The fast transition parameters (MDIE, R0KH-ID, PMKR0Name, SNonce). This is only present for Fast Transition (not during initial mobility domain association). |
| [**WDI\_TLV\_BSS\_SELECTION\_PARAMETERS**](wdi-tlv-bss-selection-parameters.md)            |                                | X        | [**WDI\_BSS\_SELECTION\_FLAGS**](https://msdn.microsoft.com/library/windows/hardware/mt297629) that provide information used by the host for BSS selection.                               |

 

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
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20WDI_TLV_CONNECT_BSS_ENTRY%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


