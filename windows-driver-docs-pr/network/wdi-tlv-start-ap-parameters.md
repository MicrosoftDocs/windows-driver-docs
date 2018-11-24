---
title: WDI_TLV_START_AP_PARAMETERS
description: WDI_TLV_START_AP_PARAMETERS is a TLV that contains the parameters for OID_WDI_TASK_START_AP.
ms.assetid: 6791754C-9786-4BE4-9915-7333E4E0AFB8
ms.date: 07/18/2017
keywords:
 - WDI_TLV_START_AP_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_START\_AP\_PARAMETERS


WDI\_TLV\_START\_AP\_PARAMETERS is a TLV that contains the parameters for [OID\_WDI\_TASK\_START\_AP](https://msdn.microsoft.com/library/windows/hardware/dn925964).

## TLV Type


0xAB

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
<td>The beacon period. If non-zero, this parameter specifies the beacon interval.</td>
</tr>
<tr class="even">
<td>UINT32</td>
<td>The DTIM period. If non-zero, this parameter specifies the number of beacon intervals between transmissions of beacon frames that contain a TIM element with a DTIM Count field that equals zero. This value is transmitted in the DTIM Period field of beacon frames.</td>
</tr>
<tr class="odd">
<td>UINT8</td>
<td>This parameter sets the dot11ExcludeUnencrypted MIB. Valid values are 0 and 1.</td>
</tr>
<tr class="even">
<td>UINT8</td>
<td>This parameter specifies if the device supports 802.11b speeds. Valid values are 0 (not supported) and 1 (supported). When this value is set to 1, the access point should allow clients using 11b rates to connect to it.</td>
</tr>
<tr class="odd">
<td>UINT8</td>
<td>Added in Windows 10, version 1511, WDI version 1.0.10.
<p>This parameter specifies whether to allow legacy SoftAP clients to connect. Valid values are 0 (not allowed) and 1 (allowed).</p></td>
</tr>
<tr class="even">
<td>UINT8</td>
<td>Added in Windows 10, version 1511, WDI version 1.0.10.
<p>MustUseSpecifiedChannels. This parameter specifies whether the AP can only be started on the channels specified in <a href="https://msdn.microsoft.com/library/windows/hardware/dn925964" data-raw-source="[OID_WDI_TASK_START_AP](https://msdn.microsoft.com/library/windows/hardware/dn925964)">OID_WDI_TASK_START_AP</a> task parameters with <a href="wdi-tlv-ap-band-channel.md" data-raw-source="[&lt;strong&gt;WDI_TLV_AP_BAND_CHANNEL&lt;/strong&gt;](wdi-tlv-ap-band-channel.md)"><strong>WDI_TLV_AP_BAND_CHANNEL</strong></a>. Valid values are 0 and 1. If it is set to 1, the AP can only be started from the specified list. If it is not set, the list is meant to be a recommendation of channels that the firmware can pick from, and it may pick another channel if it is not possible to start the AP on any of the specified channels.</p></td>
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

## See also


[OID\_WDI\_TASK\_START\_AP](https://msdn.microsoft.com/library/windows/hardware/dn925964)

 

 




