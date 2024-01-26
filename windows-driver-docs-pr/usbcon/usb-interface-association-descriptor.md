---
title: USB Interface Association Descriptor
description: USB interface association descriptor (IAD) allows the device to group interfaces that belong to a function.
ms.date: 01/17/2024
---

# USB interface association descriptor

USB interface association descriptor (IAD) allows the device to group interfaces that belong to a function. This article describes how a client driver can determine whether the device contains an IAD for a function.

The *Universal Serial Bus Specification, revision 2.0*, doesn't support grouping more than one interface of a composite device within a single function. However, the USB device working group (DWG) created USB device classes that allow for functions with multiple interfaces. The [USB Implementor's Forum](https://www.usb.org/) issued an engineering change notification (ECN) that defines a mechanism for grouping interfaces.

The ECN specifies a USB descriptor, called the interface association descriptor (IAD), that allows hardware manufacturers to define groupings of interfaces. The device classes that are most likely to use IADs include:

- USB video class specification (class code - 0x0E)
- USB audio class specification (class code - 0x01)
- USB Bluetooth class specification (class code - 0xE0)

## How to use IADs

The following subsections describe information about how to use IADs.

### Composite devices alerting Windows of IADs in firmware

Manufacturers of composite devices typically assign a value of zero to the device class (*bDeviceClass*), subclass (*bDeviceSubClass*), and protocol (*bDeviceProtocol*) fields in the device descriptor, as specified by the *Universal Serial Bus Specification*. The manufacturer can associate each individual interface with a different device class and protocol.

The USB-IF core team has devised a special class and protocol code set that notifies the operating system that one or more IADs are present in device firmware. A device descriptor must have the values that appear in the following table or the operating system doesn't detect the device's IADs or group the device's interfaces properly.

| Device descriptor field | Required value |
|---|---|
| bDeviceClass | 0xEF |
| bDeviceSubClass | 0x02 |
| bDeviceProtocol | 0x01 |

The code values alert versions of Windows that don't support IADs to install a special-purpose bus driver that correctly enumerates the device. Without these codes in the device descriptor, the system might fail to enumerate the device, or the device might not work properly.

A device can have more than one IAD. Each IAD must be located immediately before the interfaces in the interface group that the IAD describes.

The function class (*bFunctionClass*), subclass (*bFunctionSubclassClass*), and protocol (*bFunctionProtocol*) fields of the IAD must contain the values specified by the USB device class that describes the interfaces in the function.

The class and subclass fields of the IAD aren't required to match the class and subclass fields of the interfaces in the interface collection that the IAD describes. Microsoft recommends that the first interface of the collection has class and subclass fields that match the class and subclass fields of the IAD. The following table indicates which fields should match.

| IAD field | Corresponding interface field |
|---|---|
| bFunctionClass | bInterfaceClass |
| bFunctionSubclassClass | bInterfaceSubClass |

The *bFirstInterface* field of the IAD indicates the number of the first interface in the function. The *bInterfaceCount* field of the IAD indicates how many interfaces are in the interface collection. Interfaces in an IAD interface collection must be contiguous (there can be no gaps in the list of interface numbers), and so a count with a first interface number is sufficient to specify all of the interfaces in the collection.

### Accessing the contents of an IAD

Client drivers can't access IAD descriptors directly. The IAD engineering change notification (ECN) specifies that IADs must be included in the configuration information that devices return when they receive a request from host software for the configuration descriptor (GetDescriptor configuration). Host software can't retrieve IADs directly with a GetDescriptor request.

However, client drivers can query a USB device's parent driver for the device's hardware identifiers (IDs), and the device's hardware IDs contain embedded information about the fields of the IAD.

### USB interface association descriptor example

This section illustrates a descriptor layout for a composite USB device. The example device has two functions:

#### Video class function

An interface association descriptor (IAD) defines this function. The function contains two interfaces: interface zero (0) and interface one (1).

The system generates hardware and compatible identifiers (IDs) for the function, as described in [Support for the Wireless Mobile Communication Device Class](./support-for-interface-collections.md). After the OS matches the appropriate INF file, the system loads the video class driver stack.

#### Human input device (HID) function

This function only contains interface two (2).

The system generates hardware and compatible IDs for the function, as described in [Enumeration of Interface Collections on USB Composite Devices](support-for-interface-collections.md). After the OS matches the appropriate INF file, the system loads the human input device (HID) class driver.

The descriptor is as follows:

### Device descriptor

```cpp
    BYTE  bLength            0x12
    BYTE  bDescriptorType    0x01
    WORD  bcdUSB             0x0200
    BYTE  bDeviceClass       0xEF
    BYTE  bDeviceSubClass    0x02
    BYTE  bDeviceProtocol    0x01
    BYTE  bMaxPacketSize0    0x40
    WORD  idVendor           0x045E
    WORD  idProduct          0xFFFF
    WORD  bcdDevice          0x0100
    BYTE  iManufacturer      0x01
    WORD  iProduct           0x02
    WORD  iSerialNumber      0x02
    BYTE  bNumConfigurations 0x01
```

### Configuration descriptor

```cpp
    BYTE  bLength             0x09
    BYTE  bDescriptorType     0x02
    WORD  wTotalLength        0x...
    BYTE  bNumInterfaces      0x03
    BYTE  bConfigurationValue 0x01
    BYTE  iConfiguration      0x01
    BYTE  bmAttributes        0x80    // (BUS Powered)
    BYTE  bMaxPower           0x19    // (50 mA)
```

### Interface association descriptor

```cpp
    BYTE  bLength           0x08
    BYTE  bDescriptorType   0x0B
    BYTE  bFirstInterface   0x00
    BYTE  bInterfaceCount   0x02
    BYTE  bFunctionClass    0x0E
    BYTE  bFunctionSubClass 0x03
    BYTE  bFunctionProtocol 0x00
    BYTE  iFunction         0x04
```

### Video control interface descriptor

```cpp
    BYTE  bLength            0x09
    BYTE  bDescriptorType    0x04
    BYTE  bInterfaceNumber   0x00
    BYTE  bAlternateSetting  0x00
    BYTE  bNumEndpoints      0x01
    BYTE  bInterfaceClass    0x0E
    BYTE  bInterfaceSubClass 0x01
    BYTE  bInterfaceProtocol 0x00
    BYTE  iInterface         0x05
```

#### Video control class-specific descriptor

``` syntax
    . . . .
    . . . .
    . . . .
```

#### Video control endpoint descriptor

``` syntax
    . . . .
    . . . .
    . . . .
```

### Video streaming interface descriptor

```cpp
    BYTE  bLength            0x09
    BYTE  bDescriptorType    0x04
    BYTE  bInterfaceNumber   0x01
    BYTE  bAlternateSetting  0x00
    BYTE  bNumEndpoints      0x01
    BYTE  bInterfaceClass    0x0E
    BYTE  bInterfaceSubClass 0x02
    BYTE  bInterfaceProtocol 0x00
    BYTE  iInterface         0x06
```

#### Video streaming class-specific descriptor

``` syntax
    . . . .
    . . . .
    . . . .
```

#### Video streaming endpoint descriptor

``` syntax
    . . . .
    . . . .
    . . . .
```

### Human input devices (HID) interface descriptor

```cpp
    BYTE  bLength            0x09
    BYTE  bDescriptorType    0x04
    BYTE  bInterfaceNumber   0x02
    BYTE  bAlternateSetting  0x00
    BYTE  bNumEndpoints      0x01
    BYTE  bInterfaceClass    0x03
    BYTE  bInterfaceSubClass 0x01
    BYTE  bInterfaceProtocol 0x01
    BYTE  iInterface         0x07
```

#### HID class-specific descriptor

``` syntax
    . . . .
    . . . .
    . . . .
```

#### HID endpoint descriptor

``` syntax
    . . . .
    . . . .
    . . . .
```

## Related topics

- [USB descriptors](usb-descriptors.md)
