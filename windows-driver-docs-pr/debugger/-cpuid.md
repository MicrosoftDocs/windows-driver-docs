---
title: cpuid
description: The cpuid extension displays information about the processors on the system.
ms.assetid: 3dbd1079-d129-4e17-8d06-18b25fdd17c9
keywords: ["cpuid Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- cpuid
api_type:
- NA
ms.localizationpriority: medium
---

# !cpuid


The **!cpuid** extension displays information about the processors on the system.

```dbgsyntax
!cpuid [Processor]
```

## <span id="ddk__cpuid_dbg"></span><span id="DDK__CPUID_DBG"></span>Parameters


<span id="_______Processor______"></span><span id="_______processor______"></span><span id="_______PROCESSOR______"></span> *Processor*   
Specifies the processor whose information will be displayed. If you omit this parameter, all processors are displayed.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Ext.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Ext.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about how to debug multiprocessor computers, see [Multiprocessor Syntax](multiprocessor-syntax.md).

Remarks
-------

The **!cpuid** extension works during live user-mode or kernel-mode debugging, local kernel debugging, and debugging of dump files. However, user-mode minidump files contain only information about the active processor.

If you are debugging in user mode, the **!cpuid** extension describes the computer that the target application is running on. In kernel mode, it describes the target computer.

The following example shows this extension.

```dbgcmd
kd> !cpuid 
CP  F/M/S  Manufacturer        MHz 
 0  6,5,1  GenuineIntel        700 
 1  8,1,5  AuthenticAMD        700 
```

The **CP** column gives the processor number. (These numbers are always sequential, starting with zero). The **Manufacturer** column specifies the processor manufacturer. The **MHz** column specifies the processor speed, if it is available.

For an x86-based processor or an x64-based processor, the **F** column displays the processor family number, the **M** column displays the processor model number, and the **S** column displays the stepping size.

For an Itanium-based processor, the **M** column displays the processor model number, the R column displays the processor revision number, the **F** column displays the processor family number, and the **A** column displays the architecture revision number.

 

 





