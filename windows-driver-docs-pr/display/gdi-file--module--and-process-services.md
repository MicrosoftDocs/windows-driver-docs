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
ms.date: 04/20/2017
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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564803" data-raw-source="[&lt;strong&gt;EngDeleteFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564803)"><strong>EngDeleteFile</strong></a></p></td>
<td align="left"><p>Deletes a file.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564865" data-raw-source="[&lt;strong&gt;EngFindImageProcAddress&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564865)"><strong>EngFindImageProcAddress</strong></a></p></td>
<td align="left"><p>Returns the address of a function within an executable module.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564871" data-raw-source="[&lt;strong&gt;EngFindResource&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564871)"><strong>EngFindResource</strong></a></p></td>
<td align="left"><p>Determines the location of a resource in a module.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564902" data-raw-source="[&lt;strong&gt;EngFreeModule&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564902)"><strong>EngFreeModule</strong></a></p></td>
<td align="left"><p>Unmaps a file from system memory.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564919" data-raw-source="[&lt;strong&gt;EngGetCurrentProcessId&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564919)"><strong>EngGetCurrentProcessId</strong></a></p></td>
<td align="left"><p>Gets the ID of the current process.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564922" data-raw-source="[&lt;strong&gt;EngGetCurrentThreadId&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564922)"><strong>EngGetCurrentThreadId</strong></a></p></td>
<td align="left"><p>Gets the ID of the current thread.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564931" data-raw-source="[&lt;strong&gt;EngGetFileChangeTime&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564931)"><strong>EngGetFileChangeTime</strong></a></p></td>
<td align="left"><p>Returns the time a file was last written to.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564935" data-raw-source="[&lt;strong&gt;EngGetFilePath&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564935)"><strong>EngGetFilePath</strong></a></p></td>
<td align="left"><p>Determines the file path associated with the specified font file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564955" data-raw-source="[&lt;strong&gt;EngGetProcessHandle&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564955)"><strong>EngGetProcessHandle</strong></a></p></td>
<td align="left"><p>Retrieves a handle to the current client process.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564963" data-raw-source="[&lt;strong&gt;EngLoadImage&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564963)"><strong>EngLoadImage</strong></a></p></td>
<td align="left"><p>Loads the specified executable image into kernel-mode memory.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564964" data-raw-source="[&lt;strong&gt;EngLoadModule&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564964)"><strong>EngLoadModule</strong></a></p></td>
<td align="left"><p>Loads the specified data module into system memory for reading.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564965" data-raw-source="[&lt;strong&gt;EngLoadModuleForWrite&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564965)"><strong>EngLoadModuleForWrite</strong></a></p></td>
<td align="left"><p>Loads the specified executable module into system memory for writing.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564971" data-raw-source="[&lt;strong&gt;EngMapFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564971)"><strong>EngMapFile</strong></a></p></td>
<td align="left"><p>Creates or opens a file and maps it into <a href="https://msdn.microsoft.com/library/windows/hardware/ff556336#wdkgloss-system-space" data-raw-source="[&lt;em&gt;system space&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556336#wdkgloss-system-space)"><em>system space</em></a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564972" data-raw-source="[&lt;strong&gt;EngMapFontFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564972)"><strong>EngMapFontFile</strong></a></p></td>
<td align="left"><p>Obsolete. See the entry in this table for <strong>EngMapFontFileFD</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564973" data-raw-source="[&lt;strong&gt;EngMapFontFileFD&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564973)"><strong>EngMapFontFileFD</strong></a></p></td>
<td align="left"><p>Maps a font file into system memory, if necessary, and returns a pointer to the base location of the font data in the file.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564974" data-raw-source="[&lt;strong&gt;EngMapModule&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564974)"><strong>EngMapModule</strong></a></p></td>
<td align="left"><p>Returns the address and size of an executable file that was loaded by <strong>EngLoadModule</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564988" data-raw-source="[&lt;strong&gt;EngQueryFileTimeStamp&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564988)"><strong>EngQueryFileTimeStamp</strong></a></p></td>
<td align="left"><p>Returns the time stamp of a file.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565041" data-raw-source="[&lt;strong&gt;EngUnloadImage&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565041)"><strong>EngUnloadImage</strong></a></p></td>
<td align="left"><p>Unloads an image loaded by <strong>EngLoadModule</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565437" data-raw-source="[&lt;strong&gt;EngUnmapFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565437)"><strong>EngUnmapFile</strong></a></p></td>
<td align="left"><p>Unmaps the view of a file from <a href="https://msdn.microsoft.com/library/windows/hardware/ff556336#wdkgloss-system-space" data-raw-source="[&lt;em&gt;system space&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556336#wdkgloss-system-space)"><em>system space</em></a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565441" data-raw-source="[&lt;strong&gt;EngUnmapFontFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565441)"><strong>EngUnmapFontFile</strong></a></p></td>
<td align="left"><p>Obsolete. See the entry in this table for <strong>EngUnmapFontFileFD</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565445" data-raw-source="[&lt;strong&gt;EngUnmapFontFileFD&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565445)"><strong>EngUnmapFontFileFD</strong></a></p></td>
<td align="left"><p>Unmaps the specified font file from system memory.</p></td>
</tr>
</tbody>
</table>

 

 

 





