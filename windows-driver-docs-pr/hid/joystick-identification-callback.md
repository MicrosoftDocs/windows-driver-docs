---
title: Joystick Identification Callback
description: Joystick Identification Callback
ms.assetid: d5e859d2-bfe4-41ef-9d09-ebb945d299bd
keywords: ["callbacks WDK joysticks", "joysticks WDK HID , ID requests", "ID requests WDK joysticks", "identification callbacks WDK joysticks"]
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Joystick Identification Callback





```cpp
int __stdcall JoyIdRoutine( int joyid, BOOL used );
```

VJoyD calls JoyIDRoutine when a user configures or de-configures a joystick as one of the 16 joysticks. If the minidriver can support the ID requested in *joyid*, JoyIdRoutine returns a nonzero value. If the minidriver cannot support the ID, the routine returns zero value.

Whenever any change is made and joyConfigChanged is called to update the driver, VJoyD cycles through all 16 devices, starting with JOYSTICKID1. It resets all devices to unused and then loops through them again to set all those that the system needs to use. During control panel operations, this process can entail a large number of calls, which creates problem in this callback usage for initialization. This is particularly true if the call is made before the system boot is complete, that is when other services are not available.

Minidrivers that service callbacks for more than one device should attempt to keep joystick identifiers tied to a single physical device, where possible, to avoid user confusion. You can implement this relatively easily during a single session, but is probably not necessary over reboots.

 

 




