---
title: BCDEdit Options Reference
description: BCDEdit Options Reference
ms.assetid: 351f8bc3-a228-48a4-bda8-69ee8521a5d3
ms.date: 05/21/2018
ms.localizationpriority: medium
---

# BCDEdit Options Reference


*Boot entry parameters*, or *boot parameters*, are optional, system-specific settings that represent configuration options. You can add boot parameters to a boot entry for an operating system.

This section describes the boot options for supported versions of Windows that are related to developing, testing, and debugging drivers on computers with x86-based and x64-based processors. You can add these parameters to the boot entries for Windows operating systems.

> [!NOTE]
> Before setting BCDEdit options you might need to disable or suspend BitLocker and Secure Boot on the computer.

 

## In this section


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Topic</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="bcdedit--bootdebug.md" data-raw-source="[&lt;strong&gt;BCDEdit /bootdebug&lt;/strong&gt;](bcdedit--bootdebug.md)"><strong>BCDEdit /bootdebug</strong></a></p></td>
<td align="left"><p>The <strong>/bootdebug</strong> boot option enables or disables boot debugging of the current or specified Windows operating system boot entry.</p>
<blockquote>
[!Note]<br />
Before setting BCDEdit options you might need to disable or suspend BitLocker and Secure Boot on the computer.
</blockquote>
 </td>
</tr>
<tr class="even">
<td align="left"><p><a href="bcdedit--dbgsettings.md" data-raw-source="[&lt;strong&gt;BCDEdit /dbgsettings&lt;/strong&gt;](bcdedit--dbgsettings.md)"><strong>BCDEdit /dbgsettings</strong></a></p></td>
<td align="left"><p>The <strong>/dbgsettings</strong> option sets or displays the current global debugger settings for the computer. To enable or disable the kernel debugger, use the <a href="bcdedit--debug.md" data-raw-source="[&lt;strong&gt;BCDEdit /debug&lt;/strong&gt;](bcdedit--debug.md)"><strong>BCDEdit /debug</strong></a> option.</p>
<blockquote>
[!Note]<br />
Before setting BCDEdit options you might need to disable or suspend BitLocker and Secure Boot on the computer.
</blockquote>
 </td>
</tr>
<tr class="odd">
<td align="left"><p><a href="bcdedit--debug.md" data-raw-source="[&lt;strong&gt;BCDEdit /debug&lt;/strong&gt;](bcdedit--debug.md)"><strong>BCDEdit /debug</strong></a></p></td>
<td align="left"><p>The <strong>/debug</strong> boot option enables or disables kernel debugging of the Windows operating system associated with the specified boot entry or the current boot entry.</p>
<blockquote>
[!Note]<br />
Before setting BCDEdit options you might need to disable or suspend BitLocker and Secure Boot on the computer.
</blockquote>
 </td>
