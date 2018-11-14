---
title: .fiximports (Fix Target Module Imports)
description: The .fiximports command validates and corrects all static import links for a target module.
ms.assetid: 584a5060-5ab5-4126-bfec-e2fe647d50ff
keywords: ["Fix Target Module Imports (.fiximports) command", ".fiximports (Fix Target Module Imports) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .fiximports (Fix Target Module Imports)
api_type:
- NA
ms.localizationpriority: medium
---

# .fiximports (Fix Target Module Imports)


The **.fiximports** command validates and corrects all static import links for a target module.

```dbgcmd
.fiximports Module
```

## <span id="ddk_meta_fix_target_module_imports_dbg"></span><span id="DDK_META_FIX_TARGET_MODULE_IMPORTS_DBG"></span>Parameters


<span id="_______Module______"></span><span id="_______module______"></span><span id="_______MODULE______"></span> *Module*   
Specifies the target module whose imports the debugger corrects. *Module* can contain a variety of wildcard characters and specifiers. For more information about the syntax, see [String Wildcard Syntax](string-wildcard-syntax.md). If you want to include spaces in *Module*, you must enclose the parameter in quotation marks.

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
<td align="left"><p>Crash dump only (minidump only)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>All</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

You can use the **.fiximports** command only when the target is a minidump that does not contain its own executable images.

When the debugger maps images for use as memory, the debugger does not automatically connect image imports to exporters. Therefore, instructions that refer to imports are disassembled in the same manner as in a live debugging session. You can use **.fiximports** to request that the debugger perform the appropriate import linking.

 

 





