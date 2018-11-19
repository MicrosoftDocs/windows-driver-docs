---
title: WDI_TLV_P2P_PROVISION_DISCOVERY_REQUEST_INFO
description: WDI_TLV_P2P_PROVISION_DISCOVERY_REQUEST_INFO is a TLV that contains Wi-Fi Direct Provision Discovery Request information.
ms.assetid: C71F2FA9-2255-45E9-83CD-FA8DBEF5EA74
ms.date: 07/18/2017
keywords:
 - WDI_TLV_P2P_PROVISION_DISCOVERY_REQUEST_INFO Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_PROVISION\_DISCOVERY\_REQUEST\_INFO


WDI\_TLV\_P2P\_PROVISION\_DISCOVERY\_REQUEST\_INFO is a TLV that contains Wi-Fi Direct Provision Discovery Request information.

## TLV Type


0x83

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                                                                   | Multiple TLV instances allowed | Optional | Description                                                                                                                                                                                                                             |
|------------------------------------------------------------------------------------------------------------------------|--------------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_P2P\_PROVISION\_DISCOVERY\_REQUEST\_PARAMETERS**](wdi-tlv-p2p-provision-discovery-request-parameters.md) |                                |          | The Wi-Fi Direct Provision Discovery Request parameters.                                                                                                                                                                                |
| [**WDI\_TLV\_P2P\_GROUP\_ID**](wdi-tlv-p2p-group-id.md)                                                               |                                | X        | The Group ID for the target Wi-Fi Direct GO. The Group ID is optional. In the case of Wi-Fi Direct services, this is the Group ID for the local Wi-Fi Direct GO that the remote side should join.                                       |
| [**WDI\_TLV\_P2P\_PROVISION\_SERVICE\_ATTRIBUTES**](wdi-tlv-p2p-provision-service-attributes.md)                      |                                | X        | The Wi-Fi Direct Provision Service attributes.                                                                                                                                                                                          |
| [**WDI\_TLV\_P2P\_PERSISTENT\_GROUP\_ID**](wdi-tlv-p2p-persistent-group-id.md)                                        |                                | X        | The Group IP for the Persistent Group to be used for the connection. This field is valid if the Persistent Group flag in [**WDI\_TLV\_P2P\_PROVISION\_SERVICE\_ATTRIBUTES**](wdi-tlv-p2p-provision-service-attributes.md) is set to 1. |
| [**WDI\_TLV\_P2P\_SERVICE\_SESSION\_INFO**](wdi-tlv-p2p-service-session-info.md)                                      |                                | X        | Service Session information. This field is valid if [**WDI\_TLV\_P2P\_PROVISION\_SERVICE\_ATTRIBUTES**](wdi-tlv-p2p-provision-service-attributes.md) is present.                                                                       |

 

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

 

 




