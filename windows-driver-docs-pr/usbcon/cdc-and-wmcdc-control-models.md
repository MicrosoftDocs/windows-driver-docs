---
Description: CDC and WMCDC Control Models
MS-HAID:
- 'usbsystem\_ca96b130-eec6-4ef3-8933-83ea448ec472.xml'
- 'buses.cdc\_and\_wmcdc\_control\_models'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
title: CDC and WMCDC Control Models
---

# CDC and WMCDC Control Models


The CDC and WMCDC Control Models section describes the properties of interface collections that are supported in Microsoft Windows operating systems. Each description includes, among other things, a list of hardware and device identifiers (IDs) that the USB generic parent driver generates for the interface collection.

Most of the interface collections that Windows supports correspond to control models that belong to the communication device class (CDC) and wireless mobile communication device class (WMCDC), but the operating system also supports legacy audio and video interface collections and an interface collection that the Mobile Computing Promotion Consortium (MCPC) defines.

The interface collections that are described in this section are the following:

[Audio Class Interfaces](audio-class-interfaces.md)

[CDC Abstract Control Model](cdc-abstract-control-model.md)

[CDC ATM Networking Control Model](cdc-atm-networking-control-model.md)

[CDC CAPI Control Model](cdc-capi-control-model.md)

[CDC Direct Line Control Model](cdc-direct-line-control-model.md)

[CDC Ethernet Networking Control Model](https://msdn.microsoft.com/library/windows/hardware/ff537037)

[CDC Multi-Channel ISDN Control Model](cdc-multi-channel-isdn-control-model.md)

[CDC Telephone Control Model](cdc-telephone-control-model.md)

[MCPC Vendor-Unique Interfaces](mcpc-vendor-unique-interfaces.md)

[Video Class Interfaces](video-class-interfaces.md)

[WMCDC Abstract Control Model](wmcdc-abstract-control-model.md)

[WMCDC Device Management Model](wmcdc-device-management-model.md)

[WMCDC Mobile Direct Line Model](wmcdc-mobile-direct-line-model.md)

[WMCDC OBEX Control Model (Multiple PDOs)](wmcdc-obex-control-model--multiple-pdos-.md)

[WMCDC OBEX Control Model (Single PDO)](wmcdc-obex-control-model--single-pdo-.md)

[WMCDC Wireless Handset Control Model](wmcdc-wireless-handset-control-model.md)

The hardware ID formats in the preceding topics describe use the following conventions:

-   a C-language **printf** format represents integers. For example, "%04x" means a 4-digit hexadecimal integer, "%02x" means a 2-digit hexadecimal integer, and so on.

-   The integer that follows the string "Vid\_" is a 4-digit hexadecimal representation of the vendor code that the USB committee (www.usb.org) assigns to the vendor.

-   The integer that follows the string "Pid\_" is a 4-digit hexadecimal representation of the product code that the vendor assigns to the device.

-   The integer that follows the string "Rev\_" is a 4-digit hexadecimal representation of the revision number of the device.

-   The integer that follows the string "Cdc\_" is the interface subclass.

-   The integer that follows the string "Prot\_" is the protocol number.

-   The integer that follows the string "MI\_" is a 2-digit hexadecimal representation of the interface number, which is extracted from the **bInterfaceNumber** field of the interface descriptor.

## Related topics


[Support for the Wireless Mobile Communication Device Class](support-for-the-wireless-mobile-communication-device-class--wmcdc-.md)

[Enumeration of Interface Collections on USB Composite Devices](support-for-interface-collections.md)

[USB Generic Parent Driver (Usbccgp.sys)](usb-common-class-generic-parent-driver.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20CDC%20and%20WMCDC%20Control%20Models%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




