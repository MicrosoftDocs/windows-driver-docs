---
title: "!owner (WinDbg)"
description: "The !owner extension displays the owner of a module or function."
keywords: ["!owner Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- owner
api_type:
- NA
---

# !owner


The **!owner** extension displays the owner of a module or function.

```dbgcmd
!owner [Module[!Symbol]]
```

## <span id="ddk__owner_dbg"></span><span id="DDK__OWNER_DBG"></span>Parameters


<span id="_______Module______"></span><span id="_______module______"></span><span id="_______MODULE______"></span> *Module*   
Specifies the module whose owner is desired. An asterisk (\*) at the end of *Module* represents any number of additional characters.

<span id="_______Symbol______"></span><span id="_______symbol______"></span><span id="_______SYMBOL______"></span> *Symbol*   
Specifies the symbol within *Module* whose owner is desired. An asterisk (\*) at the end of *Symbol* represents any number of additional characters. If *Symbol* is omitted, the owner of the entire module is displayed.

## DLL


Ext.dll



 

## Remarks

If no parameters are used and a fault has occurred, **!owner** will display the name of the owner of the faulting module or function.

When you pass a module or function name to the **!owner** extension, the debugger displays the word **Followup** followed by the name of owner of the specified module or function.

For this extension to display useful information, you must first create a triage.ini file containing the names of the module and function owners.

For details on the triage.ini file and an example of the **!owner** extension, see [Specifying Module and Function Owners](../debugger/specifying-module-and-function-owners.md).

