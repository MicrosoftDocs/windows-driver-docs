---
title: Immediate Idle Timeout Opt-in
description: This topic discusses the ImmediateIdle registry value that a Windows 8 driver can use to opt-in to an immediate power down state, when power is no longer needed.
ms.assetid: 43721EC9-4901-4C68-9CCC-E0A71BF2200E
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# <span id="audio.immediate_idle_timeout_opt-in"></span>Immediate Idle Timeout Opt-in


This topic discusses the *ImmediateIdle* registry value that a Windows 8 driver can use to opt-in to an immediate power down state, when power is no longer needed.

In addition to the default power settings discussed in [PortCls Registry Power Settings](portcls-registry-power-settings.md), Windows 8 introduces a new registry value that is also located in the PowerSettings registry key for the associated driver. For example, if you have a driver whose key is &lt;UVXYZ&gt;, then the power settings information for the driver would be found in the following path in the Windows registry:

HKLM\\System\\CurrentControlSet\\Control\\Class\\{4D36E96C-E325-11CE-BFC1-08002BE10318}\\&lt;UVXYZ&gt;\\PowerSettings.

And in addition to the default power setting values shown in [PortCls Registry Power Settings](portcls-registry-power-settings.md), you would also include the following line for *ImmediateIdle*:

``` syntax
"ImmediateIdle"=hex:00,00,00,00  
```

*ImmediateIdle* has a data type of REG\_DWORD and its default value is "0" which equates to FALSE. In the preceding syntax fragment, the hexadecimal value of "0" means that the device will not immediately power down when power is no longer needed.

For your driver to opt-in to an immediate power down state, when power is no longer needed, you must use the following syntax:

``` syntax
"ImmediateIdle"=hex:01,00,00,00  
```

In the preceding syntax fragment, the hex value of "1" equates to TRUE, and it means that the device will immediately power down when power is no longer needed.

When the runtime power management framework invokes a callback for the **DevicePowerRequired** method, indicating that the device no longer requires power, PortCls then requests a Device Power IRP for the D-State indicated by the *IdlePowerState* registry value. If no state is supplied, then the default value of D3 is used.

If a driver opts-in to immediate idle power management, it must ensure that the Power Engine Plug-in (PEP) for the system contains the logic needed to prevent unnecessarily and continuously powering the adapter up and down for IRPs received in immediate succession. Some residency rules should be applied in order to keep the device powered up for batches of I/O requests.

In addition, the new interface introduced in Windows 7 that allows drivers to programmatically enable or disable idle power management, continues to be honored when the driver has not opted-in to immediate idle power management. This is done via the [**IPortClsPower::SetIdlePowerManagement**](https://msdn.microsoft.com/library/windows/hardware/ff536875) method and would override the settings in the registry, except for the case in which *ImmediateIdle* is set to 1 (TRUE).

 

 




