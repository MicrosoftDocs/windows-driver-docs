---
title: Cabinet File Function
description: Cabinet File Function
keywords:
- SetupAPI functions WDK , cabinet files
- .cab files
- CAB files
ms.date: 04/20/2017
---

# Cabinet File Function





A cabinet (CAB) file is a single file, usually with a .*cab* extension, that contains several compressed files as a file library. CAB files are used to organize the installation files that will be copied to the user's system. A compressed file can be spread over several CAB files.

The following function is used with CAB files. For a detailed function description, see the Microsoft Windows SDK documentation.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Function</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupiteratecabineta" data-raw-source="[&lt;strong&gt;SetupIterateCabinet&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupiteratecabineta)"><strong>SetupIterateCabinet</strong></a></p></td>
<td align="left"><p>Sends a notification to a callback function for each file that is stored in a CAB file.</p></td>
</tr>
</tbody>
</table>

 

