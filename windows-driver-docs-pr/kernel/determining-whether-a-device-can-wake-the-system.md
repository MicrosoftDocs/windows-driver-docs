---
title: Determining Whether a Device Can Wake the System
author: windows-driver-content
description: Determining Whether a Device Can Wake the System
MS-HAID:
- 'PwrMgmt\_34ea8a1f-14e1-49c5-97ed-e008016df858.xml'
- 'kernel.determining\_whether\_a\_device\_can\_wake\_the\_system'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 59f23035-4169-4dd4-ac60-882c32efda2c
keywords: ["wait/wake IRPs WDK power management , devices with wake capability", "power management WDK kernel , wake-up capabilities", "external wake signals WDK", "awakening devices", "wake-up capabilities WDK power management", "device wake ups WDK power management"]
---

# Determining Whether a Device Can Wake the System


## <a href="" id="ddk-determining-whether-a-device-can-wake-the-system-kg"></a>


Some devices, such as keyboards, modems, and network cards, can respond to external signals while in a device sleep state. As part of its power management technology, the operating system provides a way for such devices to wake a sleeping system, which can then restore its previous context. The software wake-up mechanism allows a system to awaken from any state except S5 (**PowerSystemShutdown**), depending on support in the system and device hardware and BIOS. A system in state S5 must always be rebooted.

Although the operating system is designed to awaken from any of the intermediate sleep states, the exact wake-up capabilities vary from computer to computer and device to device. Not all computers support all system sleep states; therefore, the ability to wake from certain states is meaningless on some computers.

Similarly, most devices neither support all device power states (D0 through D3) nor support wake-up from all the device power states that they do support.

The sleep states that a device can enter, along with the states from which it supports wake up, are described at enumeration by the bus driver and are stored in the [**DEVICE\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff543095) structure. The following table lists the members of this structure that are relevant to wait/wake support.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Member</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[<strong>DeviceD1</strong>](deviced1-and-deviced2.md)</p></td>
<td><p>True if device supports state PowerDeviceD1.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>DeviceD2</strong>](deviced1-and-deviced2.md)</p></td>
<td><p>True if device supports state PowerDeviceD2.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>WakeFromD0</strong>](wakefromd0--wakefromd1--wakefromd2--and-wakefromd3.md)</p></td>
<td><p>True if device can wake from PowerDeviceD0.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>WakeFromD1</strong>](wakefromd0--wakefromd1--wakefromd2--and-wakefromd3.md)</p></td>
<td><p>True if device can wake from PowerDeviceD1.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>WakeFromD2</strong>](wakefromd0--wakefromd1--wakefromd2--and-wakefromd3.md)</p></td>
<td><p>True if device can wake from PowerDeviceD2.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>WakeFromD3</strong>](wakefromd0--wakefromd1--wakefromd2--and-wakefromd3.md)</p></td>
<td><p>True if device can wake from PowerDeviceD3.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>DeviceState</strong>](devicestate.md) [PowerSystemMaximum]</p></td>
<td><p>Specifies highest device power state that this device can support for each system power state, from PowerSystemUnspecified to PowerSystemShutdown.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>SystemWake</strong>](systemwake.md)</p></td>
<td><p>Specifies lowest system power state (S0 through S4) from which the system can be awakened.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>DeviceWake</strong>](devicewake.md)</p></td>
<td><p>Specifies lowest device power state (D0 through D3) from which the device can awaken.</p></td>
</tr>
</tbody>
</table>

 

The **DeviceWake** entry lists the lowest device power state from which the device can respond to a wake-up signal. The value PowerDeviceUnspecified indicates that the device cannot wake the system. The **SystemWake** entry lists the lowest system power state from which the system can be awakened. These values are based on the capabilities of the parent devnode and drivers should not change them. For more information, see [Reporting Device Power Capabilities](reporting-device-power-capabilities.md).

In general, a device can wake the system if the following are true:

-   The device is in a power state equal to or more-powered than the **DeviceWake** value.

-   The system is in a power state equal to or more powered than the **SystemWake** value.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Determining%20Whether%20a%20Device%20Can%20Wake%20the%20System%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


