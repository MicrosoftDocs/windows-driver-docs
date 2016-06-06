---
title: General-Purpose I/O (GPIO) Driver Design Guide
author: windows-driver-content
description: This section describes how to write a driver for a general-purpose I/O (GPIO) controller device.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: D11E72AC-2B0D-4325-8BD0-9AE9B21AFD8D
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
<td><p>[GPIO Driver Support Overview](https://msdn.microsoft.com/library/windows/hardware/hh439512)</p></td>
<td><p>Starting with Windows 8, the GPIO framework extension (GpioClx) simplifies the task of writing a driver for a GPIO controller device. Additionally, GpioClx provides driver support for peripheral devices that connect to GPIO pins. GpioClx, which is a system-supplied extension to the kernel-mode driver framework (KMDF), performs processing tasks that are common to members of the GPIO device class.</p></td>
</tr>
<tr class="even">
<td><p>[GpioClx I/O and Interrupt Interfaces](https://msdn.microsoft.com/library/windows/hardware/hh439467)</p></td>
<td><p>Typically, the clients of a GPIO controller are drivers for peripheral devices that connect to GPIO pins. These drivers use GPIO pins as low-bandwidth data channels, device-select outputs, and interrupt-request inputs. Peripheral device drivers open logical connections to GPIO pins that are configured as data inputs or outputs. They use these connections to send I/O requests to these pins. In addition, peripheral device drivers can logically connect their interrupt service routines to GPIO pins that are configured as interrupt request inputs.</p></td>
</tr>
<tr class="odd">
<td><p>[GPIO-Based Hardware Resources](https://msdn.microsoft.com/library/windows/hardware/hh439476)</p></td>
<td><p>Starting with Windows 8, the general-purpose I/O (GPIO) pins that are controlled by a GPIO controller driver are available to other drivers as system-managed hardware resources. GPIO I/O pins, which are pins that are configured as data inputs or data outputs, are available as a new Windows resource type, <em>GPIO I/O resources</em>. In addition, GPIO interrupt pins, which are pins that are configured as interrupt request inputs, are available as ordinary Windows interrupt resources.</p></td>
</tr>
<tr class="even">
<td><p>[GPIO Interrupts](https://msdn.microsoft.com/library/windows/hardware/hh406467)</p></td>
<td><p>Some general-purpose I/O (GPIO) controller devices can configure their GPIO pins to function as interrupt request inputs. These interrupt request inputs are driven by peripheral devices that are physically connected to the GPIO pins. The drivers for these GPIO controllers can enable, disable, mask, unmask, and clear interrupt requests on individual GPIO pins.</p></td>
</tr>
<tr class="odd">
<td><p>[GpioClx DDI](https://msdn.microsoft.com/library/windows/hardware/hh439456)</p></td>
<td><p>The general-purpose I/O (GPIO) controller driver communicates with the GPIO framework extension (GpioClx) through the GpioClx device-driver interface (DDI). This DDI is defined in the Gpioclx.h header file and is described in [General-Purpose I/O (GPIO) Driver Reference](https://msdn.microsoft.com/library/windows/hardware/hh439515). As part of this DDI, GpioClx implements several [driver support methods](https://msdn.microsoft.com/library/windows/hardware/hh439460), which are called by the GPIO controller driver. This driver implements a set of [event callback functions](https://msdn.microsoft.com/library/windows/hardware/hh439464), which are called by GpioClx. GpioClx uses these callbacks to manage interrupt requests from GPIO pins that are configured as interrupt inputs, and to transfer data to or from GPIO pins that are configured as data inputs and outputs.</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bgpio\parports%5D:%20General-Purpose%20I/O%20%28GPIO%29%20Driver%20Design%20Guide%20%20RELEASE:%20%286/3/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


