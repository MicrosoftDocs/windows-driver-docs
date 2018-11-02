---
title: .netsyms (Disable Network Symbol Loading)
description: .netsyms (Disable Network Symbol Loading)
ms.assetid: 09347909-47C8-4a4d-8246-C32A1791F46B
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# .netsyms (Disable Network Symbol Loading)


## <span id="ddk_apc_meta_netsyms_dbg"></span><span id="DDK_APC_META_NETSYMS_DBG"></span>


Use the .netsyms command to allow or disallow loading symbols from a network path.

### <span id="kd_syntax"></span><span id="KD_SYNTAX"></span>Syntax

**.netsyms** *{yes|no}*

### <span id="parameters"></span><span id="PARAMETERS"></span>Parameters

<span id="yes"></span><span id="YES"></span>*yes*  
Enables network symbol loading. This is the default.

<span id="no"></span><span id="NO"></span>*no*  
Disables network symbol loading.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>user mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>all</p></td>
</tr>
</tbody>
</table>

 

### <span id="remarks"></span><span id="REMARKS"></span>Remarks

Use .netsyms with no argument to display the current state of this setting.

Use [**!sym noisy**](-sym.md) or the *-n* [**WinDbg Command-Line Option**](windbg-command-line-options.md) to display additional detail as symbols are loaded.

 

 





