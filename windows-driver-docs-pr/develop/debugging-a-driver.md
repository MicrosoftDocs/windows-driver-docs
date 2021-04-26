---
title: Debugging a Driver
description: Typically, debugging a kernel-mode driver requires two computers.
ms.date: 08/22/2019
ms.localizationpriority: medium
---

# Debugging a Driver

Debugging a kernel-mode driver requires two computers. The debugger runs on the *host computer*, and the code being debugged runs on the *target computer*. The target computer is also called the *test computer*. You can debug a user-mode driver on the host computer or on a separate target computer. Before you can debug a driver running on a target computer, you must configure the target computer for debugging.

For general information about debugging drivers, see [Getting Started with Windows Debugging](../debugger/getting-started-with-windows-debugging.md).

For information about configuring a target computer and setting up a debug cable using a network connection, see [Setting Up KDNET Network Kernel Debugging Automatically](../debugger/setting-up-a-network-debugging-connection-automatically.md).

## See Also

[Windows Debugging](../debugger/index.md).
