---
title: FHSS PHY Configuration
description: FHSS PHY Configuration
ms.assetid: c8fa2942-3ace-4961-9870-f7837cd1145a
keywords:
- PHY configuration WDK Native 802.11 , frequency-hopping spread spectrum
- frequency-hopping spread spectrum WDK Native 802.11
- FHSS WDK Native 802.11
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# FHSS PHY Configuration


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

The following object identifiers (OIDs) set or query the configuration of the frequency-hopping spread spectrum (FHSS) PHY.

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
<td align="left"><p>[OID_DOT11_CURRENT_CHANNEL_NUMBER](https://msdn.microsoft.com/library/windows/hardware/ff569128)</p></td>
<td align="left"><p>Queries the current channel number used by the physical media dependent (PMD) sublayer of the PHY for transmit and receive operations.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_CURRENT_DWELL_TIME](https://msdn.microsoft.com/library/windows/hardware/ff569129)</p></td>
<td align="left"><p>Queries the amount of time that the PHY can use when transmitting on a single channel.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[OID_DOT11_CURRENT_INDEX](https://msdn.microsoft.com/library/windows/hardware/ff569131)</p></td>
<td align="left"><p>Queries the current index in the hop pattern that the layer management entity (LME) of the PHY uses to determine the current channel number.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_CURRENT_PATTERN](https://msdn.microsoft.com/library/windows/hardware/ff569134)</p></td>
<td align="left"><p>Queries the current hopping pattern used by the LME of the PHY to determine the hopping sequence.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[OID_DOT11_CURRENT_SET](https://msdn.microsoft.com/library/windows/hardware/ff569137)</p></td>
<td align="left"><p>Queries the current set of patterns used by the LME of the PHY to determine the hopping sequence.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_EHCC_CAPABILITY_ENABLED](https://msdn.microsoft.com/library/windows/hardware/ff569154)</p></td>
<td align="left"><p>Queries whether the PHY is capable of enabling the hyperbolic congruence codes (HCC) or extended hyperbolic congruence codes (EHCC) algorithms to generate hopping patterns.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[OID_DOT11_EHCC_CAPABILITY_IMPLEMENTED](https://msdn.microsoft.com/library/windows/hardware/ff569155)</p></td>
<td align="left"><p>Queries whether the PHY is capable of generating hopping patterns through the HCC or EHCC algorithms.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_EHCC_NUMBER_OF_CHANNELS_FAMILY_INDEX](https://msdn.microsoft.com/library/windows/hardware/ff569156)</p></td>
<td align="left"><p>Queries the maximum value of the family index in the HCC or EHCC algorithms.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[OID_DOT11_EHCC_PRIME_RADIX](https://msdn.microsoft.com/library/windows/hardware/ff569355)</p></td>
<td align="left"><p>Queries the prime radix value for the HCC or EHCC algorithms.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_HOP_ALGORITHM_ADOPTED](https://msdn.microsoft.com/library/windows/hardware/ff569373)</p></td>
<td align="left"><p>Queries the type of algorithm that generates the hopping patterns used by the PHY.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[OID_DOT11_HOP_MODULUS](https://msdn.microsoft.com/library/windows/hardware/ff569374)</p></td>
<td align="left"><p>Queries the number of channels for the hopping set used by PHY.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_HOP_OFFSET](https://msdn.microsoft.com/library/windows/hardware/ff569375)</p></td>
<td align="left"><p>Queries the next position in the hopping set used by the PHY.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[OID_DOT11_HOP_TIME](https://msdn.microsoft.com/library/windows/hardware/ff569376)</p></td>
<td align="left"><p>Queries the time, in microseconds, that the PMD sublayer of the PHY requires to change from channel 2 to channel 80.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_HOPPING_PATTERN](https://msdn.microsoft.com/library/windows/hardware/ff569372)</p></td>
<td align="left"><p>Queries the list of hopping patterns used by the PHY.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[OID_DOT11_MAX_DWELL_TIME](https://msdn.microsoft.com/library/windows/hardware/ff569383)</p></td>
<td align="left"><p>Queries the maximum time that the PHY operates on a single channel when the 802.11 station is transmitting data.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_NUMBER_OF_HOPPING_SETS](https://msdn.microsoft.com/library/windows/hardware/ff569394)</p></td>
<td align="left"><p>Queries the total number of sets of hopping patterns used by the PHY.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[OID_DOT11_RANDOM_TABLE_FLAG](https://msdn.microsoft.com/library/windows/hardware/ff569406)</p></td>
<td align="left"><p>Queries whether the PHY uses hopping patterns from the Random Table field of the Hopping Pattern Table information element (IE).</p></td>
</tr>
</tbody>
</table>

 

 

 





