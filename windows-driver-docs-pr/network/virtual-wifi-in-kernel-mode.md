---
title: Virtual WiFi in Kernel Mode
description: Virtual WiFi in Kernel Mode
ms.assetid: 6e1dca89-782e-46f9-acd2-5e7cf505be70
keywords:
- Virtual WiFi in kernel mode WDK networking
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Virtual WiFi in Kernel Mode


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

Virtual WiFi allows an 802.11 miniport driver to connect to, or host, multiple simultaneous connections on a single wireless interface. Beginning with Windows 7, an 802.11 miniport driver must support Virtual WiFi. You must compile or recompile the driver with the NTDDI\_VERSION macro set to &gt;= NTDDI\_WIN7. In addition, the driver must support NDIS version 6.20.

The following reference topics describe how an 802.11 miniport driver implements Virtual WiFi in kernel mode.

**Virtual WiFi OIDs**

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Object identifier (OID)</th>
<th align="left">Associated structure</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[OID_DOT11_CREATE_MAC](https://msdn.microsoft.com/library/windows/hardware/ff569124)</p></td>
<td align="left"><p>[<strong>DOT11_MAC_INFO</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548689)</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_DELETE_MAC](https://msdn.microsoft.com/library/windows/hardware/ff569140)</p></td>
<td align="left"><p>[<strong>DOT11_MAC_INFO</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548689)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[OID_DOT11_VIRTUAL_STATION_CAPABILITY](https://msdn.microsoft.com/library/windows/hardware/ff569435)</p></td>
<td align="left"><p>[<strong>DOT11_EXTSTA_ATTRIBUTES</strong>](https://msdn.microsoft.com/library/windows/hardware/ff547688)</p></td>
</tr>
</tbody>
</table>

 

**Structures**

[**DOT11\_VWIFI\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff548808)

[**DOT11\_VWIFI\_COMBINATION**](https://msdn.microsoft.com/library/windows/hardware/ff548810)

[**DOT11\_VWIFI\_COMBINATION\_V2**](https://msdn.microsoft.com/library/windows/hardware/ff548811)

[**DOT11\_VWIFI\_COMBINATION\_V3**](https://msdn.microsoft.com/library/windows/hardware/hh406568)

**Structure Member**

**VWiFiAttributes** member of the [**NDIS\_MINIPORT\_ADAPTER\_NATIVE\_802\_11\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565926) structure

For more details on how to implement Virtual WiFi in your 802.11 miniport driver, see the following topics:

[Virtual WiFi Initialization](virtual-wifi-initialization.md)

[Supported Virtualization Configurations](supported-virtualization-configurations.md)

[Virtual WiFi Implementation Guidelines](virtual-wifi-implementation-guidelines.md)

[INF File Settings for Virtual WiFi](inf-file-settings-for-virtual-wifi.md)

 

 





