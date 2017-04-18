---
Description: Interfaces on a composite USB device can be grouped in collections. The USB Generic Parent Driver (Usbccgp.sys) can enumerate interface collections in four ways.
title: Enumeration of Interface Collections on USB Composite Devices
---

# Enumeration of Interface Collections on USB Composite Devices


Interfaces on a composite USB device can be grouped in collections. The [USB Generic Parent Driver (Usbccgp.sys)](usb-common-class-generic-parent-driver.md) can enumerate interface collections in four ways.

These four methods of enumeration of interface collections are arranged hierarchically in the following manner:

1.  **Vendor-supplied callback routines**

    If the vendor has registered a callback routine with the [USB Generic Parent Driver (Usbccgp.sys)](usb-common-class-generic-parent-driver.md), the generic parent driver gives precedence to the callback routine, and allows the callback routine to group interfaces rather than using some other method. For more information on the enumeration of interface collection using vendor-supplied callback routines, see [Customizing Enumeration of Interface Collections for Composite Devices](custom-enumeration-of-interface-collections-by-vendor-supplied-callbac.md).

2.  **Union Functional Descriptors**

    . If the vendor has enabled CDC and WMCDC enumeration in the USB generic parent driver, the generic parent driver uses *union functional descriptors* (UFDs) to group interfaces into collections. When enabled, this method has precedence over all other methods, except for vendor-supplied callback routines. For more information on the enumeration of devices with UFDs, see [Support for Wireless Mobile Communications Device Class](support-for-the-wireless-mobile-communication-device-class--wmcdc-.md).

3.  **Interface Association Descriptors**

    If *interface association descriptors* (IADs) are present, the USB generic parent driver always groups interfaces by using IADs rather than by using legacy methods. Microsoft recommends that vendors use IADs to define interface collections. For more information on the enumeration of devices with IADs, see [Enumeration of Interface Collections on USB Devices with IADs](enumeration-of-interface-collections-on-devices-that-have-iads.md).

4.  **Legacy audio method.**

    The USB generic parent driver is able to enumerate interface collections by using legacy techniques that are reserved for audio functions. The generic parent driver does not use this method if there are any IADs on the device. For more information on the legacy audio method of enumeration, see [Enumeration of Interface Collections on Audio Devices without IADs](enumeration-of-interface-collections-on-audio-devices-without-iads.md).

## Related topics


[USB Generic Parent Driver (Usbccgp.sys)](usb-common-class-generic-parent-driver.md)

[Microsoft-provided USB drivers](system-supplied-usb-drivers.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20Enumeration%20of%20Interface%20Collections%20on%20USB%20Composite%20Devices%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




