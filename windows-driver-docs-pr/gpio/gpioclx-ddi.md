---
title: GpioClx DDI
description: The general-purpose I/O (GPIO) controller driver communicates with the GPIO framework extension (GpioClx) through the GpioClx device-driver interface (DDI).
ms.date: 04/20/2017
---

# GpioClx DDI


The general-purpose I/O (GPIO) controller driver communicates with the GPIO framework extension (GpioClx) through the GpioClx device-driver interface (DDI). This DDI is defined in the Gpioclx.h header file and is described in [General-Purpose I/O (GPIO) Driver Reference](/windows-hardware/drivers/ddi/index). As part of this DDI, GpioClx implements several [driver support methods](/previous-versions/hh439460(v=vs.85)), which are called by the GPIO controller driver. This driver implements a set of [event callback functions](/previous-versions/hh439464(v=vs.85)), which are called by GpioClx. GpioClx uses these callbacks to manage interrupt requests from GPIO pins that are configured as interrupt inputs, and to transfer data to or from GPIO pins that are configured as data inputs and outputs.

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
<td><p><a href="/windows-hardware/drivers/gpio/driver-support-methods-in-the-gpioclx-ddi" data-raw-source="[Driver Support Methods in the GpioClx DDI](./driver-support-methods-in-the-gpioclx-ddi.md)">Driver Support Methods in the GpioClx DDI</a></p></td>
<td><p>The GPIO framework extension (GpioClx) is available starting with Windows 8. The system-supplied methods in the GpioClx DDI are implemented in the GpioClx kernel-mode driver, Msgpioclx.sys. This driver exports entry points for the <a href="/previous-versions/hh439460(v=vs.85)" data-raw-source="[GpioClx driver support methods](/previous-versions/hh439460(v=vs.85))">GpioClx driver support methods</a>. Starting with Windows 8, Msgpioclx.sys is a standard component of the operating system.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/gpio/optional-and-required-gpio-callback-functions" data-raw-source="[Optional and Required GPIO Callback Functions](./optional-and-required-gpio-callback-functions.md)">Optional and Required GPIO Callback Functions</a></p></td>
<td><p>A general-purpose I/O (GPIO) controller driver calls the <a href="/windows-hardware/drivers/ddi/gpioclx/nf-gpioclx-gpio_clx_registerclient" data-raw-source="[&lt;strong&gt;GPIO_CLX_RegisterClient&lt;/strong&gt;](/windows-hardware/drivers/ddi/gpioclx/nf-gpioclx-gpio_clx_registerclient)"><strong>GPIO_CLX_RegisterClient</strong></a> method to register as a client of the GPIO framework extension (GpioClx). During this call, the driver passes a registration packet to GpioClx that specifies a list of event callback functions that are implemented by the driver. GpioClx calls these callback functions to configure the GPIO controller hardware, perform I/O operations, and manage interrupts. GpioClx requires a GPIO controller driver to implement certain callback functions, but support for other callback functions is optional.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/gpio/gpio-device-contexts" data-raw-source="[GPIO Device Contexts](./gpio-device-contexts.md)">GPIO Device Contexts</a></p></td>
<td><p>A general-purpose I/O (GPIO) controller device is represented by a framework device object. The GPIO controller driver can associate a device context with this device object. The driver uses this device context to persistently store information about the state of the GPIO controller device.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/gpio/partitioning-a-gpio-controller-into-banks-of-pins" data-raw-source="[Partitioning a GPIO Controller into Banks of Pins](./partitioning-a-gpio-controller-into-banks-of-pins.md)">Partitioning a GPIO Controller into Banks of Pins</a></p></td>
<td><p>A driver developer can, as an option, partition a general-purpose I/O (GPIO) controller device into two or more banks of GPIO pins. For example, a GPIO controller device that has 64 GPIO pins can be described by the GPIO controller driver as two banks, each of which has 32 GPIO pins.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/gpio/implementation-issues-for-gpio-controller-drivers" data-raw-source="[Implementation Issues for GPIO Controller Drivers](./implementation-issues-for-gpio-controller-drivers.md)">Implementation Issues for GPIO Controller Drivers</a></p></td>
<td><p>The GPIO framework extension (GpioClx) provides a flexible device driver interface (DDI). This DDI enables developers to choose among alternative callback interfaces. A driver developer should implement the set of event callback functions that is best suited to the hardware architecture of the target GPIO controller device.</p></td>
</tr>
</tbody>
</table>

 

