---
title: OID\_WDI\_SET\_ADAPTER\_CONFIGURATION
author: windows-driver-content
description: OID\_WDI\_SET\_ADAPTER\_CONFIGURATION configures the adapter. It is an optional property and can only be sent before any ports are created.
ms.assetid: d1c37943-4755-4b9e-ab9c-9378aeca9c03
ms.author: windowsdriverdev 
ms.date: 0718/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - OID_WDI_SET_ADAPTER_CONFIGURATION Network Drivers Starting with Windows Vista
---

# OID\_WDI\_SET\_ADAPTER\_CONFIGURATION


OID\_WDI\_SET\_ADAPTER\_CONFIGURATION configures the adapter. It is an optional property and can only be sent before any ports are created.

| Scope   | Set serialized with task | Normal execution time (seconds) |
|---------|--------------------------|---------------------------------|
| Adapter | Yes                      | 1                               |

 

## Set property parameters


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
<td>[<strong>WDI_TLV_CONFIGURED_MAC_ADDRESS</strong>](https://msdn.microsoft.com/library/windows/hardware/dn926257)</td>
<td></td>
<td>X</td>
<td>MAC address.</td>
</tr>
<tr class="even">
<td>[<strong>WDI_TLV_UNREACHABLE_DETECTION_THRESHOLD</strong>](https://msdn.microsoft.com/library/windows/hardware/dn898075)</td>
<td></td>
<td>X</td>
<td>Unreachable detection threshold.</td>
</tr>
<tr class="odd">
<td>[<strong>WDI_TLV_P2P_GO_INTERNAL_RESET_POLICY</strong>](https://msdn.microsoft.com/library/windows/hardware/dn897879)</td>
<td></td>
<td>X</td>
<td>Policy used by the firmware for operating channel selection after a Wi-Fi Direct GO Reset is stopped/restarted.</td>
</tr>
<tr class="even">
<td>[<strong>WDI_TLV_BAND_ID_LIST</strong>](https://msdn.microsoft.com/library/windows/hardware/dn926145)</td>
<td></td>
<td>X</td>
<td>List of band IDs.</td>
</tr>
<tr class="odd">
<td>[<strong>WDI_TLV_LINK_QUALITY_BAR_MAP</strong>](https://msdn.microsoft.com/library/windows/hardware/dn897841)</td>
<td></td>
<td></td>
<td>Mapping of signal quality to Wi-Fi signal strength bars. This field should be ignored by the adapter and it should use the behavior specified in [NDIS_STATUS_WDI_INDICATION_LINK_STATE_CHANGE](ndis-status-wdi-indication-link-state-change.md) for doing Link Quality notifications.</td>
</tr>
<tr class="even">
<td>[<strong>WDI_TLV_ADAPTER_NLO_SCAN_MODE</strong>](https://msdn.microsoft.com/library/windows/hardware/mt269108)</td>
<td></td>
<td>X</td>
<td>Indicates whether the NLO scans should be performed in active or passive mode.</td>
</tr>
<tr class="odd">
<td>[<strong>WDI_TLV_PLDR_SUPPORT</strong>](https://msdn.microsoft.com/library/windows/hardware/mt593243)</td>
<td></td>
<td></td>
<td>Added in Windows 10, version 1511, WDI version 1.0.10.
<p>Specifies if PLDR is supported.</p></td>
</tr>
</tbody>
</table>

 

## Set property results


No additional data. The data in the header is sufficient.
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
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WDI_SET_ADAPTER_CONFIGURATION%20%20RELEASE:%20%286/30/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


