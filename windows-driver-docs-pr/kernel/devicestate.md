---
title: DeviceState
author: windows-driver-content
description: DeviceState
MS-HAID:
- 'PwrMgmt\_4a82cdb0-4feb-4d5a-a8f6-b7887cdae825.xml'
- 'kernel.devicestate'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 4cf650ea-cccf-411c-809f-0a01e2ceb067
keywords: ["DeviceState"]
---

# DeviceState


## <a href="" id="ddk-devicestate-kg"></a>


The **DeviceState** member of [**DEVICE\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff543095) is an array of [**DEVICE\_POWER\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff543160) values that are indexed by [**SYSTEM\_POWER\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff564565) values ranging from **PowerSystemWorking** to **PowerSystemShutdown**. Each element of the array contains the maximum (highest-powered) device power state that the device can support for the system power state denoted by the index, or **PowerDeviceUnspecified** if the system power state is not supported.

For example, on a system that supports only S0, S4, and S5 [system power states](system-power-states.md), the **DeviceState** array for a device that supports only the D0 and D3 states contains the values shown in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>DeviceState element</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>DeviceState</strong>[<strong>PowerSystemWorking</strong>]</p></td>
<td><p><strong>PowerDeviceD0</strong></p></td>
</tr>
<tr class="even">
<td><p><strong>DeviceState</strong>[<strong>PowerSystemSleeping1</strong>]</p></td>
<td><p><strong>PowerDeviceUnspecified</strong></p></td>
</tr>
<tr class="odd">
<td><p><strong>DeviceState</strong>[<strong>PowerSystemSleeping2</strong>]</p></td>
<td><p><strong>PowerDeviceUnspecified</strong></p></td>
</tr>
<tr class="even">
<td><p><strong>DeviceState</strong>[<strong>PowerSystemSleeping3</strong>]</p></td>
<td><p><strong>PowerDeviceUnspecified</strong></p></td>
</tr>
<tr class="odd">
<td><p><strong>DeviceState</strong>[<strong>PowerSystemHibernate</strong>]</p></td>
<td><p><strong>PowerDeviceD3</strong></p></td>
</tr>
<tr class="even">
<td><p><strong>DeviceState</strong>[<strong>PowerSystemShutdown</strong>]</p></td>
<td><p><strong>PowerDeviceD3</strong></p></td>
</tr>
</tbody>
</table>

 

On a system that supports all of the system power states, the following table lists the values that the array would contain for a device that must be in the D2 state or lower whenever the system goes to any intermediate sleep state and in the D3 state when the system hibernates.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>DeviceState element</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>DeviceState</strong>[<strong>PowerSystemWorking</strong>]</p></td>
<td><p><strong>PowerDeviceD0</strong></p></td>
</tr>
<tr class="even">
<td><p><strong>DeviceState</strong>[<strong>PowerSystemSleeping1</strong>]</p></td>
<td><p><strong>PowerDeviceD2</strong></p></td>
</tr>
<tr class="odd">
<td><p><strong>DeviceState</strong>[<strong>PowerSystemSleeping2</strong>]</p></td>
<td><p><strong>PowerDeviceD2</strong></p></td>
</tr>
<tr class="even">
<td><p><strong>DeviceState</strong>[<strong>PowerSystemSleeping3</strong>]</p></td>
<td><p><strong>PowerDeviceD2</strong></p></td>
</tr>
<tr class="odd">
<td><p><strong>DeviceState</strong>[<strong>PowerSystemHibernate</strong>]</p></td>
<td><p><strong>PowerDeviceD3</strong></p></td>
</tr>
<tr class="even">
<td><p><strong>DeviceState</strong>[<strong>PowerSystemShutdown</strong>]</p></td>
<td><p><strong>PowerDeviceD3</strong></p></td>
</tr>
</tbody>
</table>

 

Note that the entries in the **DeviceState** array signify the highest device power state that the device can support for the corresponding system power state. In the preceding example, the device could be in state D3 for any system power state, state D2 for system power states **PowerSystemWorking** through **PowerSystemSleeping3**, and state D1 for system state **PowerSystemWorking**.

The bus driver or ACPI filter sets these values based on the capabilities of the parent device node.

As a general rule, higher-level drivers should not change these values. However, in the rare circumstances in which such a change is necessary, a driver can specify a lower (less-powered) state than the bus driver or ACPI filter originally returned. For example, assume that **DeviceState**\[**PowerSystemSleeping1**\] maps to **PowerDeviceD2**, as in the table above. A driver can change this value to **PowerDeviceD3**, but not to **PowerDeviceD1** or **PowerDeviceD0**.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20DeviceState%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


