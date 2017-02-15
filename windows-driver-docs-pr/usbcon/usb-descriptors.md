---
Description: 'A USB device provides information about itself in data structures called USB descriptors. This section provides information about various descriptors that a client driver can obtain from a USB device.'
MS-HAID:
- 'usb-config\_c74bfa15-fd4c-4831-91ad-5b9fed7a0085.xml'
- 'buses.usb\_descriptors'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
title: USB descriptors
---

# USB descriptors


A USB device provides information about itself in data structures called *USB descriptors*. This section provides information about various descriptors that a client driver can obtain from a USB device.

## <a href="" id="ddk-usb-descriptors-kg"></a>


The host obtains descriptors from an attached device by sending various standard control requests (GET\_DESCRIPTOR requests) to the default endpoint. Those requests specify the type of descriptor to retrieve. In response to such requests, the device sends descriptors that include information about the device, its configurations, interfaces and the related endpoints. *Device descriptors* contain information about the whole device. *Configuration descriptors* contain information about each device configuration. *String descriptors* contain Unicode text strings.

Every USB device exposes a device descriptor that indicates the device’s class information, vendor and product identifiers, and number of configurations. Each configuration exposes it's configuration descriptor that indicates number of interfaces and power characteristics. Each interface exposes an interface descriptor for each of its alternate settings that contains information about the class and the number of endpoints. Each endpoint within each interface exposes endpoint descriptors that indicate the endpoint type and the maximum packet size.

For example, consider the OSR FX2 board device layout described in [USB Device Layout](usb-device-layout.md). At device level, the device exposes a device descriptor and an endpoint descriptor for the default endpoint. At configuration level, the device exposes a configuration descriptor for Configuration 0. At interface level, it exposes one interface descriptor for Alternate Setting 0. At the endpoint level, it exposes three endpoint descriptors.

## In this section


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Topic</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[USB device descriptors](usb-device-descriptors.md)</p></td>
<td><p>The device descriptor contains information about a USB device as a whole. This topic describes the [<strong>USB_DEVICE_DESCRIPTOR</strong>](https://msdn.microsoft.com/library/windows/hardware/ff539280) structure and includes information about how a client driver can send a get-descriptor request to obtain the device descriptor.</p></td>
</tr>
<tr class="even">
<td><p>[USB configuration descriptors](usb-configuration-descriptors.md)</p></td>
<td><p>A USB device exposes its capabilities in the form of a series of interfaces called a USB configuration. Each interface consists of one or more alternate settings, and each alternate setting is made up of a set of endpoints. This topic describes the various descriptors associated with a USB configuration.</p></td>
</tr>
<tr class="odd">
<td><p>[USB String Descriptors](usb-string-descriptors.md)</p></td>
<td><p>Device, configuration, and interface descriptors may contain references to string descriptors. This topic describes how to get a particular string descriptor from the device.</p></td>
</tr>
<tr class="even">
<td><p>[USB Interface Association Descriptor](usb-interface-association-descriptor.md)</p></td>
<td><p>USB interface association descriptor (IAD) allows the device to group interfaces that belong to a function. This topic describes how a client driver can determine whether the device contains an IAD for a function.</p></td>
</tr>
</tbody>
</table>

 

## Related topics


[USB Device Layout](usb-device-layout.md)

[USB Driver Development Guide](usb-driver-development-guide.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20USB%20descriptors%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