</tr>
<tr class="even">
<td align="left"><p><a href="bcdedit--deletevalue.md" data-raw-source="[&lt;strong&gt;BCDEdit /deletevalue&lt;/strong&gt;](bcdedit--deletevalue.md)"><strong>BCDEdit /deletevalue</strong></a></p></td>
<td align="left"><p>The <strong>BCDEdit /deletevalue</strong> command deletes or removes a boot entry option (and its value) from the Windows boot configuration data store (BCD). Use the <strong>BCDEdit /deletevalue</strong> command to remove options that were added using <a href="bcdedit--set.md" data-raw-source="[&lt;strong&gt;BCDEdit /set&lt;/strong&gt;](bcdedit--set.md)"><strong>BCDEdit /set</strong></a> command. You might need to remove boot entry options when you are testing and debugging your driver for Windows 7, Windows 8, Windows 8.1, Windows 10 and later versions of Windows.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="bcdedit--ems.md" data-raw-source="[&lt;strong&gt;BCDEdit /ems&lt;/strong&gt;](bcdedit--ems.md)"><strong>BCDEdit /ems</strong></a></p></td>
<td align="left"><p>The <strong>/ems</strong> option enables or disables Emergency Management Services (EMS) for the specified operating system boot entry.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="bcdedit--emssettings.md" data-raw-source="[&lt;strong&gt;BCDEdit /emssettings&lt;/strong&gt;](bcdedit--emssettings.md)"><strong>BCDEdit /emssettings</strong></a></p></td>
<td align="left"><p>The <strong>/emssettings</strong> option sets the global Emergency Management Services (EMS) settings for the computer. To enable or disable EMS, use the <strong>/ems</strong> option. The <strong>/emssettings</strong> option does not enable or disable EMS for any boot entry.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="bcdedit--set.md" data-raw-source="[&lt;strong&gt;BCDEdit /set&lt;/strong&gt;](bcdedit--set.md)"><strong>BCDEdit /set</strong></a></p></td>
<td align="left"><p>The <strong>BCDEdit /set</strong> command sets a boot entry option value in the Windows boot configuration data store (BCD) for Windows 7, Windows Server 2008, Windows 8, Windows 8.1,Windows 10, Windows Server 2012, and Windows Server 2012 R2. Use the <strong>BCDEdit /set</strong> command to configure specific boot entry elements, such as kernel debugger settings, memory options, or options that enable test-signed kernel-mode code or load alternate hardware abstraction layer (HAL) and kernel files. To remove a boot entry option, use the <a href="bcdedit--deletevalue.md" data-raw-source="[&lt;strong&gt;BCDEdit /deletevalue&lt;/strong&gt;](bcdedit--deletevalue.md)"><strong>BCDEdit /deletevalue</strong></a> command.</p></td>
</tr>
</tbody>
</table>

 

### Mapping Boot.ini Options to BCDEdit Options and Elements

