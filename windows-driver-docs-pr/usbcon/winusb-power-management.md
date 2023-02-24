---
title: WinUSB power management
description: WinUSB power management
ms.date: 02/23/2023
---

# WinUSB power management

WinUSB uses the KMDF state machines for power management. Power policies are managed through calls to [**WinUsb_SetPowerPolicy**](/windows/win32/api/winusb/nf-winusb-winusb_setpowerpolicy).

In order to modify the power behavior of WinUSB, default registry settings can be modified in the device's INF. These values must be written to the device specific location in the registry by adding the values in the **HW.AddReg** section of the INF.

The registry values described in the following list can be specified in the device's INF to modify the power behavior.

## System Wake

This feature is controlled by the **SystemWakeEnabled** DWORD registry setting. This value indicates whether the device should be allowed to wake the system from a low power state.

```inf
HKR,,SystemWakeEnabled,0x00010001,1
```

- A value of zero, or the absence of this value indicates that the device isn't allowed to wake the system.
- To allow a device to wake the system, set **SystemWakeEnabled** to a nonzero value. A check box in the device **Properties** page is automatically enabled so that the user can override the setting.

> [!NOTE]
> Changing the **SystemWakeEnabled** setting has no effect on selective suspend, this registry value only pertains to system suspend.

## Selective Suspend

Selective suspend can be disabled by any of several system or WinUSB settings. A single setting can't force WinUSB to enable selective suspend.

The following power policy settings that are specified in [**WinUsb_SetPowerPolicy**](/windows/win32/api/winusb/nf-winusb-winusb_setpowerpolicy)'s *PolicyType* parameter affect the behavior of selective suspend:

- AUTO_SUSPEND When set to zero, it doesn't set the device to selective suspend mode.
- SUSPEND_DELAY Sets the time between when the device becomes idle and when WinUSB requests the device to go into selective suspend.

The following table shows how the registry keys affect the selective suspend feature.

| Registry key | Description |
|---|---|
| **DeviceIdleEnabled** | This is a DWORD value. This registry value indicates whether the device is capable of being powered down when idle (Selective Suspend).<br><ul><li>A value of zero, or the absence of this value indicates that the device doesn't support being powered down when idle.</li><li>A nonzero value indicates that the device supports being powered down when idle.</li><li>If DeviceIdleEnabled isn't set, the value of the AUTO_SUSPEND power policy setting is ignored.</li></ul><br>`HKR,,DeviceIdleEnabled,0x00010001,1` |
| **DeviceIdleIgnoreWakeEnable** | When set to a nonzero value, it suspends the device even if it doesn't support RemoteWake. |
| **UserSetDeviceIdleEnabled** | This value is a DWORD value. This registry value indicates whether a check box should be enabled in the device **Properties** page that allows a user to override the idle defaults. When **UserSetDeviceIdleEnabled** is set to a nonzero value the check box is enabled and the user can disable powering down the device when idle. A value of zero, or the absence of this value indicates that the check box isn't enabled.<br><ul><li>If the user disables device power savings, the value of the AUTO_SUSPEND power policy setting is ignored.</li><li>If the user enables device power savings, then the value of AUTO_SUSPEND is used to determine whether to suspend the device when idle.</li></ul><br>The **UserSetDeviceIdleEnabled** is ignored if **DeviceIdleEnabled** isn't set.<br><br>`HKR,,UserSetDeviceIdleEnabled,0x00010001,1` |
| **DefaultIdleState** | This is a DWORD value. This registry value sets the default value of the AUTO_SUSPEND power policy setting. This registry key is used to enable or disable selective suspend when a handle isn't open to the device.<br><ul><li>A value of zero or the absence of this value indicates that by default, the device isn't suspended when idle. The device be allowed to suspend when idle only when the AUTO_SUSPEND power policy is enabled.</li><li>A nonzero value indicates that by default the device can be suspended when idle.</li></ul><br>This value is ignored if **DeviceIdleEnabled** isn't set.<br><br>`HKR,,DefaultIdleState,0x00010001,1` |
| **DefaultIdleTimeout** | This is a DWORD value. This registry value sets the default state of the SUSPEND_DELAY power policy setting.<br><br>The value indicates the amount of time in milliseconds to wait before determining that a device is idle.<br><br>`HKR,,DefaultIdleTimeout,0x00010001,100` |

## Detecting Idle

All writes and control transfers force the device into the **D0** power state and reset the idle timer. The IN endpoint queues aren't power managed. Read requests wake the device when they're submitted. However, a device can become idle while a read request waits.

## Related topics

- [WinUSB Architecture and Modules](winusb-architecture.md)
- [Choosing a driver model for developing a USB client driver](winusb-considerations.md)
- [WinUSB (Winusb.sys) Installation](winusb-installation.md)
- [How to Access a USB Device by Using WinUSB Functions](using-winusb-api-to-communicate-with-a-usb-device.md)
- [WinUSB Functions for Pipe Policy Modification](winusb-functions-for-pipe-policy-modification.md)
- [WinUSB functions](using-winusb-api-to-communicate-with-a-usb-device.md)
- [WinUSB](winusb.md)
- [**WinUsb_GetPowerPolicy**](/windows/win32/api/winusb/nf-winusb-winusb_getpowerpolicy)
- [**WinUsb_SetPowerPolicy**](/windows/win32/api/winusb/nf-winusb-winusb_setpowerpolicy)
