---
title: Disk Prompting and Error Handling Functions
description: Disk Prompting and Error Handling Functions
ms.assetid: e1afeeb3-02f0-4570-9910-f948646f07bf
keywords:
- SetupAPI functions WDK , disk prompting
- SetupAPI functions WDK , error handling
- errors WDK SetupAPI
- disk prompting WDK SetupAPI
- prompting disk insertion WDK SetupAPI
- media prompting WDK SetupAPI
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Disk Prompting and Error Handling Functions





You can use the general Setup functions to prompt the user to insert new media, or to handle errors that arise when files are being copied, renamed, or deleted.

The following table lists functions that provide dialog boxes for requesting installation media and reporting errors. For detailed function descriptions, see the Microsoft Windows SDK documentation.

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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa376989" data-raw-source="[&lt;strong&gt;SetupCopyError&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa376989)"><strong>SetupCopyError</strong></a></p></td>
<td align="left"><p>Generates a dialog box that informs the user of a copy error.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa376994" data-raw-source="[&lt;strong&gt;SetupDeleteError&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa376994)"><strong>SetupDeleteError</strong></a></p></td>
<td align="left"><p>Generates a dialog box that informs the user of a delete error.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa377412" data-raw-source="[&lt;strong&gt;SetupPromptForDisk&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa377412)"><strong>SetupPromptForDisk</strong></a></p></td>
<td align="left"><p>Generates a dialog box that prompts the user for an installation medium or source file location.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa377434" data-raw-source="[&lt;strong&gt;SetupRenameError&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa377434)"><strong>SetupRenameError</strong></a></p></td>
<td align="left"><p>Generates a dialog box that informs the user of a rename error.</p></td>
</tr>
</tbody>
</table>

 

 

 





