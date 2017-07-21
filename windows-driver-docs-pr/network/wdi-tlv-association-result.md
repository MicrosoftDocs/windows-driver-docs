---
title: WDI\_TLV\_ASSOCIATION\_RESULT
author: windows-driver-content
description: WDI\_TLV\_ASSOCIATION\_RESULT is a TLV that contains the results of an association.
ms.assetid: E0059A7A-0D20-403E-9A46-9633396A87C4
ms.author: windowsdriverdev 
ms.date: 0718/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - WDI_TLV_ASSOCIATION_RESULT Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_ASSOCIATION\_RESULT


WDI\_TLV\_ASSOCIATION\_RESULT is a TLV that contains the results of an association.

## TLV Type


0x35

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                                       | Multiple TLV instances allowed | Optional | Description                                                                                                                                                                                                 |
|--------------------------------------------------------------------------------------------|--------------------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_BSSID**](wdi-tlv-bssid.md)                                                   |                                |          | The BSSID of the BSS.                                                                                                                                                                                       |
| [**WDI\_TLV\_ASSOCIATION\_RESULT\_PARAMETERS**](wdi-tlv-association-result-parameters.md) |                                |          | The association result parameters.                                                                                                                                                                          |
| [**WDI\_TLV\_ASSOCIATION\_REQUEST\_FRAME**](wdi-tlv-association-request-frame.md)         |                                | X        | The association request that was used for association. This does not include the 802.11 MAC header.                                                                                                         |
| [**WDI\_TLV\_ASSOCIATION\_RESPONSE\_FRAME**](wdi-tlv-association-response-frame.md)       |                                | X        | The association response that was received. This does not include the 802.11 MAC header.                                                                                                                    |
| [**WDI\_TLV\_AUTHENTICATION\_RESPONSE\_FRAME**](wdi-tlv-authentication-response-frame.md) |                                | X        | The authentication response that was received with a failure code. This does not include the 802.11 MAC header. It should only be included if the connection attempt failed during authentication exchange. |
| [**WDI\_TLV\_BEACON\_PROBE\_RESPONSE**](wdi-tlv-beacon-probe-response.md)                 |                                | X        | The latest beacon or probe response frame received by the port. This does not include the 802.11 MAC header.                                                                                                |
| [**WDI\_TLV\_ETHERTYPE\_ENCAP\_TABLE**](wdi-tlv-ethertype-encap-table.md)                 |                                | X        | The Ethertype encapsulations for the association.                                                                                                                                                           |
| [**WDI\_TLV\_PHY\_TYPE\_LIST**](wdi-tlv-phy-type-list.md)                                 |                                | X        | The list of PHY identifiers that the 802.11 station uses to send or receive packets on the BSS network connection.                                                                                          |

 

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
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20WDI_TLV_ASSOCIATION_RESULT%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


