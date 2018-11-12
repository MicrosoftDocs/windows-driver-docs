---
title: .fpo (Control FPO Overrides)
description: The .fpo command controls the frame pointer omission (FPO) overrides.
ms.assetid: a1a20f5d-71c9-487b-bcba-a87b60d74588
keywords: [".fpo (Control FPO Overrides) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .fpo (Control FPO Overrides)
api_type:
- NA
ms.localizationpriority: medium
---

# .fpo (Control FPO Overrides)


The **.fpo** command controls the frame pointer omission (FPO) overrides.

```dbgcmd
.fpo -s [-fFlag] Address 
.fpo -d Address 
.fpo -x Address 
.fpo -o Address 
.fpo Address 
```

## <span id="ddk_meta_control_fpo_overrides_dbg"></span><span id="DDK_META_CONTROL_FPO_OVERRIDES_DBG"></span>Parameters


<span id="_______-s______"></span><span id="_______-S______"></span> **-s**   
Sets an FPO override at the specified address.

<span id="_______-fFlag______"></span><span id="_______-fflag______"></span><span id="_______-FFLAG______"></span> **-f***Flag*   
Specifies FPO flags for the override. You must not add a space between **-f** and *Flag*. If the flag takes an argument, you must add a space between the flag and that argument. If you want multiple flags, you must repeat the **-f** switch (for example, **-fb -fp 4 -fe**). You can use the **-f** switch only with **-s**. You can use one of the following values for *Flag*.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Flag</th>
<th align="left">Effect</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>b</strong></p></td>
<td align="left"><p>Sets <strong>fUseBP</strong> equal to <strong>TRUE</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>e</strong></p></td>
<td align="left"><p>Sets <strong>fUseSEH</strong> equal to <strong>TRUE</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>n</strong></p></td>
<td align="left"><p>Sets <strong>cbFrame</strong> equal to FRAME_NONFPO. (By default, cbFrame is set to FRAME_FPO.)</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>l</strong> <strong></strong> <em>Term</em></p></td>
<td align="left"><p>Sets <strong>cdwLocals</strong> equal to <em>Term</em>. <em>Term</em> should specify the local DWORD count that you want.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>p</strong> <strong></strong> <em>Term</em></p></td>
<td align="left"><p>Sets <strong>cdwParams</strong> equal to <em>Term</em>. <em>Term</em> should specify the parameter DWORD count that you want.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>r</strong> <strong></strong> <em>Term</em></p></td>
<td align="left"><p>Sets <strong>cbRegs</strong> equal to <em>Term</em>. <em>Term</em> should specify the register count that you want.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>s</strong> <strong></strong> <em>Term</em></p></td>
<td align="left"><p>Sets <strong>cbProcSize</strong> equal to <em>Term</em>. <em>Term</em> should specify the procedure size that you want.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>t</strong> <strong></strong> <em>Term</em></p></td>
<td align="left"><p>Sets <strong>cbFrame</strong> equal to <em>Term</em>. <em>Term</em> should specify one of the following frame types:</p>
<ul>
<li><p>FRAME_FPO 0</p></li>
<li><p>FRAME_TRAP 1</p></li>
<li><p>FRAME_TSS 2</p></li>
<li><p>FRAME_NONFPO 3</p></li>
</ul></td>
</tr>
</tbody>
</table>

 

<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address where the debugger sets or removes the override or the address whose overrides the debugger should display. This address must be within a module in the current module list.

<span id="_______-d______"></span><span id="_______-D______"></span> -**d**   
Removes the FPO overrides at the specified address.

<span id="_______-x______"></span><span id="_______-X______"></span> **-x**   
Removes all FPO overrides within the module that contains the *Address* address.

<span id="_______-o______"></span><span id="_______-O______"></span> **-o**   
Displays all FPO overrides within the module that contains the *Address* address.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>User mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>Live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>all</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Without parameters, the **.fpo** command displays the FPO overrides for the specified address.

Some compilers (including Microsoft Visual Studio 6.0 and earlier versions) generate FPO information to indicate how the stack frame is set up. During stack walking, the debugger uses these FPO records to understand the stack. If the compiler generated incorrect FPO information, you can use the **.fpo** command to fix this problem.

 

 





