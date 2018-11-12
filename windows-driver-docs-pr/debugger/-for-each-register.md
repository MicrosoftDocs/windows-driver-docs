---
title: for_each_register
description: The for_each_register extension executes a specified command for each register.
ms.assetid: 496DC161-D082-4C83-A6B6-6BBCE932BE76
keywords: ["for_each_register Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- for_each_register
api_type:
- NA
ms.localizationpriority: medium
---

# !for\_each\_register


The **!for\_each\_register** extension executes a specified command for each register.

```dbgcmd
!for_each_register -c:CommandString
!for_each_register -?
```

## <span id="ddk__for_each_module_dbg"></span><span id="DDK__FOR_EACH_MODULE_DBG"></span>Parameters


<span id="_______-c_CommandString______"></span><span id="_______-c_commandstring______"></span><span id="_______-C_COMMANDSTRING______"></span> **-c:**<em>CommandString</em>   
Specifies the command to be executed for each register. The aliases @\#RegisterName and @\#RegisterValue are valid during the execution of the command.

<span id="_______-_______"></span> **-?**   
Displays help for the **!for\_each\_register** extension.

## <span id="DLL"></span><span id="dll"></span>DLL


Ext.dll

## <span id="Examples"></span><span id="examples"></span><span id="EXAMPLES"></span>Examples


This example lists the name of each register.

```dbgcmd
0:000> !for_each_register -c:.echo @#RegisterName
rax
rcx
rdx
rbx
...
```

This example executes [**!address**](-address.md) for each register value.

```dbgcmd
0:000> !for_each_register -c:!address ${@#RegisterValue}
...
Usage:                  Stack
Base Address:           00000008`a568f000
End Address:            00000008`a56a0000
Region Size:            00000000`00011000
State:                  00001000    MEM_COMMIT
Protect:                00000004    PAGE_READWRITE
Type:                   00020000    MEM_PRIVATE
Allocation Base:        00000008`a5620000
Allocation Protect:     00000004    PAGE_READWRITE
More info:              ~0k
...
```

Remarks
-------

When an alias is an argument to a debugger extension (for example, [**!address**](-address.md)), use the alias interpreter [**${} (Alias Interpreter)**](-------alias-interpreter-.md) token so that the alias is resolved correctly.

For more information about how to define and use aliases as shortcuts for entering character strings (including use of the [**${}**](-------alias-interpreter-.md) token), see [Using Aliases](using-aliases.md).

 

 





