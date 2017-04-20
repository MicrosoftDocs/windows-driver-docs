---
title: 802.11 PHY Configuration
description: 802.11 PHY Configuration
ms.assetid: 6cbe794f-0109-4772-ada7-3dc2bcea143f
keywords:
- PHY configuration WDK Native 802.11
- PHY configuration WDK Native 802.11 , about PHY miniport driver configuration
- configurations WDK Native 802.11 , PHY configuration
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# 802.11 PHY Configuration


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

The IEEE physical (PHY) layer of the Native 802.11 station is configured through a set of object identifiers (OIDs) that are based on 802.11 management information base (MIB) objects. For more information about the 802.11 MIB objects, refer to Annex D of the IEEE 802.11 standards listed in [Background Reading on 802.11](background-reading-on-802-11.md).

The following OIDs query the configuration for all types of PHYs.

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
<td align="left"><p>[OID_DOT11_CURRENT_TX_POWER_LEVEL](https://msdn.microsoft.com/library/windows/hardware/ff569138)</p></td>
<td align="left"><p>Queries the power level of the PHY.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_DIVERSITY_SELECTION_RX](https://msdn.microsoft.com/library/windows/hardware/ff569148)</p></td>
<td align="left"><p>Queries the list of antennas on the PHY that are available for receive (RX) diversity operations.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[OID_DOT11_DIVERSITY_SUPPORT](https://msdn.microsoft.com/library/windows/hardware/ff569149)</p></td>
<td align="left"><p>Queries the type of antenna diversity that is supported by the PHY.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_SUPPORTED_DATA_RATES_VALUE](https://msdn.microsoft.com/library/windows/hardware/ff569422)</p></td>
<td align="left"><p>Queries the transmit and receive data rates that are supported by the Physical Layer Convergence Procedure (PLCP) and Physical Media Dependent (PMD) sublayer of the PHY.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[OID_DOT11_SUPPORTED_POWER_LEVELS](https://msdn.microsoft.com/library/windows/hardware/ff569427)</p></td>
<td align="left"><p>Queries the number of transmit power levels that are supported by the PMD sublayer of the PHY.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_TEMP_TYPE](https://msdn.microsoft.com/library/windows/hardware/ff569431)</p></td>
<td align="left"><p>Queries the operating temperature range of the PHY.</p></td>
</tr>
</tbody>
</table>

 

The following topics describe PHY-specific configuration:

[DSSS, HRDSSS, and ERP PHY Configuration](dsss--hrdsss--and-erp-phy-configuration.md)
[OFDM PHY Configuration](ofdm-phy-configuration.md)
[FHSS PHY Configuration](fhss-phy-configuration.md)
[IR PHY Configuration](ir-phy-configuration.md)
[Automatic PHY Configuration](automatic-phy-configuration.md)
**Note**  When the miniport driver is operating in the Extensible Station (ExtSTA) mode, Native 802.11 OIDs that are used for PHY configurations affect the PHY on the 802.11 station that is referenced through the current PHY identifier (ID). The operating system sets or queries the current PHY ID through [OID\_DOT11\_CURRENT\_PHY\_ID](https://msdn.microsoft.com/library/windows/hardware/ff569135).

 

 

 





