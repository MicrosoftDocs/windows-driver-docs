---
title: DSSS, HRDSSS, and ERP PHY Configuration
description: DSSS, HRDSSS, and ERP PHY Configuration
ms.assetid: 925da6fc-af14-4af9-bc11-4da8c4cf6a80
keywords: ["PHY configuration WDK Native 802.11 , direct-sequence spread spectrum", "PHY configuration WDK Native 802.11 , high-rate DSSS", "PHY configuration WDK Native 802.11 , extended rate PHY", "direct-sequence spread spectrum WDK Native 802.11", "DSSS WDK Native 802.11", "high-rate DSSS WDK Native 802.11", "HRDSSS WDK Native 802.11", "extended rate PHY WDK Native 802.11", "ERP WDK Native 802.11"]
---

# DSSS, HRDSSS, and ERP PHY Configuration


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

The following object identifiers (OIDs) query the configuration of the:

-   Direct-sequence spread spectrum (DSSS) PHY.

-   High-rate DSSS (HRDSSS) PHY.

-   Extended rate PHY (ERP).

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Name</th>
<th align="left">DSSS PHY</th>
<th align="left">HRDSSS PHY</th>
<th align="left">ERP PHY</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[OID_DOT11_CCA_MODE_SUPPORTED](https://msdn.microsoft.com/library/windows/hardware/ff569110)</p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>Queries the types of clear channel assessment (CCA) modes supported by the PHY.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_CHANNEL_AGILITY_ENABLED](https://msdn.microsoft.com/library/windows/hardware/ff569117)</p></td>
<td align="left"></td>
<td align="left"><p>X</p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>Queries whether the PHY has enabled channel agility.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[OID_DOT11_CHANNEL_AGILITY_PRESENT](https://msdn.microsoft.com/library/windows/hardware/ff569118)</p></td>
<td align="left"></td>
<td align="left"><p>X</p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>Queries whether the PHY supports channel agility.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_CURRENT_CCA_MODE](https://msdn.microsoft.com/library/windows/hardware/ff569126)</p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>Queries the current CCA mode in use by the PHY.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[OID_DOT11_DSSS_OFDM_OPTION_ENABLED](https://msdn.microsoft.com/library/windows/hardware/ff569150)</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>X</p></td>
<td align="left"><p>Queries whether the PHY has enabled the use of the hybrid DSSS-OFDM modulation.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_DSSS_OFDM_OPTION_IMPLEMENTED](https://msdn.microsoft.com/library/windows/hardware/ff569151)</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>X</p></td>
<td align="left"><p>Queries whether the PHY supports the use of the hybrid DSSS-OFDM modulation.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[OID_DOT11_ED_THRESHOLD](https://msdn.microsoft.com/library/windows/hardware/ff569153)</p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>Queries the energy detect (ED) threshold of the PHY.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_ERP_PBCC_OPTION_ENABLED](https://msdn.microsoft.com/library/windows/hardware/ff569362)</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>X</p></td>
<td align="left"><p>Queries whether the ERP PHY has enabled packet binary convolutional code (PBCC) modulation.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[OID_DOT11_ERP_PBCC_OPTION_IMPLEMENTED](https://msdn.microsoft.com/library/windows/hardware/ff569363)</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>X</p></td>
<td align="left"><p>Queries whether the ERP PHY supports PBCC modulation.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_HR_CCA_MODE_SUPPORTED](https://msdn.microsoft.com/library/windows/hardware/ff569377)</p></td>
<td align="left"></td>
<td align="left"><p>X</p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>Queries the type of CCA mode that is used by the high-rate (HR) PHY.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[OID_DOT11_PBCC_OPTION_IMPLEMENTED](https://msdn.microsoft.com/library/windows/hardware/ff569398)</p></td>
<td align="left"></td>
<td align="left"><p>X</p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>Queries whether the PHY supports PBCC modulation.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_SHORT_PREAMBLE_OPTION_IMPLEMENTED](https://msdn.microsoft.com/library/windows/hardware/ff569414)</p></td>
<td align="left"></td>
<td align="left"><p>X</p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>Queries whether the PHY supports the short Physical Layer Convergence Procedure (PLCP) preamble and header.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[OID_DOT11_SHORT_SLOT_TIME_OPTION_ENABLED](https://msdn.microsoft.com/library/windows/hardware/ff569416)</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>X</p></td>
<td align="left"><p>Queries whether the PHY supports the 802.11g short slot time option.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_SHORT_SLOT_TIME_OPTION_IMPLEMENTED](https://msdn.microsoft.com/library/windows/hardware/ff569417)</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>X</p></td>
<td align="left"><p>Queries whether the PHY has enabled the 802.11g short slot time option.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[OID_DOT11_SUPPORTED_DSSS_CHANNEL_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569423)</p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>Queries the list of frequency channels that the 802.11 station can operate with.</p></td>
</tr>
</tbody>
</table>

 

 

 





