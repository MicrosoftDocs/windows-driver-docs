---
Description: 'This topic discusses the ImmediateIdle registry value that a Windows 8 driver can use to opt-in to an immediate power down state, when power is no longer needed.'
MS-HAID: 'audio.immediate\_idle\_timeout\_opt-in'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: 'Immediate Idle Timeout Opt-in'
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

In addition, the new interface introduced in Windows 7 that allows drivers to programmatically enable or disable idle power management, continues to be honored when the driver has not opted-in to immediate idle power management. This is done via the [**IPortClsPower::SetIdlePowerManagement**](audio.iportclspower_setidlepowermanagement) method and would override the settings in the registry, except for the case in which *ImmediateIdle* is set to 1 (TRUE).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Immediate%20Idle%20Timeout%20Opt-in%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")


