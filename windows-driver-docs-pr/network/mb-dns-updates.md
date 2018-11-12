---
title: MB DNS Updates
description: MB DNS Updates
ms.assetid: be93f0b4-a075-455e-b03c-6d23a2be7b1d
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# MB DNS Updates


This topic describes the operations to notify the MB Service about DNS address updates.

Miniport drivers should set the **NameServer** registry key to update Windows about DNS address changes. The following table describes the appropriate registry key, the expected value and an example string for IPv4 and IPv6 networks. If a miniport driver supports only IPv4 networks, it should set only the IPv4 registry key. Miniport drivers should set the appropriate registry key(s) before they notify Windows about media connect events by sending [**NDIS\_STATUS\_LINK\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff567391) notifications.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">IPv4 / IPv6</th>
<th align="left">Registry Key</th>
<th align="left">Value</th>
<th align="left">Example</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>IPv4</p></td>
<td align="left"><p>HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces\InterfaceGUID\NameServer</p></td>
<td align="left"><p>Space-separated DNS server IPv4 addresses</p></td>
<td align="left"><p>10.20.30.41</p>
<p>10.20.30.40</p></td>
</tr>
<tr class="even">
<td align="left"><p>IPv6</p></td>
<td align="left"><p>HKLM\SYSTEM\CurrentControlSet\Services\Tcpip6\Parameters\Interfaces\InterfaceGUID\NameServer</p></td>
<td align="left"><p>Space-separated DNS server IPv6 addresses</p></td>
<td align="left"><p>2001:4898:7001:f000:1:2:3:4</p>
<p>2001:4898:7001:f000:1:2:3:5</p></td>
</tr>
</tbody>
</table>

 

These operations should be used only when the miniport driver specifies **EnableDhcp** to equal zero in its INF file. That is, the miniport driver does not implement DHCP.

For more information about processing IP address notifications, see [Guidelines for MB Miniport driver IP Address Notifications](guidelines-for-mb-miniport-driver-ip-address-notifications.md).

 

 





