---
Description: 'The Windows Driver Model cleanly separates the driver components that control a peripheral device (for example, a temperature sensor) on a bus from the driver components that manage the bus controller, which transfers data and control information to and from the peripheral device.'
MS-HAID: 'SPB.spb\_device\_stacks'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
title: SPB Device Stacks
author: windows-driver-content
---

# SPB Device Stacks


The Windows Driver Model cleanly separates the driver components that control a peripheral device (for example, a temperature sensor) on a bus from the driver components that manage the bus controller, which transfers data and control information to and from the peripheral device. This separation enables the hardware vendor for a peripheral device that connects to a [simple peripheral bus](buses.simple_peripheral_buses) (SPB) to write a driver that controls the device a variety of bus controllers, bus types, and hardware platforms. Similarly, the hardware vendor for an SPB controller can write a driver for this controller that can enable connections to a variety of peripheral devices.

In Windows, a peripheral device that is attached to a Plug and Play (PnP) bus is represented by two, and possibly more, [*device objects*](kernel.introduction_to_device_objects). The device objects for this device are organized hierarchically to form a [*device stack*](wdkgloss.d#wdkgloss-device-stack). A *functional* device object (FDO) represents the internal state of the device, and is created and owned by the function driver that controls the peripheral device's internal functions. Below the FDO in the stack is a *physical* device object (PDO) that represents the device's connection to the bus. The PDO is created and owned by the bus controller driver that detects and enumerates the device for the PnP manager. This PDO contains the information (for example, bus address) that the bus controller needs to access the device over the bus. If the function driver requires assistance from the bus controller to perform an I/O operation on the device, the function driver sends an I/O request packet (IRP) down the device stack to the PDO, and the bus controller driver receives the IRP. For more information, see [Device Objects and Device Stacks](kernel.device_objects_and_device_stacks).

In contrast, an SPB (for example, an I²C or SPI bus) does not support PnP, and the SPB controller driver does not detect and enumerate the peripheral devices on the SPB. Instead, the hardware platform's ACPI firmware describes these devices and their bus connections, and the ACPI driver, Acpi.sys, enumerates these devices for the PnP manager.

Additionally, Acpi.sys creates the PDO for a peripheral device on an SPB. To perform an I/O operation on this device, the device's function driver does not send an IRP down the stack to the PDO because the PDO is owned by Acpi.sys, which cannot perform I/O operations. Instead, the function driver must send the IRP to the SPB controller driver. The SPB controller driver owns the FDO for the SPB controller, which is not in the same device stack as the FDO for the peripheral device. To send this IRP, the device's function driver must first open a logical connection to the SPB controller and receive a WDFFILEOBJECT object handle to this connection. The driver then specifies this handle as the target for the IRPs that it sends to the device. The SPB controller driver receives these IRPs and (in conjunction with the [SPB framework extension](buses.spb_framework_extension), SpbCx) performs the requested I/O operations on the device. For more information about opening logical connections to SPB controllers, see [Connection IDs for SPB Peripheral Devices](buses.connection_ids_for_spb_connected_peripheral_devices).

Some IRPs can be handled entirely by drivers that are above the SPB controller driver in the I/O-request chain, including the function driver for the peripheral device. However, IRPs that require transfers of data or control information to and from the peripheral device over the bus must be processed by the SPB controller driver.

A filter driver that is designed to operate with the function driver for an SPB peripheral device can be inserted above the function driver's FDO. However, inserting such a filter between the FDO and PDO has no effect because it cannot intercept the IRPs that are exchanged between the function driver and the SPB controller driver.

If necessary, a filter driver can be inserted above the SPB controller driver (and SpbCx, which manages the queues for IRPs sent to the SPB controller driver). However, the [SPB I/O request interface](buses.using_the_spb_i_o_request_interface) is a top-level driver interface, and drivers in the I/O-request chain must ensure that I/O requests are delivered in the context of the calling thread so that SpbCx and the SPB controller driver can access user-mode buffers during I/O transfers.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5BSPB\buses%5D:%20SPB%20Device%20Stacks%20%20RELEASE:%20%286/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")


