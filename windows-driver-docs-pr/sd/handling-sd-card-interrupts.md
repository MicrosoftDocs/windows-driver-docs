---
Description: Handling SD Card Interrupts
MS-HAID:
- 'securedigital\_dg\_1cc707f6-a555-4ee8-bc25-c49d69c67d9d.xml'
- 'SD.handling\_sd\_card\_interrupts'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
title: Handling SD Card Interrupts
---

# Handling SD Card Interrupts


Secure Digital (SD) card drivers do not have interrupt service routines (ISRs) and they do not acquire interrupt request (IRQ) resources. The SD bus driver detects and intercepts hardware interrupts, and then reports them to the device driver by means of the interrupt notification callback routine [**PSDBUS\_CALLBACK\_ROUTINE**](buses.psdbus_callback_routine), as explained in sections [Secure Digital (SD) Driver Stack](buses.sd_card_driver_stack) and [Opening and Initializing an SD Bus Interface](buses.opening__initializing_and_closing_an_sd_card_bus_interface).

The device driver does not have to complete interrupt processing in the context of the interrupt notification callback routine. The driver can return from the callback routine and complete interrupt processing in its own context. When the driver finishes processing the interrupt, it informs the bus driver by an explicit call to an interrupt acknowledgment routine supplied with the SD bus interface. For more information about the interrupt acknowledgment routine, see [**PSDBUS\_ACKNOWLEDGE\_INT\_ROUTINE**](buses.psdbus_acknowledge_int_routine). When the bus driver receives this call, it re-enables the interrupt.

SD device drivers have two options with respect to the IRQ levels (IRQLs) at which they run. An SD driver can run exclusively at PASSIVE\_LEVEL, or it can run at DISPATCH\_LEVEL while in the context of the interrupt notification callback routine and at PASSIVE\_LEVEL the rest of the time. When an SD device driver runs exclusively at PASSIVE\_LEVEL, the bus driver assumes responsibility for synchronizing interrupts. Choose this option if your device can operate without strict limits on interrupt latency because it will simplify the design of your driver. In addition to offloading the task of interrupt synchronization onto the bus driver, there are other benefits. For instance, drivers must frequently transfer data in response to an interrupt. If the driver's callback routine is running at PASSIVE\_LEVEL, it is free to do a synchronous I/O operation rather than an asynchronous one. If the callback routine runs at DISPATCH\_LEVEL, the driver must wait until it is running at a lower IRQL before doing synchronous I/O.

An SD device driver specifies the IRQL at which it will run when it initializes the SD bus interface. To run at DISPATCH\_LEVEL in the interrupt notification callback routine, the driver must set the **CallbackAtDpcLevel** member of the [**SDBUS\_INTERFACE\_PARAMETERS**](buses.sdbus_interface_parameters) structure to **TRUE** and pass this structure to the interface initialization routine. For a description of the interface routine, see [**PSDBUS\_INITIALIZE\_INTERFACE\_ROUTINE**](buses.psdbus_initialize_interface_routine). To run exclusively at PASSIVE\_LEVEL, the driver must set **CallbackAtDpcLevel** to **FALSE**.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5BSD\buses%5D:%20Handling%20SD%20Card%20Interrupts%20%20RELEASE:%20%285/27/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



