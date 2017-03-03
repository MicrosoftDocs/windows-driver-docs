---
Description: 'For audio devices, the Windows operating system can enumerate groups of interfaces (interface collections) that are associated with a function and assign a single physical device object (PDO) to each group, even when the device does not have an interface association descriptor (IAD).'
MS-HAID:
- 'usbsystem\_71f6d80d-d1d6-4a45-bfe4-c3518802a032.xml'
- 'buses.enumeration\_of\_interface\_collections\_on\_audio\_devices\_without\_iads'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
title: Enumeration of Interface Collections on Audio Devices without IADs
author: windows-driver-content
---

# Enumeration of Interface Collections on Audio Devices without IADs


For audio devices, the Windows operating system can enumerate groups of interfaces (interface collections) that are associated with a function and assign a single physical device object (PDO) to each group, even when the device does not have an interface association descriptor (IAD).

The operating system groups the interfaces of composite audio devices into interface collections, if the interfaces meet the following conditions:

-   All interfaces in the interface collection must be consecutive. In other words, the interfaces must be adjacent to one another in firmware memory.
-   All interfaces in the interface collection must belong to the audio device class. The device manufacturer specifies that an interface belongs to the audio device class by assigning a value of 0x01 to the **bInterfaceClass** field of the interface descriptor.
-   Each interface in the interface collection must have a different subclass from the first interface in the collection.The **bInterfaceSubClass** field of the interface descriptor specifies the device subclass of the interface.

If an interface does not meet all of these three conditions, Windows will attempt to enumerate it separately instead of grouping it with the other audio class interfaces.

The operating system does not group audio class interfaces in a special way if an interface association descriptor (IAD) is present in device firmware. The IAD method is always the preferred method of grouping USB interfaces.

This section describes hardware and compatible identifiers (IDs) associated with the PDO that is created by the operating system for an interface collection whose interfaces belong to the audio device class.

## Hardware IDs


`USB\VID_v(4)&PID_p(4)&Rev_r(4)&MI_z(2)`

`USB\VID_v(4)&PID_p(4)&MI_z(2)`

In these hardware IDs,

-   *v(4)* is the four-digit vendor code that the USB standards committee assigns to the vendor and that is extracted from the **idVendor** field of the device descriptor.
-   *p(4)* is the four-digit product code that the vendor assigns to the device and that is extracted from the **idProduct** field of the device descriptor.
-   *r(4)* is the four-digit device release number, in binary coded decimal revision, that the vendor assigns to the device and that is extracted from the **bcdDevice** field of the device descriptor.
-   *z(2)* is the two-digit interface number that is extracted from the **bInterfaceNumber** field of the interface descriptor.

### Compatible IDs

`USB\Class_c(2)&SubClass_s(2)&Prot_p(2)`

`USB\Class_c(2)&SubClass_s(2)`

`USB\Class_c(2)`

In these compatible IDs, c(2), s(2), and p(2) contain values that are taken, respectively, from the bInterfaceClass, bInterfaceSubClass, and bInterfaceProtocol fields of the first USB interface descriptor in each interface collection.

## Related topics
[Enumeration of Interface Collections on USB Composite Devices](support-for-interface-collections.md)  
[USB Generic Parent Driver (Usbccgp.sys)](usb-common-class-generic-parent-driver.md)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20Enumeration%20of%20Interface%20Collections%20on%20Audio%20Devices%20without%20IADs%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


