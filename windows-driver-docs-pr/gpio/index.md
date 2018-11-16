---
title: General-Purpose I/O (GPIO) Driver Design Guide
description: This section describes how to write a driver for a general-purpose I/O (GPIO) controller device.
ms.assetid: D11E72AC-2B0D-4325-8BD0-9AE9B21AFD8D
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# General-Purpose I/O (GPIO) Driver Design Guide


This section describes how to write a driver for a general-purpose I/O (GPIO) controller device. A GPIO controller configures GPIO pins to perform low-speed data I/O operations, to act as device-selects, and to receive interrupt requests. Starting with Windows 8, the GPIO framework extension (GpioClx) simplifies the task of writing a driver for a GPIO controller. Additionally, GpioClx provides a uniform I/O request interface to peripheral device drivers that communicate with devices that connect to GPIO pins on a controller.

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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/hh439512" data-raw-source="[GPIO Driver Support Overview](https://msdn.microsoft.com/library/windows/hardware/hh439512)">GPIO Driver Support Overview</a></p></td>
<td><p>Starting with Windows 8, the GPIO framework extension (GpioClx) simplifies the task of writing a driver for a GPIO controller device. Additionally, GpioClx provides driver support for peripheral devices that connect to GPIO pins. GpioClx, which is a system-supplied extension to the kernel-mode driver framework (KMDF), performs processing tasks that are common to members of the GPIO device class.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/hh439467" data-raw-source="[GpioClx I/O and Interrupt Interfaces](https://msdn.microsoft.com/library/windows/hardware/hh439467)">GpioClx I/O and Interrupt Interfaces</a></p></td>
<td><p>Typically, the clients of a GPIO controller are drivers for peripheral devices that connect to GPIO pins. These drivers use GPIO pins as low-bandwidth data channels, device-select outputs, and interrupt-request inputs. Peripheral device drivers open logical connections to GPIO pins that are configured as data inputs or outputs. They use these connections to send I/O requests to these pins. In addition, peripheral device drivers can logically connect their interrupt service routines to GPIO pins that are configured as interrupt request inputs.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/hh439476" data-raw-source="[GPIO-Based Hardware Resources](https://msdn.microsoft.com/library/windows/hardware/hh439476)">GPIO-Based Hardware Resources</a></p></td>
<td><p>Starting with Windows 8, the general-purpose I/O (GPIO) pins that are controlled by a GPIO controller driver are available to other drivers as system-managed hardware resources. GPIO I/O pins, which are pins that are configured as data inputs or data outputs, are available as a new Windows resource type, <em>GPIO I/O resources</em>. In addition, GPIO interrupt pins, which are pins that are configured as interrupt request inputs, are available as ordinary Windows interrupt resources.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/hh406467" data-raw-source="[GPIO Interrupts](https://msdn.microsoft.com/library/windows/hardware/hh406467)">GPIO Interrupts</a></p></td>
<td><p>Some general-purpose I/O (GPIO) controller devices can configure their GPIO pins to function as interrupt request inputs. These interrupt request inputs are driven by peripheral devices that are physically connected to the GPIO pins. The drivers for these GPIO controllers can enable, disable, mask, unmask, and clear interrupt requests on individual GPIO pins.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/hh439456" data-raw-source="[GpioClx DDI](https://msdn.microsoft.com/library/windows/hardware/hh439456)">GpioClx DDI</a></p></td>
<td><p>The general-purpose I/O (GPIO) controller driver communicates with the GPIO framework extension (GpioClx) through the GpioClx device-driver interface (DDI). This DDI is defined in the Gpioclx.h header file and is described in <a href="https://msdn.microsoft.com/library/windows/hardware/hh439515" data-raw-source="[General-Purpose I/O (GPIO) Driver Reference](https://msdn.microsoft.com/library/windows/hardware/hh439515)">General-Purpose I/O (GPIO) Driver Reference</a>. As part of this DDI, GpioClx implements several <a href="https://msdn.microsoft.com/library/windows/hardware/hh439460" data-raw-source="[driver support methods](https://msdn.microsoft.com/library/windows/hardware/hh439460)">driver support methods</a>, which are called by the GPIO controller driver. This driver implements a set of <a href="https://msdn.microsoft.com/library/windows/hardware/hh439464" data-raw-source="[event callback functions](https://msdn.microsoft.com/library/windows/hardware/hh439464)">event callback functions</a>, which are called by GpioClx. GpioClx uses these callbacks to manage interrupt requests from GPIO pins that are configured as interrupt inputs, and to transfer data to or from GPIO pins that are configured as data inputs and outputs.</p></td>
</tr>
</tbody>
</table>

 

 

 




