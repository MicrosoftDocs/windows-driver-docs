---
title: General Native 802.11 Indications
description: General Native 802.11 Indications
ms.assetid: d82ba0d3-d7c9-4f35-8d4b-4296257e19e7
keywords:
- general status indications WDK Native 802.11
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# General Native 802.11 Indications


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

The following table describes the Native 802.11 indications that are common to all operation modes of the Native 802.11 miniport driver. For more information about operation modes, see [Native 802.11 Operation Modes](native-802-11-operation-modes.md).

The miniport driver can make these Native 802.11 indications from the initialization (INIT) or operational (OP) states of the Native 802.11 mode from which it is operating. For more information about these states, see [Native 802.11 Operating States](native-802-11-operating-states.md).

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
<td align="left"><p>[NDIS_STATUS_DOT11_MPDU_MAX_LENGTH_CHANGED](https://msdn.microsoft.com/library/windows/hardware/ff567348)</p></td>
<td align="left"><p>The driver makes this indication after the maximum MAC protocol data unit (MPDU) frame size is changed for a PHY on the 802.11 station.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[NDIS_STATUS_DOT11_SCAN_CONFIRM](https://msdn.microsoft.com/library/windows/hardware/ff567364)</p></td>
<td align="left"><p>The driver makes this indication upon completion of an explicit scan operation initiated through a set of [OID_DOT11_SCAN_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569413).</p></td>
</tr>
</tbody>
</table>

 

 

 





