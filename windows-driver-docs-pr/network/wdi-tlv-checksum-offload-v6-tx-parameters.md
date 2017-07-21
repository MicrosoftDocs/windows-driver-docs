---
title: WDI_TLV_CHECKSUM_OFFLOAD_V6_TX_PARAMETERS (0xDC)
author: windows-driver-content
description: WDI_TLV_CHECKSUM_OFFLOAD_V6_TX_PARAMETERS is a TLV that contains for Tx checksum offload for IPv6.
ms.assetid: F0340707-4E81-4E66-AF0E-A2918F4F5C7A
ms.author: windowsdriverdev 
ms.date: 0718/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - WDI_TLV_CHECKSUM_OFFLOAD_V6_TX_PARAMETERS (0xDC) Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_CHECKSUM\_OFFLOAD\_V6\_TX\_PARAMETERS (0xDC)


WDI\_TLV\_CHECKSUM\_OFFLOAD\_V6\_TX\_PARAMETERS is a TLV that contains for Tx checksum offload for IPv6.

Capability values are reported as documented in [**NDIS\_TCP\_IP\_CHECKSUM\_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff567878). Use NDIS\_OFFLOAD\_NOT\_SUPPORTED and NDIS\_OFFLOAD\_SUPPORTED when indicating capabilities through [OID\_WDI\_GET\_ADAPTER\_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/dn925838).

## TLV Type


0xDC

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
<td>Encapsulation type. Valid values are:
<ul>
<li>WDI_ENCAPSULATION_IEEE_802_11</li>
</ul></td>
</tr>
<tr class="even">
<td>UINT32</td>
<td>Specifies if offload of checksum of packets with IP extension headers is supported.</td>
</tr>
<tr class="odd">
<td>UINT32</td>
<td>Specifies if offload of checksum with TCP options is supported.</td>
</tr>
<tr class="even">
<td>UINT32</td>
<td>Specifies if TCP checksum offload is enabled.</td>
</tr>
<tr class="odd">
<td>UINT32</td>
<td>Specifies if UDP offload is enabled.</td>
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
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20WDI_TLV_CHECKSUM_OFFLOAD_V6_TX_PARAMETERS%20%280xDC%29%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


