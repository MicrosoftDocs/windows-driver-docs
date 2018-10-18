---
title: OID_WDI_SET_ADAPTER_CONFIGURATION
author: windows-driver-content
description: OID_WDI_SET_ADAPTER_CONFIGURATION configures the adapter. It is an optional property and can only be sent before any ports are created.
ms.assetid: d1c37943-4755-4b9e-ab9c-9378aeca9c03
ms.date: 07/18/2017 
keywords:
 - OID_WDI_SET_ADAPTER_CONFIGURATION Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
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

 

 




