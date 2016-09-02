---
title: Radio Power Management
description: Radio Power Management
ms.assetid: 2e788ea6-2d4a-455a-b462-d21a69a8f235
keywords: ["power management WDK Native 802.11 miniport , radio", "radio power management WDK Native 802.11 miniport"]
---

# Radio Power Management


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

The power state of the radio on the 802.11 NIC is controlled through:

-   A software setting for a Native 802.11 object identifier (OID).

-   A hardware setting, if present, on the NIC.

The following table defines the relationship between software and hardware settings on the NIC's radio power state.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Hardware setting</th>
<th align="left">Software setting</th>
<th align="left">Radio power state</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Enabled</p></td>
<td align="left"><p>Enabled</p></td>
<td align="left"><p>On</p></td>
</tr>
<tr class="even">
<td align="left"><p>Enabled</p></td>
<td align="left"><p>Disabled</p></td>
<td align="left"><p>Off</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Disabled</p></td>
<td align="left"><p>Enabled</p></td>
<td align="left"><p>Off</p></td>
</tr>
<tr class="even">
<td align="left"><p>Disabled</p></td>
<td align="left"><p>Disabled</p></td>
<td align="left"><p>Off</p></td>
</tr>
</tbody>
</table>

 

The following topics describe the methods for setting and querying radio power states:

[Querying Radio Power States](querying-radio-power-states.md)

[Setting Radio Power States](setting-radio-power-states.md)

 

 





