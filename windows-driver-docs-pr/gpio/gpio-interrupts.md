---
title: GPIO Interrupts
description: Some general-purpose I/O (GPIO) controller devices can configure their GPIO pins to function as interrupt request inputs.
ms.date: 03/03/2023
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
<td><p><a href="/windows-hardware/drivers/gpio/primary-and-secondary-interrupts" data-raw-source="[Primary and Secondary Interrupts](./primary-and-secondary-interrupts.md)">Primary and Secondary Interrupts</a></p></td>
<td><p>GPIO interrupt handling is inherently a two-stage process. The interrupt from the general-purpose I/O (GPIO) controller, which causes the GPIO framework extension (GpioClx) interrupt service routine (ISR) to run, is called the <em>primary interrupt</em>. This ISR maps the interrupting GPIO pin to a global system interrupt (GSI), and passes this GSI to the hardware abstraction layer (HAL). The HAL generates a <em>secondary interrupt</em> to run a second ISR that is logically connected to the GPIO pin through this GSI. This process is shown in the diagram in <a href="/windows-hardware/drivers/gpio/gpio-driver-support-overview#gpio-block-diagram" data-raw-source="[GPIO Driver Support Overview](./gpio-driver-support-overview.md#gpio-block-diagram)">GPIO Driver Support Overview</a>.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/gpio/gpio-based-interrupt-resources" data-raw-source="[GPIO-Based Interrupt Resources](./gpio-based-interrupt-resources.md)">GPIO-Based Interrupt Resources</a></p></td>
<td><p>Drivers for peripheral devices that send interrupts to general-purpose I/O (GPIO) pins acquire GPIO interrupts as abstract Windows interrupt resources. <a href="/windows-hardware/drivers/wdf/what-s-new-for-wdf-drivers" data-raw-source="[Kernel-mode driver framework](../wdf/index.md)">Kernel-mode driver framework</a> (KMDF) drivers receive these resources through their <a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_prepare_hardware" data-raw-source="[&lt;em&gt;EvtDevicePrepareHardware&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_prepare_hardware)"><em>EvtDevicePrepareHardware</em></a> event callback functions. </p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/gpio/passive-level-isrs" data-raw-source="[Passive-Level ISRs](./passive-level-isrs.md)">Passive-Level ISRs</a></p></td>
<td><p>Starting with Windows 8, kernel-mode driver framework (KMDF) and user-mode driver framework (UMDF) drivers can, as an option, register their interrupt service routines (ISRs) to run at passive level.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/gpio/interrupt-related-callbacks" data-raw-source="[Interrupt-Related Callbacks](./interrupt-related-callbacks.md)">Interrupt-Related Callbacks</a></p></td>
<td><p>As an option, the driver for a general-purpose I/O (GPIO) controller can provide support for GPIO interrupts. To support GPIO interrupts, a GPIO controller driver implements a set of callback functions to manage these interrupts. The driver includes pointers to these callback functions in the registration packet that the driver supplies when it registers itself as a client of GPIO framework extension (GpioClx).</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/gpio/interrupt-synchronization-for-gpio-controller-drivers" data-raw-source="[Interrupt Synchronization for GPIO Controller Drivers](./interrupt-synchronization-for-gpio-controller-drivers.md)">Interrupt Synchronization for GPIO Controller Drivers</a></p></td>
<td><p>GPIO controller drivers can call the <a href="/windows-hardware/drivers/ddi/gpioclx/nf-gpioclx-gpio_clx_acquireinterruptlock" data-raw-source="[&lt;strong&gt;GPIO_CLX_AcquireInterruptLock&lt;/strong&gt;](/windows-hardware/drivers/ddi/gpioclx/nf-gpioclx-gpio_clx_acquireinterruptlock)"><strong>GPIO_CLX_AcquireInterruptLock</strong></a> and <a href="/windows-hardware/drivers/ddi/gpioclx/nf-gpioclx-gpio_clx_releaseinterruptlock" data-raw-source="[&lt;strong&gt;GPIO_CLX_ReleaseInterruptLock&lt;/strong&gt;](/windows-hardware/drivers/ddi/gpioclx/nf-gpioclx-gpio_clx_releaseinterruptlock)"><strong>GPIO_CLX_ReleaseInterruptLock</strong></a> methods to acquire and release interrupt locks that are implemented internally by the GPIO framework extension (GpioClx). Driver code that runs at IRQL = PASSIVE_LEVEL can call these methods to synchronize to the interrupt service routine (ISR) in GpioClx. GpioClx dedicates a separate interrupt lock to each bank of pins in the GPIO controller.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/gpio/enabling-and-disabling-shared-gpio-interrupts" data-raw-source="[Enabling and Disabling Shared GPIO Interrupts](./enabling-and-disabling-shared-gpio-interrupts.md)">Enabling and Disabling Shared GPIO Interrupts</a></p></td>
<td><p>In some cases, interrupt request lines from two or more peripheral devices might connect to the same physical general-purpose I/O (GPIO) pin. The GPIO pin for a shared interrupt line is typically configured for level-triggered interrupts.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/gpio/gpio-interrupt-masks" data-raw-source="[GPIO Interrupt Masks](./gpio-interrupt-masks.md)">GPIO Interrupt Masks</a></p></td>
<td><p>General-purpose I/O (GPIO) pins that are configured as interrupt inputs can be masked and unmasked in addition to being enabled and disabled.</p></td>
</tr>
</tbody>
</table>

 

