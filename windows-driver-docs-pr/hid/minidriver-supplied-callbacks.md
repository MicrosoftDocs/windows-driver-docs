---
title: Minidriver-Supplied Callbacks
description: Minidriver-Supplied Callbacks
ms.assetid: df5bbc1c-988f-4e07-9783-4f380f85c2b6
keywords:
- joysticks WDK HID , callbacks
- virtual joystick drivers WDK HID , callbacks
- VJoyD WDK HID , callbacks
- callbacks WDK joysticks
- polling WDK joysticks
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Minidriver-Supplied Callbacks





Joystick hardware that is not polled or that has nonstandard polling requirements can implement a minidriver (which must be a VxD) that VJoyD loads when a device of that type is in use. VJoyD also calls the minidriver to access position and button information. Joystick minidrivers are not required to provide any interfaces other than to process the standard SYS\_DYNAMIC\_DEVICE\_INIT and SYS\_DYNAMIC\_DEVICE\_EXIT messages when the device is loaded and unloaded, and to define and register four joystick-specific callbacks. In addition to provide support for this original interface, the DirectX 5.0 and later VJoyD also support an extended interface. The extended interface allows registration of new callbacks to support polling, force-feedback, and hot plugging of joysticks.

On request from Msjstick.drv, VJoyD checks for the minidrivers that should be loaded and unloaded. Msjstick.drv makes the request for each device it handles and whenever joyConfigChanged receives a call. Msjstick.drv is initialized for each device it handles during the **Normal** boot sequence, which means that some devices and services may be unavailable to the minidriver at the time it is loaded. Because VJoyD loads minidrivers when they are assigned to a joystick number; not when an application needs to use the device, you should keep the processing to a minimum. You should not start any background processing, shared resource usage, or large-scale memory allocations just because the VxD is loaded. VJoyD starts with DirectX 5.0, and does its initial loading of minidrivers at a later stage in the boot process than the original.

 

 




