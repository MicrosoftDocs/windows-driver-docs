---
title: WDI_TLV_CONNECT_PARAMETERS
description: WDI_TLV_CONNECT_PARAMETERS is a TLV that contains parameters for OID_WDI_TASK_CONNECT and OID_WDI_TASK_ROAM.
ms.assetid: 6B2B4E5D-4BF9-4803-A373-FDF64AD3C99B
ms.date: 07/18/2017
keywords:
 - WDI_TLV_CONNECT_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_CONNECT\_PARAMETERS


WDI\_TLV\_CONNECT\_PARAMETERS is a TLV that contains parameters for [OID\_WDI\_TASK\_CONNECT](https://msdn.microsoft.com/library/windows/hardware/dn925948) and [OID\_WDI\_TASK\_ROAM](https://msdn.microsoft.com/library/windows/hardware/dn925958).

## TLV Type


0x33

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values

| Type | Multiple TLV instances allowed | Optional | Description |
| --- | --- | --- | --- |
| [**WDI\_TLV\_CONNECTION\_SETTINGS**](wdi-tlv-connection-settings.md) |   |   | The settings for the connection. |
| [**WDI\_TLV\_SSID**](wdi-tlv-ssid.md) | X |   | List of SSIDs that the port is allowed to connect to. |
| [**WDI\_TLV\_HESSID**](wdi-tlv-hessid.md) |   | X | List of HESSIDs that the port is allowed to connect to. This is an additional requirement to the SSID list. |
| [**WDI\_TLV\_AUTH\_ALGO\_LIST**](wdi-tlv-auth-algo-list.md) |   |   | The list of authentication algorithms that the connection can use. |
| [**WDI\_TLV\_MULTICAST\_CIPHER\_ALGO\_LIST**](wdi-tlv-multicast-cipher-algo-list.md) |   |   | The list of multicast cipher algorithms that the connection can use. |
| [**WDI\_TLV\_UNICAST\_CIPHER\_ALGO\_LIST**](wdi-tlv-unicast-cipher-algo-list.md) |   |   | The list of unicast cipher algorithms that the connection can use. |
| [**WDI\_TLV\_EXTRA\_ASSOCIATION\_REQUEST\_IES**](wdi-tlv-extra-association-request-ies.md) |   | X | The IE blobs that must be included in the association requests sent by the port. This is applicable to any BSSID that the device would associate with. It should be used in addition to the BSSID specific IEs. |
| [**WDI\_TLV\_PHY\_TYPE\_LIST**](wdi-tlv-phy-type-list.md) |   | X | The list of PHYs that are allowed to be used for the association. If not specified, any supported PHY can be used. If specified, the device must only use the listed PHYs. |
| [**WDI\_TLV\_DISALLOWED\_BSSIDS\_LIST**](wdi-tlv-disallowed-bssids-list.md) |   | X | The list of BSSIDs that are not allowed to be used for association. If specified, the adapter must not associate to any AP that is in this list. |
| [**WDI\_TLV\_ALLOWED\_BSSIDS\_LIST**](wdi-tlv-allowed-bssids-list.md) |   | X | The list of BSSIDs that are allowed to be used for association. If WDI specifies 255.255.255.255 then all BSSIDs are allowed. | 

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
