---
title: help
description: The help extension displays help text that describes the extension commands exported from the extension DLL.
ms.assetid: 9d01856e-4906-43cb-a445-71cce011a973
keywords: ["help Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- help
api_type:
- NA
ms.localizationpriority: medium
---

# !help


The **!help** extension displays help text that describes the extension commands exported from the extension DLL.

Do not confuse this extension command with the [**? (Command Help)**](---command-help-.md) or [**.help (Meta-Command Help)**](-help--meta-command-help-.md) commands.

```dbgcmd
![ExtensionDLL.]help [-v] [CommandName] 
```

## <span id="ddk__help_dbg"></span><span id="DDK__HELP_DBG"></span>Parameters


<span id="_______ExtensionDLL______"></span><span id="_______extensiondll______"></span><span id="_______EXTENSIONDLL______"></span> *ExtensionDLL*   
Displays help for the specified extension DLL. Type the name of an extension DLL without the .dll file name extension. If the DLL file is not in the extension search path (as displayed by using [**.chain (List Debugger Extensions)**](-chain--list-debugger-extensions-.md)), include the path to the DLL file. For example, to display help for uext.dll, type **!uext.help** or **!**<em>Path</em>**\\winext\\uext.help**.

If you omit the *ExtensionDLL*, the debugger will display the help text for the first extension DLL in the list of loaded DLLs.

<span id="_______-v______"></span><span id="_______-V______"></span> **-v**   
Displays the most detailed help text available. This feature is not supported in all DLLs.

<span id="_______CommandName______"></span><span id="_______commandname______"></span><span id="_______COMMANDNAME______"></span> *CommandName*   
Displays only the help text for the specified command. This feature is not supported in all DLLs or for all commands.

### <span id="DLL"></span><span id="dll"></span>DLL

This extension is supported by most extension DLLs.

Remarks
-------

Some individual commands will also display a help text if you use the **/?** or **-?** parameter with the command name.

 

 





