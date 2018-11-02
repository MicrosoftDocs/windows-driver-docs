---
title: smt
description: The smt extension displays a summary of the simultaneous multithreaded processor information.
ms.assetid: 28c07f89-6208-4b04-b7b9-825dda4f5f5a
keywords: ["smt Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- smt
api_type:
- NA
ms.localizationpriority: medium
---

# !smt


The **!smt** extension displays a summary of the simultaneous multithreaded processor information.

```dbgcmd
!smt
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

 

Remarks
-------

Here is an example:

```dbgcmd
lkd> !smt 
SMT Summary:
------------
   KeActiveProcessors: **------------------------------ (00000003)
        KiIdleSummary: -------------------------------- (00000000)
 No PRCB     Set Master SMT Set                                     IAID
  0 820f4820 Master     **------------------------------ (00000003)  00
  1 87a4d120 820f4820   **------------------------------ (00000003)  01

Maximum cores per physical processor:   2
Maximum logical processors per core:    1
```

The **No** column indicates the number of the processor.

The **PRCB** column indicates the address of the processor control block for the processor. Each logical processor is listed separately.

Each physical processor has exactly one logical processor listed as the **Master** under the **Set Master** column.

The **SMT Set** column lists the processor's simultaneous multithreaded processor set information.

The **IAID** column lists the initial Advanced Programmable Interrupt Controller identifier (APIC ID). On a true x64 computer, each processor starts with a hard-coded initial APIC ID. This ID value can be retrieved through the CPUID instruction. On certain other computers, the initial APIC ID is not necessarily unique across all processors, so the APIC ID that is accessible through the APIC's memory-mapped input/output (MMIO) space can be modified. This technique enables software to allocate unique APIC IDs for all processors within the computer. Depending on the target computer's processors, the **IAID** column may show this ID or may be blank.

 

 





