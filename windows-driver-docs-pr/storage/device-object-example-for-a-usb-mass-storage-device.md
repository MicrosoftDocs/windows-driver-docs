---
title: Device Object Example for a USB Mass Storage Device
author: windows-driver-content
description: Device Object Example for a USB Mass Storage Device
ms.assetid: 402b99f2-a253-4a43-9c73-d3d2fd066c23
keywords: ["storage drivers WDK , device objects", "device objects WDK storage", "USB mass storage device example WDK"]
---

# Device Object Example for a USB Mass Storage Device


## <span id="ddk_device_object_example_for_a_usb_mass_storage_device_kg"></span><span id="DDK_DEVICE_OBJECT_EXAMPLE_FOR_A_USB_MASS_STORAGE_DEVICE_KG"></span>


The following figure shows the device objects that are created for a composite USB mass storage device containing both a Smart Media slot and a Compact Flash slot.

![device objects that are created for a composite USB mass storage device containing both a Smart Media slot and a Compact Flash slot](images/usbstor.png)

Device Object Tree for a Composite USB Mass Storage Device

Starting from the bottom of the figure, the following list describes each device object or device object stack and its associated driver:

1.  The PCI bus driver enumerates the USB host controller. The system loads the port driver, *usbport.sys*, and its accompanying miniports (not shown in the figure). Then, *usbport.sys* creates an FDO for the host controller.

2.  The port driver enumerates the USB hubs in the system, starting with the root hub. The *usbhub.sys* driver manages all USB hubs. The figure only shows one level of hub device objects, but USB allows daisy-chaining of hub devices, so there could potentially be many more hub device objects in the tree. The hub driver detects and enumerates the USB mass storage device and creates a PDO for it.

3.  Windows supplies a USB storage port driver, *usbstor.sys*, that serves as an interface between the USB stack and the native Windows storage class drivers. The USB storage port driver creates its own functional device object (FDO). The USB storage port driver can divide the physical storage device into as many as 16 logical units. In the example depicted in the figure, the USB storage device contains separate slots for a Compact Flash device and a Smart Media device. Therefore, in this example, the USB storage port driver creates two separate PDOs, one for the Compact Flash device and another for the Smart Media device.

4.  The stack above the USB storage port driver is managed in the usual way by the native disk class driver. The disk class driver creates a PDO and an FDO for the disk as a whole (partition zero), and PDOs for each partition on the disk.

5.  The partition manager creates an FDO for each disk partition.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Device%20Object%20Example%20for%20a%20USB%20Mass%20Storage%20Device%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


