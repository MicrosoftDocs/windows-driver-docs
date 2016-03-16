---
title: Supporting Functional Power States
description: Supporting Functional Power States
ms.assetid: F96214C9-702D-402E-B873-5DF57C521B34
---

# Supporting Functional Power States


Starting in Windows 8, the power manager includes the run-time power management framework (PoFx). PoFx supports power and clock management at the component (or subdevice) level.

Starting in KMDF version 1.11, KMDF drivers can take advantage of the fine-grained power control that PoFx offers. In particular, a KMDF driver can define multiple logical components within a single device, each of which can be independently power managed.

For example, a function driver might define a unique set of functional power states for each logical component of a device. Similar to device and system power states, F0 indicates that the component is fully on, while optional states F1, F2, and so on indicate progressively lower power states. To support Fx states, a driver must be the power policy owner for the device.

The following table summarizes framework support for different functional power state scenarios.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Type</th>
<th align="left">KMDF Support</th>
<th align="left">UMDF Support</th>
<th align="left">When to use/how to Implement</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[Single component, single state (F0)](supporting-multiple-functional-power-states-for-single-component-devices.md)</p></td>
<td align="left"><p>Supported</p></td>
<td align="left"><p>Supported</p></td>
<td align="left"><p>When you want the power engine plug-in (PEP) to determine the idle timeout value, and your driver has only one F-state.</p>
<p>Call [<strong>WdfDeviceAssignS0IdleSettings</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545903) with <em>IdleTimeoutType</em> = <strong>SystemManagedIdleTimout</strong> or <strong>SystemManagedIdleTimoutWithHint</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Single component, multiple states (F0, F1, F2…)](supporting-multiple-functional-power-states-for-single-component-devices.md)</p></td>
<td align="left"><p>Supported</p></td>
<td align="left"><p>Not supported</p></td>
<td align="left"><p>When your driver has more than one F-state.</p>
<ul>
<li>Call [<strong>WdfDeviceWdmAssignPowerFrameworkSettings</strong>](https://msdn.microsoft.com/library/windows/hardware/hh451097) to register WDM PoFx callbacks.</li>
<li>Call [<strong>WdfDeviceAssignS0IdleSettings</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545903) with <em>IdleTimeoutType</em> = <strong>SystemManagedIdleTimout</strong>.</li>
</ul>
<p>In this case, KMDF handles most interactions with the PoFx.</p>
<p>For sample code, see [PoFx sample drivers](http://go.microsoft.com/fwlink/p/?LinkId=617937).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Multiple components, single or multiple states](supporting-multiple-functional-power-states-for-multiple-component-devices.md)</p></td>
<td align="left"><p>Supported using WDM interfaces</p></td>
<td align="left"><p>Not supported</p></td>
<td align="left"><p>When your driver has multiple components. In this case, you must use the PoFx interfaces directly.</p>
<p>For sample code, see [PoFx sample drivers](http://go.microsoft.com/fwlink/p/?LinkId=617937).</p></td>
</tr>
</tbody>
</table>

 

Because KMDF adds minimal abstraction on top of PoFx, it is helpful to have a basic understanding of PoFx before writing your driver. Accordingly, we recommend that you read [Overview of the Power Management Framework](https://msdn.microsoft.com/library/windows/hardware/hh406637) before reading these topics.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Supporting%20Functional%20Power%20States%20%20RELEASE:%20%283/16/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




