---
title: The Checked Build and the Debugger
description: The Checked Build and the Debugger
keywords:
- checked builds WDK , debuggers
- debuggers WDK checked builds
- host computers WDK checked builds
- target computers WDK checked builds
- null modem cables WDK
ms.date: 05/08/2020
ms.localizationpriority: medium
---

# The Checked Build and the Debugger

The typical setup for debugging kernel-mode drivers on Windows operating systems consists of two computers that are connected by means of a network, USB or serial connection. For information about setting up kernel-mode debugging, see [Windows Debugging](../debugger/index.md).

The *host computer* is the system on which the debugger runs. It should be a stable system and should always run the free build of the operating system.

The *target computer* is the system on which the driver you are testing runs. It can run either the free build or the checked build. For more accurate debugging, the checked build is preferred.

The debugger running on the host computer controls the target computer through the debugging connection you establish.

> [!NOTE]
> Checked builds were available on older versions of Windows, before Windows 10 version 1803.
> Use tools such as Driver Verifier and GFlags to check driver code in later versions of Windows.
