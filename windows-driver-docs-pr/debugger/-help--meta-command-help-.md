---
title: .help (Meta-Command Help)
description: The .help command displays a list of all meta-commands.
ms.assetid: aafd873d-3280-4873-8149-d43f684ec01d
keywords: [".help (Meta-Command Help) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .help (Meta-Command Help)
api_type:
- NA
ms.localizationpriority: medium
---

# .help (Meta-Command Help)


The **.help** command displays a list of all meta-commands.

```dbgcmd
.help
.help /D 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="________D"></span><span id="________d"></span> **/D**  
Displays output using [Debugger Markup Language](debugger-markup-language-commands.md). The output contains a list of links that you can click to see the meta-commands that beging with a particular letter.

## <span id="ddk_meta_meta_command_help_dbg"></span><span id="DDK_META_META_COMMAND_HELP_DBG"></span>


### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Modes</p></td>
<td align="left"><p>User mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p>Targets</p></td>
<td align="left"><p>Live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Platforms</p></td>
<td align="left"><p>All</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

For more information about meta-commands, use the **.help** command. For more information about standard commands, use the [**?**](---command-help-.md) command. For more information about extension commands, use the [**!help**](-help.md) extension.

 

 





