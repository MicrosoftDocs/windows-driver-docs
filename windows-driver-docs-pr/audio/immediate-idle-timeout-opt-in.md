---
title: Immediate Idle Timeout Opt-in
description: This topic discusses the ImmediateIdle registry value that a Windows 8 driver can use to opt-in to an immediate power down state, when power is no longer needed.
ms.date: 08/17/2022
---

# <span id="audio.immediate_idle_timeout_opt-in"></span>Immediate Idle Timeout Opt-in


This topic discusses the *ImmediateIdle* registry value that a Windows driver can use to opt-in to an immediate power down state, when power is no longer needed.

In addition to the default power settings discussed in [PortCls Registry Power Settings](portcls-registry-power-settings.md), Windows 8 introduced an *ImmediateIdle* registry value that is also located in the PowerSettings registry key for the associated driver. 

This inf file shows how to set *ImmediateIdle*.

```inf
[MyAudioDevice.AddReg]
HKR,PowerSettings,ImmediateIdle,%REG_BINARY%, 0x00, 0x00, 0x00, 0x00
```

*ImmediateIdle* has a data type of REG\_DWORD and its default value is "0" which equates to FALSE. In the preceding syntax fragment, the hexadecimal value of "0" means that the device will not immediately power down when power is no longer needed.

For your driver to opt-in to an immediate power down state, when power is no longer needed, you must use the following syntax:

```inf
[MyAudioDevice.AddReg]
HKR,PowerSettings,ImmediateIdle,%REG_BINARY%, 0x01, 0x00, 0x00, 0x00
```

In the preceding example, the hex value of "1" equates to TRUE, and it means that the device will immediately power down when power is no longer needed.

When the runtime power management framework invokes a callback for the **DevicePowerRequired** method, indicating that the device no longer requires power, PortCls then requests a Device Power IRP for the D-State indicated by the *IdlePowerState* registry value. If no state is supplied, then the default value of D3 is used.

If a driver opts-in to immediate idle power management, it must ensure that the Power Engine Plug-in (PEP) for the system contains the logic needed to prevent unnecessarily and continuously powering the adapter up and down for IRPs received in immediate succession. Some residency rules should be applied in order to keep the device powered up for batches of I/O requests.

In addition, the interface introduced in Windows 7 that allows drivers to programmatically enable or disable idle power management, continues to be honored when the driver has not opted-in to immediate idle power management. This is done via the [**IPortClsPower::SetIdlePowerManagement**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iportclspower-setidlepowermanagement) method and would override the settings in the registry, except for the case in which *ImmediateIdle* is set to 1 (TRUE).

 

