---
Description: 'If a USB composite device has an interface association descriptor (IAD) in its firmware, Windows enumerates interface collections as though each collection were a single device and assigns a single physical device object (PDO) to each interface collection and associates hardware and compatible identifiers (IDs) with the PDO. For a detailed description of IADs, see USB Interface Association Descriptor. This section describes the hardware IDs and compatible identifiers (IDs) assigned to interface collections associated with an IAD.'
MS-HAID:
- 'usbsystem\_31f7c94a-0f76-4fd8-af34-e5d2ce130efc.xml'
- 'buses.enumeration\_of\_interface\_collections\_on\_devices\_that\_have\_iads'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
title: Enumeration of Interface Collections on USB Devices with IADs
---

# Enumeration of Interface Collections on USB Devices with IADs


If a USB composite device has an interface association descriptor (IAD) in its firmware, Windows enumerates interface collections as though each collection were a single device and assigns a single physical device object (PDO) to each interface collection and associates hardware and compatible identifiers (IDs) with the PDO. For a detailed description of IADs, see [USB Interface Association Descriptor](usb-interface-association-descriptor.md). This section describes the hardware IDs and compatible identifiers (IDs) assigned to interface collections associated with an IAD.

## <a href="" id="hardware-ids"></a> Hardware IDs


`USB\VID_v(4)&PID_p(4)&Rev_r(4)&MI_z(2)`

`USB\VID_v(4)&PID_p(4)&MI_z(2)`

In these hardware IDs,

-   *v(4)* is the four-digit vendor code that the USB committee assigns to the vendor and that is extracted from the **idVendor** field of the device descriptor.
-   *p(4)* is the four-digit product code that the vendor assigns to the device and that is extracted from the **idProduct** field of the device descriptor.
-   *r(4)* is the four-digit device release number, in binary coded decimal revision, that the vendor assigns to the device and that is extracted from the **bcdDevice** field of the device descriptor.
-   *z(2)* is the two-digit interface number that is extracted from the **bFirstInterface** field of IAD.

## Compatible IDs


`USB\Class_c(2)&SubClass_s(2)&Prot_p(2)`

`USB\Class_c(2)&SubClass_s(2)`

`USB\Class_c(2)`

In these compatible IDs, c(2), s(2), and p(2) contain values that are taken, respectively, from the **bFunctionClass**, **bFunctionSubClass**, and **bFunctionProtocol** fields of the IAD.

You cannot use IADs recursively to bind functions of functions. In particular, if a device has IAD descriptors in its firmware, the generic parent driver will not group interfaces by audio device class, as described in [Enumeration of Interface Collections on Audio Devices without IADs](enumeration-of-interface-collections-on-audio-devices-without-iads.md).

## Related topics


[Enumeration of Interface Collections on USB Composite Devices](support-for-interface-collections.md)

[USB Generic Parent Driver (Usbccgp.sys)](usb-common-class-generic-parent-driver.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20Enumeration%20of%20Interface%20Collections%20on%20USB%20Devices%20with%20IADs%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




