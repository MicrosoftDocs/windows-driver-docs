---
title: Extensible Station Indications
description: Extensible Station Indications
ms.assetid: c261c877-f007-4dd6-9047-5d3a06517f84
keywords: ["ExtSTA status indications WDK Native 802.11", "Extensible Station status indications WDK Native 802.11"]
---

# Extensible Station Indications


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

The following table describes the Native 802.11 indications that are applicable to the Extensible Station (ExtSTA) operation mode of the Native 802.11 miniport driver. For more information about this operation mode, see [Extensible Station Operation Mode](extensible-station-operation-mode.md).

The miniport driver can only make these Native 802.11 indications from the operational (OP) state of the ExtSTA operation mode. For more information about this state, see [Extensible Station Operating States](extensible-station-operating-states.md).

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
<td align="left"><p>[NDIS_STATUS_DOT11_ASSOCIATION_COMPLETION](https://msdn.microsoft.com/library/windows/hardware/ff567319)</p></td>
<td align="left"><p>The driver makes this indication after the 802.11 station completes an association operation with an access point (AP) or peer station. For more information about this operation, see [Association Operations](association-operations.md).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[NDIS_STATUS_DOT11_ASSOCIATION_START](https://msdn.microsoft.com/library/windows/hardware/ff567321)</p></td>
<td align="left"><p>The driver makes this indication before the 802.11 station starts an association operation with an AP or peer station. For more information about this operation, see [Association Operations](association-operations.md).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[NDIS_STATUS_DOT11_CONNECTION_COMPLETION](https://msdn.microsoft.com/library/windows/hardware/ff567325)</p></td>
<td align="left"><p>The driver makes this indication after the 802.11 station completes a connection operation with a basic service set (BSS) network. For more information about this operation, see [Connection Operations](connection-operations.md).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[NDIS_STATUS_DOT11_CONNECTION_START](https://msdn.microsoft.com/library/windows/hardware/ff567328)</p></td>
<td align="left"><p>The driver makes this indication before the 802.11 station starts a connection operation with a BSS network. For more information about this operation, see [Connection Operations](connection-operations.md).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[NDIS_STATUS_DOT11_DISASSOCIATION](https://msdn.microsoft.com/library/windows/hardware/ff567334)</p></td>
<td align="left"><p>The driver makes this indication after the 802.11 station completes a disassociation operation with an AP or peer station. For more information about this operation, see [Disassociation Operations](disassociation-operations.md).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[NDIS_STATUS_DOT11_LINK_QUALITY](https://msdn.microsoft.com/library/windows/hardware/ff567344)</p></td>
<td align="left"><p>The driver makes this indication whenever the 802.11 station determines the link quality for an association with an AP or peer station that has changed significantly.</p>
<p>For more information about link quality and link quality indications, see [Link Quality Operations](link-quality-operations.md).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[NDIS_STATUS_DOT11_PHY_STATE_CHANGED](https://msdn.microsoft.com/library/windows/hardware/ff567354)</p></td>
<td align="left"><p>The driver makes this indication whenever the power state changes on a PHY that is supported by the 802.11 station.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[NDIS_STATUS_DOT11_PMKID_CANDIDATE_LIST](https://msdn.microsoft.com/library/windows/hardware/ff567355)</p></td>
<td align="left"><p>The driver makes this indication to request pairwise master key identifiers (PMKIDs) for BSSIDs to which the 802.11 station can potentially roam.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[NDIS_STATUS_DOT11_ROAMING_COMPLETION](https://msdn.microsoft.com/library/windows/hardware/ff567359)</p></td>
<td align="left"><p>The driver makes this indication after the 802.11 station completes a roaming operation with an AP or peer station. For more information about this operation, see [Roaming Operations](roaming-operations.md).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[NDIS_STATUS_DOT11_ROAMING_START](https://msdn.microsoft.com/library/windows/hardware/ff567360)</p></td>
<td align="left"><p>The driver makes this indication before the 802.11 station starts a roaming operation with an AP or peer station. For more information about this operation, see [Roaming Operations](roaming-operations.md).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[NDIS_STATUS_DOT11_TKIPMIC_FAILURE](https://msdn.microsoft.com/library/windows/hardware/ff567368)</p></td>
<td align="left"><p>The driver makes this indication whenever a received packet that has been successfully decrypted by the TKIP cipher algorithm fails the message integrity code (MIC) verification.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NDIS_STATUS_MEDIA_SPECIFIC_INDICATION</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567399)</p></td>
<td align="left"><p>The driver makes this indication to notify the IHV Extension DLL. For more information, see [IHV-Specific Indications](ihv-specific-indications.md).</p></td>
</tr>
</tbody>
</table>

 

 

 





