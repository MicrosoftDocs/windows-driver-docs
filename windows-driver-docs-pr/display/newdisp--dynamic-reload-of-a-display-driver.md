---
title: NewDisp Dynamic Reload of a Display Driver
description: NewDisp Dynamic Reload of a Display Driver
ms.assetid: 0f8ac27c-8a42-4032-9974-89a7463dccbb
keywords:
- newdisp.exe
- dyanmic driver reloads WDK Windows 2000 display
- reload driver dynamically WDK Windows 2000 display
- reboot prevention with dynamic reload WDK Windows 2000 display
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20NewDisp:%20Dynamic%20Reload%20of%20a%20Display%20Driver%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




