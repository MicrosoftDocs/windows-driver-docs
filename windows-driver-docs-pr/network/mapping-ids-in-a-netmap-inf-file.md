---
title: Mapping IDs in a Netmap.inf File
description: Mapping IDs in a Netmap.inf File
ms.assetid: 7cab4aa1-8b0b-4cdc-a093-b91be6170961
keywords:
- network component upgrades WDK , netmap.inf files
- upgrading network components WDK , netmap.inf files
- netmap.inf files WDK
- mapping network component IDs
- ID mapping WDK netmap.inf
- device IDs WDK netmap.inf
- vendor-supplied files WDK netmap.inf file
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Mapping IDs in a Netmap.inf File





**Note**  Vendor-supplied network upgrades are not supported in Microsoft Windows XP (SP1 and later), Microsoft Windows Server 2003, and later operating systems.

 

A netmap.inf file contains one or more of the following top-level sections. Each section contains ID mappings for the components listed in the **Map** column.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Section</th>
<th align="left">Map</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>OemNetAdapters</strong></p></td>
<td align="left"><p>Network adapters, excluding Async adapters</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>OemAsyncAdapters</strong></p></td>
<td align="left"><p>Async network adapters</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>OemNetProtocols</strong></p></td>
<td align="left"><p>Network protocol drivers</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>OemNetServices</strong></p></td>
<td align="left"><p>Network services</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>OemNetClients</strong></p></td>
<td align="left"><p>Network clients</p></td>
</tr>
</tbody>
</table>

 

Each entry in a section maps a network component's preupgrade device, hardware, or compatible ID to its corresponding Windows 2000 or later ID. Each entry specifies either *one-to-one* ID mapping or *one-to-many* ID mapping. These mapping strategies are described following.

Network clients are not defined as such in Windows NT 3.51 and Windows NT 4.0; therefore, if an earlier network service becomes a network client under Windows 2000 or later, its device ID mapping must be listed in the **OemNetClients** section, not in the **OemNetServices** section.

 

 





