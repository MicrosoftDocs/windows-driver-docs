---
title: Preventing System Power State Changes
author: windows-driver-content
description: Preventing System Power State Changes
ms.assetid: a744dfe7-d756-45c3-8fdf-7a403f6cde36
keywords: ["system power states WDK kernel , preventing changes", "state transitions WDK power management", "PoRegisterSystemState", "PoSetSystemState", "PoUnregisterSystemState", "working states WDK power management"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Preventing System Power State Changes


## <a href="" id="ddk-preventing-system-power-state-changes-kg"></a>


Although drivers cannot directly set system power policy, the power manager provides three routines through which a driver can prevent system transitions out of the working state: [**PoSetSystemState**](https://msdn.microsoft.com/library/windows/hardware/ff559768), [**PoRegisterSystemState**](https://msdn.microsoft.com/library/windows/hardware/ff559731), and [**PoUnregisterSystemState**](https://msdn.microsoft.com/library/windows/hardware/ff559794).

By calling **PoRegisterSystemState** or **PoSetSystemState**, a driver can notify the power manager that a user is present or that the driver requires use of the system or display.

**PoRegisterSystemState** allows a driver to register a continuous busy state. It returns a handle through which the driver can later change its settings. As long as the state registration is in effect, the power manager does not attempt to put the system to sleep. The driver cancels the state registration by calling **PoUnregisterSystemState**.

With **PoSetSystemState**, a driver notifies the power manager of the same conditions (user present, system required, display required), but this setting is not continuous. It has the effect of restarting any idle count downs associated with the specified conditions.

Using these routines, a driver can forestall many, but not all, transitions out of the working state. The power manager always shuts down the system when loss of power is imminent or when a user explicitly requests shutdown.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Preventing%20System%20Power%20State%20Changes%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


