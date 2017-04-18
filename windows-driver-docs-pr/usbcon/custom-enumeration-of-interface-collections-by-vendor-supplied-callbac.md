---
Description: Some USB devices have interface collections that the USB Interface Association Descriptor (IAD) is unable to describe.
title: Customizing Enumeration of Interface Collections for Composite Devices
---

#  Customizing Enumeration of Interface Collections for Composite Devices


Some USB devices have interface collections that the USB Interface Association Descriptor (IAD) is unable to describe. In Windows Vista and later operating systems, vendors can customize the way the [USB Generic Parent Driver (Usbccgp.sys)](usb-common-class-generic-parent-driver.md) defines and enumerates a device's interface collections. This is done through an *enumeration callback routine* in a filter driver. The callback routine assists the generic parent driver in defining custom interface collections for the device.

For the generic parent driver to define custom interface collections, the vendor of the composite device must:

1.  Implement the enumeration callback routine ([**USBC\_START\_DEVICE\_CALLBACK**](https://msdn.microsoft.com/library/windows/hardware/ff539007)).
2.  Supply a pointer to the callback routine in the *USB device configuration interface* (**StartDeviceCallback** member of [**USBC\_DEVICE\_CONFIGURATION\_INTERFACE\_V1**](https://msdn.microsoft.com/library/windows/hardware/ff538990)).
3.  Provide an INF file that matches the device ID of the composite device and explicitly loads both the USB generic parent driver and the filter driver.

## Implementation Considerations


The filter driver that contains the enumeration callback routine can be either an upper or a lower filter driver. When the USB generic parent driver receives an [**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749) request to start a composite device, it queries for the USB device configuration interface by sending an [**IRP\_MN\_QUERY\_INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff551687) request to the top of the driver stack.

On receiving an [**IRP\_MN\_QUERY\_INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff551687) request, the filter driver must check the GUID type in the **InterfaceType** member of the request to verify that the interface that is requested is of type USB\_BUS\_INTERFACE\_USBC\_CONFIGURATION\_GUID. If it is, the filter driver returns a pointer to the interface in the **Interface** member of the IRP.

The enumeration callback routine must return a pointer to an array of *function descriptors* ([**USBC\_FUNCTION\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff539001)) that describe the interface collections. Each function descriptor contains an array of interface descriptors ([**USB\_INTERFACE\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff540065)) that describe the interface collection. The callback routine must allocate both the function descriptors and the interface descriptors from non-paged pool. The generic parent driver releases this memory. The callback routine must ensure that the **NumberOfInterfaces** member of each **USB\_INTERFACE\_DESCRIPTOR** accurately reports the number of interfaces in the interface collection.

The generic parent driver creates a physical device object (PDO) for each function descriptor.

The USB device configuration interface and the enumeration callback routine is summarized in [Generic Parent Driver Routines](https://msdn.microsoft.com/library/windows/hardware/ff540134#usbccgp).

## USB Generic Parent Driver Loading Mechanism


When a composite device meets the requirements described in [Enumeration of USB Composite Devices](enumeration-of-the-composite-parent-device.md), the operating system generates a compatible ID of `USB\COMPOSITE` to indicate that the device is composite. The compatible ID produces a match in Usb.inf, and the operating system loads the USB generic parent driver, automatically, without the help of a vendor-supplied INF file.

However, this default mechanism does not work for composite devices that require custom enumeration of interface collections, because in the default mechanism the system does not load the required vendor-supplied filter driver. For the enumeration callback routine mechanism to work, the filter driver that exposes the USB device configuration interface must already be loaded when the USB generic parent enumerates the interface collections of the composite device. This requires the vendor of the composite device to install an INF file that matches the device ID of the composite device and explicitly loads both the USB generic parent driver and the filter driver.

## Related topics


[Enumeration of Interface Collections on USB Composite Devices](support-for-interface-collections.md)

[USB Generic Parent Driver (Usbccgp.sys)](usb-common-class-generic-parent-driver.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20%20Customizing%20Enumeration%20of%20Interface%20Collections%20for%20Composite%20Devices%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




