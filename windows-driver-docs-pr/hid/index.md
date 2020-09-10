---
title: Introduction to Human Interface Devices (HID)
description: This section introduces Human Interface Devices (or HID). Typically, these are devices that humans use to directly control the operation of computer systems.
ms.assetid: 19aefe5f-d82a-411f-86ab-5d1d53191524
keywords:
- pointing devices WDK
- input devices WDK
- Human Interface Devices WDK
- HID WDK
ms.date: 02/28/2020
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Introduction to Human Interface Devices (HID)

Human Interface Devices (HID) is a device class definition to replace PS/2-style connectors with a generic USB driver to support HID devices such as keyboards, mice, game controllers, etc. Prior to HID, devices could only utilize strictly-defined protocols for mice and keyboards. Hardware innovation required either overloading data in an existing protocol or creating non-standard hardware with its own specialized driver. HID provided support for these “boot mode” devices while adding support for hardware innovation through extensible, standardized and easily-programmable interfaces.

HID devices today include a broad range of devices such as alphanumeric displays, bar code readers, volume controls on speakers/headsets, auxiliary displays, sensors and many others. Many hardware vendors also use HID for their proprietary devices.

HID began with USB but was designed to be bus-agnostic. It was designed for low latency, low bandwidth devices but with flexibility to specify the rate in the underlying transport. The specification for HID over USB was ratified by the [USB-IF](https://www.usb.org/about) in 1996 and support over additional transports followed soon after. Details on currently supported transports can be found in [HID Transports Supported in Windows](./hid-transports.md). 3rd-party, vendor-specific transports are also allowed via custom transport drivers.

## HID Concepts

HID consists of two fundamental concepts, a Report Descriptor, and Reports. Reports are the actual data that is exchanged between a device and a software client. The Report Descriptor describes the format and meaning the data that the device supports.

### Reports

Applications and HID devices exchange data through Reports. There are three Report types: Input Reports, Output Reports, and Feature Reports.

| Report Type    | Description                                                                                                     |
|----------------|-----------------------------------------------------------------------------------------------------------------|
| Input Report   | Data sent from the HID device to the application, typically when the state of a control changes. |
| Output Report  | Data sent from the application to the HID device, for example to the LEDs on a keyboard.         |
| Feature Report | Data that can be manually read and/or written, and are typically related to configuration information.    |

Each Top Level Collection defined in a Report Descriptor can contain zero (0) or more reports of each type.

### Usage Tables

The [USB-IF](https://www.usb.org/about) working group publishes HID Usage Tables that are part of the Report Descriptors that describe what HID devices are allowed to do. These HID Usage Tables contain a list with descriptions of **Usages**, which describe the intended meaning and use of a particular item described in the Report Descriptor. For example, a Usage is defined for the left button of a mouse. The Report Descriptor can define where in a Report an application can find the current state of the mouse’s left button. The Usage Tables are broken up into several name spaces, called Usage Pages. Each Usage Page describes a set of related Usages to help organize the document. The combination of a Usage Page and Usage define the Usage ID that uniquely identifies a specific Usage in the Usage Tables.

## See also

[USB-IF HID Specifications](https://www.usb.org/hid).