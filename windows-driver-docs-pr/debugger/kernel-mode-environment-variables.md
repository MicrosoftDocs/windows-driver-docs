---
title: Kernel-Mode Environment Variables
description: Kernel-Mode Environment Variables
ms.assetid: 619ebe55-1b57-4182-ada9-0c99c78056b3
keywords: ["environment variables, kernel-mode", "_NT_DEBUG_PORT environment variable", "_NT_DEBUG_BAUD_RATE environment variable", "KDQUIET environment variable", "_NT_DEBUG_CACHE_SIZE environment variable", "_NT_DEBUG_BUS environment variable", "_NT_DEBUG_1394_CHANNEL environment variable", "_NT_DEBUG_1394_SYMLINK environment variable", "_NT_DEBUG_OPTIONS environment variable"]
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
<td align="left"><p>Specifies the COM port to be used in a kernel connection. For details, see [Getting Set Up for Debugging](getting-set-up-for-debugging.md).</p></td>
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
<p>2. The [<strong>r (Registers)</strong>](r--registers-.md) command no longer requires an equal sign in its syntax.</p>
<p>3. The debugger will not display a warning message when breaking into the target computer.</p>
<p>Quiet mode can also be controlled by using the [<strong>sq (Set Quiet Mode)</strong>](sq--set-quiet-mode-.md) command.</p></td>
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
<p>These options can be modified or displayed by using the [<strong>so (Set Kernel Options)</strong>](so--set-kernel-debugging-options-.md) command.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>_NT_KD_FILES = <em>MapFile</em></p></td>
<td align="left"><p>Specifies a driver replacement map file. For details and for other methods of controlling driver replacement, see [Mapping Driver Files](mapping-driver-files.md).</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Kernel-Mode%20Environment%20Variables%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




