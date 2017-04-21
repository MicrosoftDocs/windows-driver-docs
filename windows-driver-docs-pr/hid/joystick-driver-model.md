---
title: Joystick Driver Model
author: windows-driver-content
description: Joystick Driver Model
ms.assetid: 5bd41377-37ae-4ca7-8a6d-93311511ef4e
keywords:
- joysticks WDK HID , driver model
- virtual joystick drivers WDK HID , driver model
- VJoyD WDK HID , driver model
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Joystick Driver Model


## <a href="" id="ddk-joystick-driver-model-di"></a>


One of the most critical goals of the joystick driver model is to provide timely access to joystick information. Two drivers provide the Windows 95/98/Me joystick services: a 16-bit ring 3 driver (Msjstick.drv), and a 32-bit ring 0 driver (Vjoyd.vxd). The Msjstick.drv driver provides basic services such as registry update and caps information; Vjoyd.vxd provides polling services.

The API for the joystick is provided through the Mmsystem.dll dynamic-link library (DLL) for 16-bit applications on Windows 95/98/Me, and through the Winmm.dll DLL for 32-bit applications. Mmsystem.dll communicates with Msjstick.drv for all joystick services (Msjstick.drv communicates with Vjoyd.vxd to supply polling services). Winmm.dll communicates directly with Vjoyd.vxd for the polling services, and thunks to Mmsystem.dll for the basic services that are not time-critical.

In DirectX 5.0, DirectInput starts and offers an alternative, COM-based API. Dinput.dll uses VJoyD and, if available, the Human Interface Device (HID) stack, to provide polling services. HID devices are also reported through VJoyD so that applications that use the older API are still able to read the new devices. A driver supplied by the OEM, which can be either a DLL loaded by Dinput.dll, or an extended VJoyD minidriver, handles the force-feedback.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20Joystick%20Driver%20Model%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


