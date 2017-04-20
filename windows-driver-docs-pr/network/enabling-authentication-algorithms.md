---
title: Enabling Authentication Algorithms
description: Enabling Authentication Algorithms
ms.assetid: 4ff435fc-6644-4571-9599-33a154af3899
keywords:
- algorithms WDK Native 802.11 authentication
- authentication WDK Native 802.11 , algorithms
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Enabling Authentication Algorithms


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

When the miniport driver is operating in Extensible Station (ExtSTA) mode, the following object identifiers (OIDs) set or query the authentication algorithms that are enabled on the 802.11 station.

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
<td align="left"><p>[OID_DOT11_ENABLED_AUTHENTICATION_ALGORITHM](https://msdn.microsoft.com/library/windows/hardware/ff569356)</p></td>
<td align="left"><p>Sets or queries the authentication algorithms that are enabled on the 802.11 station.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_PMKID_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569400)</p></td>
<td align="left"><p>Sets or queries the list of pairwise master key identifiers (PMKIDs) that are used by the 802.11 station for RSNA preauthentication.</p></td>
</tr>
</tbody>
</table>

 

**Note**  Set requests of these OIDs can only be made while the miniport driver is in the initialization (INIT) state of the ExtSTA operation mode. For more information about this state, see [Extensible Station Operating States](extensible-station-operating-states.md).

 

When [OID\_DOT11\_CONNECT\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569122) is set, the 802.11 station only attempts to connect to a BSS network whose 802.11 Beacon or Probe Response frames specify support for any of the enabled authentication algorithms and unicast and multicast or broadcast cipher algorithms. For more information about the connection operation, see [Connection Operations](connection-operations.md).

 

 





