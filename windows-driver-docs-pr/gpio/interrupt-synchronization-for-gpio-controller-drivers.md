---
title: Interrupt Synchronization for GPIO Controller Drivers
author: windows-driver-content
description: GPIO controller drivers can call the GPIO\_CLX\_AcquireInterruptLock and GPIO\_CLX\_ReleaseInterruptLock methods to acquire and release interrupt locks that are implemented internally by the GPIO framework extension (GpioClx).
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: D9698A50-7CC2-463C-9E46-7FE428F3193E
---

# Interrupt Synchronization for GPIO Controller Drivers


GPIO controller drivers can call the [**GPIO\_CLX\_AcquireInterruptLock**](https://msdn.microsoft.com/library/windows/hardware/hh439482) and [**GPIO\_CLX\_ReleaseInterruptLock**](https://msdn.microsoft.com/library/windows/hardware/hh439494) methods to acquire and release interrupt locks that are implemented internally by the GPIO framework extension (GpioClx). Driver code that runs at IRQL = PASSIVE\_LEVEL can call these methods to synchronize to the interrupt service routine (ISR) in GpioClx. GpioClx dedicates a separate interrupt lock to each bank of pins in the GPIO controller.

If the hardware registers of the GPIO controller are memory-mapped, the ISR in GpioClx calls certain driver-implemented event callback functions at DIRQL; GpioClx calls the rest of the callback functions at PASSIVE\_LEVEL. A passive-level callback function that accesses a bank of registers might need to use an interrupt lock to synchronize to callback functions that run at DIRQL and that access the same registers.

For example, the passive-level [*CLIENT\_EnableInterrupt*](https://msdn.microsoft.com/library/windows/hardware/hh439377) and [*CLIENT\_DisableInterrupt*](https://msdn.microsoft.com/library/windows/hardware/hh439371) callback functions modify hardware settings that affect the operation of other interrupt-related callback routines that run at DIRQL. The *CLIENT\_EnableInterrupt* and *CLIENT\_DisableInterrupt* functions typically use the bank interrupt locks to synchronize their register accesses.

GpioClx automatically serializes interrupt-related and I/O-related callbacks that occur at DIRQL. GpioClx acquires the interrupt lock for the target bank before calling a callback function at DIRQL, and releases the lock after the function returns. It is an error for a callback function that is called at DIRQL to try to re-acquire the bank interrupt lock by calling **GPIO\_CLX\_AcquireInterruptLock**.

Similarly, GpioClx automatically serializes callbacks that occur at PASSIVE\_LEVEL. GpioClx internally implements a wait lock per bank. GpioClx acquires the wait lock for the target bank before calling a callback function at PASSIVE\_LEVEL, and releases the lock when the function returns. For a memory-mapped GPIO controller, GpioClx manages the bank wait locks on behalf of the driver but does not enable the driver to explicitly acquire and release the locks.

However, for a non-memory-mapped GPIO controller, **GPIO\_CLX\_AcquireInterruptLock** and **GPIO\_CLX\_ReleaseInterruptLock** acquire and release a wait lock instead of an interrupt lock. GpioClx implements a separate wait lock for each bank of pins in the GPIO controller. Because the registers are not memory-mapped, all interrupt-related and I/O-related callback functions are called at PASSIVE\_LEVEL so that they can use I/O requests to access the registers through a serial bus, such as I²C. GpioClx acquires the wait lock for the target bank before calling one of these callback functions, and releases the lock after the function returns.

It is an error for a callback function for a non-memory-mapped controller to try to re-acquire the bank wait lock by calling **GPIO\_CLX\_AcquireInterruptLock**. However, passive-level driver code outside of the callback functions can call the **GPIO\_CLX\_*Xxx*InterruptLock** methods to synchronize to the callback functions. Because GpioClx calls all interrupt-related and I/O-related callback functions at PASSIVE\_LEVEL, the bank wait locks effectively take the place of the bank interrupt locks for non-memory-mapped controllers.

Another option for a non-memory-mapped controller is for the controller driver to implement a set of wait locks. These wait locks might enable the callback routines to do more fine-grained locking and unlocking of shared resources than is possible with the wait locks implemented by GpioClx.

During the call to the [*CLIENT\_QueryControllerBasicInformation*](https://msdn.microsoft.com/library/windows/hardware/hh439399) callback routine, a GPIO controller driver reports to GpioClx whether the controller registers are memory-mapped. For more information, see the description of the **MemoryMappedController** flag in [**CLIENT\_CONTROLLER\_BASIC\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/hh439358).

For more information about interrupt locks and wait locks, see [Using Framework Locks](https://msdn.microsoft.com/library/windows/hardware/ff545446).

The following tables provide more detailed information about which callback functions are called at DIRQL instead of at PASSIVE\_LEVEL if the registers are memory-mapped. The notes that follow the tables explain when passive-level callback functions should use interrupt locks.

-   [Interrupt-related callback functions](#interrupt-related-callback-functions)
-   [I/O-related callback functions](#i-o-related-callback-functions)
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
<td><p>[<em>CLIENT_EnableInterrupt</em>](https://msdn.microsoft.com/library/windows/hardware/hh439377)</p>
<p>[<em>CLIENT_DisableInterrupt</em>](https://msdn.microsoft.com/library/windows/hardware/hh439371)</p></td>
<td><p>PASSIVE_LEVEL</p>
<p>(See note 1.)</p></td>
<td><p>PASSIVE_LEVEL</p>
<p>(See note 2.)</p></td>
</tr>
<tr class="even">
<td><p>[<em>CLIENT_ClearActiveInterrupts</em>](https://msdn.microsoft.com/library/windows/hardware/hh439341)</p>
<p>[<em>CLIENT_MaskInterrupts</em>](https://msdn.microsoft.com/library/windows/hardware/hh439380)</p>
<p>[<em>CLIENT_QueryActiveInterrupts</em>](https://msdn.microsoft.com/library/windows/hardware/hh439395)</p>
<p>[<em>CLIENT_QueryEnabledInterrupts</em>](https://msdn.microsoft.com/library/windows/hardware/dn265184)</p>
<p>[<em>CLIENT_ReconfigureInterrupt</em>](https://msdn.microsoft.com/library/windows/hardware/hh698243)</p>
<p>[<em>CLIENT_UnmaskInterrupt</em>](https://msdn.microsoft.com/library/windows/hardware/hh439435)</p></td>
<td><p>DIRQL</p>
<p>(See note 3.)</p></td>
<td><p>PASSIVE_LEVEL</p>
<p>(See note 4.)</p></td>
</tr>
<tr class="odd">
<td><p>[<em>CLIENT_PreProcessControllerInterrupt</em>](https://msdn.microsoft.com/library/windows/hardware/hh439392)</p></td>
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
<td><p>[<em>CLIENT_ConnectIoPins</em>](https://msdn.microsoft.com/library/windows/hardware/hh439347)</p>
<p>[<em>CLIENT_DisconnectIoPins</em>](https://msdn.microsoft.com/library/windows/hardware/hh439374)</p></td>
<td><p>PASSIVE_LEVEL</p>
<p>(See note 1.)</p></td>
<td><p>PASSIVE_LEVEL</p>
<p>(See note 2.)</p></td>
</tr>
<tr class="even">
<td><p>[<em>CLIENT_ReadGpioPins</em>](https://msdn.microsoft.com/library/windows/hardware/hh439404)</p>
<p>[<em>CLIENT_ReadGpioPinsUsingMask</em>](https://msdn.microsoft.com/library/windows/hardware/hh439406)</p>
<p>[<em>CLIENT_WriteGpioPins</em>](https://msdn.microsoft.com/library/windows/hardware/hh439439)</p>
<p>[<em>CLIENT_WriteGpioPinsUsingMask</em>](https://msdn.microsoft.com/library/windows/hardware/hh439445)</p></td>
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
<td><p>[<em>CLIENT_PrepareController</em>](https://msdn.microsoft.com/library/windows/hardware/hh439389)</p>
<p>[<em>CLIENT_ReleaseController</em>](https://msdn.microsoft.com/library/windows/hardware/hh439411)</p>
<p>[<em>CLIENT_StartController</em>](https://msdn.microsoft.com/library/windows/hardware/hh439424)</p>
<p>[<em>CLIENT_StopController</em>](https://msdn.microsoft.com/library/windows/hardware/hh439430)</p>
<p>[<em>CLIENT_QueryControllerBasicInformation</em>](https://msdn.microsoft.com/library/windows/hardware/hh439399)</p>
<p>[<em>CLIENT_QuerySetControllerInformation</em>](https://msdn.microsoft.com/library/windows/hardware/hh698241)</p></td>
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
<td><p>[<em>CLIENT_RestoreBankHardwareContext</em>](https://msdn.microsoft.com/library/windows/hardware/hh439414)</p>
<p>[<em>CLIENT_SaveBankHardwareContext</em>](https://msdn.microsoft.com/library/windows/hardware/hh439419)</p></td>
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

For more information about F-states, see [Component-Level Power Management](https://msdn.microsoft.com/library/windows/hardware/hh450935). For more information about the PEP, see [**PoFxPowerControl**](https://msdn.microsoft.com/library/windows/hardware/hh439518).

## Other callback functions


To enable a GPIO controller to support controller-specific operations, a GPIO controller driver implements a [*CLIENT\_ControllerSpecificFunction*](https://msdn.microsoft.com/library/windows/hardware/hh698237) event callback function. In the following table, the middle column indicates the IRQL at which the function is called if the hardware registers of the GPIO controller are memory-mapped. The rightmost column indicates the IRQL at which the function is called if the registers are not memory-mapped and must be accessed through a serial bus.

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
<td><p>[<em>CLIENT_ControllerSpecificFunction</em>](https://msdn.microsoft.com/library/windows/hardware/hh698237)</p></td>
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bgpio\parports%5D:%20Interrupt%20Synchronization%20for%20GPIO%20Controller%20Drivers%20%20RELEASE:%20%286/3/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


