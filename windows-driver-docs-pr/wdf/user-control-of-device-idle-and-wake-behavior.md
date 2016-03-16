---
title: User Control of Device Idle and Wake Behavior
description: User Control of Device Idle and Wake Behavior
ms.assetid: 776fcf82-2235-489a-8d46-3ad230da3402
keywords: ["system wake up WDK KMDF", "power management WDK KMDF wake up capabilities", "wake up capabilities WDK KMDF", "sleep power management WDK KMDF", "low power states WDK KMDF", "power management WDK KMDF idle power down", "idle power down WDK KMDF"]
---

# User Control of Device Idle and Wake Behavior


If a device has idle power-down or wake-up capabilities, you can decide whether users should be allowed to enable or disable these capabilities.

Your driver can use members of the [**WDF\_DEVICE\_POWER\_POLICY\_IDLE\_SETTINGS**](https://msdn.microsoft.com/library/windows/hardware/ff551270) structure to specify whether users with registry access can enable or disable a device's idle power-down capability.

Your driver can use members of the [**WDF\_DEVICE\_POWER\_POLICY\_WAKE\_SETTINGS**](https://msdn.microsoft.com/library/windows/hardware/ff551277) structure to specify whether users with registry access can enable or disable a device's wake-up capability.

Both of these structures allow the driver to enable the capability, disable the capability, or give users control of the capability. To give users control, in the appropriate settings structure the driver sets the **UserControlOfIdleSettings** or **UserControlOfWakeSettings** member to **IdleAllowUserControl** or **WakeAllowUserControl**, respectively, and the **Enabled** member to **WdfTrue** or **WdfUseDefault**,.

If your driver allows users to modify idle and wake settings, the framework provides a user interface, in the form of a property sheet page that Device Manager displays so that users can enable or disable the idle and wake capabilities. (The framework modifies **IdleInWorkingState** and **WakeFromSleepState** registry values. Drivers and their installation files must *not* read or modify these values.)

If a user modifies a device's settings, the framework updates the device's power state to match the new settings, if necessary. For example, if the user disables a device's idle power-down capability while the device is already in a low-power state because it was idle, the framework returns the device to its working state.

If your driver allows users to modify idle and wake settings, the framework enables these settings by default. Some driver writers might want to initially disable the settings before allowing users to modify them.

Therefore, for version 1.9 and later versions of KMDF, the framework provides two driver-definable registry values, named **WdfDefaultIdleInWorkingState** and **WdfDefaultWakeFromSleepState**, which are stored in the device's **Device Parameters\\WDF** subkey, under the device's hardware key. The values are REG\_DWORD-typed, with "0" indicating the capability is disabled and "1" indicating the capability is enabled.

Your driver's INF file can use an [**INF AddReg directive**](https://msdn.microsoft.com/library/windows/hardware/ff546320) to create and set the **WdfDefaultIdleInWorkingState** and **WdfDefaultWakeFromSleepState** registry values. For example, if your driver enables a device's idle power-down capability, but if the capability must be disabled when the device is installed, the driver's INF file can set **WdfDefaultIdleInWorkingState** to "0".

The framework examines the **WdfDefaultIdleInWorkingState** and **WdfDefaultWakeFromSleepState** registry values only if the driver has set the **UserControlOfIdleSettings** or **UserControlOfWakeSettings** member to to **IdleAllowUserControl** or **WakeAllowUserControl**, respectively, and the **Enabled** member to **WdfTrue** or **WdfUseDefault**, in the appropriate settings structure.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20User%20Control%20of%20Device%20Idle%20and%20Wake%20Behavior%20%20RELEASE:%20%283/16/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




