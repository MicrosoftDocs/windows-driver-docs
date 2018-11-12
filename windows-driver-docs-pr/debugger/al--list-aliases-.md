---
title: al (List Aliases)
description: The al command displays a list of all currently defined user-named aliases.
ms.assetid: 40e20edb-4545-4c5a-bb56-61e00b064efc
keywords: ["al (List Aliases) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- al (List Aliases)
api_type:
- NA
ms.localizationpriority: medium
---

# al (List Aliases)


The **al** command displays a list of all currently defined user-named aliases.

```dbgcmd
al
```

## <span id="ddk_cmd_list_aliases_dbg"></span><span id="DDK_CMD_LIST_ALIASES_DBG"></span>


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
<td align="left"><p>All</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about how to use aliases, see [Using Aliases](using-aliases.md).

Remarks
-------

The **al** command lists all user-named aliases. But this command does not list fixed-name aliases ($u0 to $u9).

 

 





