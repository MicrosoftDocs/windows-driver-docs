---
title: ad (Delete Alias)
description: The ad command deletes an alias from the alias list.
ms.assetid: 8ff223b6-5cfb-4d87-b45f-ad9bd51faf7f
keywords: ["ad (Delete Alias) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ad (Delete Alias)
api_type:
- NA
ms.localizationpriority: medium
---

# ad (Delete Alias)


The **ad** command deletes an alias from the alias list.

```dbgcmd
ad [/q] Name 
ad * 
```

## <span id="ddk_cmd_delete_alias_dbg"></span><span id="DDK_CMD_DELETE_ALIAS_DBG"></span>Parameters


<span id="________q______"></span><span id="________Q______"></span> **/q**   
Specifies quiet mode. This mode hides the error message if the alias that *Name* specifies does not exist.

<span id="_______Name______"></span><span id="_______name______"></span><span id="_______NAME______"></span> *Name*   
Specifies the name of the alias to delete. If you specify an asterisk (\*), all aliases are deleted (even if there is an alias whose name is "\*").

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

You can use the **ad** command to delete any user-named alias. But you cannot use this command to delete a fixed-name alias ($u0 to $u9).

 

 





