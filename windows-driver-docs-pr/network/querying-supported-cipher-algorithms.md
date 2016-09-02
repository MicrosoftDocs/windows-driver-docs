---
title: Querying Supported Cipher Algorithms
description: Querying Supported Cipher Algorithms
ms.assetid: 37f533f1-e3a8-4b61-bee3-f54be3a5a9a8
keywords: ["cipher operations WDK Native 802.11 , cipher algorithms", "algorithms WDK Native 802.11 cipher", "querying cipher algorithms"]
---

# Querying Supported Cipher Algorithms


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

When the miniport driver is operating in Extensible Station (ExtSTA) mode, the following object identifiers (OIDs) query the cipher algorithms that are supported by the 802.11 station.

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
<td align="left"><p>[OID_DOT11_SUPPORTED_UNICAST_ALGORITHM_PAIR](https://msdn.microsoft.com/library/windows/hardware/ff569430)</p></td>
<td align="left"><p>Queries the authentication and cipher algorithms supported for unicast packets sent or received by the 802.11 station.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_SUPPORTED_MULTICAST_ALGORITHM_PAIR](https://msdn.microsoft.com/library/windows/hardware/ff569424)</p></td>
<td align="left"><p>Queries the authentication and cipher algorithms supported for multicast or broadcast packets sent or received by the 802.11 station.</p></td>
</tr>
</tbody>
</table>

 

When these OIDs are queried, the miniport driver returns a list of supported cipher algorithms for each supported 802.11 authentication algorithm. For any authentication algorithm, the 802.11 station can support different cipher algorithms for unicast and multicast or broadcast packets.

The miniport driver only returns 802.11 authentication and cipher algorithms supported for the current desired basic service set (BSS) type, as specified through the value of the IEEE **dot11DesiredBSSType** management information base (MIB) object. For more information about this MIB object, see [OID\_DOT11\_DESIRED\_BSS\_TYPE](https://msdn.microsoft.com/library/windows/hardware/ff569142).

 

 





