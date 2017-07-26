---
title: WDI_TLV_RECEIVE_FILTER_FIELD (0x65)
author: windows-driver-content
description: WDI_TLV_RECEIVE_FILTER_FIELD is a TLV that contains a receive filter test criterion for one field in a network header.
ms.assetid: 9037CD08-742E-4A99-A37B-9969A2BC666A
ms.author: windowsdriverdev 
ms.date: 0718/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - WDI_TLV_RECEIVE_FILTER_FIELD (0x65) Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_RECEIVE\_FILTER\_FIELD (0x65)


WDI\_TLV\_RECEIVE\_FILTER\_FIELD is a TLV that contains a receive filter test criterion for one field in a network header.

## TLV Type


0x65

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
<td>UINT32</td>
<td>Specifies a bitwise OR of flags. The possible flag value is WDI_RECEIVE_FILTER_FIELD_MAC_HEADER_VLAN_UNTAGGED_OR_ZERO. If this flag is set, the network adapter must only indicate received packets that pass the following criteria:
<ul>
<li>The packet's MAC address matches the specified MAC header field test.</li>
<li>The packet either does not contain a VLAN tag or has a VLAN tag with an ID of zero.</li>
</ul></td>
</tr>
<tr class="even">
<td>[<strong>NDIS_FRAME_HEADER</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565581) (UINT32)</td>
<td>Frame header. Specifies the type of the frame header.</td>
</tr>
<tr class="odd">
<td>[<strong>NDIS_RECEIVE_FILTER_TEST</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567183) (UINT32)</td>
<td>Receive filter test. Specifies the type of test that the receive filter performs.</td>
</tr>
<tr class="even">
<td>UINT32</td>
<td>Header field. Specifies the protocol-specific header field type with the union as documented in the [<strong>NDIS_RECEIVE_FILTER_FIELD_PARAMETERS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567169).HeaderField.</td>
</tr>
<tr class="odd">
<td>UINT8[16]</td>
<td>Field value. Specifies the value that the miniport adapter compares to the corresponding header field value in incoming packets. The location of the header field value is determined by the field type that is specified in the <em>header field</em> element. This value is in network byte order and is specified with the union as documented in the [<strong>NDIS_RECEIVE_FILTER_FIELD_PARAMETERS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567169).FieldValue.</td>
</tr>
<tr class="even">
<td>UINT8[16]</td>
<td>Test result value. If the <em>receive filter test</em> element is set to ReceiveFilterTestMaskEqual, the network adapter first calculates a result from the value in the <em>field value</em> member and the header field value as specified by the <em>header field</em> member. The adapter then compares the calculated result with <em>result value</em>. This value is specified with the union as documented in the [<strong>NDIS_RECEIVE_FILTER_FIELD_PARAMETERS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567169).ResultValue.</td>
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20WDI_TLV_RECEIVE_FILTER_FIELD%20%280x65%29%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


