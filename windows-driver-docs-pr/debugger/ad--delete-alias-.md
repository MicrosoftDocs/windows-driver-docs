---
title: ad (Delete Alias)
description: The ad command deletes an alias from the alias list.
keywords: ["ad (Delete Alias) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- ad (Delete Alias)
api_type:
- NA
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

### Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

 

### Additional Information

For more information about how to use aliases, see [Using Aliases](using-aliases.md).

## Remarks

You can use the **ad** command to delete any user-named alias. But you cannot use this command to delete a fixed-name alias ($u0 to $u9).

 

 





