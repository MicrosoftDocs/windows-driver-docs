---
Description: The USB generic parent driver handles Wireless Handset Control Model (WHCM) interfaces in a special way, as described in Support for Wireless Mobile Communications Device Class and Enumerating Interface Collections on WMCDC.The following list summarizes the most important ways in which the handling of CDC and WMCDC interface collections differs from that of other interface collections: The wireless mobile communication device class permits a limited amount of nesting of interface collections. In particular, a logical handset interface collection (that is, a WHCM interface collection) can contain other subordinate interface collections. For example, a WMCDC-compliant phone can have an WHCM interface collection, which in turn, contains an abstract control model collection and an OBEX collection. You can configure the USB generic parent driver to not enumerate WHCM interface collections. WHCM interface collections that are not enumerated remain hidden, but the generic parent driver uses information from the union function descriptors (UFDs) that belong to an WHCM interface collections to group and enumerate subordinate interface collections. You can configure the USB generic parent driver to create separate physical device objects (PDOs) for OBEX control model interface collections, or to create a single PDO for all OBEX control model interface collections. The list of interface numbers in a UFD can have gaps. That is, the interface numbers of a UFD can refer to interfaces that are not contiguous. This type of numbering is not valid, for example, for the USB Interface Association Descriptor (IAD), whose interfaces must be contiguous and have sequential numbers. UFDs can include related audio interface collections Hardware identifiers (IDs) for CDC and WMCDC interface collections must include the interface subclass. Other USB interfaces, whose hardware IDs contain a MI\_%02X suffix that specifies the interface number, do not contain information about the interface subclass. The subclass information is included in the hardware ID to allow vendors to provide INF files with hardware ID matches for specific interface collections, instead of relying on the position of the interface in the descriptor layout to determine which driver to load for the collection. The subclass information in the hardware ID also allows a gradual migration path from current vendor-supplied drivers that manage WMCDC interface collections to alternatives, such as user-mode drivers. For examples of CDC and WMCDC hardware IDs, see CDC and WMCDC Control Models. For a general discussion of how USB interface hardware IDs are formatted, see Identifiers for USB Devices.
MS-HAID:
- 'usbsystem\_49f63946-e50a-4980-98b1-b5d0075215f4.xml'
- 'buses.handling\_cdc\_and\_wmcdc\_interface\_collections'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
title: Handling CDC and WMCDC Interface Collections
---

# Handling CDC and WMCDC Interface Collections


The USB generic parent driver handles Wireless Handset Control Model (WHCM) interfaces in a special way, as described in [Support for Wireless Mobile Communications Device Class](support-for-the-wireless-mobile-communication-device-class--wmcdc-.md) and [Enumerating Interface Collections on WMCDC](enumerating-interface-collections-on-wireless-mobile-communication-dev.md).

The following list summarizes the most important ways in which the handling of CDC and WMCDC interface collections differs from that of other interface collections:

-   The wireless mobile communication device class permits a limited amount of nesting of interface collections. In particular, a logical handset interface collection (that is, a WHCM interface collection) can contain other subordinate interface collections. For example, a WMCDC-compliant phone can have an WHCM interface collection, which in turn, contains an abstract control model collection and an OBEX collection.
-   You can configure the USB generic parent driver to not enumerate WHCM interface collections. WHCM interface collections that are not enumerated remain hidden, but the generic parent driver uses information from the union function descriptors (UFDs) that belong to an WHCM interface collections to group and enumerate subordinate interface collections.
-   You can configure the USB generic parent driver to create separate physical device objects (PDOs) for OBEX control model interface collections, or to create a single PDO for all OBEX control model interface collections.
-   The list of interface numbers in a UFD can have gaps. That is, the interface numbers of a UFD can refer to interfaces that are not contiguous. This type of numbering is not valid, for example, for the [USB Interface Association Descriptor (IAD)](usb-interface-association-descriptor.md), whose interfaces must be contiguous and have sequential numbers.
-   UFDs can include related audio interface collections
-   Hardware identifiers (IDs) for CDC and WMCDC interface collections must include the interface subclass. Other USB interfaces, whose hardware IDs contain a MI\_%02X suffix that specifies the interface number, do not contain information about the interface subclass. The subclass information is included in the hardware ID to allow vendors to provide INF files with hardware ID matches for specific interface collections, instead of relying on the position of the interface in the descriptor layout to determine which driver to load for the collection. The subclass information in the hardware ID also allows a gradual migration path from current vendor-supplied drivers that manage WMCDC interface collections to alternatives, such as user-mode drivers. For examples of CDC and WMCDC hardware IDs, see [CDC and WMCDC Control Models](cdc-and-wmcdc-control-models.md). For a general discussion of how USB interface hardware IDs are formatted, see [Identifiers for USB Devices](https://msdn.microsoft.com/library/windows/hardware/ff546284).

## Related topics


[Support for the Wireless Mobile Communication Device Class](support-for-the-wireless-mobile-communication-device-class--wmcdc-.md)

[Enumeration of Interface Collections on USB Composite Devices](support-for-interface-collections.md)

[USB Generic Parent Driver (Usbccgp.sys)](usb-common-class-generic-parent-driver.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20Handling%20CDC%20and%20WMCDC%20Interface%20Collections%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




