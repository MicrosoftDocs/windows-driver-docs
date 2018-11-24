---
title: NewDisp Dynamic Reload of a Display Driver
description: NewDisp Dynamic Reload of a Display Driver
ms.assetid: 0f8ac27c-8a42-4032-9974-89a7463dccbb
keywords:
- newdisp.exe
- dyanmic driver reloads WDK Windows 2000 display
- reload driver dynamically WDK Windows 2000 display
- reboot prevention with dynamic reload WDK Windows 2000 display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NewDisp: Dynamic Reload of a Display Driver


## <span id="ddk_newdisp_dynamic_reload_of_a_display_driver_gg"></span><span id="DDK_NEWDISP_DYNAMIC_RELOAD_OF_A_DISPLAY_DRIVER_GG"></span>


The Driver Development Kit (DDK) provides a tool that allows a display driver to be dynamically reloaded without rebooting. This tool, called *newdisp.exe*, accelerates display driver testing during development by making reboots less necessary when updating display driver code.

**Note**  This tool is not available in the Windows Vista and later releases of the Windows Driver Kit (WDK).

 

**To run *newdisp.exe***

1.  Close all Direct3D and OpenGL applications.

2.  Copy your updated display driver's DLL into the *\\system32* directory.

3.  Run *newdisp* (without any arguments).

Each time *newdisp* is invoked, it reloads the display driver. Assuming that no driver references exist at the time of invocation, *newdisp* accomplishes the dynamic reload by:

-   Calling **ChangeDisplaySettings** with 640x480x16 colors, which causes the system to load and run the 16 color VGA display driver DLL, and at the same causes the old display driver DLL to be unloaded from memory.

-   Immediately performing another **ChangeDisplaySettings** callback to the original mode, which causes the new display driver DLL to be loaded from *\\system32* directory, and the 16 color VGA display driver DLL to be unloaded.

A reference to the driver instance exists if the driver has active Direct3D, [**WNDOBJ**](https://msdn.microsoft.com/library/windows/hardware/ff570599), or [**DRIVEROBJ**](https://msdn.microsoft.com/library/windows/hardware/ff556162) objects. When *newdisp* is run while a reference to the driver instance exists, the old display driver DLL will never be unloaded, and correspondingly the new display driver DLL will never be loaded.

*Newdisp* relies on dynamic driver loading functionality that has been added to Windows 2000 and later to reload the driver without rebooting; consequently, it does not work on Windows NT 4.0 and previous operating system versions. It also does not work if the VGA driver cannot be loaded on the graphics device, or if the native display driver supports a mode of 640x480x16 colors instead of letting that mode be handled by the VGA driver.

Note that *newdisp* does not currently cause the video miniport driver to be reloaded. If the miniport driver is changed, the system must be rebooted to install and test it.

 

 





