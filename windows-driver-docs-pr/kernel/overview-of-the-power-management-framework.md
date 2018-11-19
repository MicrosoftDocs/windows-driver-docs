---
title: Overview of the Power Management Framework
description: Starting with Windows 8, the run-time power management framework (PoFx) supports power and clock management at the component (or subdevice) level.
ms.assetid: 9F2D8ACD-44D5-46E0-9FC7-1B38B99450FF
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Overview of the Power Management Framework


Starting with Windows 8, the run-time power management framework (PoFx) supports power and clock management at the component (or subdevice) level. A device driver registers with PoFx to independently manage power usage in the individual components in a device. PoFx provides the fine-grained control necessary to extend the time that a Windows portable computer, tablet, phone, or other mobile device can run on a battery charge. PoFx reduces power usage in a way that maintains the appearance of a mobile device that is always on and always connected.

A component, or subdevice, is a functional hardware unit in a device that can be turned on or switched to a low-power state independently of the other components in the same device. For example, an audio device might have separate components for playback and recording whose power states can be managed independently of each other. If the playback component is being used, but the recording component is idle, the recording component can be switched to a low-power state without interfering with the activity of the playback component.

## In this section


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Topic</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="component-level-power-management.md" data-raw-source="[Component-Level Power Management](component-level-power-management.md)">Component-Level Power Management</a></p></td>
<td><p>Starting with Windows 8, the power management framework (PoFx) enables a driver to manage the power states of the individual components in a device. Component-level power management exists side-by-side with device-level power management.</p></td>
</tr>
<tr class="even">
<td><p><a href="component-level-performance-management.md" data-raw-source="[Component-Level Performance State Management](component-level-performance-management.md)">Component-Level Performance State Management</a></p></td>
<td><p>Starting with Windows 10, the power management framework (PoFx) enables a driver to define one or more sets of individually adjustable performance states for individual components within a device. The driver can use performance states to throttle a component&#39;s workload to provide just enough performance for its current needs.</p></td>
</tr>
</tbody>
</table>

 

 

 




