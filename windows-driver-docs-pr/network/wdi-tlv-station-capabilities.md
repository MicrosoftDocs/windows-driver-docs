---
title: WDI_TLV_STATION_CAPABILITIES
description: WDI_TLV_STATION_CAPABILITIES is a TLV that contains the capabilities of a station.
ms.assetid: 567445F1-EEDC-4302-B709-ED76D044A971
ms.date: 07/18/2017
keywords:
 - WDI_TLV_STATION_CAPABILITIES Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_STATION\_CAPABILITIES


WDI\_TLV\_STATION\_CAPABILITIES is a TLV that contains the capabilities of a station.

## TLV Type


0x11

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
<td>The scan SSID list size.</td>
</tr>
<tr class="even">
<td>UINT32</td>
<td>The desired BSSID list size.</td>
</tr>
<tr class="odd">
<td>UINT32</td>
<td>The desired SSID list size.</td>
</tr>
<tr class="even">
<td>UINT32</td>
<td>The privacy exemption list size.</td>
</tr>
<tr class="odd">
<td>UINT32</td>
<td>The key mapping table size.</td>
</tr>
<tr class="even">
<td>UINT32</td>
<td>The default key table size.</td>
</tr>
<tr class="odd">
<td>UINT32</td>
<td>The maximum length of the WEP key value.</td>
</tr>
<tr class="even">
<td>UINT32</td>
<td>The maximum number per STA default key tables.</td>
</tr>
<tr class="odd">
<td>UINT8</td>
<td>Supported QoS flags. Specifies whether the device supports WMM.
<p>Valid values are 0 (not supported) and 1 (supported).</p></td>
</tr>
<tr class="even">
<td>UINT8</td>
<td>Specifies whether host-FIPS mode is implemented.
<p>If the field is set to DOT11_EXTSTA_ATTRIBUTES_SAFEMODE_OID_SUPPORTED with no other bits set, the driver implements the 802.11 safe mode of operation.</p>
<p>If the field is set to DOT11_EXTSTA_ATTRIBUTES_SAFEMODE_CERTIFIED, the NIC has received a validation certificate from the National Institute of Standards and Technology (NIST) under Federal Information Processing Standards (FIPS) Publication 140-2, Security Requirements for Cryptographic Modules. In this mode, the hardware is responsible for ensuring compliance to FIPS standard.</p>
<p>If the field is set to zero (0), FIPS mode is not implemented by the NIC.</p></td>
</tr>
<tr class="odd">
<td>UINT8</td>
<td>Specifies whether 802.11w MFP capability is supported.
<p>Valid values are 0 (not supported) and 1 (supported).</p></td>
</tr>
<tr class="even">
<td>UINT8</td>
<td>Specifies whether auto power save is supported.
<p>Valid values are 0 (not supported) and 1 (supported).</p></td>
</tr>
<tr class="odd">
<td>UINT8</td>
<td>Specifies whether the adapter maintains the Station BSS List cache.
<p>Valid values are 0 (no) and 1 (yes).</p></td>
</tr>
<tr class="even">
<td>UINT8</td>
<td>Specifies whether the adapter may attempt association to a BSSID that is not specified in the Preferred BSSID list during a Station connect.
<p>Valid values are 0 (no) and 1 (yes).</p></td>
</tr>
<tr class="odd">
<td>UINT32</td>
<td>The maximum supported Network Offload List size.</td>
</tr>
<tr class="even">
<td>UINT8</td>
<td>Specifies whether or not the adapter can track HESSIDs associated with SSIDs and connect/roam only to those APs that match the specified SSID+HESSID.
<p>Valid values are 0 (not supported) and 1 (supported).</p></td>
</tr>
<tr class="odd">
<td>UINT8</td>
<td>Specifies whether the adapter can offload connectivity to networks belonging to specific HESSIDs.</td>
</tr>
<tr class="even">
<td>UINT8</td>
<td>Specifies whether disconnected standby is supported.
<p>Valid values are 0 (not supported) and 1 (supported).</p></td>
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

 

 




