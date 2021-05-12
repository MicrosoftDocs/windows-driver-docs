---
title: Boot Parameters to Enable Debugging
description: Boot Parameters to Enable Debugging
keywords:
- boot parameters WDK
- boot entry parameters WDK
- kernel debugging support WDK boot options
- local debugging WDK boot parameters
- single-computer debugging WDK boot parameters
- cable debugging WDK boot parameters
- IEEE 1394 cable WDK boot parameters
- 1394 connection WDK boot parameters
- USB 2.0 debugging connection WDK boot parameters
- null-modem cable WDK boot parameters
ms.date: 09/21/2020
ms.localizationpriority: medium
---

# Boot Parameters to Enable Debugging

When a kernel debugging connection is established, the system gives a kernel debugger control over its execution. Also, when a bug check occurs or a kernel-mode program communicates with a debugger, the computer waits for a response from a kernel debugger before it continues.

> [!IMPORTANT]
> Setting up a network debugging manually is a complex and error prone process.
> To set up network debugging automatically, see **[Setting Up KDNET Network Kernel Debugging Automatically](../debugger/setting-up-a-network-debugging-connection-automatically.md)**. Using the KDNET utility is **strongly** recommended for all debugger users.

For information on manual setup of a network connection, see [Setting Up Kernel-Mode Debugging over a Network Cable Manually](../debugger/setting-up-a-network-debugging-connection.md).

>[!Note]
> Before setting BCDEdit options you might need to disable or suspend BitLocker and Secure Boot on the computer.

You can use the **bcdedit** command to view the current debugger boot entries and to change their settings. For more details, see [**BCDEdit /debug**](./bcdedit--debug.md) and [**BCDEdit /dbgsettings**](./bcdedit--dbgsettings.md).

## Boot Parameters to Debug the Boot Process in Windows

To enable boot debugging, use the [**BCDEdit /bootdebug**](./bcdedit--bootdebug.md) command and specify the appropriate boot component. If you wish to perform kernel debugging after Windows starts, use the [**BCDEdit /debug**](./bcdedit--debug.md) command as well. You must also select a debugging connection, just as in normal kernel debugging. For more details, see [**BCDEdit /bootdebug**](./bcdedit--bootdebug.md).

## See also

For information about Windows debugging tools, see [Windows Debugging](../debugger/index.md).

For information about setting up and configuring a kernel-mode debugging session, see [Setting Up Kernel-Mode Debugging Manually](../debugger/setting-up-kernel-mode-debugging-in-windbg--cdb--or-ntsd.md) and [Setting Up KDNET Network Kernel Debugging Automatically](../debugger/setting-up-a-network-debugging-connection-automatically.md).
