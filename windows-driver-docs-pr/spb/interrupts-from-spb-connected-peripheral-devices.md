---
title: Interrupts from SPB-Connected Peripheral Devices
description: Unlike a bus such as PCI, a simple peripheral bus (SPB), such as I²C or SPI, provides no standardized, bus-specific means to convey interrupt requests from peripheral devices to the processor.
ms.date: 04/20/2017
---

# Interrupts from SPB-Connected Peripheral Devices


Unlike a bus such as PCI, a [simple peripheral bus](/previous-versions/hh450903(v=vs.85)) (SPB), such as I²C or SPI, provides no standardized, bus-specific means to convey interrupt requests from peripheral devices to the processor. Instead, an SPB-connected peripheral device signals an interrupt through a separate hardware path that lies outside of both the SPB and the SPB controller. The details of this interrupt path tend to vary from one hardware platform to the next, but Windows hides these details from the driver for an SPB-connected peripheral device to enable the driver to work across a variety of hardware platforms.




Typically, the interrupt request line from an SPB-connected peripheral device is connected to a pin on a general-purpose I/O (GPIO) controller, and the GPIO controller relays interrupts from the device to the processor. For more information, see [GPIO Interrupts](../gpio/gpio-interrupts.md).

The peripheral device driver acquires this GPIO interrupt as an abstract Windows interrupt resource (**CmResourceTypeInterrupt**) and connects the interrupt to the driver's interrupt service routine (ISR). The interrupt resource abstraction hides the platform-specific details of the interrupt from the driver. For example, the driver can ignore details such as whether the interrupt is received from a GPIO pin or from some other source. To maintain this abstraction, the kernel's interrupt trap handler, which runs at DIRQL, might need to silence an active interrupt request by clearing or temporarily masking the interrupt at the GPIO pin. The hardware registers of the GPIO controller typically are memory-mapped and can be accessed at DIRQL.

In contrast, an SPB-connected peripheral device is not memory-mapped, and the ISR for this device must typically run at IRQL = PASSIVE\_LEVEL. To access the hardware registers in the device, the ISR sends I/O requests to perform serial transfers over the SPB. Such transfers are relatively slow and cannot be performed in an ISR that runs at DIRQL. However, a passive-level ISR can send an I/O request synchronously and then block until the request completes.

For an edge-triggered interrupt, the kernel's trap handler automatically clears the interrupt request at the GPIO pin, and then schedules the device's ISR to run at passive level. The trap handler must clear the interrupt to prevent the same interrupt from occurring again after the trap handler returns.

For a level-triggered interrupt, the kernel's interrupt trap handler automatically masks the interrupt request at the GPIO pin, and then schedules the device's ISR to run at passive level. The ISR must clear the interrupt request from the device. After the ISR returns, the kernel unmasks the interrupt request at the GPIO pin.

The device's passive-level ISR should perform only the initial servicing of the interrupt, and then return to avoid delaying passive-level ISRs for other devices. Typically, the driver should defer additional interrupt-related processing to the interrupt worker thread, which runs at a lower priority than the ISR.

Starting with Windows 8, the [User-Mode Driver Framework](../wdf/overview-of-the-umdf.md) (UMDF) supports ISRs for UMDF drivers. The UMDF driver for an SPB peripheral device calls the [**IWDFDevice3::CreateInterrupt**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdevice3-createinterrupt) method to connect an ISR to the interrupt from the device. When the device signals an interrupt request, the kernel's trap handler schedules the ISR to run at passive level. For more information, see [Accessing Hardware and Handling Interrupts](../wdf/accessing-hardware-and-handling-interrupts.md).

Starting with Windows 8, the [Kernel-Mode Driver Framework](../wdf/index.md) (KMDF) supports passive-level ISRs. The KMDF driver for an SPB peripheral device calls the [**WdfInterruptCreate**](/windows-hardware/drivers/ddi/wdfinterrupt/nf-wdfinterrupt-wdfinterruptcreate) method to connect a passive-level ISR to the interrupt from the device. One of the input parameters to this method is a pointer to a [**WDF\_INTERRUPT\_CONFIG**](/windows-hardware/drivers/ddi/wdfinterrupt/ns-wdfinterrupt-_wdf_interrupt_config) structure that contains configuration information for the interrupt. To configure the ISR to run at passive level, set the **PassiveHandling** member of this structure to **TRUE**. For more information, see [Supporting Passive-Level Interrupts](../wdf/supporting-passive-level-interrupts.md).

 

