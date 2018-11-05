---
title: .browse (Display Command in Browser)
description: The .browse command displays the output of a specified command in a new Command Browser window.
ms.assetid: 37822DDE-8AA8-4DB9-8213-08E73110ACE5
keywords: [".browse (Display Command in Browser) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .browse (Display Command in Browser)
api_type:
- NA
ms.localizationpriority: medium
---

# .browse (Display Command in Browser)


The **.browse** command displays the output of a specified command in a new [Command Browser window](command-browser-window.md).

```dbgcmd
.browse Command
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="Command"></span><span id="command"></span><span id="COMMAND"></span>*Command*  
The command to be executed and displayed in a new Command Browser window.

Remarks
-------

The following example uses the **.browse** command to display the output of the [**.chain /D**](-chain--list-debugger-extensions-.md) command in a Command Browser window.

```dbgcmd
.browse .chain /D
```

 

 





