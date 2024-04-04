---
title: ".trap (Display Trap Frame)"
description: "The .trap command displays the trap frame register state and also sets the register context."
keywords: ["Display Trap Frame (.trap) command", "trap frame", ".trap (Display Trap Frame) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .trap (Display Trap Frame)
api_type:
- NA
---

# .trap (Display Trap Frame)

The **.trap** command displays the trap frame register state and also sets the register context.

```dbgcmd
.trap [Address]
```

## Parameters

<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Hexadecimal address of the trap frame on the target system. Omitting the address does not display any trap frame information, but it does reset the register context.

## Environment

|  Item       | Description       |
|-----------|------------------|
| Modes     | kernel mode only |
| Targets   | live, crash dump |
| Platforms | all              |

## Additional Information

For more information about the register context and other context settings, see [Changing Contexts](../debugger/changing-contexts.md).

## Remarks

The **.trap** command displays the important registers for the specified trap frame.

This command also instructs the kernel debugger to use the specified context record as the register context. After this command is executed, the debugger will have access to the most important registers and the stack trace for this thread. This register context persists until you allow the target to execute or use another register context command ([**.thread**](-thread--set-register-context-.md), [**.cxr**](-cxr--display-context-record-.md), or **.trap**). See [Register Context](../debugger/changing-contexts.md#register-context) for full details.

This extension is commonly used when debugging bug check 0xA and 0x7F. For details and an example, see [**Bug Check 0xA**](../debugger/bug-check-0xa--irql-not-less-or-equal.md) (IRQL\_NOT\_LESS\_OR\_EQUAL).
