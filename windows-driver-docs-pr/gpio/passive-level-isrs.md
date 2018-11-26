---
title: Passive-Level ISRs
description: Starting with Windows 8, kernel-mode driver framework (KMDF) and user-mode driver framework (UMDF) drivers can, as an option, register their interrupt service routines (ISRs) to run at passive level.
ms.assetid: E7556046-D85C-4CD1-8C27-578BF5CAFF2B
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Passive-Level ISRs


Starting with Windows 8, kernel-mode driver framework (KMDF) and user-mode driver framework (UMDF) drivers can, as an option, register their interrupt service routines (ISRs) to run at passive level.

For more information about passive-level ISRs for KMDF and UMDF drivers, see the following topics:

-   [Supporting Passive-Level Interrupts](https://msdn.microsoft.com/library/windows/hardware/hh451035)
-   [Accessing Hardware and Handling Interrupts](https://msdn.microsoft.com/library/windows/hardware/hh439560)

If a peripheral device uses a general-purpose I/O (GPIO) pin to relay an interrupt request to the processor, the Windows interrupt abstraction conveniently enables the driver for this device to ignore the hardware-specific details of the GPIO controller to which this pin belongs. When the kernel trap handler runs in response to a GPIO-relayed interrupt request from the device, this handler automatically clears or masks, as required, the interrupt in the GPIO hardware registers. Additionally, the kernel trap handler either directly calls the device's ISR, or schedules this ISR to run in another thread.

Frequently, GPIO hardware registers are memory-mapped, in which case the kernel trap handler can directly access them at DIRQL. However, the hardware registers of the peripheral device might not be memory-mapped, in which case, the peripheral device driver must use I/O requests to access them. If so, the ISR for the peripheral device driver must run at IRQL = PASSIVE\_LEVEL so that it can use I/O requests to silence the interrupt or to perform the initial servicing of the interrupt. A passive-level ISR can send an I/O request synchronously and, if necessary, block until the request is completed.

To support a passive-level ISR for a peripheral device that generates an edge-triggered interrupt request signal, the kernel trap handler clears the pending interrupt at the GPIO pin, and then schedules the ISR to run in a passive-level kernel thread.

To support a passive-level ISR for a peripheral device that generates a level-triggered interrupt request signal, the kernel trap handler masks the pending interrupt at the GPIO pin, and then schedules the ISR to run in a passive-level kernel thread. The ISR is responsible for clearing the interrupt request in the peripheral device. After the ISR returns, the kernel thread unmasks the interrupt at the GPIO pin.

Because the interrupt remains masked until the ISR returns, the device's passive-level ISR should perform only the initial servicing of the interrupt, and then return to avoid delaying passive-level ISRs for other devices. Typically, the driver should defer additional interrupt-related processing to the interrupt worker thread, which runs at a lower priority than the ISR.

 

 




