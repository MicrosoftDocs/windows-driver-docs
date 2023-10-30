---
title: al (List Aliases)
description: The al command displays a list of all currently defined user-named aliases.
keywords: ["al (List Aliases) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- al (List Aliases)
api_type:
- NA
---

# al (List Aliases)


The **al** command displays a list of all currently defined user-named aliases.

```dbgcmd
al
```

## <span id="ddk_cmd_list_aliases_dbg"></span><span id="DDK_CMD_LIST_ALIASES_DBG"></span>


### Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

 

### Additional Information

For more information about how to use aliases, see [Using Aliases](using-aliases.md).

## Remarks

The **al** command lists all user-named aliases. But this command does not list fixed-name aliases ($u0 to $u9).

 

 





