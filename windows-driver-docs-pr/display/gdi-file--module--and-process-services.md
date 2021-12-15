---
title: GDI File, Module, and Process Services
description: GDI File, Module, and Process Services
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
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engdeletefile" data-raw-source="[&lt;strong&gt;EngDeleteFile&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engdeletefile)"><strong>EngDeleteFile</strong></a></p></td>
<td align="left"><p>Deletes a file.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engfindimageprocaddress" data-raw-source="[&lt;strong&gt;EngFindImageProcAddress&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engfindimageprocaddress)"><strong>EngFindImageProcAddress</strong></a></p></td>
<td align="left"><p>Returns the address of a function within an executable module.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engfindresource" data-raw-source="[&lt;strong&gt;EngFindResource&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engfindresource)"><strong>EngFindResource</strong></a></p></td>
<td align="left"><p>Determines the location of a resource in a module.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engfreemodule" data-raw-source="[&lt;strong&gt;EngFreeModule&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engfreemodule)"><strong>EngFreeModule</strong></a></p></td>
<td align="left"><p>Unmaps a file from system memory.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-enggetcurrentprocessid" data-raw-source="[&lt;strong&gt;EngGetCurrentProcessId&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-enggetcurrentprocessid)"><strong>EngGetCurrentProcessId</strong></a></p></td>
<td align="left"><p>Gets the ID of the current process.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-enggetcurrentthreadid" data-raw-source="[&lt;strong&gt;EngGetCurrentThreadId&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-enggetcurrentthreadid)"><strong>EngGetCurrentThreadId</strong></a></p></td>
<td align="left"><p>Gets the ID of the current thread.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-enggetfilechangetime" data-raw-source="[&lt;strong&gt;EngGetFileChangeTime&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-enggetfilechangetime)"><strong>EngGetFileChangeTime</strong></a></p></td>
<td align="left"><p>Returns the time a file was last written to.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-enggetfilepath" data-raw-source="[&lt;strong&gt;EngGetFilePath&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-enggetfilepath)"><strong>EngGetFilePath</strong></a></p></td>
<td align="left"><p>Determines the file path associated with the specified font file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-enggetprocesshandle" data-raw-source="[&lt;strong&gt;EngGetProcessHandle&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-enggetprocesshandle)"><strong>EngGetProcessHandle</strong></a></p></td>
<td align="left"><p>Retrieves a handle to the current client process.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engloadimage" data-raw-source="[&lt;strong&gt;EngLoadImage&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engloadimage)"><strong>EngLoadImage</strong></a></p></td>
<td align="left"><p>Loads the specified executable image into kernel-mode memory.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engloadmodule" data-raw-source="[&lt;strong&gt;EngLoadModule&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engloadmodule)"><strong>EngLoadModule</strong></a></p></td>
<td align="left"><p>Loads the specified data module into system memory for reading.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engloadmoduleforwrite" data-raw-source="[&lt;strong&gt;EngLoadModuleForWrite&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engloadmoduleforwrite)"><strong>EngLoadModuleForWrite</strong></a></p></td>
<td align="left"><p>Loads the specified executable module into system memory for writing.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engmapfile" data-raw-source="[&lt;strong&gt;EngMapFile&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engmapfile)"><strong>EngMapFile</strong></a></p></td>
<td align="left"><p>Creates or opens a file and maps it into <a href="/windows-hardware/drivers/#wdkgloss-system-space" data-raw-source="&lt;em&gt;system space&lt;/em&gt;"><em>system space</em></a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engmapfontfile" data-raw-source="[&lt;strong&gt;EngMapFontFile&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engmapfontfile)"><strong>EngMapFontFile</strong></a></p></td>
<td align="left"><p>Obsolete. See the entry in this table for <strong>EngMapFontFileFD</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engmapfontfilefd" data-raw-source="[&lt;strong&gt;EngMapFontFileFD&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engmapfontfilefd)"><strong>EngMapFontFileFD</strong></a></p></td>
<td align="left"><p>Maps a font file into system memory, if necessary, and returns a pointer to the base location of the font data in the file.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engmapmodule" data-raw-source="[&lt;strong&gt;EngMapModule&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engmapmodule)"><strong>EngMapModule</strong></a></p></td>
<td align="left"><p>Returns the address and size of an executable file that was loaded by <strong>EngLoadModule</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engqueryfiletimestamp" data-raw-source="[&lt;strong&gt;EngQueryFileTimeStamp&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engqueryfiletimestamp)"><strong>EngQueryFileTimeStamp</strong></a></p></td>
<td align="left"><p>Returns the time stamp of a file.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engunloadimage" data-raw-source="[&lt;strong&gt;EngUnloadImage&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engunloadimage)"><strong>EngUnloadImage</strong></a></p></td>
<td align="left"><p>Unloads an image loaded by <strong>EngLoadModule</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engunmapfile" data-raw-source="[&lt;strong&gt;EngUnmapFile&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engunmapfile)"><strong>EngUnmapFile</strong></a></p></td>
<td align="left"><p>Unmaps the view of a file from <a href="/windows-hardware/drivers/#wdkgloss-system-space" data-raw-source="&lt;em&gt;system space&lt;/em&gt;"><em>system space</em></a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engunmapfontfile" data-raw-source="[&lt;strong&gt;EngUnmapFontFile&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engunmapfontfile)"><strong>EngUnmapFontFile</strong></a></p></td>
<td align="left"><p>Obsolete. See the entry in this table for <strong>EngUnmapFontFileFD</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engunmapfontfilefd" data-raw-source="[&lt;strong&gt;EngUnmapFontFileFD&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engunmapfontfilefd)"><strong>EngUnmapFontFileFD</strong></a></p></td>
<td align="left"><p>Unmaps the specified font file from system memory.</p></td>
</tr>
</tbody>
</table>

 

