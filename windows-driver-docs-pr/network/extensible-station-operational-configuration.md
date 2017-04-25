---
title: Extensible Station Operational Configuration
description: Extensible Station Operational Configuration
ms.assetid: a06b7cbc-5ee3-4557-bbf8-048b2823bd84
keywords:
- configurations WDK Native 802.11 , Extensible Station mode
- Extensible Station operational configuration WDK Native 802.11
- ExtSTA operational configuration WDK Native 802.11
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Extensible Station Operational Configuration


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

The following object identifiers (OIDs) set or query the operating attributes of the Native 802.11 miniport driver that operates in the Extensible Station (ExtSTA) mode.

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
<td align="left"><p>[OID_DOT11_ACTIVE_PHY_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569102)</p></td>
<td align="left"><p>Queries the list of PHYs on the 802.11 station that can be used for transmitting and receiving packets over the current basic service set (BSS) connection.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_AUTO_CONFIG_ENABLED](https://msdn.microsoft.com/library/windows/hardware/ff569106)</p></td>
<td align="left"><p>Sets or queries the automatic mode for the media access control (MAC) or PHY configuration</p>
<p>For more information about these configuration modes, see [Automatic MAC Configuration](automatic-mac-configuration.md) and [Automatic PHY Configuration](automatic-phy-configuration.md).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[OID_DOT11_CURRENT_PHY_ID](https://msdn.microsoft.com/library/windows/hardware/ff569135)</p></td>
<td align="left"><p>Sets or queries the PHY identifier (ID) that the miniport driver uses when PHY-layer OIDs are set or queried. For more information about PHY-layer OIDs, see [802.11 PHY Configuration](802-11-phy-configuration.md).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_DESIRED_PHY_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569144)</p></td>
<td align="left"><p>Sets or queries the list of PHY IDs that the 802.11 station uses when connecting to and operating in a BSS.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[OID_DOT11_EXTSTA_CAPABILITY](https://msdn.microsoft.com/library/windows/hardware/ff569366)</p></td>
<td align="left"><p>Queries the sizes of various tables and lists supported by the 802.11 station.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_HARDWARE_PHY_STATE](https://msdn.microsoft.com/library/windows/hardware/ff569370)</p></td>
<td align="left"><p>Queries the power state of the current PHY type on the 802.11 station. The current PHY type is determined through a query of [OID_DOT11_CURRENT_PHY_ID](https://msdn.microsoft.com/library/windows/hardware/ff569135).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[OID_DOT11_MEDIA_STREAMING_ENABLED](https://msdn.microsoft.com/library/windows/hardware/ff569386)</p></td>
<td align="left"><p>Sets or queries the current setting of media streaming on the 802.11 station. For more information about media streaming, see [Native 802.11 Media Streaming](native-802-11-media-streaming.md).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_STATISTICS](https://msdn.microsoft.com/library/windows/hardware/ff569420)</p></td>
<td align="left"><p>Queries statistics gathered by the miniport driver for the IEEE 802.11 interface. For more information about 802.11 statistics, see [Native 802.11 Statistics](native-802-11-statistics.md).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[OID_DOT11_UNREACHABLE_DETECTION_THRESHOLD](https://msdn.microsoft.com/library/windows/hardware/ff569434)</p></td>
<td align="left"><p>Sets or queries the maximum amount of time before the 802.11 station determines that it has lost connectivity to an access point (AP) or peer station.</p></td>
</tr>
</tbody>
</table>

 

When the miniport driver is operating in the ExtSTA mode, it requires configuration for the following operations:

-   802.11 network operations within a basic service set (BSS) network. For more information about the configuration requirements for this operation, see [Native 802.11 Network Operations](native-802-11-network-operations.md).
-   802.11 authentication operations. For more information about the configuration requirements for this operation, see [Native 802.11 Authentication Operations](native-802-11-authentication-operations.md).
-   802.11 cipher operations. For more information about the configuration requirements for this operation, see [Native 802.11 Cipher Operations](native-802-11-cipher-operations.md).

 

 





