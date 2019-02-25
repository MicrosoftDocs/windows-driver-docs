---
title: Remote NDIS File Naming Conventions
description: Remote NDIS File Naming Conventions
ms.assetid: 9c5b2cfe-c38f-4314-a91c-f27c77ea1f63
keywords:
- Remote NDIS WDK networking , driver names
- Remote NDIS WDK networking , operating system support
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Remote NDIS File Naming Conventions





In order to support legacy Remote NDIS devices, multiple Remote NDIS drivers have been included with various versions of Windows. The following table lists the Remote NDIS driver names used in each version of Windows.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Remote NDIS file name</th>
<th align="left">Windows version in which this driver is available</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Rndismp.sys Usb8023.sys</p></td>
<td align="left"><p>These binaries are shipped only for legacy device support. No Remote NDIS device INF file should reference these drivers.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Rndismpy.sys Usb8023y.sys</p></td>
<td align="left"><p>Windows 2000. Were provided separately from the operating system. These are the only binaries for which Microsoft grants redistribution rights.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Rndismpx.sys Usb8023x.sys Netrndis.inf</p></td>
<td align="left"><ul>
<li><p>Windows XP SP2 and later</p></li>
<li><p>Windows XP x64</p></li>
<li><p>Windows Server 2003 SP1 (x86, x64, ia64) and later</p></li>
<li><p>Windows Vista (x86, x64) and later</p></li>
</ul>
<p>The Rndismpx.sys and Usb8023x.sys binaries ship as part of the operating system. The Netrndis.inf file is an internal file that is part of the operating system. All these files must be referenced by the IHV-provided INF file as described in <a href="remote-ndis-inf-template.md" data-raw-source="[Remote NDIS INF Template](remote-ndis-inf-template.md)">Remote NDIS INF Template</a>.</p></td>
</tr>
</tbody>
</table>

 

**Note**  Remote NDIS is not supported on Windows 98/Me/SE or prior versions.

 

 

 





