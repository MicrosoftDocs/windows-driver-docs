---
title: Introduction to HID Concepts
description: This section introduces Human Interface Devices (or HID). Typically, these are devices that humans use to directly control the operation of computer systems.
ms.assetid: 477FF911-5A17-4EA5-9403-1D7B4E8B3BA5
keywords:
- Human Interface Devices
- HID
- keyboards
- mice
- sensory data
- accelerometers
- gyroscope
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Introduction to HID Concepts


This section introduces Human Interface Devices (or HID). Typically, these are devices that humans use to directly control the operation of computer systems.

## History of HID


The definition of HID started as a device class over USB. The goal at that time was to define a replacement to PS/2 and create an interface over USB, allowing the creation of a generic driver for HID devices like keyboards, mice, and game controllers. Prior to HID, devices had to conform to strictly defined protocols for mice and keyboards. All hardware innovations necessitated overloading the use of data in an existing protocol, or the creation of non-standard hardware that needed its own drivers. The vision of HID started with finding a way for providing basic support for these “boot mode” devices in the operating system, but still allowing hardware vendors to provide differentiation with extensible, standardized and easily programmable interfaces.

Today, HID devices include: alphanumeric displays, barcode readers, volume controls on speakers/headsets, auxiliary displays, sensors, and MRI’s (yes, in hospitals). In addition, many hardware vendors use HID for their proprietary devices.

HID started over USB but was designed in a bus agnostic fashion from the very beginning. It was originally designed for low latency, low bandwidth devices but is flexible, and the rate is specified by the underlying transport. The specification for HID over USB was ratified in the late 1990s, and support over additional transports started soon after that. Today, HID has a standard protocol over multiple transports, and the following transports are supported natively in Windows 8 for HID:

-   USB
-   Bluetooth
-   Bluetooth LE
-   I²C

Vendor specific transports are also allowed via 3rd party vendor-specific transport drivers. More details will be provided in later sections.

## HID Concepts


HID is built on a couple of fundamental concepts, a Report Descriptor, and reports. Reports are the actual data blobs that are exchanged between a device and a software client. The Report Descriptor describes the format and meaning of each data blob that it supports.

### Reports

When applications and HID devices exchange data, this is done through Reports. There are three report types: Input Reports, Output Reports, and Feature Reports.

| Report Type    | Description                                                                                                     |
|----------------|-----------------------------------------------------------------------------------------------------------------|
| Input Report   | Data blobs that are sent from the HID device to the application, typically when the state of a control changes. |
| Output Report  | Data blobs that are sent from the application to the HID device, for example to the LEDs on a keyboard.         |
| Feature Report | Data blobs that can be manually read and/or written, and are typically related to configuration information.    |

 

Each Top Level Collection defined in a Report Descriptor can contain zero (0) or more reports of each type.

### Usage Tables

The HID working group publishes a set of documents that make up the HID Usage Tables. This is effectively the dictionary that describes what HID devices are allowed to do. These HID Usage Tables contain a list with descriptions of the Usages. A Usage provides information to an application developer about the intended meaning and use of a particular item described in the Report Descriptor. For example, there is a Usage defined for the left button of a mouse. The Report Descriptor can define where in a report an application can find the current state of the mouse’s left button. The Usage Tables are broken up into several name spaces, called Usage Pages. Each Usage Page describes a set of related Usages to help organize the document. The combination of a Usage Page and Usage defines the Usage ID that uniquely identifies a specific Usage in the Usage Tables.

## The HID Application Programming Interface (API)


There are three categories of HID APIs: device discovery and setup, data movement, and report creation/interpretation.

### Device Discovery and Setup

The following list identifies the HID API that an application can use to: identify the properties of a HID device, and to establish communication with that device. In addition, an application can use some of these API to identify a Top Level Collection.

