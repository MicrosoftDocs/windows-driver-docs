---
Description: USB interface association descriptor (IAD) allows the device to group interfaces that belong to a function. 
title: USB Interface Association Descriptor
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# USB Interface Association Descriptor


USB interface association descriptor (IAD) allows the device to group interfaces that belong to a function. This topic describes how a client driver can determine whether the device contains an IAD for a function.

The Universal Serial Bus Specification, revision 2.0, does not support grouping more than one interface of a composite device within a single function. However, the USB Device Working Group (DWG) created USB device classes that allow for functions with multiple interfaces, and the USB Implementor's Forum issued an Engineering Change Notification (ECN) that defines a mechanism for grouping interfaces.

The ECN specifies a USB descriptor, called the Interface Association Descriptor (IAD), that allows hardware manufacturers to define groupings of interfaces. The device classes that are most likely to use IADs include:

-   USB Video Class Specification (Class Code - 0x0E)

-   USB Audio Class Specification (Class Code - 0x01)

-   USB Bluetooth Class Specification (Class Code - 0xE0)

Windows 7, Windows Server 2008, Windows Vista, Microsoft Windows Server 2003 Service Pack 1 (SP1), and Microsoft Windows XP Service Pack 2 (SP2) support IADs.

The following subsections describe information about how to use IADs.

### <a href="" id="how-should-a-composite-device-alert-the-operating-system-that-it-has-i"></a>How should a composite device alert the operating system that it has IADs in its firmware?

Manufacturers of composite devices typically assign a value of zero to the device class (*bDeviceClass*), subclass (*bDeviceSubClass*), and protocol (*bDeviceProtocol*) fields in the device descriptor, as specified by the Universal Serial Bus Specification. This allows the manufacturer to associate each individual interface with a different device class and protocol.

The USB-IF core team has devised a special class and protocol code set that notifies the operating system that one or more IADs are present in device firmware. A device's device descriptor must have the values that appear in the following table or else the operating system will not detect the device's IADs or group the device's interfaces properly.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Device descriptor field</th>
<th>Required value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><em>bDeviceClass</em></p></td>
<td><p>0xEF</p></td>
</tr>
<tr class="even">
<td><p><em>bDeviceSubClass</em></p></td>
<td><p>0x02</p></td>
</tr>
<tr class="odd">
<td><p><em>bDeviceProtocol</em></p></td>
<td><p>0x01</p></td>
</tr>
</tbody>
</table>

 

These code values also alert versions of Windows that do not support IADs to install a special-purpose bus driver that correctly enumerates the device. Without these codes in the device descriptor, the system might fail to enumerate the device, or the device might not work properly.

A device can have more than one IAD. Each IAD must be located immediately before the interfaces in the interface group that the IAD describes.

The function class (*bFunctionClass*), subclass (*bFunctionSubclassClass*), and protocol (*bFunctionProtocol*) fields of the IAD must contain the values that are specified by the USB device class that describes the interfaces in the function.

The class and subclass fields of the IAD are not required to match the class and subclass fields of the interfaces in the interface collection that the IAD describes. However, Microsoft recommends that the first interface of the collection have class and subclass fields that match the class and subclass fields of the IAD. The following table indicates which fields should match.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>IAD field</th>
<th>Corresponding interface field</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><em>bFunctionClass</em></p></td>
<td><p><em>bInterfaceClass</em></p></td>
</tr>
<tr class="even">
<td><p><em>bFunctionSubclassClass</em></p></td>
<td><p><em>bInterfaceSubClass</em></p></td>
</tr>
</tbody>
</table>

 

The *bFirstInterface* field of the IAD indicates the number of the first interface in the function. The *bInterfaceCount* field of the IAD indicates how many interfaces are in the interface collection. Interfaces in an IAD interface collection must be contiguous (there can be no gaps in the list of interface numbers), and so a count with a first interface number is sufficient to specify all of the interfaces in the collection.

### Accessing the contents of an IAD

Client drivers cannot access IAD descriptors directly. The IAD Engineering Change Notification (ECN) specifies that IADs must be included in the configuration information that devices return when they receive a request from host software for the configuration descriptor (GetDescriptor Configuration). Host software cannot retrieve IADs directly with a GetDescriptor request.

However, client drivers can query a USB device's parent driver for the device's hardware identifiers (IDs), and the device's hardware IDs contain embedded information about the fields of the IAD.

### USB Interface Association Descriptor Example

The following illustrates a descriptor layout for a composite USB device. The example device has two functions:

<a href="" id="function-1--video-class"></a>**Function 1: Video Class**  
This function is defined by an interface association descriptor (IAD) and contains two interfaces: interface zero (0) and interface one (1).

