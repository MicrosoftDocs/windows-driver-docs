---
title: IR PHY Configuration
description: IR PHY Configuration
ms.assetid: 985d3334-e4cf-479a-b070-328c151989e4
keywords:
- PHY configuration WDK Native 802.11 , infrared
- infrared PHY WDK Native 802.11
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# IR PHY Configuration


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

The following object identifiers (OIDs) query the configuration of the clear channel assessment (CCA) mechanism of the infrared (IR) PHY. For more information about CCA, refer to Clause 16.4.8.5 of the IEEE 802.11-2012 standard.

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
<td align="left"><p>[OID_DOT11_CCA_WATCHDOG_COUNT_MAX](https://msdn.microsoft.com/library/windows/hardware/ff569112)</p></td>
<td align="left"><p>Queries when the PHY can ignore energy detected on the channel through the CCA mechanism.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_CCA_WATCHDOG_COUNT_MIN](https://msdn.microsoft.com/library/windows/hardware/ff569113)</p></td>
<td align="left"><p>Queries the minimum allowed value for the IEEE 802.11 <strong>dot11CCAWatchdogCountMax</strong> management information base (MIB) object. For more information about this MIB object, see [OID_DOT11_CCA_WATCHDOG_COUNT_MAX](https://msdn.microsoft.com/library/windows/hardware/ff569112).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[OID_DOT11_CCA_WATCHDOG_TIMER_MAX](https://msdn.microsoft.com/library/windows/hardware/ff569114)</p></td>
<td align="left"><p>Queries when the PHY can ignore energy detected in the channel through the CCA mechanism.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_CCA_WATCHDOG_TIMER_MIN](https://msdn.microsoft.com/library/windows/hardware/ff569115)</p></td>
<td align="left"><p>Queries the minimum allowed value for the IEEE 802.11 <strong>dot11CCAWatchdogTimerMax</strong> MIB object. For more information about this MIB object, see [OID_DOT11_CCA_WATCHDOG_TIMER_MAX](https://msdn.microsoft.com/library/windows/hardware/ff569114).</p></td>
</tr>
</tbody>
</table>

 

 

 





