---
Description: WinUSB Power Management
title: WinUSB Power Management
author: windows-driver-content
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WinUSB Power Management


WinUSB uses the KMDF state machines for power management. Power policies are managed through calls to [**WinUsb\_SetPowerPolicy**](https://msdn.microsoft.com/library/windows/hardware/ff540309).

In order to modify the power behavior of WinUSB, default registry settings can be modified in the device?s INF. These values must be written to the device specific location in the registry by adding the values in the **HW.AddReg** section of the INF.

The registry values described in the following list can be specified in the device?s INF to modify the power behavior.

<a href="" id="system-wake"></a>**System Wake**  
This feature is controlled by the **SystemWakeEnabled** DWORD registry setting. This value indicates whether the device should be allowed to wake the system from a low power state.

``` syntax
HKR,,SystemWakeEnabled,0x00010001,1
```

-   A value of zero, or the absence of this value indicates that the device is not allowed to wake the system.
-   To allow a device to wake the system, set **SystemWakeEnabled** to a nonzero value. A check box in the device **Properties** page is automatically enabled so that the user can override the setting.

**Note**  Changing the **SystemWakeEnabled** setting has no affect on selective suspend, this registry value only pertains to system suspend.

 

<a href="" id="selective-suspend"></a>**Selective Suspend**  
Selective suspend can be disabled by any of several system or WinUSB settings. A single setting cannot force WinUSB to enable selective suspend.

The following power policy settings that are specified in [**WinUsb\_SetPowerPolicy**](https://msdn.microsoft.com/library/windows/hardware/ff540309)'s *PolicyType* parameter affect the behavior of selective suspend:

-   AUTO\_SUSPEND When set to zero, it does not set the device to selective suspend mode.
-   SUSPEND\_DELAY Sets the time between when the device becomes idle and when WinUSB requests the device to go into selective suspend.

The following table shows how the registry keys affect the selective suspend feature.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Registry key</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>DeviceIdleEnabled</strong></td>
<td>This is a DWORD value. This registry value indicates whether the device is capable of being powered down when idle (Selective Suspend).
<ul>
<li>A value of zero, or the absence of this value indicates that the device does not support being powered down when idle.</li>
<li>A nonzero value indicates that the device supports being powered down when idle.</li>
<li>If DeviceIdleEnabled is not set, the value of the AUTO_SUSPEND power policy setting is ignored.</li>
</ul>
<pre class="syntax" space="preserve"><code>HKR,,DeviceIdleEnabled,0x00010001,1</code></pre></td>
</tr>
<tr class="even">
<td><strong>DeviceIdleIgnoreWakeEnable</strong></td>
<td>When set to a nonzero value, it suspends the device even if it does not support RemoteWake.</td>
</tr>
<tr class="odd">
<td><strong>UserSetDeviceIdleEnabled</strong></td>
<td>This value is a DWORD value. This registry value indicates whether a check box should be enabled in the device <strong>Properties</strong> page that allows a user to override the idle defaults. When <strong>UserSetDeviceIdleEnabled</strong> is set to a nonzero value the check box is enabled and the user can disable powering down the device when idle. A value of zero, or the absence of this value indicates that the check box is not enabled.
<ul>
<li>If the user disables device power savings, the value of the AUTO_SUSPEND power policy setting is ignored.</li>
<li>If the user enables device power savings, then the value of AUTO_SUSPEND is used to determine whether to suspend the device when idle.</li>
</ul>
<p>The <strong>UserSetDeviceIdleEnabled</strong> is ignored if <strong>DeviceIdleEnabled</strong> is not set.</p>
<pre class="syntax" space="preserve"><code>HKR,,UserSetDeviceIdleEnabled,0x00010001,1</code></pre></td>
</tr>
<tr class="even">
<td><strong>DefaultIdleState</strong></td>
<td>This is a DWORD value. This registry value sets the default value of the AUTO_SUSPEND power policy setting. This registry key is used to enable or disable selective suspend when a handle is not open to the device.
<ul>
<li>A value of zero or the absence of this value indicates that by default, the device is not suspended when idle. The device be allowed to suspend when idle only when the AUTO_SUSPEND power policy is enabled.</li>
<li>A nonzero value indicates that by default the device is allowed to be suspended when idle.</li>
</ul>
<p>This value is ignored if <strong>DeviceIdleEnabled</strong> is not set.</p>
<pre class="syntax" space="preserve"><code>HKR,,DefaultIdleState,0x00010001,1</code></pre></td>
</tr>
<tr class="odd">
<td><strong>DefaultIdleTimeout</strong></td>
<td>This is a DWORD value. This registry value sets the default state of the SUSPEND_DELAY power policy setting.
<p>The value indicates the amount of time in milliseconds to wait before determining that a device is idle.</p>
<pre class="syntax" space="preserve"><code>HKR,,DefaultIdleTimeout,0x00010001,100</code></pre></td>
</tr>
</tbody>
</table>

 

<a href="" id="detecting-idle"></a>**Detecting Idle**  
All writes and control transfers force the device into the **D0** power state and reset the idle timer. The IN endpoint queues are not power managed. Read requests wake the device when they are submitted. However, a device can become idle while a read request waits.

## Related topics
[WinUSB Architecture and Modules](winusb-architecture.md)  
[Choosing a driver model for developing a USB client driver](winusb-considerations.md)  
[WinUSB (Winusb.sys) Installation](winusb-installation.md)  
[How to Access a USB Device by Using WinUSB Functions](using-winusb-api-to-communicate-with-a-usb-device.md)  
[WinUSB Functions for Pipe Policy Modification](winusb-functions-for-pipe-policy-modification.md)  
[WinUSB Functions](https://msdn.microsoft.com/library/windows/hardware/ff540046#winusb)  
[WinUSB](winusb.md)  
[**WinUsb\_GetPowerPolicy**](https://msdn.microsoft.com/library/windows/hardware/ff540275)  
[**WinUsb\_SetPowerPolicy**](https://msdn.microsoft.com/library/windows/hardware/ff540309)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20WinUSB%20Power%20Management%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


