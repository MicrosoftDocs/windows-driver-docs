---
title: The Checked Build and the Debugger
description: The Checked Build and the Debugger
ms.assetid: 851d9b5b-cd1c-4b1e-b3ec-d13645795705
keywords: ["checked builds WDK , debuggers", "debuggers WDK checked builds", "host computers WDK checked builds", "target computers WDK checked builds", "null modem cables WDK"]
---

# The Checked Build and the Debugger


## <span id="ddk_the_checked_build_and_the_debugger_tools"></span><span id="DDK_THE_CHECKED_BUILD_AND_THE_DEBUGGER_TOOLS"></span>


The typical setup for debugging kernel-mode drivers on Windows operating systems consists of two computers that are connected by means of a network, USB, serial, or 1394 connection. For information about setting up kernel-mode debugging, see [Windows Debugging](https://msdn.microsoft.com/library/windows/hardware/ff551063).

The *host computer* is the system on which the debugger runs. It should be a stable system and should always run the free build of the operating system.

The *target computer* is the system on which the driver you are testing runs. It can run either the free build or the checked build. For more accurate debugging, the checked build is preferred.

The debugger running on the host computer controls the target computer through the debugging connection you establish.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20The%20Checked%20Build%20and%20the%20Debugger%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




