---
title: ah (Assertion Handling)
description: The ah command controls the assertion handling status for specific addresses.
keywords: ["ah (Assertion Handling) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- ah (Assertion Handling)
api_type:
- NA
---

# ah (Assertion Handling)

The **ah** command controls the assertion handling status for specific addresses.

```dbgcmd
ahb [Address] 
ahi [Address] 
ahd [Address] 
ahc 
ah 
```

## Parameters

**ahb**

Breaks into the debugger if an assertion fails at the specified address.

**ahi**  
Ignores an assertion failure at the specified address.

**ahd**

Deletes any assertion-handling information at the specified address. This deletion causes the debugger to return to its default state for that address.

*Address*

Specifies the address of the instruction whose assertion-handling status is being set. If you omit this parameter, the debugger uses the current program counter.

**ahc**

Deletes all assertion-handling information for the current process.

**ah**

Displays the current assertion-handling settings.

### Environment

|  Item     | Description            |
|-----------|------------------------|
| Modes     | user mode, kernel mode |
| Targets   | live debugging only    |
| Platforms | all                    |

### Additional Information

For more information about break status and handling status, descriptions of all event codes, a list of the default status for all events, and details about other methods of controlling this status, see [Controlling Exceptions and Events](controlling-exceptions-and-events.md).

## Remarks

The **ah\\*** command controls the assertion handling status for a specific address. The [**sx\* asrt**](sx--sxd--sxe--sxi--sxn--sxr--sx---set-exceptions-.md) command controls the global assertion handling status. If you use **ah\\*** for a certain address and then an assert occurs there, the debugger responds based on the **ah\\*** settings and ignores the **sx\* asrt** settings.

When the debugger encounters an assertion, the debugger first checks whether handling has been configured for that specific address. If you have not configured the handling, the debugger uses the global setting.

The **ah\\*** command affects only the current process. When the current process ends, all status settings are lost.

Assertion handling status affects only STATUS\_ASSERTION\_EXCEPTION exceptions. This handling does not affect the kernel-mode ASSERT routine.