The following table provides a mapping from the boot options used in operating systems prior to Windows Vista (in Boot.ini), to the BCDEdit options and the BCD elements used in Windows. For information about the BCD boot elements see [BCD Reference](http://go.microsoft.com/fwlink/p/?linkid=56420).

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Boot.ini</th>
<th align="left">BCDEdit option</th>
<th align="left">BCD element type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>/3GB</p></td>
<td align="left"><p><strong>increaseuserva</strong></p></td>
<td align="left"><p>BcdOSLoaderInteger_IncreaseUserVa</p></td>
</tr>
<tr class="even">
<td align="left"><p>/BASEVIDEO</p></td>
<td align="left"><p><strong>vga</strong></p></td>
<td align="left"><p>BcdOSLoaderBoolean_UseVgaDriver</p></td>
</tr>
<tr class="odd">
<td align="left"><p>/BOOTLOG</p></td>
<td align="left"><p><strong>bootlog</strong></p></td>
<td align="left"><p>BcdOSLoaderBoolean_BootLogInitialization</p></td>
</tr>
<tr class="even">
<td align="left"><p>/BREAK</p></td>
<td align="left"><p><strong>halbreakpoint</strong></p></td>
<td align="left"><p>BcdOSLoaderBoolean_DebuggerHalBreakpoint</p></td>
</tr>
<tr class="odd">
<td align="left"><p>/CRASHDEBUG</p></td>
<td align="left"><p><strong>/dbgsettings /start</strong></p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>/DEBUG, BOOTDEBUG</p></td>
<td align="left"><p><strong>/debug</strong></p>
<p><strong>/bootdebug</strong></p></td>
<td align="left"><p>BcdLibraryBoolean_DebuggerEnabled</p></td>
</tr>
<tr class="odd">
<td align="left"><p>/DEBUG</p></td>
<td align="left"><p><strong>/debug</strong></p></td>
<td align="left"><p>BcdOSLoaderBoolean_KernelDebuggerEnabled</p></td>
</tr>
<tr class="even">
<td align="left"><p>/DEBUG, /DEBUGPORT=</p></td>
<td align="left"><p><strong>/dbgsettings</strong></p></td>
<td align="left"><p>BcdLibraryInteger_DebuggerType</p></td>
</tr>
<tr class="odd">
<td align="left"><p>/DEBUGPORT=</p></td>
<td align="left"><p><strong>/dbgsettings</strong></p></td>
<td align="left"><p>BcdLibraryInteger_SerialDebuggerPort</p>
<p>BcdLibraryInteger_SerialDebuggerBaudRate</p>
<p>BcdLibraryInteger_1394DebuggerChannel</p>
<p>BcdLibraryString_UsbDebuggerTargetName</p>
<p>BcdLibraryInteger_DebuggerNetHostIP</p>
<p>BcdLibraryInteger_DebuggerNetPort</p>
<p>BcdLibraryBoolean_DebuggerNetDhcp</p>
<p>BcdLibraryString_DebuggerNetKey</p></td>
</tr>
<tr class="even">
<td align="left"><p>/EXECUTE</p></td>
<td align="left"><p><strong>nx</strong></p></td>
<td align="left"><p>BcdOSLoaderInteger_NxPolicy</p></td>
</tr>
<tr class="odd">
<td align="left"><p>/FASTDETECT</p></td>
<td align="left"></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>/HAL=</p></td>
<td align="left"><p><strong>hal</strong></p></td>
<td align="left"><p>BcdOSLoaderString_HalPath</p></td>
</tr>
<tr class="odd">
<td align="left"><p>/KERNEL=</p></td>
<td align="left"><p><strong>kernel</strong></p></td>
<td align="left"><p>BcdOSLoaderString_KernelPath</p></td>
</tr>
<tr class="even">
<td align="left"><p>/MAXMEM=</p></td>
<td align="left"><p><strong>truncatememory</strong></p></td>
<td align="left"><p>BcdLibraryInteger_TruncatePhysicalMemory</p></td>
</tr>
<tr class="odd">
<td align="left"><p>/NODEBUG</p></td>
<td align="left"><p><strong>/debug</strong></p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>/NOEXECUTE</p></td>
<td align="left"><p><strong>nx</strong> {</p></td>
<td align="left"><p>BcdOSLoaderInteger_NxPolicy</p></td>
</tr>
<tr class="odd">
<td align="left"><p>/NOGUIBOOT</p></td>
<td align="left"><p><strong>quietboot</strong></p></td>
<td align="left"><p>BcdOSLoaderBoolean_DisableBootDisplay</p></td>
</tr>
<tr class="even">
<td align="left"><p>/NOLOWMEM</p></td>
<td align="left"><p><strong>nolowmem</strong></p></td>
<td align="left"><p>BcdOSLoaderBoolean_NoLowMemory</p></td>
</tr>
<tr class="odd">
<td align="left"><p>/NOPAE</p></td>
<td align="left"><p><strong>pae</strong></p></td>
<td align="left"><p>BcdOSLoaderInteger_PAEPolicy</p></td>
</tr>
<tr class="even">
<td align="left"><p>/ONECPU</p></td>
<td align="left"><p><strong>onecpu</strong></p></td>
<td align="left"><p>BcdOSLoaderBoolean_UseBootProcessorOnly</p></td>
</tr>
<tr class="odd">
<td align="left"><p>/PAE</p></td>
<td align="left"><p><strong>pae</strong></p></td>
<td align="left"><p>BcdOSLoaderInteger_PAEPolicy</p></td>
</tr>
<tr class="even">
<td align="left"><p>/PCILOCK</p></td>
<td align="left"><p><strong>usefirmwarepcisettings</strong></p></td>
<td align="left"><p>BcdOSLoaderInteger_UseFirmwarePciSettings</p></td>
</tr>
<tr class="odd">
<td align="left"><p>/REDIRECT</p></td>
<td align="left"><p><strong>/ems</strong></p>
<p><strong>/emssettings</strong> [ <strong>BIOS</strong> ] |</p>
<p>[ <strong>EMSPORT:</strong>{<em>port</em>} | [<strong>EMSBAUDRATE:</strong> {<em>baudrate</em>}] ]</p></td>
<td align="left"><p>BcdOSLoaderBoolean_EmsEnabled</p></td>
</tr>
<tr class="even">
<td align="left"><p>/SOS</p></td>
<td align="left"><p><strong>sos</strong></p></td>
<td align="left"></td>
</tr>
</tbody>
</table>

 ## See also
 
 [Adding Boot Entries](https://docs.microsoft.com/windows-hardware/drivers/devtest/adding-boot-entries)

 

 





