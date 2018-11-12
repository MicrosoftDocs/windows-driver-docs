---
title: acpiirqarb
description: The acpiirqarb extension displays the contents of the ACPI IRQ arbiter structure, which contains the configuration of I/O devices to system interrupt controller inputs and processor IDT entries.
ms.assetid: c57884cd-c70c-4091-871d-c2a35db8d73f
keywords: ["acpiirqarb Windows Debugging"]
ms.author: domars
ms.date: 09/17/2018
topic_type:
- apiref
api_name:
- acpiirqarb
api_type:
- NA
ms.localizationpriority: medium
---

# !acpiirqarb


The **!acpiirqarb** extension displays the contents of the Advanced Configuration and Power Interface (ACPI) IRQ arbiter structure, which contains the configuration of I/O devices to system interrupt controller inputs and processor interrupt dispatch table (IDT) entries.

```dbgcmd
!acpiirqarb
```

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

For information about the ACPI, see the Microsoft Windows Driver Kit (WDK) documentation, the Windows SDK documentation, and *Microsoft Windows Internals* by Mark Russinovich and David Solomon. (These books and resources may not be available in some languages and countries.) Also see [ACPI Debugging](acpi-debugging.md) for information about other extensions that are associated with the ACPI.

 

 





