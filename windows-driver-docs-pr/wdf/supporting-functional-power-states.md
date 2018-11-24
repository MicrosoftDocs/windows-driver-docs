---
title: Supporting Functional Power States
description: Supporting Functional Power States
ms.assetid: F96214C9-702D-402E-B873-5DF57C521B34
ms.date: 04/20/2017
ms.localizationpriority: medium
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
<td align="left"><p><a href="supporting-multiple-functional-power-states-for-single-component-devices.md" data-raw-source="[Single component, single state (F0)](supporting-multiple-functional-power-states-for-single-component-devices.md)">Single component, single state (F0)</a></p></td>
<td align="left"><p>Supported</p></td>
<td align="left"><p>Supported</p></td>
<td align="left"><p>When you want the power engine plug-in (PEP) to determine the idle timeout value, and your driver has only one F-state.</p>
<p>Call <a href="https://msdn.microsoft.com/library/windows/hardware/ff545903" data-raw-source="[&lt;strong&gt;WdfDeviceAssignS0IdleSettings&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545903)"><strong>WdfDeviceAssignS0IdleSettings</strong></a> with <em>IdleTimeoutType</em> = <strong>SystemManagedIdleTimout</strong> or <strong>SystemManagedIdleTimoutWithHint</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="supporting-multiple-functional-power-states-for-single-component-devices.md" data-raw-source="[Single component, multiple states (F0, F1, F2…)](supporting-multiple-functional-power-states-for-single-component-devices.md)">Single component, multiple states (F0, F1, F2…)</a></p></td>
<td align="left"><p>Supported</p></td>
<td align="left"><p>Not supported</p></td>
<td align="left"><p>When your driver has more than one F-state.</p>
<ul>
<li>Call <a href="https://msdn.microsoft.com/library/windows/hardware/hh451097" data-raw-source="[&lt;strong&gt;WdfDeviceWdmAssignPowerFrameworkSettings&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh451097)"><strong>WdfDeviceWdmAssignPowerFrameworkSettings</strong></a> to register WDM PoFx callbacks.</li>
<li>Call <a href="https://msdn.microsoft.com/library/windows/hardware/ff545903" data-raw-source="[&lt;strong&gt;WdfDeviceAssignS0IdleSettings&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545903)"><strong>WdfDeviceAssignS0IdleSettings</strong></a> with <em>IdleTimeoutType</em> = <strong>SystemManagedIdleTimout</strong>.</li>
</ul>
<p>In this case, KMDF handles most interactions with the PoFx.</p>
<p>For sample code, see <a href="http://go.microsoft.com/fwlink/p/?LinkId=617937" data-raw-source="[PoFx sample drivers](http://go.microsoft.com/fwlink/p/?LinkId=617937)">PoFx sample drivers</a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="supporting-multiple-functional-power-states-for-multiple-component-devices.md" data-raw-source="[Multiple components, single or multiple states](supporting-multiple-functional-power-states-for-multiple-component-devices.md)">Multiple components, single or multiple states</a></p></td>
<td align="left"><p>Supported using WDM interfaces</p></td>
<td align="left"><p>Not supported</p></td>
<td align="left"><p>When your driver has multiple components. In this case, you must use the PoFx interfaces directly.</p>
<p>For sample code, see <a href="http://go.microsoft.com/fwlink/p/?LinkId=617937" data-raw-source="[PoFx sample drivers](http://go.microsoft.com/fwlink/p/?LinkId=617937)">PoFx sample drivers</a>.</p></td>
</tr>
</tbody>
</table>

 

Because KMDF adds minimal abstraction on top of PoFx, it is helpful to have a basic understanding of PoFx before writing your driver. Accordingly, we recommend that you read [Overview of the Power Management Framework](https://msdn.microsoft.com/library/windows/hardware/hh406637) before reading these topics.

 

 





