---
title: Enabling Cipher Algorithms
description: Enabling Cipher Algorithms
ms.assetid: 5e949b8b-1262-4dbf-8e72-c0b6d7d93d33
keywords:
- cipher operations WDK Native 802.11 , cipher algorithms
- algorithms WDK Native 802.11 cipher
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Enabling Cipher Algorithms


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

When the miniport driver is operating in Extensible Station (ExtSTA) mode, the following object identifiers (OIDs) set or query the cipher algorithms that are enabled on the 802.11 station.

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
<td align="left"><p>[OID_DOT11_ENABLED_UNICAST_CIPHER_ALGORITHM](https://msdn.microsoft.com/library/windows/hardware/ff569358)</p></td>
<td align="left"><p>Sets or queries the cipher algorithms enabled for unicast packets sent or received by the 802.11 station.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_ENABLED_MULTICAST_CIPHER_ALGORITHM](https://msdn.microsoft.com/library/windows/hardware/ff569357)</p></td>
<td align="left"><p>Sets or queries the cipher algorithms supported for multicast or broadcast packets that are sent or received by the 802.11 station.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[OID_DOT11_UNICAST_USE_GROUP_ENABLED](https://msdn.microsoft.com/library/windows/hardware/ff569433)</p></td>
<td align="left"><p>Sets or queries the support for the &quot;Use Group Key&quot; cipher suite. For more information about the &quot;Use Group Key&quot; cipher suite, refer to Clause 7.3.2.9.1 of the IEEE 802.11i-2004 standard.</p></td>
</tr>
</tbody>
</table>

 

**Note** Set requests of these OIDs can only be made while the miniport driver is in the initialization (INIT) state of the ExtSTA operation mode. For more information about this state, see [Extensible Station Operating States](extensible-station-operating-states.md).

When [OID\_DOT11\_CONNECT\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569122) is set, the 802.11 station only attempts to connect to a BSS network whose 802.11 Beacon or Probe Response frames specify support for any of the enabled authentication algorithms, unicast and multicast or broadcast cipher algorithms. For more information about the connection operation, see [Connection Operations](connection-operations.md).

 

 





