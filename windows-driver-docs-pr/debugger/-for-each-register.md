---
title: for\_each\_register
description: The for\_each\_register extension executes a specified command for each register.
ms.assetid: 496DC161-D082-4C83-A6B6-6BBCE932BE76
keywords: ["for_each_register Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- for_each_register
api_type:
- NA
---

# !for\_each\_register


The **!for\_each\_register** extension executes a specified command for each register.

``` syntax
!for_each_register -c:CommandString
!for_each_register -?
```

## <span id="ddk__for_each_module_dbg"></span><span id="DDK__FOR_EACH_MODULE_DBG"></span>Parameters


<span id="_______-c_CommandString______"></span><span id="_______-c_commandstring______"></span><span id="_______-C_COMMANDSTRING______"></span> **-c:***CommandString*   
Specifies the command to be executed for each register. The aliases @\#RegisterName and @\#RegisterValue are valid during the execution of the command.

<span id="_______-_______"></span> **-?**   
Displays help for the **!for\_each\_register** extension.

## <span id="DLL"></span><span id="dll"></span>DLL


Ext.dll

## <span id="Examples"></span><span id="examples"></span><span id="EXAMPLES"></span>Examples


This example lists the name of each register.

``` syntax
0:000> !for_each_register -c:.echo @#RegisterName
rax
rcx
rdx
rbx
...
```

This example executes [**!address**](-address.md) for each register value.

``` syntax
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!for_each_register%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




