---
title: WDI_TLV_START_AP_PARAMETERS
author: windows-driver-content
description: WDI_TLV_START_AP_PARAMETERS is a TLV that contains the parameters for OID_WDI_TASK_START_AP.
ms.assetid: 6791754C-9786-4BE4-9915-7333E4E0AFB8
ms.author: windowsdriverdev 
ms.date: 0718/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - WDI_TLV_START_AP_PARAMETERS Network Drivers Starting with Windows Vista
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
<p>MustUseSpecifiedChannels. This parameter specifies whether the AP can only be started on the channels specified in [OID_WDI_TASK_START_AP](https://msdn.microsoft.com/library/windows/hardware/dn925964) task parameters with [<strong>WDI_TLV_AP_BAND_CHANNEL</strong>](wdi-tlv-ap-band-channel.md). Valid values are 0 and 1. If it is set to 1, the AP can only be started from the specified list. If it is not set, the list is meant to be a recommendation of channels that the firmware can pick from, and it may pick another channel if it is not possible to start the AP on any of the specified channels.</p></td>
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20WDI_TLV_START_AP_PARAMETERS%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


