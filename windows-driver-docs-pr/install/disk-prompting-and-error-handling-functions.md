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
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Disk Prompting and Error Handling Functions


## <a href="" id="ddk-disk-prompting-and-error-handling-functions-dg"></a>


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
<td align="left"><p>[<strong>SetupCopyError</strong>](https://msdn.microsoft.com/library/windows/desktop/aa376989)</p></td>
<td align="left"><p>Generates a dialog box that informs the user of a copy error.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupDeleteError</strong>](https://msdn.microsoft.com/library/windows/desktop/aa376994)</p></td>
<td align="left"><p>Generates a dialog box that informs the user of a delete error.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupPromptForDisk</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377412)</p></td>
<td align="left"><p>Generates a dialog box that prompts the user for an installation medium or source file location.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupRenameError</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377434)</p></td>
<td align="left"><p>Generates a dialog box that informs the user of a rename error.</p></td>
</tr>
</tbody>
</table>

 

 

 





