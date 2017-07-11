---
title: WDI\_TLV\_P2P\_INVITATION\_REQUEST\_PARAMETERS
description: WDI\_TLV\_P2P\_INVITATION\_REQUEST\_PARAMETERS is a TLV that contains Wi-Fi Direct Invitation Request parameters.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: CC9B0454-4522-4589-8E21-4986BAEBC6D0
keywords: ["WDI_TLV_P2P_INVITATION_REQUEST_PARAMETERS Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- WDI_TLV_P2P_INVITATION_REQUEST_PARAMETERS
api_location:
- wditypes.hpp
api_type:
- HeaderDef
---

# WDI\_TLV\_P2P\_INVITATION\_REQUEST\_PARAMETERS


WDI\_TLV\_P2P\_INVITATION\_REQUEST\_PARAMETERS is a TLV that contains Wi-Fi Direct Invitation Request parameters.

## TLV Type


0x7C

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>UINT16</td>
<td>The Group Owner Configuration Timeout in milliseconds.</td>
</tr>
<tr class="even">
<td>UINT16</td>
<td>The Client Configuration Timeout in milliseconds.</td>
</tr>
<tr class="odd">
<td>UINT8</td>
<td>The invitation flags as defined by the Wi-Fi Direct specification.</td>
</tr>
<tr class="even">
<td>UINT8</td>
<td>A bit that indicates whether or not the outgoing Invitation Request is an invitation to a local Group Owner.
<p>Valid values are 0 and 1. This bit is set to 1 if it is an invitation to a local GO.</p></td>
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20WDI_TLV_P2P_INVITATION_REQUEST_PARAMETERS%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




