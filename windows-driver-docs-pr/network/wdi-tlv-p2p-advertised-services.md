---
title: WDI\_TLV\_P2P\_ADVERTISED\_SERVICES
description: WDI\_TLV\_P2P\_ADVERTISED\_SERVICES is a TLV that contains a list of advertised services.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: C210DDF3-0349-4108-82EC-1823F562E5D7
keywords: ["WDI_TLV_P2P_ADVERTISED_SERVICES Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- WDI_TLV_P2P_ADVERTISED_SERVICES
api_location:
- wditypes.hpp
api_type:
- HeaderDef
---

# WDI\_TLV\_P2P\_ADVERTISED\_SERVICES


WDI\_TLV\_P2P\_ADVERTISED\_SERVICES is a TLV that contains a list of advertised services.

## TLV Type


0xEF

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>Type</th>
<th>Multiple TLV instances allowed</th>
<th>Optional</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[<strong>WDI_TLV_P2P_ADVERTISED_SERVICE_ENTRY</strong>](wdi-tlv-p2p-advertised-service-entry.md)</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td>A list of advertised services.</td>
</tr>
<tr class="even">
<td><p>[<strong>WDI_TLV_P2P_ADVERTISED_PREFIX_ENTRY</strong>](wdi-tlv-p2p-advertised-prefix-entry.md)</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>A list of advertised prefixes that are derived from the list of advertised services.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>WDI_TLV_P2P_ASP2_ADVERTISED_SERVICE_ENTRY</strong>](wdi-tlv-p2p-asp2-advertised-service-entry.md)</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>Added in Windows 10, version 1607, WDI version 1.0.21.</p>
<p>A list of advertised ASP2 services.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>WDI_TLV_P2P_SERVICE_UPDATE_INDICATOR</strong>](wdi-tlv-p2p-service-update-indicator.md)</p></td>
<td></td>
<td></td>
<td><p>The service update indicator to include in ANQP responses if the driver supports responding to service information discovery ANQP requests.</p></td>
</tr>
</tbody>
</table>

 

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20WDI_TLV_P2P_ADVERTISED_SERVICES%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




