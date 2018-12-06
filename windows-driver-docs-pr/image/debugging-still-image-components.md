---
title: Debugging Still Image Components
description: Debugging Still Image Components
ms.assetid: 587b8db7-7fca-4b70-8901-3adbde07718f
ms.date: 07/18/2018
ms.localizationpriority: medium
---

# Debugging Still Image Components

To aid the debugging of vendor-supplied still image components, the still image event monitor's behavior can be modified with command-line options, using the **Run** option of the **Start** menu. The following options are available:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Command Line Option</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>stimon /h</strong></p></td>
<td><p>Hides the message window.</p></td>
</tr>
<tr class="even">
<td><p><strong>Stimon /r</strong></p></td>
<td><p>Refreshes the event monitor&#39;s device list.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Stimon /t</strong><em>number</em></p></td>
<td><p>Modifies the polling interval to the number of seconds specified by <em>number</em>. Typically used for increasing the polling interval.</p></td>
</tr>
<tr class="even">
<td><p><strong>Stimon /v</strong></p></td>
<td><p>Makes a window visible that displays event monitor messages.</p></td>
</tr>
</tbody>
</table>

The event monitor can be stopped and started by using the Computer Management window. The event monitor is listed as the "Still Image Service".
