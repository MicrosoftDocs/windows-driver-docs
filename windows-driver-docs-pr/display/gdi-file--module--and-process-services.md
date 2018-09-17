---
title: GDI File, Module, and Process Services
description: GDI File, Module, and Process Services
ms.assetid: abf37bed-cad9-4fbc-95fe-346b0c07c81b
keywords:
- GDI WDK Windows 2000 display , module services
- graphics drivers WDK Windows 2000 display , module services
- drawing WDK GDI , module services
- GDI WDK Windows 2000 display , file services
- graphics drivers WDK Windows 2000 display , file services
- drawing WDK GDI , file services
- GDI WDK Windows 2000 display , process services
- graphics drivers WDK Windows 2000 display , process services
- drawing WDK GDI , process services
- process services WDK GDI
- file services WDK GDI
- modules WDK GDI
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# GDI File, Module, and Process Services


## <span id="ddk_gdi_file_module_and_process_services_gg"></span><span id="DDK_GDI_FILE_MODULE_AND_PROCESS_SERVICES_GG"></span>


GDI provides a variety of services for file, module, and process manipulation.

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
<td align="left"><p>[<strong>EngDeleteFile</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564803)</p></td>
<td align="left"><p>Deletes a file.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngFindImageProcAddress</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564865)</p></td>
<td align="left"><p>Returns the address of a function within an executable module.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EngFindResource</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564871)</p></td>
<td align="left"><p>Determines the location of a resource in a module.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngFreeModule</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564902)</p></td>
<td align="left"><p>Unmaps a file from system memory.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EngGetCurrentProcessId</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564919)</p></td>
<td align="left"><p>Gets the ID of the current process.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngGetCurrentThreadId</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564922)</p></td>
<td align="left"><p>Gets the ID of the current thread.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EngGetFileChangeTime</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564931)</p></td>
<td align="left"><p>Returns the time a file was last written to.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngGetFilePath</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564935)</p></td>
<td align="left"><p>Determines the file path associated with the specified font file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EngGetProcessHandle</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564955)</p></td>
<td align="left"><p>Retrieves a handle to the current client process.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngLoadImage</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564963)</p></td>
<td align="left"><p>Loads the specified executable image into kernel-mode memory.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EngLoadModule</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564964)</p></td>
<td align="left"><p>Loads the specified data module into system memory for reading.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngLoadModuleForWrite</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564965)</p></td>
<td align="left"><p>Loads the specified executable module into system memory for writing.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EngMapFile</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564971)</p></td>
<td align="left"><p>Creates or opens a file and maps it into [<em>system space</em>](https://msdn.microsoft.com/library/windows/hardware/ff556336#wdkgloss-system-space).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngMapFontFile</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564972)</p></td>
<td align="left"><p>Obsolete. See the entry in this table for <strong>EngMapFontFileFD</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EngMapFontFileFD</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564973)</p></td>
<td align="left"><p>Maps a font file into system memory, if necessary, and returns a pointer to the base location of the font data in the file.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngMapModule</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564974)</p></td>
<td align="left"><p>Returns the address and size of an executable file that was loaded by <strong>EngLoadModule</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EngQueryFileTimeStamp</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564988)</p></td>
<td align="left"><p>Returns the time stamp of a file.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngUnloadImage</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565041)</p></td>
<td align="left"><p>Unloads an image loaded by <strong>EngLoadModule</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EngUnmapFile</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565437)</p></td>
<td align="left"><p>Unmaps the view of a file from [<em>system space</em>](https://msdn.microsoft.com/library/windows/hardware/ff556336#wdkgloss-system-space).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngUnmapFontFile</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565441)</p></td>
<td align="left"><p>Obsolete. See the entry in this table for <strong>EngUnmapFontFileFD</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EngUnmapFontFileFD</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565445)</p></td>
<td align="left"><p>Unmaps the specified font file from system memory.</p></td>
</tr>
</tbody>
</table>

 

 

 