The system generates hardware and compatible identifiers (IDs) for the function, as described in [Support for the Wireless Mobile Communication Device Class](support-for-the-wireless-mobile-communication-device-class--wmcdc-.md). After matching the appropriate INF file, the system loads the Video Class driver stack.

<a href="" id="function-2--human-input-device"></a>**Function 2: Human Input Device**  
This function contains only one interface: interface two (2).

The system generates hardware and compatible IDs for the function, as described in [Enumeration of Interface Collections on USB Composite Devices](support-for-interface-collections.md). After matching the appropriate INF file, the system loads the Human Input Device (HID) class driver.

The descriptor is as follows:

### Device Descriptor:

```cpp
    BYTE  bLength      0x12
    BYTE  bDescriptorType    0x01
    WORD  bcdUSB      0x0200
    BYTE  bDeviceClass     0xEF
    BYTE  bDeviceSubClass   0x02
    BYTE  bDeviceProtocol    0x01
    BYTE  bMaxPacketSize0   0x40
    WORD  idVendor      0x045E
    WORD  idProduct      0xFFFF
    WORD  bcdDevice     0x0100
    BYTE  iManufacturer     0x01
    WORD  iProduct      0x02
    WORD  iSerialNumber    0x02
    BYTE  bNumConfigurations  0x01
```

### Configuration Descriptor:

```cpp
    BYTE  bLength      0x09
    BYTE  bDescriptorType    0x02
    WORD  wTotalLength    0x....
    BYTE  bNumInterfaces    0x03
    BYTE  bConfigurationValue  0x01
    BYTE  iConfiguration     0x01
    BYTE  bmAttributes     0x80 (BUS Powered)
    BYTE  bMaxPower     0x19 (50 mA)
```

### Interface Association Descriptor:

```cpp
    BYTE  bLength      0x08
    BYTE  bDescriptorType    0x0B
    BYTE  bFirstInterface    0x00
    BYTE  bInterfaceCount    0x02
    BYTE  bFunctionClass    0x0E
    BYTE  bFunctionSubClass   0x03
    BYTE  bFunctionProtocol   0x00
    BYTE  iFunction      0x04
```

### Interface Descriptor (Video Control):

```cpp
    BYTE  bLength      0x09
    BYTE  bDescriptorType    0x04
    BYTE  bInterfaceNumber   0x00
    BYTE  bAlternateSetting   0x00
    BYTE  bNumEndpoints    0x01
    BYTE  bInterfaceClass    0x0E
    BYTE  bInterfaceSubClass   0x01
    BYTE  bInterfaceProtocol   0x00
    BYTE  iInterface      0x05
```

### Class Specific Descriptor(s):

``` syntax
    . . . .
    . . . .
    . . . .
```

### Endpoint Descriptor(s):

``` syntax
    . . . .
    . . . .
    . . . .
```

### Interface Descriptor (Video Streaming):

```cpp
    BYTE  bLength      0x09
    BYTE  bDescriptorType    0x04
    BYTE  bInterfaceNumber   0x01
    BYTE  bAlternateSetting   0x00
    BYTE  bNumEndpoints    0x01
    BYTE  bInterfaceClass    0x0E
    BYTE  bInterfaceSubClass   0x02
    BYTE  bInterfaceProtocol   0x00
    BYTE  iInterface      0x06
```

### <a href="" id="class-specific-descriptor-s--video"></a>Class Specific Descriptor(s):

``` syntax
    . . . .
    . . . .
    . . . .
```

### <a href="" id="endpoint-descriptor-s--video"></a>Endpoint Descriptor(s):

``` syntax
    . . . .
    . . . .
    . . . .
```

### Interface Descriptor (Human Input Devices):

```cpp
    BYTE  bLength      0x09
    BYTE  bDescriptorType    0x04
    BYTE  bInterfaceNumber   0x02
    BYTE  bAlternateSetting   0x00
    BYTE  bNumEndpoints    0x01
    BYTE  bInterfaceClass    0x03
    BYTE  bInterfaceSubClass   0x01
    BYTE  bInterfaceProtocol   0x01
    BYTE  iInterface      0x07
```

### <a href="" id="class-specific-descriptor-s--hid"></a>Class Specific Descriptor(s):

``` syntax
    . . . .
    . . . .
    . . . .
```

### <a href="" id="endpoint-descriptor-s--hid"></a>Endpoint Descriptor(s):

``` syntax
    . . . .
    . . . .
    . . . .
```

## Related topics
[USB Descriptors](usb-descriptors.md)  



