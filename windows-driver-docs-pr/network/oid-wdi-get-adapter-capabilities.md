---
title: OID_WDI_GET_ADAPTER_CAPABILITIES
author: windows-driver-content
description: OID_WDI_GET_ADAPTER_CAPABILITIES is a read-only property that is issued from the host to the adapter during initialization and requests the adapter’s capabilities.
ms.assetid: e79deb29-bc0b-472e-b549-86bf71fe66ff
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - OID_WDI_GET_ADAPTER_CAPABILITIES Network Drivers Starting with Windows Vista
---

# OID\_WDI\_GET\_ADAPTER\_CAPABILITIES


OID\_WDI\_GET\_ADAPTER\_CAPABILITIES is a read-only property that is issued from the host to the adapter during initialization and requests the adapter’s capabilities.

| Scope   | Set serialized with task | Normal execution time (seconds) |
|---------|--------------------------|---------------------------------|
| Adapter | Set not supported        | 1                               |

 

## Get property parameters


No additional parameters. The data in the header is sufficient.
## Get property results


If the adapter supports Wi-Fi Direct, both [**WDI\_TLV\_AP\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/dn926129) and [**WDI\_TLV\_P2P\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/dn897863) must be specified

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>TLV</th>
<th>Multiple TLV instances allowed</th>
<th>Optional</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[<strong>WDI_TLV_COMMUNICATION_CONFIGURATION_ATTRIBUTES</strong>](https://msdn.microsoft.com/library/windows/hardware/dn926255)</td>
<td></td>
<td>X</td>
<td>Host-adapter communication protocol configuration attributes.</td>
</tr>
<tr class="even">
<td>[<strong>WDI_TLV_INTERFACE_ATTRIBUTES</strong>](https://msdn.microsoft.com/library/windows/hardware/dn897835)</td>
<td></td>
<td></td>
<td>Interface attributes.</td>
</tr>
<tr class="odd">
<td>[<strong>WDI_TLV_STATION_ATTRIBUTES</strong>](https://msdn.microsoft.com/library/windows/hardware/dn898066)</td>
<td></td>
<td></td>
<td>Station attributes.</td>
</tr>
<tr class="even">
<td>[<strong>WDI_TLV_AP_ATTRIBUTES</strong>](https://msdn.microsoft.com/library/windows/hardware/dn926129)</td>
<td></td>
<td>X</td>
<td>Access point attributes.</td>
</tr>
<tr class="odd">
<td>[<strong>WDI_TLV_VIRTUALIZATION_ATTRIBUTES</strong>](https://msdn.microsoft.com/library/windows/hardware/dn898078)</td>
<td></td>
<td>X</td>
<td>Virtualization attributes.</td>
</tr>
<tr class="even">
<td>[<strong>WDI_TLV_P2P_ATTRIBUTES</strong>](https://msdn.microsoft.com/library/windows/hardware/dn897863)</td>
<td></td>
<td>X</td>
<td>The Wi-Fi Direct attributes.</td>
</tr>
<tr class="odd">
<td>[<strong>WDI_TLV_DATAPATH_ATTRIBUTES</strong>](https://msdn.microsoft.com/library/windows/hardware/dn926277)</td>
<td></td>
<td>X</td>
<td>Datapath attributes.</td>
</tr>
<tr class="even">
<td>[<strong>WDI_TLV_BAND_INFO</strong>](https://msdn.microsoft.com/library/windows/hardware/dn926146)</td>
<td>X</td>
<td>X</td>
<td>Band information.</td>
</tr>
<tr class="odd">
<td>[<strong>WDI_TLV_PHY_INFO</strong>](https://msdn.microsoft.com/library/windows/hardware/dn898023)</td>
<td>X</td>
<td>X</td>
<td>PHY information.</td>
</tr>
<tr class="even">
<td>[<strong>WDI_TLV_PM_CAPABILITIES</strong>](https://msdn.microsoft.com/library/windows/hardware/dn898032)</td>
<td></td>
<td>X</td>
<td>Power management capabilities.</td>
</tr>
<tr class="odd">
<td>[<strong>WDI_TLV_COUNTRY_REGION_LIST</strong>](https://msdn.microsoft.com/library/windows/hardware/dn926268)</td>
<td></td>
<td>X</td>
<td>Country or region codes.</td>
</tr>
<tr class="even">
<td>[<strong>WDI_TLV_RECEIVE_COALESCING_CAPABILITIES</strong>](https://msdn.microsoft.com/library/windows/hardware/dn898046)</td>
<td></td>
<td>X</td>
<td>Hardware assisted receive filter capabilities.</td>
</tr>
<tr class="odd">
<td>[<strong>WDI_TLV_TCP_OFFLOAD_CAPABILITIES</strong>](https://msdn.microsoft.com/library/windows/hardware/dn898069)</td>
<td></td>
<td>X</td>
<td>TCP/IP offload capabilities.</td>
</tr>
<tr class="even">
<td><p>[<strong>WDI_TLV_SUPPORTED_GUIDS</strong>](https://msdn.microsoft.com/library/windows/hardware/mt769918)</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>Added in Windows 10, version 1607, WDI version 1.0.21.</p>
<p>A list of GUIDs that are passed on to NDIS when WDI is queried for [OID_GEN_SUPPORTED_GUIDS](https://msdn.microsoft.com/library/windows/hardware/ff569641).</p></td>
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
<td>Dot11wdi.h</td>
</tr>
</tbody>
</table>

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WDI_GET_ADAPTER_CAPABILITIES%20%20RELEASE:%20%286/30/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


