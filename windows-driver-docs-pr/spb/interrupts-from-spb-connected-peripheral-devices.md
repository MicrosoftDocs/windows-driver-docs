---
Description: 'Unlike a bus such as PCI, a simple peripheral bus (SPB), such as I²C or SPI, provides no standardized, bus-specific means to convey interrupt requests from peripheral devices to the processor.'
MS-HAID: 'SPB.interrupts\_from\_spb\_connected\_peripheral\_devices'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
title: 'Interrupts from SPB-Connected Peripheral Devices'
author: windows-driver-content
---

# Interrupts from SPB-Connected Peripheral Devices


Unlike a bus such as PCI, a [simple peripheral bus](buses.simple_peripheral_buses) (SPB), such as I²C or SPI, provides no standardized, bus-specific means to convey interrupt requests from peripheral devices to the processor. Instead, an SPB-connected peripheral device signals an interrupt through a separate hardware path that lies outside of both the SPB and the SPB controller. The details of this interrupt path tend to vary from one hardware platform to the next, but Windows hides these details from the driver for an SPB-connected peripheral device to enable the driver to work across a variety of hardware platforms.

## <a href="" id="interrupts-spb-peripheral-devices"></a>


Typically, the interrupt request line from an SPB-connected peripheral device is connected to a pin on a general-purpose I/O (GPIO) controller, and the GPIO controller relays interrupts from the device to the processor. For more information, see [GPIO Interrupts](parports.gpio_interrupts).

The peripheral device driver acquires this GPIO interrupt as an abstract Windows interrupt resource (**CmResourceTypeInterrupt**) and connects the interrupt to the driver's interrupt service routine (ISR). The interrupt resource abstraction hides the platform-specific details of the interrupt from the driver. For example, the driver can ignore details such as whether the interrupt is received from a GPIO pin or from some other source. To maintain this abstraction, the kernel's interrupt trap handler, which runs at DIRQL, might need to silence an active interrupt request by clearing or temporarily masking the interrupt at the GPIO pin. The hardware registers of the GPIO controller typically are memory-mapped and can be accessed at DIRQL.

In contrast, an SPB-connected peripheral device is not memory-mapped, and the ISR for this device must typically run at IRQL = PASSIVE\_LEVEL. To access the hardware registers in the device, the ISR sends I/O requests to perform serial transfers over the SPB. Such transfers are relatively slow and cannot be performed in an ISR that runs at DIRQL. However, a passive-level ISR can send an I/O request synchronously and then block until the request completes.

For an edge-triggered interrupt, the kernel's trap handler automatically clears the interrupt request at the GPIO pin, and then schedules the device's ISR to run at passive level. The trap handler must clear the interrupt to prevent the same interrupt from occurring again after the trap handler returns.

For a level-triggered interrupt, the kernel's interrupt trap handler automatically masks the interrupt request at the GPIO pin, and then schedules the device's ISR to run at passive level. The ISR must clear the interrupt request from the device. After the ISR returns, the kernel unmasks the interrupt request at the GPIO pin.

The device's passive-level ISR should perform only the initial servicing of the interrupt, and then return to avoid delaying passive-level ISRs for other devices. Typically, the driver should defer additional interrupt-related processing to the interrupt worker thread, which runs at a lower priority than the ISR.

Starting with Windows 8, the [User-Mode Driver Framework](umdf.overview_of_the_umdf) (UMDF) supports ISRs for UMDF drivers. The UMDF driver for an SPB peripheral device calls the [**IWDFDevice3::CreateInterrupt**](umdf.iwdfdevice3_createinterrupt) method to connect an ISR to the interrupt from the device. When the device signals an interrupt request, the kernel's trap handler schedules the ISR to run at passive level. For more information, see [Accessing Hardware and Handling Interrupts](umdf.accessing_hardware_and_handling_interrupts).

Starting with Windows 8, the [Kernel-Mode Driver Framework](kmdf.kernel_mode_driver_framework_overview) (KMDF) supports passive-level ISRs. The KMDF driver for an SPB peripheral device calls the [**WdfInterruptCreate**](kmdf.wdfinterruptcreate) method to connect a passive-level ISR to the interrupt from the device. One of the input parameters to this method is a pointer to a [**WDF\_INTERRUPT\_CONFIG**](kmdf.wdf_interrupt_config) structure that contains configuration information for the interrupt. To configure the ISR to run at passive level, set the **PassiveHandling** member of this structure to **TRUE**. For more information, see [Supporting Passive-Level Interrupts](kmdf.supporting_passive_level_interrupts).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5BSPB\buses%5D:%20Interrupts%20from%20SPB-Connected%20Peripheral%20Devices%20%20RELEASE:%20%286/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")


