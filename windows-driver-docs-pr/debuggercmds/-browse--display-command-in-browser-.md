---
title: ".browse (Display Command in Browser)"
description: "The .browse command displays the output of a specified command in a new Command Browser window."
keywords: [".browse (Display Command in Browser) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .browse (Display Command in Browser)
api_type:
- NA
---

# .browse (Display Command in Browser)


The **.browse** command displays the output of a specified command in a new [Command Browser window](../debugger/command-browser-window.md).

```dbgcmd
.browse Command
```

## Parameters


<span id="Command"></span><span id="command"></span><span id="COMMAND"></span>*Command*  
The command to be executed and displayed in a new Command Browser window.

## Remarks

The following example uses the **.browse** command to display the output of the [**.chain /D**](-chain--list-debugger-extensions-.md) command in a Command Browser window.

```dbgcmd
.browse .chain /D
```

