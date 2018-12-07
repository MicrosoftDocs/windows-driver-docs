---
title: Porting Packet-Processing Drivers and Apps to WFP
description: Windows Filtering Platform (WFP) enables TCP/IP packet filtering, inspection, and modification, connection monitoring or authorization, IPsec rules and processing, and RPC filtering.
ms.assetid: 9BB77BB8-1382-4F65-A4E8-80E229F43425
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting Packet-Processing Drivers and Apps to WFP


Windows Filtering Platform (WFP) enables TCP/IP packet filtering, inspection, and modification, connection monitoring or authorization, IPsec rules and processing, and RPC filtering. Generally, you must convert your TCP/IP filtering or connection monitoring component in Windows XP and Windows Server 2003 to use a WFP user-mode application or service, a WFP kernel-mode callout driver, or both for Windows Vista and Windows Server 2008 and later. The following table lists the existing methods for packet processing in Windows XP and Windows Server 2003 and how you must change them in Windows Vista and Windows Server 2008 and later to use WFP.

**Note**  As of Windows 8, the Transport Driver Interface (TDI) feature and Layered Service Providers (LSPs) feature are deprecated.

 

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Existing method in Windows XPand Windows Server 2003</th>
<th align="left">New method in Windows Vista and Windows Server 2008 and later</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">Firewall hook or filter hook driver for simple packet filtering.</td>
<td align="left">User-mode application or service that uses the <a href="https://msdn.microsoft.com/library/windows/desktop/aa366510" data-raw-source="[WFP Win32 API](https://msdn.microsoft.com/library/windows/desktop/aa366510)">WFP Win32 API</a>.</td>
</tr>
<tr class="even">
<td align="left">Firewall hook or filter hook driver for deep packet inspection or modification.</td>
<td align="left">IP layer, Transport layer, or Application Layer Enforcement (ALE) layer callout driver and optional user-mode application or service that uses the <a href="https://msdn.microsoft.com/library/windows/desktop/aa366510" data-raw-source="[WFP Win32 API](https://msdn.microsoft.com/library/windows/desktop/aa366510)">WFP Win32 API</a>.</td>
</tr>
<tr class="odd">
<td align="left">Transport Driver Interface (TDI) filter driver for simple packet filtering.</td>
<td align="left">User-mode application or service that uses the <a href="https://msdn.microsoft.com/library/windows/desktop/aa366510" data-raw-source="[WFP Win32 API](https://msdn.microsoft.com/library/windows/desktop/aa366510)">WFP Win32 API</a>.</td>
</tr>
<tr class="even">
<td align="left">TDI filter driver for deep packet or stream inspection or modification.</td>
<td align="left"><p>Transport layer, Stream layer, and/or ALE callout driver and optional user-mode application or service that uses the <a href="https://msdn.microsoft.com/library/windows/desktop/aa366510" data-raw-source="[WFP Win32 API](https://msdn.microsoft.com/library/windows/desktop/aa366510)">WFP Win32 API</a></p></td>
</tr>
<tr class="odd">
<td align="left">TDI filter driver for TCP connection or User Datagram Protocol (UDP) traffic management.</td>
<td align="left"><p>For TCP connection management: ALE callout driver and optional user-mode application or service that uses the <a href="https://msdn.microsoft.com/library/windows/desktop/aa366510" data-raw-source="[WFP Win32 API](https://msdn.microsoft.com/library/windows/desktop/aa366510)">WFP Win32 API</a>.</p>
<p>For TCP proxying:</p>
<ul>
<li>In Windows Vista: Packet modification callout driver.</li>
<li>In Windows 7 and later: ALE_REDIRECT layer callout driver.</li>
</ul>
<p>For MAC-level filtering:</p>
<ul>
<li>In Windows 8 and later: MAC_FRAME layer callout driver.</li>
<li>In Windows Vista and Windows 7: NDIS lightweight filter driver.</li>
</ul>
<p>For UDP traffic management: Stream or Datagram Data layer callout driver and optional user-mode application or service that uses the <a href="https://msdn.microsoft.com/library/windows/desktop/aa366510" data-raw-source="[WFP Win32 API](https://msdn.microsoft.com/library/windows/desktop/aa366510)">WFP Win32 API</a>.</p></td>
</tr>
<tr class="even">
<td align="left">Windows Sockets LSP for simple packet filtering.</td>
<td align="left">User-mode application or service that uses the <a href="https://msdn.microsoft.com/library/windows/desktop/aa366510" data-raw-source="[WFP Win32 API](https://msdn.microsoft.com/library/windows/desktop/aa366510)">WFP Win32 API</a>.</td>
</tr>
<tr class="odd">
<td align="left">Windows Sockets LSP for deep packet inspection or modification.</td>
<td align="left"><p>IP layer, ALE, Transport (such as Datagram Data), or Stream layer callout driver and optional user-mode application or service that uses the <a href="https://msdn.microsoft.com/library/windows/desktop/aa366510" data-raw-source="[WFP Win32 API](https://msdn.microsoft.com/library/windows/desktop/aa366510)">WFP Win32 API</a>.</p></td>
</tr>
<tr class="even">
<td align="left">Network Device Interface Specification (NDIS) intermediate driver for simple packet filtering.</td>
<td align="left"><p>For IP-based filtering: User-mode application or service that uses the <a href="https://msdn.microsoft.com/library/windows/desktop/aa366510" data-raw-source="[WFP Win32 API](https://msdn.microsoft.com/library/windows/desktop/aa366510)">WFP Win32 API</a>.</p>
<p>For MAC-based filtering:</p>
<ul>
<li>In Windows 8 and later: MAC_FRAME layer callout driver.</li>
<li>In Windows Vista and Windows 7: NDIS lightweight filter driver.</li>
</ul></td>
</tr>
<tr class="odd">
<td align="left">NDIS intermediate driver for TCP connection or UDP traffic management.</td>
<td align="left"><p>TCP connection management: ALE callout driver and optional user-mode application or service that uses the <a href="https://msdn.microsoft.com/library/windows/desktop/aa366510" data-raw-source="[WFP Win32 API](https://msdn.microsoft.com/library/windows/desktop/aa366510)">WFP Win32 API</a>.</p>
<p>UDP traffic management: ALE or Transport layer callout driver and optional user-mode application or service that uses the <a href="https://msdn.microsoft.com/library/windows/desktop/aa366510" data-raw-source="[WFP Win32 API](https://msdn.microsoft.com/library/windows/desktop/aa366510)">WFP Win32 API</a>.</p></td>
</tr>
<tr class="even">
<td align="left">NDIS lightweight filter driver to perform media access control (MAC)-level filtering.</td>
<td align="left"><p>In Windows 8 and later: MAC_FRAME layer callout driver.</p>
<p>In Windows Vista and Windows 7: NDIS lightweight filter driver.</p></td>
</tr>
</tbody>
</table>

 

 

 





