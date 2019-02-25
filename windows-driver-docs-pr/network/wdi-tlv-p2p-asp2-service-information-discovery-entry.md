---
title: WDI_TLV_P2P_ASP2_SERVICE_INFORMATION_DISCOVERY_ENTRY
description: WDI_TLV_P2P_ASP2_SERVICE_INFORMATION_DISCOVERY_ENTRY is a TLV that contains an ASP2 Service Information Discovery Entry.
ms.assetid: 67F1CDE2-8003-44D3-B338-FE7C5EA48C29
ms.date: 07/18/2017
keywords:
 - WDI_TLV_P2P_ASP2_SERVICE_INFORMATION_DISCOVERY_ENTRY Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_ASP2\_SERVICE\_INFORMATION\_DISCOVERY\_ENTRY


WDI\_TLV\_P2P\_ASP2\_SERVICE\_INFORMATION\_DISCOVERY\_ENTRY is a TLV that contains an ASP2 Service Information Discovery Entry.

**Note**  This TLV was added in Windows 10, version 1607, WDI version 1.0.21.

 

## TLV Type


0x12D

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                                      | Multiple TLV instances allowed | Optional | Description                                                                                                         |
|-------------------------------------------------------------------------------------------|--------------------------------|----------|---------------------------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_P2P\_SERVICE\_NAME**](wdi-tlv-p2p-service-name.md)                          |                                |          | Name of the service (UTF-8), up to 21 bytes.                                                                        |
| [**WDI\_TLV\_P2P\_INSTANCE\_NAME**](wdi-tlv-p2p-instance-name.md)                        |                                |          | Instance name of the service (UTF-8), up to 63 bytes.                                                               |
| [**WDI\_TLV\_P2P\_SERVICE\_INFORMATION**](wdi-tlv-p2p-service-information.md)            |                                | X        | Request service information to be used for the ANQP query request to download service information for this Service. |
| [**WDI\_TLV\_P2P\_SERVICE\_UPDATE\_INDICATOR**](wdi-tlv-p2p-service-update-indicator.md) |                                | X        | Service Update indicator to be used for the ANQP query request.                                                     |
| [**WDI\_TLV\_P2P\_SERVICE\_TRANSACTION\_ID**](wdi-tlv-p2p-service-transaction-id.md)     |                                | X        | Service transaction ID to be used for the ANQP query request.                                                       |

 

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

 

 




