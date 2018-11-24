---
title: GPIO Interrupts
description: Some general-purpose I/O (GPIO) controller devices can configure their GPIO pins to function as interrupt request inputs.
ms.assetid: 0F56AD4C-E0BF-49F1-AB67-0107D08DEF9F
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GPIO Interrupts


Some general-purpose I/O (GPIO) controller devices can configure their GPIO pins to function as interrupt request inputs. These interrupt request inputs are driven by peripheral devices that are physically connected to the GPIO pins. The drivers for these GPIO controllers can enable, disable, mask, unmask, and clear interrupt requests on individual GPIO pins.

Support for GPIO interrupts is optional. The GPIO framework extension (GpioClx) does not require GPIO controllers to support GPIO interrupts.

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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/hh698263" data-raw-source="[Primary and Secondary Interrupts](https://msdn.microsoft.com/library/windows/hardware/hh698263)">Primary and Secondary Interrupts</a></p></td>
<td><p>GPIO interrupt handling is inherently a two-stage process. The interrupt from the general-purpose I/O (GPIO) controller, which causes the GPIO framework extension (GpioClx) interrupt service routine (ISR) to run, is called the <em>primary interrupt</em>. This ISR maps the interrupting GPIO pin to a global system interrupt (GSI), and passes this GSI to the hardware abstraction layer (HAL). The HAL generates a <em>secondary interrupt</em> to run a second ISR that is logically connected to the GPIO pin through this GSI. This process is shown in the diagram in <a href="https://msdn.microsoft.com/library/windows/hardware/hh439512#gpio-block-diagram" data-raw-source="[GPIO Driver Support Overview](https://msdn.microsoft.com/library/windows/hardware/hh439512#gpio-block-diagram)">GPIO Driver Support Overview</a>.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/hh698246" data-raw-source="[GPIO-Based Interrupt Resources](https://msdn.microsoft.com/library/windows/hardware/hh698246)">GPIO-Based Interrupt Resources</a></p></td>
<td><p>Drivers for peripheral devices that send interrupts to general-purpose I/O (GPIO) pins acquire GPIO interrupts as abstract Windows interrupt resources. <a href="https://msdn.microsoft.com/library/windows/hardware/ff544296" data-raw-source="[Kernel-mode driver framework](https://msdn.microsoft.com/library/windows/hardware/ff544296)">Kernel-mode driver framework</a> (KMDF) drivers receive these resources through their <a href="https://msdn.microsoft.com/library/windows/hardware/ff540880" data-raw-source="[&lt;em&gt;EvtDevicePrepareHardware&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540880)"><em>EvtDevicePrepareHardware</em></a> event callback functions. </p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/hh698262" data-raw-source="[Passive-Level ISRs](https://msdn.microsoft.com/library/windows/hardware/hh698262)">Passive-Level ISRs</a></p></td>
<td><p>Starting with Windows 8, kernel-mode driver framework (KMDF) and user-mode driver framework (UMDF) drivers can, as an option, register their interrupt service routines (ISRs) to run at passive level.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/hh698260" data-raw-source="[Interrupt-Related Callbacks](https://msdn.microsoft.com/library/windows/hardware/hh698260)">Interrupt-Related Callbacks</a></p></td>
<td><p>As an option, the driver for a general-purpose I/O (GPIO) controller can provide support for GPIO interrupts. To support GPIO interrupts, a GPIO controller driver implements a set of callback functions to manage these interrupts. The driver includes pointers to these callback functions in the registration packet that the driver supplies when it registers itself as a client of GPIO framework extension (GpioClx).</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/jj851070" data-raw-source="[Interrupt Synchronization for GPIO Controller Drivers](https://msdn.microsoft.com/library/windows/hardware/jj851070)">Interrupt Synchronization for GPIO Controller Drivers</a></p></td>
<td><p>GPIO controller drivers can call the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439482" data-raw-source="[&lt;strong&gt;GPIO_CLX_AcquireInterruptLock&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh439482)"><strong>GPIO_CLX_AcquireInterruptLock</strong></a> and <a href="https://msdn.microsoft.com/library/windows/hardware/hh439494" data-raw-source="[&lt;strong&gt;GPIO_CLX_ReleaseInterruptLock&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh439494)"><strong>GPIO_CLX_ReleaseInterruptLock</strong></a> methods to acquire and release interrupt locks that are implemented internally by the GPIO framework extension (GpioClx). Driver code that runs at IRQL = PASSIVE_LEVEL can call these methods to synchronize to the interrupt service routine (ISR) in GpioClx. GpioClx dedicates a separate interrupt lock to each bank of pins in the GPIO controller.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/hh698245" data-raw-source="[Enabling and Disabling Shared GPIO Interrupts](https://msdn.microsoft.com/library/windows/hardware/hh698245)">Enabling and Disabling Shared GPIO Interrupts</a></p></td>
<td><p>In some cases, interrupt request lines from two or more peripheral devices might connect to the same physical general-purpose I/O (GPIO) pin. The GPIO pin for a shared interrupt line is typically configured for level-triggered interrupts.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/hh698251" data-raw-source="[GPIO Interrupt Masks](https://msdn.microsoft.com/library/windows/hardware/hh698251)">GPIO Interrupt Masks</a></p></td>
<td><p>General-purpose I/O (GPIO) pins that are configured as interrupt inputs can be masked and unmasked in addition to being enabled and disabled.</p></td>
</tr>
</tbody>
</table>

 

 

 




