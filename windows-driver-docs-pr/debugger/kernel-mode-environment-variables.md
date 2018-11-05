---
title: Kernel-Mode Environment Variables
description: Kernel-Mode Environment Variables
ms.assetid: 619ebe55-1b57-4182-ada9-0c99c78056b3
keywords: ["environment variables, kernel-mode", "_NT_DEBUG_PORT environment variable", "_NT_DEBUG_BAUD_RATE environment variable", "KDQUIET environment variable", "_NT_DEBUG_CACHE_SIZE environment variable", "_NT_DEBUG_BUS environment variable", "_NT_DEBUG_1394_CHANNEL environment variable", "_NT_DEBUG_1394_SYMLINK environment variable", "_NT_DEBUG_OPTIONS environment variable"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Kernel-Mode Environment Variables


## <span id="ddk_kernel_mode_environment_variables_dbg"></span><span id="DDK_KERNEL_MODE_ENVIRONMENT_VARIABLES_DBG"></span>


The following table lists the environment variables that are used only in kernel-mode debugging.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Variable</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>_NT_DEBUG_PORT = <em>ComPort</em></p></td>
<td align="left"><p>Specifies the COM port to be used in a kernel connection. For details, see <a href="getting-set-up-for-debugging.md" data-raw-source="[Getting Set Up for Debugging](getting-set-up-for-debugging.md)">Getting Set Up for Debugging</a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>_NT_DEBUG_BAUD_RATE = <em>BaudRate</em></p></td>
<td align="left"><p>Specifies the baud rate to be used over the COM port connection.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>_NT_DEBUG_BUS = 1394</p></td>
<td align="left"><p>Specifies that kernel debugging will be done over a 1394 cable connection.</p></td>
</tr>
<tr class="even">
<td align="left"><p>_NT_DEBUG_1394_CHANNEL = <em>1394Channel</em></p></td>
<td align="left"><p>Specifies the channel to be used for the 1394 kernel connection.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>_NT_DEBUG_1394_SYMLINK = <em>Protocol</em></p></td>
<td align="left"><p>Specifies the connection protocol to be used for the 1394 kernel connection.</p></td>
</tr>
<tr class="even">
<td align="left"><p>KDQUIET =<em>Anything</em></p></td>
<td align="left"><p>If KDQUIET is defined, the debugger will run in <em>quiet mode</em>. Quiet mode involves three distinct effects:</p>
<p>1. The debugger does not display messages each time an extension DLL is loaded or unloaded.</p>
<p>2. The <strong><a href="r--registers-.md" data-raw-source="[r (Registers)](r--registers-.md)">r (Registers)</a></strong> command no longer requires an equal sign in its syntax.</p>
<p>3. The debugger will not display a warning message when breaking into the target computer.</p>
<p>Quiet mode can also be controlled by using the <strong><a href="sq--set-quiet-mode-.md" data-raw-source="[sq (Set Quiet Mode)](sq--set-quiet-mode-.md)">sq (Set Quiet Mode)</a></strong> command.</p></td>
</tr>
<tr class="odd">
<td align="left"><p></p>
_NT_DEBUG_CACHE_SIZE
= <em>Size</em></td>
<td align="left"><p>Specifies the maximum kernel debugging cache size, in bytes. This cache holds data received by the host computer from the serial connection. The default is 1,024,000.</p></td>
</tr>
<tr class="even">
<td align="left"><p>_NT_DEBUG_OPTIONS = <em>Option</em></p></td>
<td align="left"><p>Specifies one of the following two values:</p>
<p>NOEXTWARNING tells the debugger not to output a warning when it cannot find an extension command.</p>
<p>NOVERSIONCHECK tells the debugger not to check the version of debugger extensions.</p>
<p></p>
<p>These options can be modified or displayed by using the <strong><a href="so--set-kernel-debugging-options-.md" data-raw-source="[so (Set Kernel Options)](so--set-kernel-debugging-options-.md)">so (Set Kernel Options)</a></strong> command.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>_NT_KD_FILES = <em>MapFile</em></p></td>
<td align="left"><p>Specifies a driver replacement map file. For details and for other methods of controlling driver replacement, see <a href="mapping-driver-files.md" data-raw-source="[Mapping Driver Files](mapping-driver-files.md)">Mapping Driver Files</a>.</p></td>
</tr>
</tbody>
</table>

 

 

 





