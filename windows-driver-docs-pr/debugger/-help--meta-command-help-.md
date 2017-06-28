---
title: .help (Meta-Command Help)
description: The .help command displays a list of all meta-commands.
ms.assetid: aafd873d-3280-4873-8149-d43f684ec01d
keywords: [".help (Meta-Command Help) Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- .help (Meta-Command Help)
api_type:
- NA
---

# .help (Meta-Command Help)


The **.help** command displays a list of all meta-commands.

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.help%20%28Meta-Command%20Help%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




