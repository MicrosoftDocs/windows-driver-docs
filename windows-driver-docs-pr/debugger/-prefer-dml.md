---
title: .prefer_dml (Prefer Debugger Markup Language)
description: The .prefer_dml command sets the default behavior for commands that are capable of providing output in the Debugger Markup Language (DML) format.
ms.assetid: BBB96770-A575-4E31-AE8B-9226BB61727D
keywords: [".prefer_dml (Prefer Debugger Markup Language) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .prefer_dml (Prefer Debugger Markup Language)
api_type:
- NA
ms.localizationpriority: medium
---

# .prefer\_dml (Prefer Debugger Markup Language)


The **.prefer\_dml** command sets the default behavior for commands that are capable of providing output in the Debugger Markup Language (DML) format.

```dbgcmd
.prefer_dml 0
.prefer_dml 1
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______0"></span> 0  
By default, all commands will provide plain text output.

<span id="_______1"></span> 1  
By default, commands that are capable of providing DML output will provide DML output.

## <span id="see_also"></span>See also


[Debugger Markup Language Commands](debugger-markup-language-commands.md)

 

 






