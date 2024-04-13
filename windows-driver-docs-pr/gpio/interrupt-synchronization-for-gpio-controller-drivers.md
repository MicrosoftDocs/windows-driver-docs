---
title: Interrupt Synchronization for GPIO Controller Drivers
description: GPIO controller drivers can call the GPIO_CLX_AcquireInterruptLock and GPIO_CLX_ReleaseInterruptLock methods to acquire and release interrupt locks that are implemented internally by the GPIO framework extension (GpioClx).
ms.date: 03/03/2023
---

# Interrupt Synchronization for GPIO Controller Drivers


GPIO controller drivers can call the [**GPIO\_CLX\_AcquireInterruptLock**](/windows-hardware/drivers/ddi/gpioclx/nf-gpioclx-gpio_clx_acquireinterruptlock) and [**GPIO\_CLX\_ReleaseInterruptLock**](/windows-hardware/drivers/ddi/gpioclx/nf-gpioclx-gpio_clx_releaseinterruptlock) methods to acquire and release interrupt locks that are implemented internally by the GPIO framework extension (GpioClx). Driver code that runs at IRQL = PASSIVE\_LEVEL can call these methods to synchronize to the interrupt service routine (ISR) in GpioClx. GpioClx dedicates a separate interrupt lock to each bank of pins in the GPIO controller.

If the hardware registers of the GPIO controller are memory-mapped, the ISR in GpioClx calls certain driver-implemented event callback functions at DIRQL; GpioClx calls the rest of the callback functions at PASSIVE\_LEVEL. A passive-level callback function that accesses a bank of registers might need to use an interrupt lock to synchronize to callback functions that run at DIRQL and that access the same registers.

For example, the passive-level [*CLIENT\_EnableInterrupt*](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_enable_interrupt) and [*CLIENT\_DisableInterrupt*](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_disable_interrupt) callback functions modify hardware settings that affect the operation of other interrupt-related callback routines that run at DIRQL. The *CLIENT\_EnableInterrupt* and *CLIENT\_DisableInterrupt* functions typically use the bank interrupt locks to synchronize their register accesses.

GpioClx automatically serializes interrupt-related and I/O-related callbacks that occur at DIRQL. GpioClx acquires the interrupt lock for the target bank before calling a callback function at DIRQL, and releases the lock after the function returns. It is an error for a callback function that is called at DIRQL to try to re-acquire the bank interrupt lock by calling **GPIO\_CLX\_AcquireInterruptLock**.

Similarly, GpioClx automatically serializes callbacks that occur at PASSIVE\_LEVEL. GpioClx internally implements a wait lock per bank. GpioClx acquires the wait lock for the target bank before calling a callback function at PASSIVE\_LEVEL, and releases the lock when the function returns. For a memory-mapped GPIO controller, GpioClx manages the bank wait locks on behalf of the driver but does not enable the driver to explicitly acquire and release the locks.

However, for a non-memory-mapped GPIO controller, **GPIO\_CLX\_AcquireInterruptLock** and **GPIO\_CLX\_ReleaseInterruptLock** acquire and release a wait lock instead of an interrupt lock. GpioClx implements a separate wait lock for each bank of pins in the GPIO controller. Because the registers are not memory-mapped, all interrupt-related and I/O-related callback functions are called at PASSIVE\_LEVEL so that they can use I/O requests to access the registers through a serial bus, such as I²C. GpioClx acquires the wait lock for the target bank before calling one of these callback functions, and releases the lock after the function returns.

It is an error for a callback function for a non-memory-mapped controller to try to re-acquire the bank wait lock by calling **GPIO\_CLX\_AcquireInterruptLock**. However, passive-level driver code outside of the callback functions can call the **GPIO\_CLX\_*Xxx*InterruptLock** methods to synchronize to the callback functions. Because GpioClx calls all interrupt-related and I/O-related callback functions at PASSIVE\_LEVEL, the bank wait locks effectively take the place of the bank interrupt locks for non-memory-mapped controllers.

Another option for a non-memory-mapped controller is for the controller driver to implement a set of wait locks. These wait locks might enable the callback routines to do more fine-grained locking and unlocking of shared resources than is possible with the wait locks implemented by GpioClx.

During the call to the [*CLIENT\_QueryControllerBasicInformation*](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_query_controller_basic_information) callback routine, a GPIO controller driver reports to GpioClx whether the controller registers are memory-mapped. For more information, see the description of the **MemoryMappedController** flag in [**CLIENT\_CONTROLLER\_BASIC\_INFORMATION**](/windows-hardware/drivers/ddi/gpioclx/ns-gpioclx-_client_controller_basic_information).

For more information about interrupt locks and wait locks, see [Using Framework Locks](../wdf/using-framework-locks.md).

