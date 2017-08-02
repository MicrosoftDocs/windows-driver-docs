---
title: WDI_TLV_BSS_ENTRY
author: windows-driver-content
description: WDI_TLV_BSS_ENTRY is a TLV that contains BSS entry information.
ms.assetid: 1D3AAB94-9FCE-4243-994A-7195440DDFCA
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - WDI_TLV_BSS_ENTRY Network Drivers Starting with Windows Vista
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20WDI_TLV_BSS_ENTRY%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


