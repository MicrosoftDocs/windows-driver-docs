---
title: Introduction to Boot Options
description: The concept and content of boot options are very similar on all computers that run Microsoft Windows operating systems.
ms.assetid: e8e835c4-75de-4ce1-965f-d9b822e15044
keywords:
- boot options WDK , about boot options
- storing boot options
- boot loaders WDK
ms.date: 07/02/2018
ms.localizationpriority: medium
---

# Introduction to Boot Options

The concept and content of boot options are very similar on all computers that run Microsoft Windows operating systems. However, prior to Windows Vista, computers with different processor firmware store boot options differently and require different tools to view and edit the options on each system.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Version of Windows</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><span id="______Windows_7__Windows_Server_2008__Windows_Vista"></span><span id="______windows_7__windows_server_2008__windows_vista"></span><span id="______WINDOWS_7__WINDOWS_SERVER_2008__WINDOWS_VISTA"></span>Windows Server 2016, Windows 10, Windows Server 2012 R2, Windows 8.1, Windows Server 2012, Windows 8, Windows Server 2008 R2, Windows 7, Windows Server 2008, Windows Vista</p></td>
<td align="left"><p>Windows Vista, and later versions of Windows, store boot option in a firmware-independent storage and configuration system. Windows Vista also introduces a new Boot Manager and system-specific boot loaders. For more information, see <a href="boot-options-in-windows-vista-and-later.md" data-raw-source="[Boot Options in Windows Vista and Later](boot-options-in-windows-vista-and-later.md)">Boot Options in Windows Vista and Later</a>.</p></td>
</tr>
</tbody>
</table>

This section includes:
- [Boot Options in a Boot.ini File](boot-options-in-a-boot-ini-file.md) (Windows XP, Windows Server 2003)
- [Boot Options in EFI NVRAM](boot-options-in-efi-nvram.md) (Windows XP, Windows Server 2003)
- [Overview of Boot Options in Windows Vista and Later](boot-options-in-windows-vista-and-later.md)
