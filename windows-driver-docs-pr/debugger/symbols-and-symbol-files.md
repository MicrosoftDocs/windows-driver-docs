---
title: Symbols and Symbol Files
description: Symbols and Symbol Files
ms.assetid: b9ace4f0-8363-4dec-806f-798d30983dc1
keywords: ["symbols, overview"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Symbols and Symbol Files


## <span id="ddk_symbol_files_overview_dbg"></span><span id="DDK_SYMBOL_FILES_OVERVIEW_DBG"></span>


When applications, libraries, drivers, or operating systems are linked, the linker that creates the .exe and .dll files also creates a number of additional files known as *symbol files*.

Symbol files hold a variety of data which are not actually needed when running the binaries, but which could be very useful in the debugging process.

Typically, symbol files might contain:

-   Global variables

-   Local variables

-   Function names and the addresses of their entry points

-   Frame pointer omission (FPO) records

-   Source-line numbers

Each of these items is called, individually, a *symbol*. For example, a single symbol file Myprogram.pdb might contain several hundred symbols, including global variables and function names and hundreds of local variables. Often, software companies release two versions of each symbol file: a full symbol file containing both *public symbols* and *private symbols*, and a reduced (stripped) file containing only public symbols. For details, see [Public and Private Symbols](public-and-private-symbols.md).

When debugging, you must make sure that the debugger can access the symbol files that are associated with the target you are debugging. Both live debugging and debugging crash dump files require symbols. You must obtain the proper symbols for the code that you wish to debug, and load these symbols into the debugger.

### <span id="windows_symbols"></span><span id="WINDOWS_SYMBOLS"></span>Windows Symbols

Windows keeps its symbols in files with the extension .pdb.

The compiler and the linker control the symbol format. The Visual C++ linker, places all symbols into .pdb files.

The Windows operating system is built in two versions. The [*free build*](https://msdn.microsoft.com/library/windows/hardware/ff556280#wdkgloss-free-build) (or *retail build*) has relatively small binaries, and the [*checked build*](https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-checked-build) (or *debug build*) has larger binaries, with more debugging symbols in the code itself. Each of these builds has its own symbol files. When debugging a target on Windows, you must use the symbol files that match the build of Windows on the target.

The following table lists several of the directories which exist in a standard Windows symbol tree:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Directory</th>
<th align="left">Contains Symbol Files for</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>ACM</p></td>
<td align="left"><p>Microsoft Audio Compression Manager files</p></td>
</tr>
<tr class="even">
<td align="left"><p>COM</p></td>
<td align="left"><p>Executable files (.com)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>CPL</p></td>
<td align="left"><p>Control Panel programs</p></td>
</tr>
<tr class="even">
<td align="left"><p>DLL</p></td>
<td align="left"><p>Dynamic-link library files (.dll)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>DRV</p></td>
<td align="left"><p>Driver files (.drv)</p></td>
</tr>
<tr class="even">
<td align="left"><p>EXE</p></td>
<td align="left"><p>Executable files (.exe)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>SCR</p></td>
<td align="left"><p>Screen-saver files</p></td>
</tr>
<tr class="even">
<td align="left"><p>SYS</p></td>
<td align="left"><p>Driver files (.sys)</p></td>
</tr>
</tbody>
</table>

 

 

 





