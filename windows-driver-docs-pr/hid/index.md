---
title: Introduction to Human Interface Devices (HID)
description: This article introduces Human Interface Devices (or HID), which people use to directly control the operation of computer systems.
keywords:
- pointing devices WDK
- input devices WDK
- Human Interface Devices WDK
- HID WDK
ms.date: 12/07/2023
ms.topic: article
---

# Introduction to Human Interface Devices (HID)

Human Interface Devices (HID) is a device class definition to replace PS/2-style connectors with a generic USB driver to support HID devices such as keyboards, mice, game controllers, and so on. Prior to HID, devices could only utilize strictly defined protocols for mice and keyboards. Hardware innovation required either overloading data in an existing protocol or creating nonstandard hardware with its own specialized driver. HID provides support for boot mode devices while adding support for innovation through extensible, standardized, and easily programmable interfaces.

HID devices include alphanumeric displays, bar code readers, speakers, headsets, auxiliary displays, sensors, and many others. Hardware vendors also use HID for their proprietary devices.

HID began with USB but was designed to be bus-agnostic. It was designed for low latency, low bandwidth devices but with flexibility to specify the rate in the underlying transport. The [USB-IF](https://www.usb.org/about) ratified the specification for HID over USB in 1996. Support for HID over other transports soon followed. Details on currently supported transports can be found in [HID Transports Supported in Windows](./hid-transports.md). Third-party, vendor-specific transports are also allowed via custom transport drivers.

## HID concepts

HID consists of two fundamental concepts, a report descriptor, and reports. Reports are the actual data that is exchanged between a device and a software client. The report descriptor describes the format and meaning the data that the device supports.

### Reports

Applications and HID devices exchange data through reports. There are three report types:

| Report type | Description |
|--|--|
| Input report | Data sent from the HID device to the application, typically when the state of a control changes. |
| Output report | Data sent from the application to the HID device, for example to the LEDs on a keyboard. |
| Feature report | Data that can be manually read and written, and are typically related to configuration information. |

Each top level collection defined in a report descriptor can contain zero or more reports of each type.

### Usage tables

The [USB-IF](https://www.usb.org/about) working group publishes HID usage tables that are part of the report descriptors that describe what HID devices are allowed to do. These HID usage tables contain a list with descriptions of **Usages** describing the intended meaning and use of a particular item in the report descriptor. For example, a usage is defined for the left button of a mouse. The report descriptor can define where in a report an application can find the current state of the mouse's left button. The usage tables are broken up into several name spaces, called usage pages. Each usage page describes a set of related usages to help organize the document. The combination of a usage and a usage page define the usage ID that uniquely identifies a specific usage in the usage tables.

## See also

- [USB-IF HID Specifications](https://www.usb.org/hid)
