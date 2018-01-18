---
title: BCDEdit Options Reference
description: BCDEdit Options Reference
ms.assetid: 351f8bc3-a228-48a4-bda8-69ee8521a5d3
---

# BCDEdit Options Reference


*Boot entry parameters*, or *boot parameters*, are optional, system-specific settings that represent configuration options. You can add boot parameters to a boot entry for an operating system.

This section describes the boot options for Windows 10, Windows 8.1, Windows 8, Windows 7, and Windows Vista, that are related to developing, testing, and debugging drivers on computers with x86-based and x64-based processors. You can add these parameters to the boot entries for Windows operating systems.

> \[!Note\]
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
<td align="left"><p>[<strong>BCDEdit /bootdebug</strong>](bcdedit--bootdebug.md)</p></td>
<td align="left"><p>The <strong>/bootdebug</strong> boot option enables or disables boot debugging of the current or specified Windows operating system boot entry.</p>
<blockquote>
[!Note]<br />
Before setting BCDEdit options you might need to disable or suspend BitLocker and Secure Boot on the computer.
</blockquote>
 </td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>BCDEdit /dbgsettings</strong>](bcdedit--dbgsettings.md)</p></td>
<td align="left"><p>The <strong>/dbgsettings</strong> option sets or displays the current global debugger settings for the computer. To enable or disable the kernel debugger, use the [<strong>BCDEdit /debug</strong>](bcdedit--debug.md) option.</p>
<blockquote>
[!Note]<br />
Before setting BCDEdit options you might need to disable or suspend BitLocker and Secure Boot on the computer.
</blockquote>
 </td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>BCDEdit /debug</strong>](bcdedit--debug.md)</p></td>
<td align="left"><p>The <strong>/debug</strong> boot option enables or disables kernel debugging of the Windows operating system associated with the specified boot entry or the current boot entry.</p>
<blockquote>
[!Note]<br />
Before setting BCDEdit options you might need to disable or suspend BitLocker and Secure Boot on the computer.
</blockquote>
 </td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>BCDEdit /deletevalue</strong>](bcdedit--deletevalue.md)</p></td>
<td align="left"><p>The <strong>BCDEdit /deletevalue</strong> command deletes or removes a boot entry option (and its value) from the Windows boot configuration data store (BCD). Use the <strong>BCDEdit /deletevalue</strong> command to remove options that were added using [<strong>BCDEdit /set</strong>](bcdedit--set.md) command. You might need to remove boot entry options when you are testing and debugging your driver for Windows 7, Windows 8, Windows 8.1, Windows 10 and later versions of Windows.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>BCDEdit /ems</strong>](bcdedit--ems.md)</p></td>
<td align="left"><p>The <strong>/ems</strong> option enables or disables Emergency Management Services (EMS) for the specified operating system boot entry.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>BCDEdit /emssettings</strong>](bcdedit--emssettings.md)</p></td>
<td align="left"><p>The <strong>/emssettings</strong> option sets the global Emergency Management Services (EMS) settings for the computer. To enable or disable EMS, use the <strong>/ems</strong> option. The <strong>/emssettings</strong> option does not enable or disable EMS for any boot entry.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>BCDEdit /set</strong>](bcdedit--set.md)</p></td>
<td align="left"><p>The <strong>BCDEdit /set</strong> command sets a boot entry option value in the Windows boot configuration data store (BCD) for Windows 7, Windows Server 2008, Windows 8, Windows 8.1,Windows 10, Windows Server 2012, and Windows Server 2012 R2. Use the <strong>BCDEdit /set</strong> command to configure specific boot entry elements, such as kernel debugger settings, memory options, or options that enable test-signed kernel-mode code or load alternate hardware abstraction layer (HAL) and kernel files. To remove a boot entry option, use the [<strong>BCDEdit /deletevalue</strong>](bcdedit--deletevalue.md) command.</p></td>
</tr>
</tbody>
</table>

 

### Mapping Boot.ini Options to BCDEdit Options and Elements

The following table provides a mapping from the boot options used in operating systems prior to Windows Vista (in Boot.ini), to the BCDEdit options and the BCD elements used in Windows. For information about the BCD boot elements see [BCD Reference](http://go.microsoft.com/fwlink/p/?linkid=56420) on MSDN.

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

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20BCDEdit%20Options%20Reference%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




