---
title: Joystick Driver Model
description: Joystick Driver Model
ms.assetid: 5bd41377-37ae-4ca7-8a6d-93311511ef4e
keywords:
- joysticks WDK HID , driver model
- virtual joystick drivers WDK HID , driver model
- VJoyD WDK HID , driver model
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Joystick Driver Model





One of the most critical goals of the joystick driver model is to provide timely access to joystick information. Two drivers provide the Windows 95/98/Me joystick services: a 16-bit ring 3 driver (Msjstick.drv), and a 32-bit ring 0 driver (Vjoyd.vxd). The Msjstick.drv driver provides basic services such as registry update and caps information; Vjoyd.vxd provides polling services.

The API for the joystick is provided through the Mmsystem.dll dynamic-link library (DLL) for 16-bit applications on Windows 95/98/Me, and through the Winmm.dll DLL for 32-bit applications. Mmsystem.dll communicates with Msjstick.drv for all joystick services (Msjstick.drv communicates with Vjoyd.vxd to supply polling services). Winmm.dll communicates directly with Vjoyd.vxd for the polling services, and thunks to Mmsystem.dll for the basic services that are not time-critical.

In DirectX 5.0, DirectInput starts and offers an alternative, COM-based API. Dinput.dll uses VJoyD and, if available, the Human Interface Device (HID) stack, to provide polling services. HID devices are also reported through VJoyD so that applications that use the older API are still able to read the new devices. A driver supplied by the OEM, which can be either a DLL loaded by Dinput.dll, or an extended VJoyD minidriver, handles the force-feedback.

 

 




