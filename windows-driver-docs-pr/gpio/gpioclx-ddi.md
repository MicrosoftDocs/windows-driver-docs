---
title: GpioClx DDI
author: windows-driver-content
description: The general-purpose I/O (GPIO) controller driver communicates with the GPIO framework extension (GpioClx) through the GpioClx device-driver interface (DDI).
ms.assetid: AE8883C3-178F-44AB-AB1D-65DEC1472929
---

# GpioClx DDI


The general-purpose I/O (GPIO) controller driver communicates with the GPIO framework extension (GpioClx) through the GpioClx device-driver interface (DDI). This DDI is defined in the Gpioclx.h header file and is described in [General-Purpose I/O (GPIO) Driver Reference](https://msdn.microsoft.com/library/windows/hardware/hh439515). As part of this DDI, GpioClx implements several [driver support methods](https://msdn.microsoft.com/library/windows/hardware/hh439460), which are called by the GPIO controller driver. This driver implements a set of [event callback functions](https://msdn.microsoft.com/library/windows/hardware/hh439464), which are called by GpioClx. GpioClx uses these callbacks to manage interrupt requests from GPIO pins that are configured as interrupt inputs, and to transfer data to or from GPIO pins that are configured as data inputs and outputs.

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
<td><p>[Driver Support Methods in the GpioClx DDI](https://msdn.microsoft.com/library/windows/hardware/hh439453)</p></td>
<td><p>The GPIO framework extension (GpioClx) is available starting with Windows 8. The system-supplied methods in the GpioClx DDI are implemented in the GpioClx kernel-mode driver, Msgpioclx.sys. This driver exports entry points for the [GpioClx driver support methods](https://msdn.microsoft.com/library/windows/hardware/hh439460). Starting with Windows 8, Msgpioclx.sys is a standard component of the operating system.</p></td>
</tr>
<tr class="even">
<td><p>[Optional and Required GPIO Callback Functions](https://msdn.microsoft.com/library/windows/hardware/hh406514)</p></td>
<td><p>A general-purpose I/O (GPIO) controller driver calls the [<strong>GPIO_CLX_RegisterClient</strong>](https://msdn.microsoft.com/library/windows/hardware/hh439490) method to register as a client of the GPIO framework extension (GpioClx). During this call, the driver passes a registration packet to GpioClx that specifies a list of event callback functions that are implemented by the driver. GpioClx calls these callback functions to configure the GPIO controller hardware, perform I/O operations, and manage interrupts. GpioClx requires a GPIO controller driver to implement certain callback functions, but support for other callback functions is optional.</p></td>
</tr>
<tr class="odd">
<td><p>[GPIO Device Contexts](https://msdn.microsoft.com/library/windows/hardware/hh406460)</p></td>
<td><p>A general-purpose I/O (GPIO) controller device is represented by a framework device object. The GPIO controller driver can associate a device context with this device object. The driver uses this device context to persistently store information about the state of the GPIO controller device.</p></td>
</tr>
<tr class="even">
<td><p>[Partitioning a GPIO Controller into Banks of Pins](https://msdn.microsoft.com/library/windows/hardware/hh406517)</p></td>
<td><p>A driver developer can, as an option, partition a general-purpose I/O (GPIO) controller device into two or more banks of GPIO pins. For example, a GPIO controller device that has 64 GPIO pins can be described by the GPIO controller driver as two banks, each of which has 32 GPIO pins.</p></td>
</tr>
<tr class="odd">
<td><p>[Implementation Issues for GPIO Controller Drivers](https://msdn.microsoft.com/library/windows/hardware/hh406479)</p></td>
<td><p>The GPIO framework extension (GpioClx) provides a flexible device driver interface (DDI). This DDI enables developers to choose among alternative callback interfaces. A driver developer should implement the set of event callback functions that is best suited to the hardware architecture of the target GPIO controller device.</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------


