---
Description: SD Card Driver Stack
MS-HAID:
- 'securedigital\_dg\_d9c564f2-63e2-4429-ad4d-3f28f97baba7.xml'
- 'SD.sd\_card\_driver\_stack'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
title: SD Card Driver Stack
---

# SD Card Driver Stack


Secure Digital (SD) card technology began with portable, miniature memory cards, but with the release of the Secure Digital I/O (SDIO) specification, the Secure Digital Association (SDA) has broadened the definition of SD technology to include a large variety of card functions, such as Bluetooth devices, video cameras, Wireless LAN devices, and Global Positioning System (GPS) receivers. This document explains how the operating system supports the card function extensions to SD technology.

Card readers for many early SD storage devices were designed to connect to the USB bus. Windows manages these devices with the USB mass storage driver (*usbstor.sys*) and the native storage class driver (*disk.sys*), as depicted in the following diagram:

![diagram illustrating a device stack for an early sd storage device](images/sdio-usb.png)

For a more complete description of the device stack that Windows creates for a memory card that connects to the USB bus, see [Device Object Example for a USB Mass Storage Device](storage.device_object_example_for_a_usb_mass_storage_device).

The operating system provides support for SD host controllers that connect directly to the PCI bus. When the system enumerates an SD host controller, it loads a native SD bus driver (*sdbus.sys*). If a user inserts an SD memory card, Windows loads a native SD storage class driver (*sffdisk.sys*) and storage miniport driver (*sffp\_sd.sys*) on top of the bus driver. If a user inserts an SD card with a different kind of function, such as GPS or wireless LAN, Windows loads a vendor-supplied driver for the device.

All device drivers in the SD stack, whether native or vendor-supplied, must communicate with the SD bus driver by calling routines in the static SD bus library (*sdbus.lib*). SD drivers must link to this library when they compile. The following diagram depicts the SD driver stack that the system creates when it enumerates an SD controller and accompanying cards:

![diagram illustrating the relationship between the sd software and hardware components](images/sdiostack.png)

SD device drivers cannot directly access the host-controller register set, nor can they embed pass-through commands for the host controller in I/O request packets (IRPs). SD device drivers issue commands to the host controller by calling the SD bus library routines, and then the library generates the appropriate SD commands for the host controller.

SD device drivers must handle standard PnP and power IRPs, but they do not request or manage hardware resources, such as ports, memory, or interrupt vectors. Consequently, SD device drivers are not required to map any hardware resources when handling an [**IRP\_MN\_START\_DEVICE**](kernel.irp_mn_start_device) request. However, when an SD device driver receives an [**IRP\_MN\_STOP\_DEVICE**](kernel.irp_mn_stop_device) request, it must stop all I/O operations. Furthermore, the driver must close its interface to the SD bus driver in response to an [**IRP\_MN\_QUERY\_REMOVE\_DEVICE**](kernel.irp_mn_query_remove_device) request.

When a hardware interrupt occurs, the SD bus library intercepts the interrupt, masks out further interrupts, and notifies the SD device driver by means of a callback routine that a hardware interrupt has occurred. For a description of the callback routine that the bus driver uses to notify an SD device driver of hardware interrupts, see [**PSDBUS\_CALLBACK\_ROUTINE**](buses.psdbus_callback_routine). For a general explanation of how the SD driver stack and libraries manage hardware interrupts, see [Handling Secure Digital (SD) Hardware Interrupts](buses.handling_sd_card_interrupts).

The *ntddsd.h* header file, which is provided in the Windows Driver Kit (WDK), declares the prototypes for the routines exposed by the SD bus library.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5BSD\buses%5D:%20SD%20Card%20Driver%20Stack%20%20RELEASE:%20%285/27/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



