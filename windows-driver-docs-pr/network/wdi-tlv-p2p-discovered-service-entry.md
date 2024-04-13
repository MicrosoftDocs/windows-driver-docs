---
title: WDI_TLV_P2P_DISCOVERED_SERVICE_ENTRY
ms.topic: reference
description: WDI_TLV_P2P_DISCOVERED_SERVICE_ENTRY is a TLV that contains a discovered service entry.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_P2P_DISCOVERED_SERVICE_ENTRY Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_P2P\_DISCOVERED\_SERVICE\_ENTRY

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_P2P\_DISCOVERED\_SERVICE\_ENTRY is a TLV that contains a discovered service entry.

## TLV Type


0x112

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                           | Multiple TLV instances allowed | Optional | Description                                                                                                                                                               |
|--------------------------------------------------------------------------------|--------------------------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_P2P\_SERVICE\_NAME**](wdi-tlv-p2p-service-name.md)               |                                |          | The name of the service, in UTF-8, up to 255 bytes.                                                                                                                       |
| [**WDI\_TLV\_P2P\_SERVICE\_INFORMATION**](wdi-tlv-p2p-service-information.md) |                                | X        | The Service Information for the service.                                                                                                                                  |
| [**WDI\_TLV\_P2P\_SERVICE\_STATUS**](wdi-tlv-p2p-service-status.md)           |                                |          | The Service Status of the service.                                                                                                                                        |
| [**WDI\_TLV\_P2P\_ADVERTISEMENT\_ID**](wdi-tlv-p2p-advertisement-id.md)       |                                |          | An ID that uniquely identifies the service instance.                                                                                                                      |
| [**WDI\_TLV\_P2P\_CONFIG\_METHODS**](wdi-tlv-p2p-config-methods.md)           |                                |          | The Configuration Methods as defined in [**WDI\_WPS\_CONFIGURATION\_METHOD**](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_wps_configuration_method). Only PinDisplay, PinKeypad and WFDS are applicable. |

 

## Requirements

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

 

