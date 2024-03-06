---
title: Forcing a System Crash with the Power Button
description: Forcing a System Crash with the Power Button
keywords: ["boot process, causing system crash from power button", "system crash, power button", "bug check, power button"]
ms.date: 12/11/2023
---

# Forcing a System Crash with the Power Button

A [Bug Check 0x1C8: MANUALLY_INITIATED_POWER_BUTTON_HOLD](bug-check-0x1c8--manually-initiated-power-button-hold.md) manual system crash can be forced by pressing and holding the power button when the following registry value is set in the registry key shown:

```reg
[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Power]
"PowerButtonBugcheck"=dword:00000001
```

To enable the manual system crash power button hold feature, run the following commands from an elevated command prompt:

```dos
REG ADD HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Power /v PowerButtonBugCheck /t REG_DWORD /d 0x1 /f
```

If this registry value does *not* exist, the system must be rebooted for this change to take effect.

If this registry value *does* exist and the value is changed, the system does *not* need to be rebooted for the change to take effect.

The bug check occurs when the power button is held for 7 seconds, but released before the UEFI Reset occurs at 10 seconds.

When the feature is triggered the regular bug check Blue screen or Green screen is not displayed. Instead, you will see a black screen which displays *Please release the power button. We just need a few more seconds to shut down* and a percent completion indicator.

It is important that you release the power button once you see this screen. If you continue to hold the power button longer, then you may trigger the firmware hard power off timeout which is usually about 10 seconds. If this happens, the dump may not complete and can be corrupted.

On some systems such as ARM64 laptops, the firmware timer is shorter, so you must release the power button immediately after 7 seconds to prevent the hard power-off from interrupting the completion of dump.

This feature is available in Windows 10 1809 / Windows Server 2019 and newer.

## Bug Check 0x11C8: MANUALLY\_INITIATED\_POWER\_BUTTON\_HOLD_LIVE_DUMP

Instead of rebooting the PC, it is also possible to create a live dump with a Long Power Button Hold (LPBH). For general information about live dumps, see [Kernel Live Dump Code Reference](bug-check-code-reference-live-dump.md).

To enable the Power Button Hold Live Dump feature the *PowerButtonLiveDump* value under following registry key is set:

```reg
[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Power]
"PowerButtonLiveDump"=dword:00000001
```

To enable the Power Button Live Dump feature, run the following commands from an elevated command prompt:

```dos
REG ADD HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Power /v PowerButtonLiveDump /t REG_DWORD /d 0x1 /f
```

If this registry key does *not* exist, the system must be rebooted for this change to take effect.

If this registry key *does* exist and the value is changed, the system does *not* need to be rebooted for the change to take effect.

This feature is available in Windows 10 version 22000 and newer.

### PowerButtonLiveDump Customization

The PowerButtonLiveDump registry value can be customized as below.


Name           | Length in bits | Offset from start | Meaning            | Default Value 
|--------------|----------------|-------------------|--------------------|-----------------|
Enabled        |    1           | 0                 | When set, power button live dump is enabled. |	N/A
UserPages	   |    1           | 1                 | When set, will request to capture User Mode memory in the live dump.  |	0
HypervisorPages| 	1           | 2                 | When set, will request to capture Hypervisor pages in the live dump. |	0
Reserved       | 	1	        | 3                 | Reserved                                                               |	N/A
TimeoutInSec   |	4           | 4                 | Specify the timeout value in seconds of when to capture the Live Dump File. Only values from 2 to 6 (including 2 and 6) are valid. If any other value is specified, the default timeout value, 5 seconds, will be used.	| 5
Reserved       |	24	        | 8                 | Reserved                                                               |	N/A

For example, running the following command from an elevated command prompt will enable the PowerButtonLiveDump feature with UserPages included and TimeoutInSec of 2. Kernel will request to capture a Full Live Dump file when the power button is held for 2 seconds.

```dos
REG ADD HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Power /v PowerButtonLiveDump /t REG_DWORD /d 0x23 /f
```

## PowerButtonBugcheck and PowerButtonLiveDump Prioritization 

If both PowerButtonBugcheck and PowerButtonLiveDump are configured and enabled on the same device, the PowerButtonBugcheck will occur when invoked, while the PowerButtonLiveDump will not.

## Device Support for Long Power Button Hold (LPBH)

To support Long Power Button Hold, the device needs:

- A General Purpose I/O (GPIO) based Power Button
- Firmware to route the power event to the Windows Power Manager
- The bug check feature to be enabled in the registry

## See also

[Bug Check 0x11C8: MANUALLY_INITIATED_POWER_BUTTON_HOLD_LIVE_DUMP](bug-check-0x1c8--manually-initiated-power-button-hold.md)

[Inside Show - Bugcheck 0x1C8 MANUALLY_INITIATED_POWER_BUTTON_HOLD](/shows/inside/0x1c8)

[ACPI button device](../hid/acpi-button-device.md)