---
title: Sending Output to the Debugger
description: Sending Output to the Debugger
ms.assetid: e0640e70-9846-4239-a3ff-b78788751384
keywords: ["sending output to the debugger", "OutputDebugString function", "DbgPrint function", "DbgPrintEx function", "KdPrint function", "KdPrintEx function"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Sending Output to the Debugger


## <span id="ddk_sending_output_to_the_debugger_dbg"></span><span id="DDK_SENDING_OUTPUT_TO_THE_DEBUGGER_DBG"></span>


User-mode and kernel-mode code use different routines to send output to the debugger.

### <span id="user_mode_output_routines"></span><span id="USER_MODE_OUTPUT_ROUTINES"></span>User-Mode Output Routines

**OutputDebugString** sends a null-terminated string to the debugger of the calling process. In a user-mode driver, **OutputDebugString** displays the string in the Debugger Command window. If a debugger is not running, this routine has no effect. **OutputDebugString** does not support the variable arguments of a **printf** formatted string.

For complete documentation of this routine, see the Microsoft Windows SDK.

### <span id="kernel_mode_output_routines"></span><span id="KERNEL_MODE_OUTPUT_ROUTINES"></span>Kernel-Mode Output Routines

**DbgPrint** displays output in the debugger window. This routine supports the basic **printf** format parameters. Only kernel-mode code can call **DbgPrint**.

**DbgPrintEx** is similar to **DbgPrint**, but it allows you to "tag" your messages. When running the debugger, you can permit only those messages with certain tags to be sent. This allows you to view only those messages that you are interested in. For details, see [Reading and Filtering Debugging Messages](reading-and-filtering-debugging-messages.md).

**Note**   In Windows Vista and later versions of Windows, **DbgPrint** produces tagged messages as well. This is a change from previous versions of Windows.

 

**KdPrint** and **KdPrintEx** are identical to **DbgPrint** and **DbgPrintEx**, respectively, when compiled in the checked build environment. When compiled in the free build environment, they have no effect.

For complete documentation of these routines, as well as the build environment, see the Windows Driver Kit.

 

 





