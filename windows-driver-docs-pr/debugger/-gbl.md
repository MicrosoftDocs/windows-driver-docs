---
title: gbl
description: The gbl extension displays header information from the ACPI BIOS Root System Description (RSDT) table of the target computer.
ms.assetid: 1fc59112-27c4-465c-b460-8d6b0e83a39b
keywords: ["ACPI (Advanced Configuration and Power Interface), RSDT header information", "global lock", "gbl Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- gbl
api_type:
- NA
ms.localizationpriority: medium
---

# !gbl


The **!gbl** extension displays header information from the ACPI BIOS Root System Description (RSDT) table of the target computer.

```dbgcmd
!gbl [-v]
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______-v______"></span><span id="_______-V______"></span> **-v**   
Verbose. Displays detailed information about the table.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Unavailable</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Kdexts.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about the ACPI and ACPI tables, see [Other ACPI Debugging Extensions](other-acpi-debugging-extensions.md) and the [ACPI Specification](https://go.microsoft.com/fwlink/p/?linkid=57185) Web site. Also see the Microsoft Windows SDK documentation, the Windows Driver Kit (WDK) documentation, and *Microsoft Windows Internals* by Mark Russinovich and David Solomon. (These resources may not be available in some languages and countries.)

 

 





