---
title: .bugcheck (Display Bug Check Data)
description: The .bugcheck command displays the data from a bug check on the target computer.
ms.assetid: 4b453b5a-4a3c-4056-92e7-b6a17f987fa4
keywords: [".bugcheck (Display Bug Check Data) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .bugcheck (Display Bug Check Data)
api_type:
- NA
ms.localizationpriority: medium
---

# .bugcheck (Display Bug Check Data)


The **.bugcheck** command displays the data from a bug check on the target computer.

```dbgsyntax
    .bugcheck 
```

## <span id="ddk_meta_display_bug_check_data_dbg"></span><span id="DDK_META_DISPLAY_BUG_CHECK_DATA_DBG"></span>


### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>kernel mode only</p></td>
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

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about bug checks, see [Bug Checks (Blue Screens)](bug-checks--blue-screens-.md). For a description of individual bug checks, see the [Bug Check Code Reference](bug-check-code-reference2.md) section.

Remarks
-------

This command displays the current bug check data. (This bug check data will be accessible until the crashed machine is rebooted.)

You can also display bug check data on 32-bit systems by using **dd NT!KiBugCheckData L5**, or on 64-bit systems by using **dq NT!KiBugCheckData L5**. However, the .bugcheck command is more reliable, because it works in some scenarios that the [**d\* (Display Memory)**](d--da--db--dc--dd--dd--df--dp--dq--du--dw--dw--dyb--dyd--display-memor.md) command will not (such as user-mode minidumps).

The [**!analyze**](-analyze.md) extension command is also useful after a bug check occurs.

 

 





