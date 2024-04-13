---
title: "!gflag (WinDbg)"
description: "The !gflag extension sets or displays the global flags."
keywords: ["!gflag Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- gflag
api_type:
- NA
---

# !gflag

The **!gflag** extension sets or displays the global flags.

```dbgcmd
!gflag [+|-] Value 
!gflag {+|-} Abbreviation 
!gflag -? 
!gflag 
```

## Parameters

<span id="_______Value______"></span><span id="_______value______"></span><span id="_______VALUE______"></span> *Value*   
Specifies a 32-bit hexadecimal number. If you do not use a plus sign (**+**) or minus sign (**-**), this number becomes the new value of the global flag bit field. If you add a plus sign (**+**) before this number, the number specifies one or more global flag bits to set to 1. If you add a minus sign (**-**) before this number, the number specifies one or more global flag bits to set to zero.

<span id="_______Abbreviation______"></span><span id="_______abbreviation______"></span><span id="_______ABBREVIATION______"></span> *Abbreviation*   
Specifies a single global flag. *Abbreviation* is a three-letter abbreviation for a global flag that is set to 1 (**+**) or to zero (**-**).

<span id="_______-_______"></span> **-?**   
Displays some Help text for this extension, including a list of global flag abbreviations, in the [Debugger Command window](../debugger/debugger-command-window.md).

## DLL

Exts.dll

## Additional Information

You can also set these flags by using the Global Flags utility (Gflags.exe).

## Remarks

If you do not specify any arguments, the **!gflag** extension displays the current global flag settings.

The following table contains the abbreviations that you can use for the *Abbreviation* parameter.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Value</th>
<th align="left">Name</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x00000001</p></td>
<td align="left"><p>"soe"</p></td>
<td align="left"><p>Stop on exception.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x00000002</p></td>
<td align="left"><p>"sls"</p></td>
<td align="left"><p>Show loader snaps.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x00000004</p></td>
<td align="left"><p>"dic"</p></td>
<td align="left"><p>Debug initial command.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x00000008</p></td>
<td align="left"><p>"shg"</p></td>
<td align="left"><p>Stop if the GUI stops responding (that is, hangs).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x00000010</p></td>
<td align="left"><p>"htc"</p></td>
<td align="left"><p>Enable heap tail checking.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x00000020</p></td>
<td align="left"><p>"hfc"</p></td>
<td align="left"><p>Enable heap free checking.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x00000040</p></td>
<td align="left"><p>"hpc"</p></td>
<td align="left"><p>Enable heap parameter checking.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x00000080</p></td>
<td align="left"><p>"hvc"</p></td>
<td align="left"><p>Enable heap validation on call.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x00000100</p></td>
<td align="left"><p>"ptc"</p></td>
<td align="left"><p>Enable pool tail checking.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x00000200</p></td>
<td align="left"><p>"pfc"</p></td>
<td align="left"><p>Enable pool free checking.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x00000400</p></td>
<td align="left"><p>"ptg"</p></td>
<td align="left"><p>Enable pool tagging.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x00000800</p></td>
<td align="left"><p>"htg"</p></td>
<td align="left"><p>Enable heap tagging.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x00001000</p></td>
<td align="left"><p>"ust"</p></td>
<td align="left"><p>Create a user-mode stack trace DB.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x00002000</p></td>
<td align="left"><p>"kst"</p></td>
<td align="left"><p>Create a kernel-mode stack trace DB.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x00004000</p></td>
<td align="left"><p>"otl"</p></td>
<td align="left"><p>Maintain a list of objects for each type.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x00008000</p></td>
<td align="left"><p>"htd"</p></td>
<td align="left"><p>Enable heap tagging by DLL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x00010000</p></td>
<td align="left"><p>"idp"</p></td>
<td align="left"><p>Unused.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x00020000</p></td>
<td align="left"><p>"d32"</p></td>
<td align="left"><p>Enable debugging of the Microsoft Win32 subsystem.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x00040000</p></td>
<td align="left"><p>"ksl"</p></td>
<td align="left"><p>Enable loading of kernel debugger symbols.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x00080000</p></td>
<td align="left"><p>"dps"</p></td>
<td align="left"><p>Disable paging of kernel stacks.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x00100000</p></td>
<td align="left"><p>"scb"</p></td>
<td align="left"><p>Enable critical system breaks.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x00200000</p></td>
<td align="left"><p>"dhc"</p></td>
<td align="left"><p>Disable heap coalesce on free.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x00400000</p></td>
<td align="left"><p>"ece"</p></td>
<td align="left"><p>Enable close exception.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x00800000</p></td>
<td align="left"><p>"eel"</p></td>
<td align="left"><p>Enable exception logging.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x01000000</p></td>
<td align="left"><p>"eot"</p></td>
<td align="left"><p>Enable object handle type tagging.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x02000000</p></td>
<td align="left"><p>"hpa"</p></td>
<td align="left"><p>Put heap allocations at the end of pages.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x04000000</p></td>
<td align="left"><p>"dwl"</p></td>
<td align="left"><p>Debug WINLOGON.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x08000000</p></td>
<td align="left"><p>"ddp"</p></td>
<td align="left"><p>Disable kernel-mode <strong>DbgPrint</strong> and <strong>KdPrint</strong> output.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x10000000</p></td>
<td align="left"><p>NULL</p></td>
<td align="left"><p>Unused.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x20000000</p></td>
<td align="left"><p>"sue"</p></td>
<td align="left"><p>Stop on unhandled user-mode exception</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x40000000</p></td>
<td align="left"><p>NULL</p></td>
<td align="left"><p>Unused.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x80000000</p></td>
<td align="left"><p>"dpd"</p></td>
<td align="left"><p>Disable protected DLL verification.</p></td>
</tr>
</tbody>
</table>
