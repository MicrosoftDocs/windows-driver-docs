---
title: User Control of Device Idle and Wake Behavior in UMDF
description: User Control of Device Idle and Wake Behavior in UMDF
ms.assetid: 9341c412-dd0a-4e80-a164-250e24004082
keywords:
- power management WDK UMDF , idle power-down
- power management WDK UMDF , wake-up
- idle power-down capabilities WDK UMDF
- idle power-down capabilities WDK UMDF , user control
- wake-up capabilities WDK UMDF
- wake-up capabilities WDK UMDF , user control
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# User Control of Device Idle and Wake Behavior in UMDF


[!include[UMDF 1 Deprecation](../umdf-1-deprecation.md)]

If a device has idle power-down or wake-up capabilities, you can decide whether users should be allowed to enable or disable these capabilities.

Your UMDF-based driver can use the [**IWDFDevice2::AssignS0IdleSettings**](https://msdn.microsoft.com/library/windows/hardware/ff556920) method to specify whether users with registry access can enable or disable a device's idle power-down capability.

Your driver can use the [**IWDFDevice2::AssignSxWakeSettings**](https://msdn.microsoft.com/library/windows/hardware/ff556923) method to specify whether users with registry access can enable or disable a device's wake-up capability.

Both of these methods allow the driver to enable the capability, disable the capability, or give users control of the capability:

-   When a driver calls the **AssignS0IdleSettings** method, it can give users control of a device's idle capabilities by setting the *UserControlOfIdleSettings* parameter to **IdleAllowUserControl** and setting the *Enabled* parameter to **WdfTrue** or **WdfUseDefault**.

-   When a driver calls the **AssignSxWakeSettings** method, it can give users control of a device's wake capabilities by setting the *UserControlOfWakeSettings* parameter to **WakeAllowUserControl** and setting the *Enabled* parameter to **WdfTrue** or **WdfUseDefault**.

If your driver allows users to modify idle and wake settings, the framework provides a user interface, in the form of a property sheet page that Device Manager displays so that users can enable or disable the idle and wake capabilities. (The framework modifies **IdleInWorkingState** and **WakeFromSleepState** registry values. Drivers and their installation files must not read or modify these values.)

If a user modifies a device's settings, the framework updates the device's power state to match the new settings, if necessary. For example, if the user disables a device's idle power-down capability while the device is already in a low-power state because it was idle, the framework returns the device to its working state.

If your driver allows users to modify idle and wake settings, the framework enables these settings by default. Some driver writers might want to initially disable the settings before allowing users to modify them.

Therefore, versions 1.9 and later of the framework provide two driver-definable registry values, named **WdfDefaultIdleInWorkingState** and **WdfDefaultWakeFromSleepState**, which are stored in the device's **Device Parameters\\WDF** subkey, under the device's [hardware key](https://msdn.microsoft.com/library/windows/hardware/ff561381). The values are REG\_DWORD-typed, with "0" indicating the capability is disabled and "1" indicating the capability is enabled.

Your driver's INF file can use an [**INF AddReg directive**](https://msdn.microsoft.com/library/windows/hardware/ff546320) to create and set the **WdfDefaultIdleInWorkingState** and **WdfDefaultWakeFromSleepState** registry values. For example, if your driver enables a device's idle power-down capability, but if the capability must be disabled when the device is installed, the driver's INF file can set **WdfDefaultIdleInWorkingState** to "0".

The framework examines the **WdfDefaultIdleInWorkingState** registry value only if the driver sets the *UserControlOfIdleSettings* parameter to **IdleAllowUserControl** and the *Enabled* parameter to **WdfTrue** or **WdfUseDefault** when the driver calls the [**IWDFDevice2::AssignS0IdleSettings**](https://msdn.microsoft.com/library/windows/hardware/ff556920) method.

The framework examines the **WdfDefaultWakeFromSleepState** registry values only if the driver sets the *UserControlOfWakeSettings* parameter to **IWakeAllowUserControl** and the *Enabled* parameter to **WdfTrue** or **WdfUseDefault** when the driver calls the [**IWDFDevice2::AssignSxWakeSettings**](https://msdn.microsoft.com/library/windows/hardware/ff556923) method.

 

 





