---
title: WDI\_TLV\_CONNECT\_PARAMETERS
author: windows-driver-content
description: WDI\_TLV\_CONNECT\_PARAMETERS is a TLV that contains parameters for OID\_WDI\_TASK\_CONNECT and OID\_WDI\_TASK\_ROAM.
ms.assetid: 6B2B4E5D-4BF9-4803-A373-FDF64AD3C99B
ms.author: windowsdriverdev 
ms.date: 0718/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - WDI_TLV_CONNECT_PARAMETERS Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_CONNECT\_PARAMETERS


WDI\_TLV\_CONNECT\_PARAMETERS is a TLV that contains parameters for [OID\_WDI\_TASK\_CONNECT](https://msdn.microsoft.com/library/windows/hardware/dn925948) and [OID\_WDI\_TASK\_ROAM](https://msdn.microsoft.com/library/windows/hardware/dn925958).

## TLV Type


0x33

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


Type
Multiple TLV instances allowed
Optional
Description
[**WDI\_TLV\_CONNECTION\_SETTINGS**](wdi-tlv-connection-settings.md)
The settings for the connection.
[**WDI\_TLV\_SSID**](wdi-tlv-ssid.md)
X
List of SSIDs that the port is allowed to connect to.
[**WDI\_TLV\_HESSID**](wdi-tlv-hessid.md)
X
List of HESSIDs that the port is allowed to connect to. This is an additional requirement to the SSID list.
[**WDI\_TLV\_AUTH\_ALGO\_LIST**](wdi-tlv-auth-algo-list.md)
The list of authentication algorithms that the connection can use.
[**WDI\_TLV\_MULTICAST\_CIPHER\_ALGO\_LIST**](wdi-tlv-multicast-cipher-algo-list.md)
The list of multicast cipher algorithms that the connection can use.
[**WDI\_TLV\_UNICAST\_CIPHER\_ALGO\_LIST**](wdi-tlv-unicast-cipher-algo-list.md)
The list of unicast cipher algorithms that the connection can use.
[**WDI\_TLV\_EXTRA\_ASSOCIATION\_REQUEST\_IES**](wdi-tlv-extra-association-request-ies.md)
X
The IE blobs that must be included in the association requests sent by the port. This is applicable to any BSSID that the device would associate with. It should be used in addition to the BSSID specific IEs.
[**WDI\_TLV\_PHY\_TYPE\_LIST**](wdi-tlv-phy-type-list.md)
X
The list of PHYs that are allowed to be used for the association. If not specified, any supported PHY can be used. If specified, the device must only use the listed PHYs.
[**WDI\_TLV\_DISALLOWED\_BSSIDS\_LIST**](wdi-tlv-disallowed-bssids-list.md)
X
The list of BSSIDs that are not allowed to be used for association. If specified, the adapter must not associate to any AP that is not in this list.
[**WDI\_TLV\_ALLOWED\_BSSIDS\_LIST**](wdi-tlv-allowed-bssids-list.md)
X
The list of BSSIDs that are allowed to be used for association. If WDI specifies 255.255.255.255 then all BSSIDs are allowed.
 

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
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20WDI_TLV_CONNECT_PARAMETERS%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


