---
title: View the Call Stack in Visual Studio
description: Learn how to view the Call Stack in the Visual Studio Debug menu by installing the Windows Driver Kit.
ms.date: 12/14/2022
---

# View the Call Stack in Visual Studio

> [!IMPORTANT]
> This feature isn't available in Windows 10, version 1507 or later versions of the WDK.
>
The procedures shown in this article require that you have the Windows Driver Kit integrated into Visual Studio. To get the integrated environment, first install Microsoft Visual Studio, and then install the Windows Driver Kit (WDK). For more information, see [Windows driver development](../index.yml).

## Use the Call Stack window

To open the **Call Stack** window in Visual Studio, from the **Debug** menu, choose **Windows>Call Stack**. To set the local context to a particular row in the stack trace display, select and hold (or double-click) the first column of the row.

## View the Call Stack by entering commands

In the **Immediate window**, you can view the Call Stack by entering one of the [k (Display Stack Backtrace)](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md) commands. If the **Immediate window** isn't already open, from the **Debug** menu, choose **Windows>Immediate**.
