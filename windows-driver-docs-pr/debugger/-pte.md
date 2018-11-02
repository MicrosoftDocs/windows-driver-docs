---
title: pte
description: The pte extension displays the page table entry (PTE) and page directory entry (PDE) for the specified address.
ms.assetid: e5603e58-8d9f-4693-bca2-a319080187cc
keywords: ["page table entry (PTE)", "PTE (page table entry)", "page directory entry (PDE)", "PDE (page directory entry)", "pte Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- pte
api_type:
- NA
ms.localizationpriority: medium
---

# !pte


The **!pte** extension displays the page table entry (PTE) and page directory entry (PDE) for the specified address.

Syntax

```dbgcmd
!pte VirtualAddress 
!pte PTE 
!pte LiteralAddress 1 
```

## <span id="ddk__pte_dbg"></span><span id="DDK__PTE_DBG"></span>Parameters


<span id="_______VirtualAddress______"></span><span id="_______virtualaddress______"></span><span id="_______VIRTUALADDRESS______"></span> *VirtualAddress*   
Specifies the virtual address whose page table is desired.

<span id="_______PTE______"></span><span id="_______pte______"></span> *PTE*   
Specifies the address of an actual PTE.

<span id="_______LiteralAddress_______1______"></span><span id="_______literaladdress_______1______"></span><span id="_______LITERALADDRESS_______1______"></span> *LiteralAddress* **** **1**   
Specifies the address of an actual PTE or PDE.

### <span id="DLL"></span><span id="dll"></span>DLL

Kdexts.dll

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about page tables, page directories, and an explanation of the status bits, see *Microsoft Windows Internals*, by Mark Russinovich and David Solomon. (This book may not be available in some languages and countries.)

Remarks
-------

If one parameter is supplied and this parameter is an address in the region of memory where the page tables are stored, the debugger treats this as the *PTE* parameter. This parameter is taken as the actual address of the desired PTE, and the debugger will display this PTE and the corresponding PDE.

If one parameter is supplied and this parameter is not an address in this region, the debugger treats this as the *VirtualAddress* parameter. The PTE and PDE that hold the mapping for this address are displayed.

If two parameters are supplied and the second parameter is **1** (or any other small number), the debugger treats the first parameter as *LiteralAddress*. This address is interpreted as the actual address of a PTE and also as the actual address of a PDE, and the corresponding (and possibly invalid) data will be shown.

(x86 or x64 target computer only) If two parameters are supplied and the second parameter is greater than the first, the debugger treats the two parameters as *StartAddress* and *EndAddress*. The command then displays the PTEs for each page in the specified memory range.

For a list of all system PTEs, use the [**!sysptes**](-sysptes.md) extension.

Here is an example from an x86 target computer:

```dbgcmd
kd> !pte 801544f4
801544F4  - PDE at C0300800        PTE at C0200550
          contains 0003B163      contains 00154121
        pfn 3b G-DA--KWV    pfn 154 G--A--KRV
```

The first line of this example restates the virtual address being investigated. It then gives the virtual address of the PDE and the PTE, which contain information about the virtual-physical mapping of this address.

The second line gives the actual contents of the PDE and the PTE.

The third line takes these contents and analyzes them, breaking them into the page frame number (PFN) and the status bits.

See the [**!pfn**](-pfn.md) extension or the [Converting Virtual Addresses to Physical Addresses](converting-virtual-addresses-to-physical-addresses.md) section for information about how to interpret and use the PFN.

On an x86 or x64 target computer, the status bits for the PDE and the PTE are shown in the following table. The **!pte** display indicates these bits with capital letters or dashes, and adds additional information as well.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Bit</th>
<th align="left">Display when set</th>
<th align="left">Display when clear</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x200</p></td>
<td align="left"><p>C</p></td>
<td align="left"><p>-</p></td>
<td align="left"><p>Copy on write.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x100</p></td>
<td align="left"><p>G</p></td>
<td align="left"><p>-</p></td>
<td align="left"><p>Global.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x80</p></td>
<td align="left"><p>L</p></td>
<td align="left"><p>-</p></td>
<td align="left"><p>Large page. This only occurs in PDEs, never in PTEs.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x40</p></td>
<td align="left"><p>D</p></td>
<td align="left"><p>-</p></td>
<td align="left"><p>Dirty.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x20</p></td>
<td align="left"><p>A</p></td>
<td align="left"><p>-</p></td>
<td align="left"><p>Accessed.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x10</p></td>
<td align="left"><p>N</p></td>
<td align="left"><p>-</p></td>
<td align="left"><p>Cache disabled.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x8</p></td>
<td align="left"><p>T</p></td>
<td align="left"><p>-</p></td>
<td align="left"><p>Write-through.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x4</p></td>
<td align="left"><p>U</p></td>
<td align="left"><p>K</p></td>
<td align="left"><p>Owner (user mode or kernel mode).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x2</p></td>
<td align="left"><p>W</p></td>
<td align="left"><p>R</p></td>
<td align="left"><p>Writeable or read-only. Only on multiprocessor computers and any computer running Windows Vista or later.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x1</p></td>
<td align="left"><p>V</p></td>
<td align="left"></td>
<td align="left"><p>Valid.</p></td>
</tr>
<tr class="odd">
<td align="left"></td>
<td align="left"><p>E</p></td>
<td align="left"><p>-</p></td>
<td align="left"><p>Executable page. For platforms that do not support a hardware execute/noexecute bit, including many x86 systems, the E is always displayed.</p></td>
</tr>
</tbody>
</table>

 

On an Itanium target computer, the status bits for the PDE and the PTE are slightly different from those of the PPE. The Itanium PPE bits are as follows:

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Display when set</th>
<th align="left">Display when clear</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>V</p></td>
<td align="left"></td>
<td align="left"><p>Valid.</p></td>
</tr>
<tr class="even">
<td align="left"><p>U</p></td>
<td align="left"><p>K</p></td>
<td align="left"><p>Owner (user mode or kernel mode).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>D</p></td>
<td align="left"><p>-</p></td>
<td align="left"><p>Dirty.</p></td>
</tr>
<tr class="even">
<td align="left"><p>A</p></td>
<td align="left"><p>-</p></td>
<td align="left"><p>Accessed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>W</p></td>
<td align="left"><p>R</p></td>
<td align="left"><p>Writeable or read-only. Only on multiprocessor computers and any computer running Windows Vista or later.</p></td>
</tr>
<tr class="even">
<td align="left"><p>E</p></td>
<td align="left"><p>-</p></td>
<td align="left"><p>Execute.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>C</p></td>
<td align="left"><p>-</p></td>
<td align="left"><p>Copy on write.</p></td>
</tr>
</tbody>
</table>

 

 

 





