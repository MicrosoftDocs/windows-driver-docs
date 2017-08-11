---
title: WDI_TLV_PM_CAPABILITIES (0x42)
author: windows-driver-content
description: WDI_TLV_PM_CAPABILITIES is a TLV that contains power management capabilities.
ms.assetid: DE8A5333-BE2B-4CBB-8C75-45ABBE35A635
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - WDI_TLV_PM_CAPABILITIES (0x42) Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_PM\_CAPABILITIES (0x42)


WDI\_TLV\_PM\_CAPABILITIES is a TLV that contains power management capabilities.

## TLV Type


0x42

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>UINT32</td>
<td>Specifies the power management supported flags.
<p>Valid flags are:</p>
<ul>
<li>NDIS_PM_WAKE_PACKET_INDICATION_SUPPORTED</li>
<li>NDIS_PM_SELECTIVE_SUSPEND_SUPPORTED (0x00000002)</li>
</ul></td>
</tr>
<tr class="even">
<td>UINT32</td>
<td>Specifies the supported Wake-on-LAN patterns.
<p>Valid patterns are:</p>
<ul>
<li>NDIS_PM_WOL_BITMAP_PATTERN_SUPPORTED (0x00000001)</li>
<li>NDIS_PM_WOL_MAGIC_PACKET_SUPPORTED (0x00000002)</li>
<li>NDIS_PM_WOL_IPV4_TCP_SYN_SUPPORTED (0x00000004)</li>
<li>NDIS_PM_WOL_IPV6_TCP_SYN_SUPPORTED (0x00000008)</li>
<li>NDIS_PM_WOL_IPV4_DEST_ADDR_WILDCARD_SUPPORTED (0x00000200)</li>
<li>NDIS_PM_WOL_IPV6_DEST_ADDR_WILDCARD_SUPPORTED (0x00000800)</li>
<li>NDIS_PM_WOL_EAPOL_REQUEST_ID_MESSAGE_SUPPORTED (0x00010000)</li>
</ul></td>
</tr>
<tr class="odd">
<td>UINT32</td>
<td>Specifies the total number of Wake-on-LAN patterns.</td>
</tr>
<tr class="even">
<td>UINT32</td>
<td>Specifies the maximum Wake-on-LAN pattern size.</td>
</tr>
<tr class="odd">
<td>UINT32</td>
<td>Specifies the maximum Wake-on-LAN pattern offset.</td>
</tr>
<tr class="even">
<td>UINT32</td>
<td>Specifies the maximum Wake-on-LAN packet save buffer.</td>
</tr>
<tr class="odd">
<td>UINT32</td>
<td>Specifies the supported protocol offloads.
<p>Valid offloads are:</p>
<ul>
<li>NDIS_PM_PROTOCOL_OFFLOAD_ARP_SUPPORTED (0x00000001)</li>
<li>NDIS_PM_PROTOCOL_OFFLOAD_NS_SUPPORTED (0x00000002)</li>
<li>NDIS_PM_PROTOCOL_OFFLOAD_80211_RSN_REKEY_SUPPORTED (0x00000080)</li>
</ul></td>
</tr>
<tr class="even">
<td>UINT32</td>
<td>Specifies the number of ARP offload IPv4 addresses.</td>
</tr>
<tr class="odd">
<td>UINT32</td>
<td>Specifies the number of NS offload IPv6 addresses.</td>
</tr>
<tr class="even">
<td>[<strong>NDIS_DEVICE_POWER_STATE</strong>](https://msdn.microsoft.com/library/windows/hardware/gg602135)</td>
<td>Specifies the minimum magic packet wake-up.</td>
</tr>
<tr class="odd">
<td>[<strong>NDIS_DEVICE_POWER_STATE</strong>](https://msdn.microsoft.com/library/windows/hardware/gg602135)</td>
<td>Specifies the minimum pattern wake-up.</td>
</tr>
<tr class="even">
<td>[<strong>NDIS_DEVICE_POWER_STATE</strong>](https://msdn.microsoft.com/library/windows/hardware/gg602135)</td>
<td>Specifies the minimum link change wake-up.</td>
</tr>
<tr class="odd">
<td>UINT32</td>
<td>Specifies the supported wake-up events.
<p>Valid events are:</p>
<ul>
<li>NDIS_PM_WAKE_ON_MEDIA_CONNECT_SUPPORTED (0x00000001)</li>
<li>NDIS_PM_WAKE_ON_MEDIA_DISCONNECT_SUPPORTED (0x00000002)</li>
</ul></td>
</tr>
<tr class="even">
<td>UINT32</td>
<td>Specifies the media-specific wake-up events.
<p>Valid events are:</p>
<ul>
<li>NDIS_WLAN_WAKE_ON_NLO_DISCOVERY_SUPPORTED (0x00000001)</li>
<li>NDIS_WLAN_WAKE_ON_AP_ASSOCIATION_LOST_SUPPORTED (0x00000002)</li>
<li>NDIS_WLAN_WAKE_ON_GTK_HANDSHAKE_ERROR_SUPPORTED (0x00000004)</li>
<li>NDIS_WLAN_WAKE_ON_4WAY_HANDSHAKE_REQUEST_SUPPORTED (0x00000008)</li>
</ul></td>
</tr>
</tbody>
</table>

 

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Minimum supported client</p></td>
<td><p>Windows 10</p></td>
</tr>
<tr class="even">
<td><p>Minimum supported server</p></td>
<td><p>Windows Server 2016</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Wditypes.hpp</td>
</tr>
</tbody>
</table>

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20WDI_TLV_PM_CAPABILITIES%20%280x42%29%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


