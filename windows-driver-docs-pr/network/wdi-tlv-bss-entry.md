---
title: WDI_TLV_BSS_ENTRY
description: WDI_TLV_BSS_ENTRY is a TLV that contains BSS entry information.
ms.assetid: 1D3AAB94-9FCE-4243-994A-7195440DDFCA
ms.date: 07/18/2017
keywords:
 - WDI_TLV_BSS_ENTRY Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_BSS\_ENTRY


WDI\_TLV\_BSS\_ENTRY is a TLV that contains BSS entry information.

## TLV Type


0x8

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                                      | Multiple TLV instances allowed | Optional                                                                            | Description                                                                                                                                                                                                                                                       |
|-------------------------------------------------------------------------------------------|--------------------------------|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_BSSID**](wdi-tlv-bssid.md)                                                  |                                |                                                                                     | The BSSID of the BSS.                                                                                                                                                                                                                                             |
| [**WDI\_TLV\_PROBE\_RESPONSE\_FRAME**](wdi-tlv-probe-response-frame.md)                  |                                | X                                                                                   | The probe response frame. If no probe response frame has been received, this is empty.                                                                                                                                                                            |
| [**WDI\_TLV\_BEACON\_FRAME**](wdi-tlv-beacon-frame.md)                                   |                                | X                                                                                   | The beacon frame. If no beacon has been received, this is empty.                                                                                                                                                                                                  |
| [**WDI\_TLV\_BSS\_ENTRY\_SIGNAL\_INFO**](wdi-tlv-bss-entry-signal-info.md)               |                                |                                                                                     | The signal information (received signal strength and link quality) of the BSS.                                                                                                                                                                                    |
| [**WDI\_TLV\_BSS\_ENTRY\_CHANNEL\_INFO**](wdi-tlv-bss-entry-channel-info.md)             |                                |                                                                                     | The logical channel number and band ID for the BSS entry.                                                                                                                                                                                                         |
| [**WDI\_TLV\_BSS\_ENTRY\_DEVICE\_CONTEXT**](wdi-tlv-bss-entry-device-context.md)         |                                | X                                                                                   | Device context about the peer. This context is provided from the IHV component and can be used to store per-BSS entry state that the IHV component wants to maintain. To avoid lifetime management issues, the IHV component must not use pointers in this field. |
| [**WDI\_TLV\_BSS\_ENTRY\_AGE\_INFO**](wdi-tlv-bss-entry-age-info.md)                     |                                | X (Note: This TLV is mandatory if the BSS list is maintained by the IHV component.) | The age information for this BSS entry, including the timestamp of when this entry was most recently discovered.                                                                                                                                                  |
| [**WDI\_TLV\_P2P\_DISCOVERED\_SERVICE\_ENTRY**](wdi-tlv-p2p-discovered-service-entry.md) | X                              | X                                                                                   | The list of services found on the remote device, including the service information retrieved with a GAS query if the discovery request specified WDI\_P2P\_SERVICE\_DISCOVERY\_TYPE\_SERVICE\_INFORMATION as the discovery type.                                  |

 

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

 

 