-   [**HidD\_GetAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff538900)
-   [**HidD\_GetHidGuid**](https://msdn.microsoft.com/library/windows/hardware/ff538924)
-   [**HidD\_GetIndexedString**](https://msdn.microsoft.com/library/windows/hardware/ff538927)
-   [**HidD\_GetManufacturerString**](https://msdn.microsoft.com/library/windows/hardware/ff538959)
-   [**HidD\_GetPhysicalDescriptor**](https://msdn.microsoft.com/library/windows/hardware/ff539677)
-   [**HidD\_GetPreparsedData**](https://msdn.microsoft.com/library/windows/hardware/ff539679)
-   [**HidD\_GetProductString**](https://msdn.microsoft.com/library/windows/hardware/ff539681)
-   [**HidD\_GetSerialNumberString**](https://msdn.microsoft.com/library/windows/hardware/ff539683)
-   [**HidD\_GetNumInputBuffers**](https://msdn.microsoft.com/library/windows/hardware/ff539675)
-   [**HidD\_SetNumInputBuffers**](https://msdn.microsoft.com/library/windows/hardware/ff539686)

### Data Movement

The following list identifies the HID API that an application can use to move data back and forth between the app and a selected device.

-   [**HidD\_GetInputReport**](https://msdn.microsoft.com/library/windows/hardware/ff538945)
-   [**HidD\_SetFeature**](https://msdn.microsoft.com/library/windows/hardware/ff539684)
-   [**HidD\_SetOutputReport**](https://msdn.microsoft.com/library/windows/hardware/ff539690)
-   [ReadFile](https://msdn.microsoft.com/library/windows/desktop/aa365467.aspx)
-   [WriteFile](https://msdn.microsoft.com/library/windows/desktop/aa365747.aspx)

### Report Creation and Interpretation

If you are writing a HID app for your own hardware, you have existing knowledge of the size and format of each report issued by your device. In this case, your app can cast the input and output report buffers to structs and consume the data.

If, however, you are writing a HID app that communicates with all devices that expose common functionality (for example, a music app that needs to detect when a play button is pressed), you may not know the size and format of the HID reports. This category of application understands certain Top Level Collections and certain usages.

In order to interpret the reports received from a device, or to create reports to be sent, the application needs to leverage the Report Descriptor in order to determine if and where a particular usage is located in the reports, and (potentially) the units of values in the reports. This is where HID parsing is required. Windows provides a HID parser for use by drivers and applications. This parser exposes a set of APIs (HidP\_\*) that can be used to discover the types of usages supported by a device, determine the state of such usages in a report, or to build a report to change the state of a usage in the device.

The following list identifies the HID parser APIs.

-   [**HidP\_GetButtonCaps**](https://msdn.microsoft.com/library/windows/hardware/ff539707)
-   [**HidP\_GetButtons**](https://msdn.microsoft.com/library/windows/hardware/ff539708)
-   [**HidP\_GetButtonsEx**](https://msdn.microsoft.com/library/windows/hardware/ff539712)
-   [**HidP\_GetCaps**](https://msdn.microsoft.com/library/windows/hardware/ff539715)
-   [**HidP\_GetData**](https://msdn.microsoft.com/library/windows/hardware/ff539718)
-   [**HidP\_GetExtendedAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff539721)
-   [**HidP\_GetLinkCollectionNodes**](https://msdn.microsoft.com/library/windows/hardware/ff539725)
-   [**HidP\_GetScaledUsageValue**](https://msdn.microsoft.com/library/windows/hardware/ff539729)
-   [**HidP\_GetSpecificButtonCaps**](https://msdn.microsoft.com/library/windows/hardware/ff539733)
-   [**HidP\_GetSpecificValueCaps**](https://msdn.microsoft.com/library/windows/hardware/ff539737)
-   [**HidP\_GetUsages**](https://msdn.microsoft.com/library/windows/hardware/ff539742)
-   [**HidP\_GetUsagesEx**](https://msdn.microsoft.com/library/windows/hardware/ff539745)
-   [**HidP\_GetUsageValue**](https://msdn.microsoft.com/library/windows/hardware/ff539748)
-   [**HidP\_GetUsageValueArray**](https://msdn.microsoft.com/library/windows/hardware/ff539750)
-   [**HidP\_GetValueCaps**](https://msdn.microsoft.com/library/windows/hardware/ff539754)
-   [**HidP\_InitializeReportForID**](https://msdn.microsoft.com/library/windows/hardware/ff539757)
-   [**HidP\_IsSameUsageAndPage**](https://msdn.microsoft.com/library/windows/hardware/ff539761)
-   [**HidP\_MaxDataListLength**](https://msdn.microsoft.com/library/windows/hardware/ff539768)
-   [**HidP\_MaxUsageListLength**](https://msdn.microsoft.com/library/windows/hardware/ff539770)
-   [**HidP\_SetButtons**](https://msdn.microsoft.com/library/windows/hardware/ff539779)
-   [**HidP\_SetData**](https://msdn.microsoft.com/library/windows/hardware/ff539783)
-   [**HidP\_SetScaledUsageValue**](https://msdn.microsoft.com/library/windows/hardware/ff539787)
-   [**HidP\_SetUsages**](https://msdn.microsoft.com/library/windows/hardware/ff539792)
-   [**HidP\_SetUsageValue**](https://msdn.microsoft.com/library/windows/hardware/ff539797)
-   [**HidP\_SetUsageValueArray**](https://msdn.microsoft.com/library/windows/hardware/ff539801)
-   [**HidP\_UnsetButtons**](https://msdn.microsoft.com/library/windows/hardware/ff539812)
-   [**HidP\_UnsetUsages**](https://msdn.microsoft.com/library/windows/hardware/ff539819)
-   [**HidP\_UsageAndPageListDifference**](https://msdn.microsoft.com/library/windows/hardware/ff539824)
-   [**HidP\_UsageListDifference**](https://msdn.microsoft.com/library/windows/hardware/ff539826)

 

 




