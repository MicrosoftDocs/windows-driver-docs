---
title: .chain (List Debugger Extensions)
description: The .chain command lists all loaded debugger extensions in their default search order.
ms.assetid: 73139b02-265a-424d-9de8-f4f3736e62db
keywords: [".chain (List Debugger Extensions) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .chain (List Debugger Extensions)
api_type:
- NA
ms.localizationpriority: medium
---

# .chain (List Debugger Extensions)


The **.chain** command lists all loaded debugger extensions in their default search order.

```dbgsyntax
.chain
.chain /D
```

## <span id="ddk_meta_close_handle_dbg"></span><span id="DDK_META_CLOSE_HANDLE_DBG"></span>Parameters


<span id="________D______"></span><span id="________d______"></span> **/D**   
Displays the output using [Debugger Markup Language](debugger-markup-language-commands.md). In the output, each listed module is a link that you can click to get information about the extensions that are implemented by the module.

## <span id="ddk_meta_list_debugger_extensions_dbg"></span><span id="DDK_META_LIST_DEBUGGER_EXTENSIONS_DBG"></span>


### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Modes</p></td>
<td align="left"><p>user mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p>Targets</p></td>
<td align="left"><p>live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Platforms</p></td>
<td align="left"><p>all</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For details on loading, unloading, and controlling extensions, see [Loading Debugger Extension DLLs](loading-debugger-extension-dlls.md). For details on executing extension commands and an explanation of the default search order, see [Using Debugger Extension Commands](using-debugger-extension-commands.md).

 

 





