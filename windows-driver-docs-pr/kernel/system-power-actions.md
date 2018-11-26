---
title: System Power Actions
description: System Power Actions
ms.assetid: e8ab99d4-c18d-4ba8-bfe8-8eebb881c384
keywords: ["system power actions WDK power management", "system power states WDK kernel , power actions", "power actions WDK power management", "POWER_ACTION"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# System Power Actions





When the power manager sends an IRP to set or query the system power state, it specifies a system power state along with an additional parameter that gives information about the power state change. This parameter, passed at **Irp-&gt;Parameters.Power.ShutdownType**, is an enumerator of the POWER\_ACTION type. The enumerator characterizes the system power state request, as shown in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>POWER_ACTION enumerator</th>
<th>System power state requested</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>PowerActionNone</strong></p></td>
<td><p>S0 or no system power IRP active</p></td>
</tr>
<tr class="even">
<td><p><strong>PowerActionSleep</strong></p></td>
<td><p>S1, S2, or S3</p></td>
</tr>
<tr class="odd">
<td><p><strong>PowerActionHibernate</strong></p></td>
<td><p>S4</p></td>
</tr>
<tr class="even">
<td><p><strong>PowerActionShutdown</strong> (Microsoft Windows 2000 and later systems only)</p></td>
<td><p>S5</p></td>
</tr>
<tr class="odd">
<td><p><strong>PowerActionShutdownReset</strong></p></td>
<td><p>S5</p></td>
</tr>
<tr class="even">
<td><p><strong>PowerActionShutdownOff</strong></p></td>
<td><p>S5</p></td>
</tr>
</tbody>
</table>

 

When a driver receives a system query or set-power IRP for S5, it can check **ShutdownType** For more information about the requested shutdown. A driver can use this information to optimize its shutdown sequence when the machine is resetting instead of shutting off power indefinitely. Drivers of most devices retain power when the system resets. However, for certain devices, such as a video streaming device that performs direct memory access (DMA), a driver might choose to power down its device when the system is resetting, thus stopping any ongoing I/O.

When a device power policy owner sends a *device* power IRP to its device stack in response to a system power IRP, drivers can use the **ShutdownType** parameter to get information about the current *system* power IRP. In this case, the value of **ShutdownType** indicates the currently requested system power state, or it is **PowerActionNone** if a system request is not outstanding. Drivers should not, however, rely on this information if the device IRP requests state D0.

In Windows 98/Me, this member always contains **PowerActionNone** when the IRP requests a device power state.

 

 




