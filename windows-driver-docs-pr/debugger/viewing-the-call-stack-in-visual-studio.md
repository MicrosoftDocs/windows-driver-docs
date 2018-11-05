---
title: Viewing the Call Stack in Visual Studio
description: The procedure describes how to view the Call Stack in Visual Studio
ms.assetid: 060A2441-C1A7-4485-82E5-2C024E6A3FBE
ms.author: domars
ms.date: 05/11/2018
ms.localizationpriority: medium
---

# Viewing the Call Stack in Visual Studio

> [!IMPORTANT]
> This feature is not available in Windows 10, version 1507 and later versions of the WDK.
>

The procedures shown in this topic require that you have the Windows Driver Kit integrated into Visual Studio. To get the integrated environment, first install Microsoft Visual Studio, and then install the Windows Driver Kit (WDK). For more information, see [Windows Driver Development](https://msdn.microsoft.com/library/windows/hardware/ff557573).

## <span id="Using_the_Call_Stack_Window"></span><span id="using_the_call_stack_window"></span><span id="USING_THE_CALL_STACK_WINDOW"></span>Using the Call Stack Window


To open the **Call Stack** window in Visual Studio, from the **Debug** menu, choose **Windows&gt;Call Stack**. To set the local context to a particular row in the stack trace display, double click the first column of the row.

## <span id="Viewing_the_Call_Stack_by_Entering_Commands"></span><span id="viewing_the_call_stack_by_entering_commands"></span><span id="VIEWING_THE_CALL_STACK_BY_ENTERING_COMMANDS"></span>Viewing the Call Stack by Entering Commands


In the Debugger Immediate Window, you can view the call stack by entering one of the [**k (Display Stack Backtrace)**](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md) commands. If the Debugger Immediate window is not already open, from the **Debug** menu, choose **Windows&gt;Immediate**.

 

 





