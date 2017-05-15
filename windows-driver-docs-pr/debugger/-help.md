---
title: help
description: The help extension displays help text that describes the extension commands exported from the extension DLL.
ms.assetid: 9d01856e-4906-43cb-a445-71cce011a973
keywords: ["help Windows Debugging"]
topic_type:
- apiref
api_name:
- help
api_type:
- NA
---

# !help


The **!help** extension displays help text that describes the extension commands exported from the extension DLL.

Do not confuse this extension command with the [**? (Command Help)**](---command-help-.md) or [**.help (Meta-Command Help)**](-help--meta-command-help-.md) commands.

``` syntax
    ![ExtensionDLL.]help [-v] [CommandName] 
```

## <span id="ddk__help_dbg"></span><span id="DDK__HELP_DBG"></span>Parameters


<span id="_______ExtensionDLL______"></span><span id="_______extensiondll______"></span><span id="_______EXTENSIONDLL______"></span> *ExtensionDLL*   
Displays help for the specified extension DLL. Type the name of an extension DLL without the .dll file name extension. If the DLL file is not in the extension search path (as displayed by using [**.chain (List Debugger Extensions)**](-chain--list-debugger-extensions-.md)), include the path to the DLL file. For example, to display help for uext.dll, type **!uext.help** or **!***Path***\\winext\\uext.help**.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!help%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




