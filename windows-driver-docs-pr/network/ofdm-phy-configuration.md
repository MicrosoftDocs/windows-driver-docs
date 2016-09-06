---
title: OFDM PHY Configuration
description: OFDM PHY Configuration
ms.assetid: 0ec458c2-1427-44d7-a1a4-f70b1d73fbb4
keywords: ["PHY configuration WDK Native 802.11 , orthogonal frequency division multiplexing", "orthogonal frequency division multiplexing WDK Native 802.11", "OFDM WDK Native 802.11"]
---

# OFDM PHY Configuration


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

The following object identifiers (OIDs) set or query the configuration of the orthogonal frequency division multiplexing (OFDM) PHY.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Name</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[OID_DOT11_CURRENT_FREQUENCY](https://msdn.microsoft.com/library/windows/hardware/ff569130)</p></td>
<td align="left"><p>Sets or queries the frequency channel that is currently used by the PHY.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_FREQUENCY_BANDS_SUPPORTED](https://msdn.microsoft.com/library/windows/hardware/ff569369)</p></td>
<td align="left"><p>Queries the unlicensed national information infrastructure (U-NII) bands in which the PHY is capable of operating.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[OID_DOT11_TI_THRESHOLD](https://msdn.microsoft.com/library/windows/hardware/ff569432)</p></td>
<td align="left"><p>Queries the TI threshold used by the PHY to detect a busy media.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_SUPPORTED_OFDM_FREQUENCY_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569425)</p></td>
<td align="left"><p>Queries the list of channel center frequencies that the 802.11 station can operate with.</p></td>
</tr>
</tbody>
</table>

 

 

 





