---
title: ".hh (Open HTML Help File)"
description: "The .hh command opens the Debugging Tools for Windows documentation."
keywords: [".hh (Open HTML Help File) Windows Debugging"]
ms.date: 05/23/2017
ai-usage: ai-assisted
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

## Parameters

<span id="_______Text______"></span><span id="_______text______"></span><span id="_______TEXT______"></span> *Text*   
Specifies the text to find in the index of the Help documentation.

## Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |


You cannot use this command when you are performing [remote debugging through Remote.exe](../debugger/remote-debugging-through-remote-exe.md).

## Additional Information

In current WinDbg builds, **.hh** opens the integrated **Help** toolwindow, which renders the debugger documentation as Markdown content in the debugger UI (instead of the legacy HTML Help viewer). The Help toolwindow provides table-of-contents and search-based navigation, plus browser-style **Home**, **Back**, and **Forward** navigation (including keyboard shortcuts such as Alt+Left, Alt+Right, and Alt+Home).

When *Text* is specified, WinDbg first attempts a keyword lookup and, if no direct keyword match is found, automatically searches and opens the first matching topic.

## Remarks

The **.hh** command opens the Debugging Tools for Windows documentation. If you specify *Text*, the debugger opens the help window and searches for *Text* as a keyword in the index. If you do not specify *Text*, the debugger opens the help window at the top level index.
