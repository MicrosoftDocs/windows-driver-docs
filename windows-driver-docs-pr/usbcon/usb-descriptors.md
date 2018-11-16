---
Description: A USB device provides information about itself in data structures called USB descriptors. This section provides information about various descriptors that a client driver can obtain from a USB device.
title: USB descriptors
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# USB descriptors


A USB device provides information about itself in data structures called *USB descriptors*. This section provides information about various descriptors that a client driver can obtain from a USB device.




The host obtains descriptors from an attached device by sending various standard control requests (GET\_DESCRIPTOR requests) to the default endpoint. Those requests specify the type of descriptor to retrieve. In response to such requests, the device sends descriptors that include information about the device, its configurations, interfaces and the related endpoints. *Device descriptors* contain information about the whole device. *Configuration descriptors* contain information about each device configuration. *String descriptors* contain Unicode text strings.

Every USB device exposes a device descriptor that indicates the device’s class information, vendor and product identifiers, and number of configurations. Each configuration exposes its configuration descriptor that indicates number of interfaces and power characteristics. Each interface exposes an interface descriptor for each of its alternate settings that contains information about the class and the number of endpoints. Each endpoint within each interface exposes endpoint descriptors that indicate the endpoint type and the maximum packet size.

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
<td><p><a href="usb-device-descriptors.md" data-raw-source="[USB device descriptors](usb-device-descriptors.md)">USB device descriptors</a></p></td>
<td><p>The device descriptor contains information about a USB device as a whole. This topic describes the <a href="https://msdn.microsoft.com/library/windows/hardware/ff539280" data-raw-source="[&lt;strong&gt;USB_DEVICE_DESCRIPTOR&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff539280)"><strong>USB_DEVICE_DESCRIPTOR</strong></a> structure and includes information about how a client driver can send a get-descriptor request to obtain the device descriptor.</p></td>
</tr>
<tr class="even">
<td><p><a href="usb-configuration-descriptors.md" data-raw-source="[USB configuration descriptors](usb-configuration-descriptors.md)">USB configuration descriptors</a></p></td>
<td><p>A USB device exposes its capabilities in the form of a series of interfaces called a USB configuration. Each interface consists of one or more alternate settings, and each alternate setting is made up of a set of endpoints. This topic describes the various descriptors associated with a USB configuration.</p></td>
</tr>
<tr class="odd">
<td><p><a href="usb-string-descriptors.md" data-raw-source="[USB String Descriptors](usb-string-descriptors.md)">USB String Descriptors</a></p></td>
<td><p>Device, configuration, and interface descriptors may contain references to string descriptors. This topic describes how to get a particular string descriptor from the device.</p></td>
</tr>
<tr class="even">
<td><p><a href="usb-interface-association-descriptor.md" data-raw-source="[USB Interface Association Descriptor](usb-interface-association-descriptor.md)">USB Interface Association Descriptor</a></p></td>
<td><p>USB interface association descriptor (IAD) allows the device to group interfaces that belong to a function. This topic describes how a client driver can determine whether the device contains an IAD for a function.</p></td>
</tr>
</tbody>
</table>

 

## Related topics
[USB Device Layout](usb-device-layout.md)  
[USB Driver Development Guide](usb-driver-development-guide.md)  



