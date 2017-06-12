---
title: System Syntax
description: System Syntax
ms.assetid: f2b327cd-8ba5-45f3-9116-756df82358f4
keywords: ["system, command syntax", "(system identifier)", "system, system identifier ( )", "syntax rules for commands, systems", "syntax rules for commands, (system identifier)"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# System Syntax


## <span id="ddk_system_syntax_dbg"></span><span id="DDK_SYSTEM_SYNTAX_DBG"></span>


Many debugger commands have process identifiers as their parameters.

Two vertical bars ( || ) appear before the system identifier. The system identifier can be one of the following values.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">System identifier</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>||.</strong></p></td>
<td align="left"><p>The current system</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>||#</strong></p></td>
<td align="left"><p>The system that caused the current exception or debug event.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>||*</strong></p></td>
<td align="left"><p>All systems.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>||</strong><em>ddd</em></p></td>
<td align="left"><p>The system whose ordinal is <em>ddd</em>.</p></td>
</tr>
</tbody>
</table>

 

Systems are assigned ordinals in the order that the debugger attaches to them.

When debugging begins, the current system is the one that caused the present exception or debug event (or the one that the debugger most recently attached to). That system remains the current system until you specify a new one by using a [**||s (Set Current System)**](--s--set-current-system-.md) command or by using the [Processes and Threads window](processes-and-threads-window.md) in WinDbg.

Example
-------
This example shows three dump files are loaded. System 1 is active and system 2 caused the debug event.

```
||1:1:017> ||
   0 User mini dump: c:\notepad.dmp
.  1 User mini dump: c:\paint.dmp
#  2 User mini dump: c:\calc.dmp

```


Remarks
-------

To work with multiple systems, you can use the [.opendump](-opendump--open-dump-file-.md) to debug multiple crash dumps at the same time. For more information about how to control a multiple-target session, see [Debugging Multiple Targets](debugging-multiple-targets.md).

**Note**   There are complications, when you debug live targets and dump targets together, because commands behave differently for each type of debugging. For example, if you use the **g (Go)** command when the current system is a dump file, the debugger begins executing, but you cannot break back into the debugger, because the break command is not recognized as valid for dump file debugging.




[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20System%20Syntax%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




