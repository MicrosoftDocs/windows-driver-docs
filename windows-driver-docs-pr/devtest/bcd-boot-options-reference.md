---
title: BCDEdit Options Reference
description: BCDEdit Options Reference
ms.assetid: 351f8bc3-a228-48a4-bda8-69ee8521a5d3
ms.date: 04/22/2019
ms.localizationpriority: medium
---

# BCDEdit Options Reference

*Boot entry parameters*, or *boot parameters*, are optional, system-specific settings that represent configuration options. You can add boot parameters to a boot entry for an operating system.

This section describes the boot options for supported versions of Windows that are related to developing, testing, and debugging drivers on computers with x86-based and x64-based processors. You can add these parameters to the boot entries for Windows operating systems.

> [!CAUTION]
> Administrative privileges are required to use BCDEdit to modify BCD. Changing some boot entry options using the **BCDEdit /set** command could render your computer inoperable. As an alternative, use the System Configuration utility (MSConfig.exe) to change boot settings.
 
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

 ## See also
 
 [Adding Boot Entries](https://docs.microsoft.com/windows-hardware/drivers/devtest/adding-boot-entries)
