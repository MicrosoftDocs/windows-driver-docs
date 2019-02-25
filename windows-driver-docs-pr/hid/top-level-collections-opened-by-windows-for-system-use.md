---
title: Top-Level Collections Opened by Windows for System Use
description: Top-Level Collections Opened by Windows for System Use
ms.assetid: e489ce46-379e-4ba9-a0e3-5848b1f4a17b
keywords:
- top-level collections WDK HID
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Top-Level Collections Opened by Windows for System Use





Windows opens the following [top-level collections](top-level-collections.md) for system use:

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Device Type</th>
<th>Usage Page</th>
<th>Usage ID</th>
<th>Windows Client</th>
<th>Access Mode</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Pointer</p></td>
<td><p>0x01</p></td>
<td><p>0x01</p></td>
<td><p>Win32 subsystem</p></td>
<td><p>Exclusive</p></td>
</tr>
<tr class="even">
<td><p>Mouse</p></td>
<td><p>0x01</p></td>
<td><p>0x02</p></td>
<td><p>Win32 subsystem</p></td>
<td><p>Exclusive</p></td>
</tr>
<tr class="odd">
<td><p>Joystick</p></td>
<td><p>0x01</p></td>
<td><p>0x04</p></td>
<td><p>DirectInput</p></td>
<td><p>Shared</p></td>
</tr>
<tr class="even">
<td><p>Game pad</p></td>
<td><p>0x01</p></td>
<td><p>0x05</p></td>
<td><p>DirectInput</p></td>
<td><p>Shared</p></td>
</tr>
<tr class="odd">
<td><p>Keyboard</p></td>
<td><p>0x01</p></td>
<td><p>0x06</p></td>
<td><p>Win32 subsystem</p></td>
<td><p>Exclusive</p></td>
</tr>
<tr class="even">
<td><p>Keypad</p></td>
<td><p>0x01</p></td>
<td><p>0x07</p></td>
<td><p>Win32 subsystem</p></td>
<td><p>Exclusive</p></td>
</tr>
<tr class="odd">
<td><p>System Control</p></td>
<td><p>0x01</p></td>
<td><p>0x80</p></td>
<td><p>Win32 subsystem</p></td>
<td><p>Shared</p></td>
</tr>
<tr class="even">
<td><p>Consumer Audio Control</p></td>
<td><p>0x0C</p></td>
<td><p>0x01</p></td>
<td><p>hidserv.exe in Windows 2000 and hidserv.dll (one of the SVC host services) in Microsoft Windows XP</p></td>
<td><p>Shared</p></td>
</tr>
</tbody>
</table>

 

 

 




