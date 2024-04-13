---
title: WDI_TLV_P2P_ADVERTISED_SERVICE_ENTRY
ms.topic: reference
description: WDI_TLV_P2P_ADVERTISED_SERVICE_ENTRY is a TLV that contains an advertised service entry.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_P2P_ADVERTISED_SERVICE_ENTRY Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_P2P\_ADVERTISED\_SERVICE\_ENTRY

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_P2P\_ADVERTISED\_SERVICE\_ENTRY is a TLV that contains an advertised service entry.

## TLV Type


0xFC

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                           | Multiple TLV instances allowed | Optional | Description                                                                                                                                                              |
|--------------------------------------------------------------------------------|--------------------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_P2P\_SERVICE\_NAME**](wdi-tlv-p2p-service-name.md)               |                                |          | Name of the service, in UTF-8, up to 255 bytes.                                                                                                                          |
| [**WDI\_TLV\_P2P\_SERVICE\_NAME\_HASH**](wdi-tlv-p2p-service-name-hash.md)    |                                |          | Hash of Service Name.                                                                                                                                                    |
| [**WDI\_TLV\_P2P\_SERVICE\_INFORMATION**](wdi-tlv-p2p-service-information.md) |                                | X        | Service Information for this service.                                                                                                                                    |
| [**WDI\_TLV\_P2P\_SERVICE\_STATUS**](wdi-tlv-p2p-service-status.md)           |                                |          | Service Status of this service.                                                                                                                                          |
| [**WDI\_TLV\_P2P\_ADVERTISEMENT\_ID**](wdi-tlv-p2p-advertisement-id.md)       |                                |          | An ID that uniquely identifies the service instance.                                                                                                                     |
| [**WDI\_TLV\_P2P\_CONFIG\_METHODS**](wdi-tlv-p2p-config-methods.md)           |                                |          | Configuration methods as defined in [**WDI\_WPS\_CONFIGURATION\_METHOD**](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_wps_configuration_method). Only PIN display, PIN keypad, and WFDS are applicable. |

 

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

 

