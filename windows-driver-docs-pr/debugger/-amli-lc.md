---
title: amli lc
description: The amli lc extension lists all active ACPI contexts.
ms.assetid: 070db570-ab8c-47ce-88fa-dc5f16c1c2ee
keywords: ["amli lc Windows Debugging"]
ms.author: domars
ms.date: 09/17/2018
topic_type:
- apiref
api_name:
- amli lc
api_type:
- NA
ms.localizationpriority: medium
---

# !amli lc


The **!amli lc** extension lists all active ACPI contexts.

Syntax

```dbgcmd
   !amli lc
```

## <span id="ddk__amli_lc_dbg"></span><span id="DDK__AMLI_LC_DBG"></span>


### <span id="DLL"></span><span id="dll"></span>DLL

Kdexts.dll

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about related commands and their uses, see [The AMLI Debugger](the-amli-debugger.md).

Remarks
-------

Each context corresponds to a method currently running in the AML interpreter.

Here is an example:

```console
AMLI(? for help)-> lc
 Ctxt=80e3f000, ThID=00000000, Flgs=A--C-----, pbOp=00000000, Obj=\_SB.LNKA._STA
 Ctxt=80e41000, ThID=00000000, Flgs=A--C-----, pbOp=00000000, Obj=\_SB.LNKB._STA
 Ctxt=80e9a000, ThID=00000000, Flgs=A--C-----, pbOp=00000000, Obj=\_SB.LNKC._STA
 Ctxt=80ea8000, ThID=00000000, Flgs=A--C-----, pbOp=00000000, Obj=\_SB.LNKD._STA
*Ctxt=80e12000, ThID=80e6eda8, Flgs=---CR----, pbOp=80e5d5ac, Obj=\_SB.LNKA._STA
```

The **Obj** field gives the full path and name of the method as it appears in the ACPI tables.

The **Ctxt** field gives the address of the context block. The asterisk (**\\**<em>) indicates the *current context</em>. This is the context that was being executed by the interpreter when the break occurred.

The abbreviation **pbOp** indicates the instruction pointer (pointer to binary op codes).

There are nine flags that can be displayed in the **Flgs** section. If a flag is not set, a hyphen is displayed instead. The full list of flags is as follows:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Flag</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>A</p></td>
<td align="left"><p>Asynchronous evaluation</p></td>
</tr>
<tr class="even">
<td align="left"><p>N</p></td>
<td align="left"><p>Nested evaluation</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Q</p></td>
<td align="left"><p>In the ready queue</p></td>
</tr>
<tr class="even">
<td align="left"><p>C</p></td>
<td align="left"><p>Needs a callback</p></td>
</tr>
<tr class="odd">
<td align="left"><p>R</p></td>
<td align="left"><p>Running</p></td>
</tr>
<tr class="even">
<td align="left"><p>W</p></td>
<td align="left"><p>Ready</p></td>
</tr>
<tr class="odd">
<td align="left"><p>T</p></td>
<td align="left"><p>Time-out</p></td>
</tr>
<tr class="even">
<td align="left"><p>D</p></td>
<td align="left"><p>Timer dispatch</p></td>
</tr>
<tr class="odd">
<td align="left"><p>P</p></td>
<td align="left"><p>Timer pending</p></td>
</tr>
</tbody>
</table>

 

 

 





