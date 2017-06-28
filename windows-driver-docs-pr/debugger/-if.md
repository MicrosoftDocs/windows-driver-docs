---
title: .if
description: The .if token behaves like the if keyword in C.
ms.assetid: ccd74461-759f-400d-90da-efba2e4498e6
keywords: [".if Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- .if
api_type:
- NA
---

# .if


The **.if** token behaves like the **if** keyword in C.

```
.if (Condition) { Commands } 

.if (Condition) { Commands } .else { Commands } 

.if (Condition) { Commands } .elsif (Condition) { Commands } 

.if (Condition) { Commands } .elsif (Condition) { Commands } .else { Commands } 
```

## <span id="ddk_token_if_dbg"></span><span id="DDK_TOKEN_IF_DBG"></span>Syntax Elements


<span id="_______Condition______"></span><span id="_______condition______"></span><span id="_______CONDITION______"></span> *Condition*   
Specifies a condition. If this evaluates to zero, it is treated as false; otherwise it is true. Enclosing *Condition* in parentheses is optional. *Condition* must be an expression, not a debugger command. It will be evaluated by the default expression evaluator (MASM or C++). For details, see [Numerical Expression Syntax](numerical-expression-syntax.md).

<span id="_______Commands______"></span><span id="_______commands______"></span><span id="_______COMMANDS______"></span> *Commands*   
Specifies one or more commands that will be executed conditionally. This block of commands needs to be enclosed in braces, even if it consists of a single command. Multiple commands should be separated by semicolons, but the final command before the closing brace does not need to be followed by a semicolon.

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about other control flow tokens and their use in debugger command programs, see [Using Debugger Command Programs](using-debugger-command-programs.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.if%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




