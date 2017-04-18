---
title: Minidriver-Supplied Callbacks
author: windows-driver-content
description: Minidriver-Supplied Callbacks
ms.assetid: df5bbc1c-988f-4e07-9783-4f380f85c2b6
keywords: ["joysticks WDK HID , callbacks", "virtual joystick drivers WDK HID , callbacks", "VJoyD WDK HID , callbacks", "callbacks WDK joysticks", "polling WDK joysticks"]
---

# Minidriver-Supplied Callbacks


## <a href="" id="ddk-minidriver-supplied-callbacks-di"></a>


Joystick hardware that is not polled or that has nonstandard polling requirements can implement a minidriver (which must be a VxD) that VJoyD loads when a device of that type is in use. VJoyD also calls the minidriver to access position and button information. Joystick minidrivers are not required to provide any interfaces other than to process the standard SYS\_DYNAMIC\_DEVICE\_INIT and SYS\_DYNAMIC\_DEVICE\_EXIT messages when the device is loaded and unloaded, and to define and register four joystick-specific callbacks. In addition to provide support for this original interface, the DirectX 5.0 and later VJoyD also support an extended interface. The extended interface allows registration of new callbacks to support polling, force-feedback, and hot plugging of joysticks.

On request from Msjstick.drv, VJoyD checks for the minidrivers that should be loaded and unloaded. Msjstick.drv makes the request for each device it handles and whenever joyConfigChanged receives a call. Msjstick.drv is initialized for each device it handles during the **Normal** boot sequence, which means that some devices and services may be unavailable to the minidriver at the time it is loaded. Because VJoyD loads minidrivers when they are assigned to a joystick number; not when an application needs to use the device, you should keep the processing to a minimum. You should not start any background processing, shared resource usage, or large-scale memory allocations just because the VxD is loaded. VJoyD starts with DirectX 5.0, and does its initial loading of minidrivers at a later stage in the boot process than the original.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20Minidriver-Supplied%20Callbacks%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


