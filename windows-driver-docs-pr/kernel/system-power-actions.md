---
title: System Power Actions
author: windows-driver-content
description: System Power Actions
ms.assetid: e8ab99d4-c18d-4ba8-bfe8-8eebb881c384
keywords: ["system power actions WDK power management", "system power states WDK kernel , power actions", "power actions WDK power management", "POWER_ACTION"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# System Power Actions


## <a href="" id="ddk-system-power-actions-kg"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20System%20Power%20Actions%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


