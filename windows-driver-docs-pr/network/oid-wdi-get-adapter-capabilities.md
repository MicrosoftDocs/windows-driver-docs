---
title: OID_WDI_GET_ADAPTER_CAPABILITIES
description: OID_WDI_GET_ADAPTER_CAPABILITIES is a read-only property that is issued from the host to the adapter during initialization and requests the adapter’s capabilities.
ms.assetid: e79deb29-bc0b-472e-b549-86bf71fe66ff
ms.date: 07/18/2017
keywords:
 - OID_WDI_GET_ADAPTER_CAPABILITIES Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WDI\_GET\_ADAPTER\_CAPABILITIES


OID\_WDI\_GET\_ADAPTER\_CAPABILITIES is a read-only property that is issued from the host to the adapter during initialization and requests the adapter’s capabilities.

| Scope   | Set serialized with task | Normal execution time (seconds) |
|---------|--------------------------|---------------------------------|
| Adapter | Set not supported        | 1                               |

 

## Get property parameters


No additional parameters. The data in the header is sufficient.
## Get property results


If the adapter supports Wi-Fi Direct, both [**WDI\_TLV\_AP\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/dn926129) and [**WDI\_TLV\_P2P\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/dn897863) must be specified.

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
<td><a href="https://msdn.microsoft.com/library/windows/hardware/dn926255" data-raw-source="[&lt;strong&gt;WDI_TLV_COMMUNICATION_CONFIGURATION_ATTRIBUTES&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn926255)"><strong>WDI_TLV_COMMUNICATION_CONFIGURATION_ATTRIBUTES</strong></a></td>
<td></td>
<td>X</td>
<td>Host-adapter communication protocol configuration attributes.</td>
</tr>
<tr class="even">
<td><a href="https://msdn.microsoft.com/library/windows/hardware/dn897835" data-raw-source="[&lt;strong&gt;WDI_TLV_INTERFACE_ATTRIBUTES&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn897835)"><strong>WDI_TLV_INTERFACE_ATTRIBUTES</strong></a></td>
<td></td>
<td></td>
<td>Interface attributes.</td>
</tr>
<tr class="odd">
<td><a href="https://msdn.microsoft.com/library/windows/hardware/dn898066" data-raw-source="[&lt;strong&gt;WDI_TLV_STATION_ATTRIBUTES&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn898066)"><strong>WDI_TLV_STATION_ATTRIBUTES</strong></a></td>
<td></td>
<td></td>
<td>Station attributes.</td>
</tr>
<tr class="even">
<td><a href="https://msdn.microsoft.com/library/windows/hardware/dn926129" data-raw-source="[&lt;strong&gt;WDI_TLV_AP_ATTRIBUTES&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn926129)"><strong>WDI_TLV_AP_ATTRIBUTES</strong></a></td>
<td></td>
<td>X</td>
<td>Access point attributes.</td>
</tr>
<tr class="odd">
<td><a href="https://msdn.microsoft.com/library/windows/hardware/dn898078" data-raw-source="[&lt;strong&gt;WDI_TLV_VIRTUALIZATION_ATTRIBUTES&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn898078)"><strong>WDI_TLV_VIRTUALIZATION_ATTRIBUTES</strong></a></td>
<td></td>
<td>X</td>
<td>Virtualization attributes.</td>
</tr>
<tr class="even">
<td><a href="https://msdn.microsoft.com/library/windows/hardware/dn897863" data-raw-source="[&lt;strong&gt;WDI_TLV_P2P_ATTRIBUTES&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn897863)"><strong>WDI_TLV_P2P_ATTRIBUTES</strong></a></td>
<td></td>
<td>X</td>
<td>The Wi-Fi Direct attributes.</td>
</tr>
<tr class="odd">
<td><a href="https://msdn.microsoft.com/library/windows/hardware/dn926277" data-raw-source="[&lt;strong&gt;WDI_TLV_DATAPATH_ATTRIBUTES&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn926277)"><strong>WDI_TLV_DATAPATH_ATTRIBUTES</strong></a></td>
<td></td>
<td>X</td>
<td>Datapath attributes.</td>
</tr>
<tr class="even">
<td><a href="https://msdn.microsoft.com/library/windows/hardware/dn926146" data-raw-source="[&lt;strong&gt;WDI_TLV_BAND_INFO&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn926146)"><strong>WDI_TLV_BAND_INFO</strong></a></td>
<td>X</td>
<td>X</td>
<td>Band information.</td>
</tr>
<tr class="odd">
<td><a href="https://msdn.microsoft.com/library/windows/hardware/dn898023" data-raw-source="[&lt;strong&gt;WDI_TLV_PHY_INFO&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn898023)"><strong>WDI_TLV_PHY_INFO</strong></a></td>
<td>X</td>
<td>X</td>
<td>PHY information.</td>
</tr>
<tr class="even">
<td><a href="https://msdn.microsoft.com/library/windows/hardware/dn898032" data-raw-source="[&lt;strong&gt;WDI_TLV_PM_CAPABILITIES&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn898032)"><strong>WDI_TLV_PM_CAPABILITIES</strong></a></td>
<td></td>
<td>X</td>
<td>Power management capabilities.</td>
</tr>
<tr class="odd">
<td><a href="https://msdn.microsoft.com/library/windows/hardware/dn926268" data-raw-source="[&lt;strong&gt;WDI_TLV_COUNTRY_REGION_LIST&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn926268)"><strong>WDI_TLV_COUNTRY_REGION_LIST</strong></a></td>
<td></td>
<td>X</td>
<td>Country or region codes.</td>
</tr>
<tr class="even">
<td><a href="https://msdn.microsoft.com/library/windows/hardware/dn898046" data-raw-source="[&lt;strong&gt;WDI_TLV_RECEIVE_COALESCING_CAPABILITIES&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn898046)"><strong>WDI_TLV_RECEIVE_COALESCING_CAPABILITIES</strong></a></td>
<td></td>
<td>X</td>
<td>Hardware assisted receive filter capabilities.</td>
</tr>
<tr class="odd">
<td><a href="https://msdn.microsoft.com/library/windows/hardware/dn898069" data-raw-source="[&lt;strong&gt;WDI_TLV_TCP_OFFLOAD_CAPABILITIES&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn898069)"><strong>WDI_TLV_TCP_OFFLOAD_CAPABILITIES</strong></a></td>
<td></td>
<td>X</td>
<td>TCP/IP offload capabilities.</td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/mt769918" data-raw-source="[&lt;strong&gt;WDI_TLV_SUPPORTED_GUIDS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/mt769918)"><strong>WDI_TLV_SUPPORTED_GUIDS</strong></a></p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>Added in Windows 10, version 1607, WDI version 1.0.21.</p>
<p>A list of GUIDs that are passed on to NDIS when WDI is queried for <a href="https://msdn.microsoft.com/library/windows/hardware/ff569641" data-raw-source="[OID_GEN_SUPPORTED_GUIDS](https://msdn.microsoft.com/library/windows/hardware/ff569641)">OID_GEN_SUPPORTED_GUIDS</a>.</p></td>
</tr>
<tr class="odd">
<td><p><a href="wdi-tlv-os-power-management-features.md" data-raw-source="[&lt;strong&gt;WDI_TLV_OS_POWER_MANAGEMENT_FEATURES&lt;/strong&gt;](wdi-tlv-os-power-management-features.md)"><strong>WDI_TLV_OS_POWER_MANAGEMENT_FEATURES</strong></a></p></td>
<td></td>
<td></td>
<td><p>Added in Windows 10, version 1803, WDI version 1.1.6.</p>
<p>Used to enable advanced OS power management features.</p>
</td>
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

 

 




