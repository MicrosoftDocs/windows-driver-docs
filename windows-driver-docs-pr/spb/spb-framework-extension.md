---
Description: 'Starting with Windows 8, the SPB framework extension (SpbCx) is a system-supplied extension to the Kernel-Mode Driver Framework (KMDF).'
MS-HAID: 'SPB.spb\_framework\_extension'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
title: 'SPB Framework Extension (SpbCx)'
---

# SPB Framework Extension (SpbCx)


Starting with Windows 8, the SPB framework extension (SpbCx) is a system-supplied extension to the [Kernel-Mode Driver Framework](kmdf.kernel_mode_driver_framework_overview) (KMDF). SpbCx works together with an [SPB controller driver](buses.spb_controller_driver_overview) to perform I/O operations on peripheral devices that are connected to a [simple peripheral bus](buses.simple_peripheral_buses) (SPB), such as I²C or SPI.

The SPB controller driver performs all hardware-specific operations. These operations include accessing the hardware registers of the SPB controller to configure the controller and to initiate bus transfers to and from SPB-connected peripheral devices.

SpbCx performs processing tasks that are common to SPB controller devices. In particular, SpbCx manages the I/O request queues for an SPB controller. These queues contain I/O requests for peripheral devices that are attached to the bus. The hardware vendor for the SPB controller supplies an SPB controller driver to perform all hardware-specific operations that are required to handle these requests.

The division of responsibilities between SpbCx and the SPB controller driver is as follows:

-   SpbCx manages the generic functions that are common to all members of the SPB controller device class. SpbCx provides much of the default request handling and flow control for the controller driver. Starting with Windows 8, SpbCx is an inbox component of the Windows operating system.

-   The SPB controller driver manages the hardware-specific functions in the SPB controller device. Hardware vendors supply controller drivers for their SPB controller devices.

SpbCx and the SPB controller driver run in kernel mode. SpbCx is a framework extension, and the SPB controller driver is a KMDF driver. The SPB controller driver calls the methods in the SpbCx device-driver interface (DDI) to perform SPB-specific operations, and calls KMDF methods to perform other, more generic driver functions. For information about building a KMDF driver, see [Building and Loading a Framework-Based Driver](kmdf.building_and_loading_a_framework_based_driver).

SPB controller drivers statically link to the DDI entry points in the SpbCx stub library, Spbcx.lib. At run time, this library performs the necessary driver-version negotiation to dynamically link to the framework extension module, Spbcx.sys, which implements the DDI. An SPB controller driver that requires a particular version of Spbcx.sys can safely link to a version of Spbcx.sys that has a higher version number. However, this driver cannot link to a version of Spbcx.sys that has a lower version number. The SpbCx I/O request interface is similarly backward compatible.

Although a hardware vendor has the option of writing a monolithic SPB controller driver that does not use SpbCx, a significant effort is required to do so. By comparison, a controller driver that uses SpbCx is easier to develop and is typically more reliable.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5BSPB\buses%5D:%20SPB%20Framework%20Extension%20%28SpbCx%29%20%20RELEASE:%20%286/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



