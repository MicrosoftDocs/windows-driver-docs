---
title: WDI_TLV_P2P_PROVISION_DISCOVERY_RESPONSE_INFO
description: WDI_TLV_P2P_PROVISION_DISCOVERY_RESPONSE_INFO is a TLV that contains Wi-Fi Direct Provision Discovery Response information.
ms.assetid: EB7C4A5C-27D8-4A84-BC91-0DED51FB74C2
ms.date: 07/18/2017
keywords:
 - WDI_TLV_P2P_PROVISION_DISCOVERY_RESPONSE_INFO Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_PROVISION\_DISCOVERY\_RESPONSE\_INFO


WDI\_TLV\_P2P\_PROVISION\_DISCOVERY\_RESPONSE\_INFO is a TLV that contains Wi-Fi Direct Provision Discovery Response information.

## TLV Type


0x87

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                                                                     | Multiple TLV instances allowed | Optional | Description                                                                                                                                                                                                                             |
|--------------------------------------------------------------------------------------------------------------------------|--------------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_P2P\_PROVISION\_DISCOVERY\_RESPONSE\_PARAMETERS**](wdi-tlv-p2p-provision-discovery-response-parameters.md) |                                |          | The provision discovery response parameters.                                                                                                                                                                                            |
| [**WDI\_TLV\_P2P\_PROVISION\_SERVICE\_ATTRIBUTES**](wdi-tlv-p2p-provision-service-attributes.md)                        |                                | X        | The Provision Service attributes.                                                                                                                                                                                                       |
| [**WDI\_TLV\_P2P\_GROUP\_ID**](wdi-tlv-p2p-group-id.md)                                                                 |                                | X        | The Group ID if Wi-Fi Direct Service is supported.                                                                                                                                                                                      |
| [**WDI\_TLV\_P2P\_PERSISTENT\_GROUP\_ID**](wdi-tlv-p2p-persistent-group-id.md)                                          |                                | X        | The Group IP for the Persistent Group to be used for the connection. This field is valid if the Persistent Group flag in [**WDI\_TLV\_P2P\_PROVISION\_SERVICE\_ATTRIBUTES**](wdi-tlv-p2p-provision-service-attributes.md) is set to 1. |
| [**WDI\_TLV\_P2P\_SERVICE\_SESSION\_INFO**](wdi-tlv-p2p-service-session-info.md)                                        |                                | X        | The Service Session information.                                                                                                                                                                                                        |

 

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

 

 




