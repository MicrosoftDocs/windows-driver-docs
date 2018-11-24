---
title: Sending Output to the Debugger
description: Sending Output to the Debugger
ms.assetid: ee167261-78cd-4178-ba98-3250cc735657
keywords:
- debugging code WDK , sending output
- sending output to debugger
- output routines WDK
- user-mode output routines WDK
- kernel-mode output routines WDK
- routines WDK debugging , output
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Sending Output to the Debugger


## <span id="ddk_sending_output_to_the_debugger_tools"></span><span id="DDK_SENDING_OUTPUT_TO_THE_DEBUGGER_TOOLS"></span>


User-mode and kernel-mode drivers use different routines to send output to the debugger.

### <span id="user_mode_output_routines"></span><span id="USER_MODE_OUTPUT_ROUTINES"></span>User-Mode Output Routines

The **OutputDebugString** routine sends a null-terminated string to the debugger of the calling process. In a user-mode driver, **OutputDebugString** displays the string in the Debugger Command window. If a debugger is not running, this routine has no effect. **OutputDebugString** does not support the variable arguments of a **printf** formatted string.

The prototype for this routine is as follows:

```
VOID OutputDebugString(
   LPCTSTR lpOutputString
   );
```

This routine can be called by any user-mode driver that includes the windows.h header. For complete documentation of this routine and other user-mode routines useful for debugging, see the Microsoft Windows SDK.

### <span id="kernel_mode_output_routines"></span><span id="KERNEL_MODE_OUTPUT_ROUTINES"></span>Kernel-Mode Output Routines

The [**DbgPrint**](https://msdn.microsoft.com/library/windows/hardware/ff543632) routine displays output in the debugger window. This routine supports the basic **printf** format parameters. Only kernel-mode drivers can call **DbgPrint**.

The [**DbgPrintEx**](https://msdn.microsoft.com/library/windows/hardware/ff543634) routine is similar to **DbgPrint**, but it allows you to "tag" your messages. When running the debugger, you can permit only those messages with certain tags to be sent. This allows you to view only those messages that you are interested in. For details, see [Reading and Filtering Debugging Messages](reading-and-filtering-debugging-messages.md).

**Note**   In Windows Vista and later versions of Windows, **DbgPrint** produces tagged messages as well. In previous versions of Windows, **DbgPrint** produced untagged messages.

 

The [**KdPrint**](https://msdn.microsoft.com/library/windows/hardware/ff548092) and [**KdPrintEx**](https://msdn.microsoft.com/library/windows/hardware/ff548100) macros are identical to **DbgPrint** and **DbgPrintEx**, respectively, when compiled in the checked build environment. When compiled in the free build environment, they have no effect.

 

 





