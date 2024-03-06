---
title: .hh (Open HTML Help File)
description: The .hh command opens the Debugging Tools for Windows documentation.
keywords: [".hh (Open HTML Help File) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .hh (Open HTML Help File)
api_type:
- NA
---

# .hh (Open HTML Help File)


The **.hh** command opens the Debugging Tools for Windows documentation.

```dbgcmd
.hh [Text] 
```

## <span id="ddk_meta_open_html_help_file_dbg"></span><span id="DDK_META_OPEN_HTML_HELP_FILE_DBG"></span>Parameters


<span id="_______Text______"></span><span id="_______text______"></span><span id="_______TEXT______"></span> *Text*   
Specifies the text to find in the index of the Help documentation.

### Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

 

You cannot use this command when you are performing [remote debugging through Remote.exe](../debugger/remote-debugging-through-remote-exe.md).

### Additional Information

For more information about the Help documentation, see [Using the Help File](../debugger/using-the-help-documentation.md).

## Remarks

The **.hh** command opens the Debugging Tools for Windows documentation (Debugger.chm). If you specify *Text*, the debugger opens the **Index** pane in the documentation and searches for *Text* as a keyword in the index. If you do not specify *Text*, the debugger opens the **Contents** pane of the documentation.

 

 





