---
title: The Checked Build and the Debugger
description: The Checked Build and the Debugger
ms.assetid: 851d9b5b-cd1c-4b1e-b3ec-d13645795705
keywords:
- checked builds WDK , debuggers
- debuggers WDK checked builds
- host computers WDK checked builds
- target computers WDK checked builds
- null modem cables WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# The Checked Build and the Debugger


## <span id="ddk_the_checked_build_and_the_debugger_tools"></span><span id="DDK_THE_CHECKED_BUILD_AND_THE_DEBUGGER_TOOLS"></span>


The typical setup for debugging kernel-mode drivers on Windows operating systems consists of two computers that are connected by means of a network, USB, serial, or 1394 connection. For information about setting up kernel-mode debugging, see [Windows Debugging](https://msdn.microsoft.com/library/windows/hardware/ff551063).

The *host computer* is the system on which the debugger runs. It should be a stable system and should always run the free build of the operating system.

The *target computer* is the system on which the driver you are testing runs. It can run either the free build or the checked build. For more accurate debugging, the checked build is preferred.

The debugger running on the host computer controls the target computer through the debugging connection you establish.

 

 





