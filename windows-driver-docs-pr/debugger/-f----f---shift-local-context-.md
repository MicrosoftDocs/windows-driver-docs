---
title: .f+, .f- (Shift Local Context)
description: The .f+ command shifts the frame index to the next frame in the current stack. The .f- command shifts the frame index to the previous frame in the current stack.
ms.assetid: aade5ec0-4d40-4ff1-9d4b-f3ad81b54b79
keywords: [".f+, .f- (Shift Local Context) Windows Debugging"]
topic_type:
- apiref
api_name:
- .f+, .f- (Shift Local Context)
api_type:
- NA
---

# .f+, .f- (Shift Local Context)


The **.f+** command shifts the frame index to the next frame in the current stack. The **.f-** command shifts the frame index to the previous frame in the current stack.

``` syntax
    .f+  
.f-  
```

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>User mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>Live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>All</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about the local context and other context settings, see [Changing Contexts](changing-contexts.md). For more information about how to display local variables and other memory-related commands, see [Reading and Writing Memory](reading-and-writing-memory.md).

Remarks
-------

The *frame* specifies the local context (scope) that the debugger uses to interpret local variables

The **.f+** and .f- commands are shortcuts for moving to the next and previous frames in the current stack. These commands are equivalent to the following [**.frame**](-frame--set-local-context-.md) commands, but the **.f** commands are shorter for convenience:

-   **.f+** is the same as **.frame @$frame + 1**.

-   **.f-** is the same as **.frame @$frame - 1**.

The dollar sign ($) identifies the frame value as a [pseudo-register](pseudo-register-syntax.md). The at sign (@ causes the debugger to access the value more quickly, because it notifies the debugger that a string is a register or pseudo-register.

When an application is running, the meaning of local variables depends on the location of the program counter, because the scope of such variables extends only to the function that they are defined in. Unless you use an **.f+** or **.f-** command (or a [**.frame**](-frame--set-local-context-.md) command), the debugger uses the scope of the current function (the current frame on the stack) as the local context.

The *frame number* is the position of the stack frame within the stack trace. You can view this stack trace by using the [**k, kb, kc, kd, kp, kP, kv (Display Stack Backtrace)**](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md) command or the [Calls window](calls-window.md). The first line (the current frame) represents frame number 0. The subsequent lines represent frame numbers 1, 2, 3, and so on.

You can set the local context to a different stack frame to view new local variable information. However, the actual variables that are available depend on the code that is executed.

The debugger resets the local context to the scope of the program counter if any program execution occurs. The local context is reset to the top stack frame if the register context is changed.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.f+,%20.f-%20%28Shift%20Local%20Context%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