The following tables provide more detailed information about which callback functions are called at DIRQL instead of at PASSIVE\_LEVEL if the registers are memory-mapped. The notes that follow the tables explain when passive-level callback functions should use interrupt locks.

-   [Interrupt-related callback functions](#interrupt-related-callback-functions)
-   [I/O-related callback functions](#io-related-callback-functions)
-   [GPIO initialization and setup-related callback functions](#gpio-initialization-and-setup-related-callback-functions)
-   [GPIO power management-related callback functions](#gpio-power-management-related-callback-functions)
-   [Other callback functions](#other-callback-functions)

## Interrupt-related callback functions


To support GPIO pins that are configured as interrupt inputs, a GPIO controller driver implements a set of event callback functions to manage interrupt requests through these pins. In the following table, the middle column indicates the IRQL at which the functions are called if the hardware registers of the GPIO controller are memory-mapped. The rightmost column indicates the IRQL at which the functions are called if the registers are not memory-mapped and must be accessed through a serial bus.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Callback function</th>
<th>IRQL if memory-mapped (MemoryMappedController = 1)</th>
<th>IRQL if serially accessed (MemoryMappedController = 0)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_enable_interrupt" data-raw-source="[&lt;em&gt;CLIENT_EnableInterrupt&lt;/em&gt;](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_enable_interrupt)"><em>CLIENT_EnableInterrupt</em></a></p>
<p><a href="/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_disable_interrupt" data-raw-source="[&lt;em&gt;CLIENT_DisableInterrupt&lt;/em&gt;](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_disable_interrupt)"><em>CLIENT_DisableInterrupt</em></a></p></td>
<td><p>PASSIVE_LEVEL</p>
<p>(See note 1.)</p></td>
<td><p>PASSIVE_LEVEL</p>
<p>(See note 2.)</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_clear_active_interrupts" data-raw-source="[&lt;em&gt;CLIENT_ClearActiveInterrupts&lt;/em&gt;](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_clear_active_interrupts)"><em>CLIENT_ClearActiveInterrupts</em></a></p>
<p><a href="/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_mask_interrupts" data-raw-source="[&lt;em&gt;CLIENT_MaskInterrupts&lt;/em&gt;](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_mask_interrupts)"><em>CLIENT_MaskInterrupts</em></a></p>
<p><a href="/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_query_active_interrupts" data-raw-source="[&lt;em&gt;CLIENT_QueryActiveInterrupts&lt;/em&gt;](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_query_active_interrupts)"><em>CLIENT_QueryActiveInterrupts</em></a></p>
<p><a href="/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_query_enabled_interrupts" data-raw-source="[&lt;em&gt;CLIENT_QueryEnabledInterrupts&lt;/em&gt;](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_query_enabled_interrupts)"><em>CLIENT_QueryEnabledInterrupts</em></a></p>
<p><a href="/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_reconfigure_interrupt" data-raw-source="[&lt;em&gt;CLIENT_ReconfigureInterrupt&lt;/em&gt;](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_reconfigure_interrupt)"><em>CLIENT_ReconfigureInterrupt</em></a></p>
<p><a href="/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_unmask_interrupt" data-raw-source="[&lt;em&gt;CLIENT_UnmaskInterrupt&lt;/em&gt;](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_unmask_interrupt)"><em>CLIENT_UnmaskInterrupt</em></a></p></td>
<td><p>DIRQL</p>
<p>(See note 3.)</p></td>
<td><p>PASSIVE_LEVEL</p>
<p>(See note 4.)</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_pre_process_controller_interrupt" data-raw-source="[&lt;em&gt;CLIENT_PreProcessControllerInterrupt&lt;/em&gt;](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_pre_process_controller_interrupt)"><em>CLIENT_PreProcessControllerInterrupt</em></a></p></td>
<td><p>DIRQL</p>
<p>(See note 5.)</p></td>
<td><p>DIRQL</p>
<p>(See note 6.)</p></td>
</tr>
</tbody>
</table>

 

**Notes**

1.  GpioClx does not acquire the bank interrupt lock before calling this callback function. The callback function can acquire the bank interrupt lock, if necessary, to synchronize accesses of registers that are shared with callback functions that run at DIRQL.

2.  GpioClx serializes the call to this callback function with other interrupt-related and I/O-related callback functions that are called at PASSIVE\_LEVEL. Thus, the callback function should not try to acquire the bank wait lock.

3.  GpioClx acquires the bank interrupt lock before calling this callback function, and releases the lock after the function returns. Thus, the callback function should not try to acquire the bank interrupt lock.

4.  GpioClx serializes the call to this callback function with other interrupt-related and I/O-related callback functions that are called at PASSIVE\_LEVEL. Thus, the callback function should not try to acquire the bank wait lock.

5.  GpioClx acquires the bank interrupt lock before calling this callback function, and releases the lock after the function returns. Thus, the callback function should not try to acquire the bank interrupt lock.

6.  GpioClx does not acquire the bank interrupt lock before calling this callback function. The GPIO controller driver is responsible for providing any synchronization that might be required.

## I/O-related callback functions


To support GPIO pins that are configured as data I/O pins, a GPIO controller driver implements a set of event callback functions to manage I/O operations through these pins. In the following table, the middle column indicates the IRQL at which the functions are called if the hardware registers of the GPIO controller are memory-mapped. The rightmost column indicates the IRQL at which the functions are called if the registers are not memory-mapped and must be accessed through a serial bus.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Callback function</th>
<th>IRQL if memory-mapped (MemoryMappedController = 1)</th>
<th>IRQL if serially accessed (MemoryMappedController = 0)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_connect_io_pins" data-raw-source="[&lt;em&gt;CLIENT_ConnectIoPins&lt;/em&gt;](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_connect_io_pins)"><em>CLIENT_ConnectIoPins</em></a></p>
<p><a href="/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_disconnect_io_pins" data-raw-source="[&lt;em&gt;CLIENT_DisconnectIoPins&lt;/em&gt;](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_disconnect_io_pins)"><em>CLIENT_DisconnectIoPins</em></a></p></td>
<td><p>PASSIVE_LEVEL</p>
<p>(See note 1.)</p></td>
<td><p>PASSIVE_LEVEL</p>
<p>(See note 2.)</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_read_pins" data-raw-source="[&lt;em&gt;CLIENT_ReadGpioPins&lt;/em&gt;](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_read_pins)"><em>CLIENT_ReadGpioPins</em></a></p>
<p><a href="/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_read_pins_mask" data-raw-source="[&lt;em&gt;CLIENT_ReadGpioPinsUsingMask&lt;/em&gt;](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_read_pins_mask)"><em>CLIENT_ReadGpioPinsUsingMask</em></a></p>
<p><a href="/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_write_pins" data-raw-source="[&lt;em&gt;CLIENT_WriteGpioPins&lt;/em&gt;](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_write_pins)"><em>CLIENT_WriteGpioPins</em></a></p>
<p><a href="/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_write_pins_mask" data-raw-source="[&lt;em&gt;CLIENT_WriteGpioPinsUsingMask&lt;/em&gt;](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_write_pins_mask)"><em>CLIENT_WriteGpioPinsUsingMask</em></a></p></td>
<td><p>DIRQL</p>
<p>(See note 3.)</p></td>
<td><p>PASSIVE_LEVEL</p>
<p>(See note 4.)</p></td>
</tr>
</tbody>
</table>

 

**Notes**

1.  GpioClx does not acquire the bank interrupt lock before calling this callback function. The callback function can acquire the interrupt lock, if necessary, to synchronize accesses of registers that are shared with callback functions that run at DIRQL.

2.  GpioClx serializes the call to this callback function with other interrupt-related and I/O-related callback functions that are called at PASSIVE\_LEVEL. Thus, the callback function should not try to acquire the bank wait lock.

3.  GpioClx acquires the bank interrupt lock before calling this callback function, and releases the lock after the function returns. Thus, the callback function should not try to acquire the bank interrupt lock.

4.  GpioClx serializes the call to this callback function with other interrupt-related and I/O-related callback functions that are called at PASSIVE\_LEVEL. Thus, the callback function should not try to acquire the bank wait lock.

## GPIO initialization and setup-related callback functions


To set up a GPIO controller to perform I/O and interrupt operations, a GPIO controller driver implements a set of event callback functions to initialize the controller. In the following table, the middle column indicates the IRQL at which the functions are called if the hardware registers of the GPIO controller are memory-mapped. The rightmost column indicates the IRQL at which the functions are called if the registers are not memory-mapped and must be accessed through a serial bus.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Callback function</th>
<th>IRQL if memory-mapped (MemoryMappedController = 1)</th>
<th>IRQL if serially accessed (MemoryMappedController = 0)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_prepare_controller" data-raw-source="[&lt;em&gt;CLIENT_PrepareController&lt;/em&gt;](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_prepare_controller)"><em>CLIENT_PrepareController</em></a></p>
<p><a href="/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_release_controller" data-raw-source="[&lt;em&gt;CLIENT_ReleaseController&lt;/em&gt;](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_release_controller)"><em>CLIENT_ReleaseController</em></a></p>
<p><a href="/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_start_controller" data-raw-source="[&lt;em&gt;CLIENT_StartController&lt;/em&gt;](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_start_controller)"><em>CLIENT_StartController</em></a></p>
<p><a href="/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_stop_controller" data-raw-source="[&lt;em&gt;CLIENT_StopController&lt;/em&gt;](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_stop_controller)"><em>CLIENT_StopController</em></a></p>
<p><a href="/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_query_controller_basic_information" data-raw-source="[&lt;em&gt;CLIENT_QueryControllerBasicInformation&lt;/em&gt;](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_query_controller_basic_information)"><em>CLIENT_QueryControllerBasicInformation</em></a></p>
<p><a href="/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_query_set_controller_information" data-raw-source="[&lt;em&gt;CLIENT_QuerySetControllerInformation&lt;/em&gt;](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_query_set_controller_information)"><em>CLIENT_QuerySetControllerInformation</em></a></p></td>
<td><p>PASSIVE_LEVEL</p>
<p>(See note 1.)</p></td>
<td><p>PASSIVE_LEVEL</p>
<p>(See note 2.)</p></td>
</tr>
</tbody>
</table>

 

**Notes**

1.  When GpioClx calls any of these callback functions, bank interrupt locks are not available. Thus, these callback functions should not try to acquire the bank interrupt lock.

2.  The GpioClx bank wait locks are not available when these callback functions are called. Thus, the driver should not try to acquire a bank wait lock to synchronize to these callback functions.

## GPIO power management-related callback functions


To enable a GPIO controller to change device power states, a GPIO controller driver implements a set of event callback functions to save and restore the hardware settings during these changes. In the following table, the middle column indicates the IRQL at which the functions are called if the hardware registers of the GPIO controller are memory-mapped. The rightmost column indicates the IRQL at which the functions are called if the registers are not memory-mapped and must be accessed through a serial bus.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Callback function</th>
<th>IRQL if memory-mapped (MemoryMappedController = 1)</th>
<th>IRQL if serially accessed (MemoryMappedController = 0)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_restore_bank_hardware_context" data-raw-source="[&lt;em&gt;CLIENT_RestoreBankHardwareContext&lt;/em&gt;](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_restore_bank_hardware_context)"><em>CLIENT_RestoreBankHardwareContext</em></a></p>
<p><a href="/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_save_bank_hardware_context" data-raw-source="[&lt;em&gt;CLIENT_SaveBankHardwareContext&lt;/em&gt;](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_save_bank_hardware_context)"><em>CLIENT_SaveBankHardwareContext</em></a></p></td>
<td><p>DIRQL or HIGH_LEVEL</p>
<p>(See Notes.)</p></td>
<td><p>Not supported.</p></td>
</tr>
</tbody>
</table>

 

**Notes**

-   For regular F-state transitions: The save/restore callback functions are called with the bank interrupt lock held by GpioClx at DIRQL. Thus, neither callback function should try to acquire the bank interrupt lock.

<!-- -->

-   For critical F-state transitions: The save/restore callbacks are called when the power engine plug-in (PEP) is invoked to save and restore the GPIO state. The save/restore callback functions are called at HIGH\_LEVEL in the context of the last processor to go idle, which occurs late in the platform deep-idle transition sequence. Thus, neither callback function should try to acquire the bank interrupt lock.

For more information about F-states, see [Component-Level Power Management](../kernel/component-level-power-management.md). For more information about the PEP, see [**PoFxPowerControl**](/windows-hardware/drivers/ddi/wdm/nf-wdm-pofxpowercontrol).

## Other callback functions


To enable a GPIO controller to support controller-specific operations, a GPIO controller driver implements a [*CLIENT\_ControllerSpecificFunction*](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_controller_specific_function) event callback function. In the following table, the middle column indicates the IRQL at which the function is called if the hardware registers of the GPIO controller are memory-mapped. The rightmost column indicates the IRQL at which the function is called if the registers are not memory-mapped and must be accessed through a serial bus.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Callback function</th>
<th>IRQL if memory-mapped (MemoryMappedController = 1)</th>
<th>IRQL if serially accessed (MemoryMappedController = 0)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_controller_specific_function" data-raw-source="[&lt;em&gt;CLIENT_ControllerSpecificFunction&lt;/em&gt;](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_controller_specific_function)"><em>CLIENT_ControllerSpecificFunction</em></a></p></td>
<td><p>PASSIVE_LEVEL</p>
<p>(See note 1.)</p></td>
<td><p>PASSIVE_LEVEL</p>
<p>(See note 2.)</p></td>
</tr>
</tbody>
</table>

 

**Notes**

1.  GpioClx does not acquire the bank interrupt lock before calling this callback function. The callback function can acquire the bank interrupt lock, if necessary, to synchronize accesses of registers that are shared with callback functions that run at DIRQL.

2.  GpioClx serializes the call to this callback function with other interrupt-related and I/O-related callback functions that are called at PASSIVE\_LEVEL. Thus, the callback function should not try to acquire the bank wait lock.

