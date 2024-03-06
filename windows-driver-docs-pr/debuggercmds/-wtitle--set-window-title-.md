---
title: .wtitle (Set Window Title)
description: The .wtitle command sets the title in the main WinDbg window or in the NTSD, CDB, or KD window.
keywords: [".wtitle (Set Window Title) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .wtitle (Set Window Title)
api_type:
- NA
---

# .wtitle (Set Window Title)


The **.wtitle** command sets the title in the main WinDbg window or in the NTSD, CDB, or KD window.

```dbgcmd
.wtitle Title 
```

## <span id="ddk_meta_set_window_title_dbg"></span><span id="DDK_META_SET_WINDOW_TITLE_DBG"></span>Parameters


<span id="_______Title______"></span><span id="_______title______"></span><span id="_______TITLE______"></span> *Title*   
The title to use for the window.

### Environment

This command cannot be used in script files.

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

 

## Remarks

For CDB, NTSD, or KD, if the **.wtitle** command has not been used, the window title matches the command line used to launch the debugger.

For WinDbg, if **.wtitle** has not been used, the main window title includes the name of the target. If a debugging server is active, its connection string is displayed as well. If multiple debugging servers are active, only the most recent one is displayed.

When **.wtitle** is used, *Title* replaces all this information. Even if a debugging server is started later, *Title* will not change.

The WinDbg version number is always displayed in the window title bar, regardless of whether this command is used.

 

 





