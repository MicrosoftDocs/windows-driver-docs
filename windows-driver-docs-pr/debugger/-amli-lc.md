---
title: amli lc
description: The amli lc extension lists all active ACPI contexts.
ms.assetid: 070db570-ab8c-47ce-88fa-dc5f16c1c2ee
keywords: ["amli lc Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- amli lc
api_type:
- NA
---

# !amli lc


The **!amli lc** extension lists all active ACPI contexts.

Syntax

```
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

```
AMLI(? for help)-> lc
 Ctxt=80e3f000, ThID=00000000, Flgs=A--C-----, pbOp=00000000, Obj=\_SB.LNKA._STA
 Ctxt=80e41000, ThID=00000000, Flgs=A--C-----, pbOp=00000000, Obj=\_SB.LNKB._STA
 Ctxt=80e9a000, ThID=00000000, Flgs=A--C-----, pbOp=00000000, Obj=\_SB.LNKC._STA
 Ctxt=80ea8000, ThID=00000000, Flgs=A--C-----, pbOp=00000000, Obj=\_SB.LNKD._STA
*Ctxt=80e12000, ThID=80e6eda8, Flgs=---CR----, pbOp=80e5d5ac, Obj=\_SB.LNKA._STA
```

The **Obj** field gives the full path and name of the method as it appears in the ACPI tables.

The **Ctxt** field gives the address of the context block. The asterisk (**\***) indicates the *current context*. This is the context that was being executed by the interpreter when the break occurred.

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

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!amli%20lc%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




