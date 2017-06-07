---
title: What's new in driver development
description: This section describes new features for driver development in Windows 10.
ms.assetid: 5502AAF9-2400-4338-A646-C746B29F9A44
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# What's new in driver development
<a href="" id="top"></a>

The following highlights new features for driver development in Windows 10.

* [Open publishing](#open-publishing)
* [Debugging Tools for Windows](#debugging-tools-for-windows)
* [Driver Verifier](#driver-verifier)
* [Windows Driver Frameworks](#windows-driver-frameworks)
* [Universal Windows drivers](#universal-windows-drivers)
* [Windows Compatible hardware development boards](#windows-compatible-hardware-development-boards)
* [Power Management Framework](#power-management-framework)
* [System-Supplied Driver Interfaces](#system-supplied-driver-interfaces)
* [WPP Software Tracing](#wpp-software-tracing)
* [Kernel](#kernel)

This table describes Windows 10 feature updates by driver technology.

| Driver |  [version 1703](#version-1703) |  [version 1607](#version-1607) |  [Windows 10](#version-1507) |
|---|:---:|:---:|:---:|
| Audio | [![details](checkmark.png)](#audio-1703) | [![details](checkmark.png)](#audio)  |![not available](minus.png) |
| Bluetooth | [![not available](checkmark.png)](#bluetooth-1703) | ![not available](minus.png) | [![details](checkmark.png)](#bluetooth) |
| Buses and Ports | ![not available](minus.png) | ![not available](minus.png) |[![details](checkmark.png)](#buses-and-ports) |
| Camera | [![details](checkmark.png)](#camera-1703) |[![details](checkmark.png)](#camera-1607) |[![details](checkmark.png)](#camera-1507)|
| Cellular | ![not available](minus.png) | ![not available](minus.png) |[![details](checkmark.png)](#cellular)|
| Display | ![not available](minus.png) | ![not available](minus.png) |[![details](checkmark.png)](#display)|
| Human Interface Device (HID)| ![not available](minus.png) | ![not available](minus.png) |[![details](checkmark.png)](#human-interface-device)|
| Location | ![not available](minus.png) |[![details](checkmark.png)](#location-1607) |[![details](checkmark.png)](#location-1507) |
| Near Field Communication | ![not available](minus.png) | ![not available](minus.png) |[![details](checkmark.png)](#near-field-communication)|
| Networking | [![details](checkmark.png)](#networking-1703)| ![not available](minus.png) |[![details](checkmark.png)](#networking-1507) |
| POS |[![details](checkmark.png)](#pos) | ![not available](minus.png) | ![not available](minus.png) |
| Print |![not available](minus.png) |[![details](checkmark.png)](#print-1607) |[![details](checkmark.png)](#print-1507)|
| Smart Card | ![not available](minus.png) | ![not available](minus.png) |[![details](checkmark.png)](#smart-card) |
| Storage | ![not available](minus.png) | ![not available](minus.png) |[![details](checkmark.png)](#storage) |
| System-Supplied Driver Interfaces | ![not available](minus.png) | ![not available](minus.png) |[![details](checkmark.png)](#system-supplied-driver-interfaces) |
| USB | [![details](checkmark.png)](#usb-1703) | ![not available](minus.png) |[![details](checkmark.png)](#usb)|
| WLAN | ![not available](minus.png) |[![details](checkmark.png)](#wlan-1607) |[![details](checkmark.png)](#wlan-1507)|

## What's new in driver development

[Back to Top](#top)

This section highlights new features for driver development in Windows 10.

### Open publishing

We're making the docs more community-driven. On many pages of the Windows driver documentation, you can suggest changes directly. Look for the **Contribute** button in the upper right corner of a page. It looks like this:

![screenshot of contribute button](contribute-button.png)

When you click **Contribute**, you'll arrive at the Markdown source file for that topic in a [GitHub repository](https://github.com/MicrosoftDocs/windows-driver-docs). You can click **Edit** and suggest changes right here.

For more details, see [CONTRIBUTING.md](https://github.com/MicrosoftDocs/windows-driver-docs/blob/staging/CONTRIBUTING.md) in the repo. And thanks for taking the time to improve the docs!

### Debugging Tools for Windows

This section describes the changes for the debugging tools for Windows.

**Windows 10, version 1703**

New topics:

* [JavaScript Debugger Scripting](https://msdn.microsoft.com/en-us/library/windows/hardware/mt790253(v=vs.85).aspx)
* Published 40 undocumented stop codes in the [Bug Check Code Reference](https://msdn.microsoft.com/library/windows/hardware/hh994433)
* New [!ioctldecode command](https://msdn.microsoft.com/en-us/library/windows/hardware/mt790255(v=vs.85).aspx)

Updated topics:

* New command capabilities in the [dx (Display Debugger Object Model Extension)](https://msdn.microsoft.com/library/windows/hardware/dn936815) command
* [dtx (Display Type - Extended Debugger Object Model Information)](https://msdn.microsoft.com/en-us/library/windows/hardware/mt790251(v=vs.85).aspx) command
* Updates to the [Configuring tools.ini](https://msdn.microsoft.com/en-us/library/windows/hardware/ff539232(v=vs.85).aspx) topic with additional options in the tools.ini file for the command line debuggers

**Windows 10, version 1607**

Changes include a new topic about [Debugging a UWP app using WinDbg](https://msdn.microsoft.com/library/windows/hardware/mt757092), and updates to the 30 most-viewed developer bug check topics in [Bug Check Code Reference](https://msdn.microsoft.com/library/windows/hardware/hh994433).

**Windows 10, version 1507**

The following new commands are available in the Windows debugger:

* [**dx (Display NatVis Expression)**](https://msdn.microsoft.com/library/windows/hardware/dn936815) - A new debugger command which displays object information using the NatVis extension model.
* [**.settings**](https://msdn.microsoft.com/library/windows/hardware/dn925473) - A new command that sets, modifies, displays, loads and saves settings in the Debugger.Settings namespace.

### Driver Verifier

Driver verifier includes new driver validation rules for the following technologies:

-   New [Rules for Audio Drivers](https://msdn.microsoft.com/library/windows/hardware/dn906757)
-   New [Rules for AVStream Drivers](https://msdn.microsoft.com/library/windows/hardware/dn906758)
-   Four new [Rules for KMDF Drivers](https://msdn.microsoft.com/library/windows/hardware/ff551709)
-   Three new [Rules for NDIS Drivers](https://msdn.microsoft.com/library/windows/hardware/ff551713)
-   New [Nullcheck rules](https://msdn.microsoft.com/en-us/library/windows/hardware/mt779099(v=vs.85).aspx) *Added in version 1703*

### <a href="" id="windows-driver-frameworks"></a>Windows Driver Frameworks (WDF)

Windows 10, version 1607 includes Kernel-Mode Driver Framework (KMDF) version 1.19 and User-Mode Driver Framework (UMDF) version 2.19.

For info on what's included in these framework versions, see [What's New for WDF Drivers in Windows 10](wdf/index.md).

### Universal Windows drivers

Starting in Windows 10, you can write a single driver that works on OneCoreUAP-based editions of Windows, such as Windows 10 for desktop editions (Home, Pro, Enterprise, and Education), Windows 10 Mobile, and Windows 10 IoT Core (IoT Core). Such a driver is called a Universal Windows driver. A Universal Windows driver calls a subset of the interfaces that are available to a Windows driver. For information about how to build, install, deploy, and debug a Universal Windows driver for Windows 10, see [Getting Started with Universal Windows drivers](https://msdn.microsoft.com/windows-drivers/develop/getting_started_with_universal_drivers).

When you build a Universal Windows driver using Microsoft Visual Studio 2015, Visual Studio automatically checks if the APIs that your driver calls are valid for a Universal Windows driver. You can also use the ApiValidator.exe as a standalone tool to perform this task. The ApiValidator.exe tool is part of the Windows Driver Kit (WDK) for Windows 10. For info, see [Validating Universal Windows drivers](https://msdn.microsoft.com/windows-drivers/develop/validating_universal_drivers).

Universal Windows drivers also require a special kind of INF file called a *universal INF*. A universal INF can use a subset of the directives and sections available to a legacy INF file. To learn more, see [Using a Universal INF File](https://msdn.microsoft.com/library/windows/hardware/dn941087). To see which sections and directives apply, see [INF File Sections and Directives](https://msdn.microsoft.com/library/windows/hardware/ff547433).

When you're ready, use the [InfVerif](https://msdn.microsoft.com/library/windows/hardware/dn929319) tool to test your driver's INF file. In addition to reporting INF syntax problems, the tool reports if the INF file will work with a Universal Windows driver.

You can also find information about which APIs you can call from a Universal Windows driver. This information is located in the Requirements block at the bottom of MSDN reference pages.

For example, you'll see a listing similar to this one that tells you if a given DDI is **Universal.**

![target platform set to universal in requirements block](targetplatform.png)

For more info, see [Target platform on MSDN driver reference pages](https://msdn.microsoft.com/windows-drivers/develop/windows_10_editions_for_universal_drivers).

### Windows compatible hardware development boards

Windows is now supported on more affordable boards such as the Raspberry Pi 2. Become a part of our early adopter community and load Windows on that board. For more information, see [Windows compatible hardware development boards](https://msdn.microsoft.com/library/windows/hardware/dn914597).

### <a href="" id="power-management-framework"></a>Power Management Framework (PoFx)

The power management framework (PoFx) enables a driver to define one or more sets of individually adjustable performance states for individual components within a device. The driver can use performance states to throttle a component's workload to provide just enough performance for its current needs. For more information, see [Component-Level Performance State Management](https://msdn.microsoft.com/library/windows/hardware/dn939352).

### WPP Software Tracing

[WPP Software Tracing](https://msdn.microsoft.com/library/windows/hardware/ff556204) introduces a new feature: Inflight Trace Recorder. If the driver enables WPP tracing and WPP Recorder, trace logging is turned on automatically and you can easily view messages without starting or stopping trace sessions. For more fine tuned control over the log, WPP Recorder allows a KMDF driver to create and manage custom buffers.

-   [WPP Recorder for logging traces](https://msdn.microsoft.com/library/windows/hardware/dn914610)
-   [**WppRecorderLogGetDefault**](https://msdn.microsoft.com/library/windows/hardware/dn895240)
-   [**WppRecorderLogCreate**](https://msdn.microsoft.com/library/windows/hardware/dn914615) (KMDF only)
-   [**WppRecorderDumpLiveDriverData**](https://msdn.microsoft.com/library/windows/hardware/dn914612)

### Kernel

[Windows Kernel-Mode Process and Thread Manager](https://msdn.microsoft.com/en-us/library/windows/hardware/ff565772(v=vs.85).aspx) - Starting in Windows 10 version 1703, the Windows Subsystem for Linux (WSL) enables a user to run native Linux ELF64 binaries on Windows, alongside other Windows applications. For more information about WSL architecture and the user-mode and kernel-mode components that are required to run the binaries, see the posts on the [Windows Subsystem for Linux](https://blogs.msdn.microsoft.com/wsl/) blog.

## <a href="" id="version-1703"></a>What's new for Windows 10, version 1703 (latest)

This section describes new features and improvements for driver development in Windows 10, version 1703.

[Back to Top](#top)


### <a href="" id="audio-1703"></a>Audio

New topics:

* [Implementing Audio Module Communication](https://docs.microsoft.com/en-us/windows-hardware/drivers/audio/implementing-audio-module-communication) describes the support for communication from Universal Windows Platform (UWP) apps to kernel mode audio device drivers.
* New DDIs and properties reference topics to support APO Module Communications discovery. For example:
    - A new KS Property Set, identified by [KSPROPSETID_AudioModule](https://msdn.microsoft.com/en-us/library/windows/hardware/mt808144.aspx), has been defined for three properties specific to audio modules.
    - Support for the [KSPROPERTY_AUDIOMODULE_COMMAND](https://msdn.microsoft.com/library/windows/hardware/mt808141.aspx) property allows Audio Module clients to send custom commands to query and set parameters on Audio Modules. 
    - New Port Class Notifications [IPortClsNotifications](https://msdn.microsoft.com/library/windows/hardware/mt808133.aspx) that provide notification helpers to miniports to support audio module communication.


### Battery

Updated DDI documentation.

### <a href="" id="camera-1703"></a>Camera

New topics:

* [USB Video Class (VCC) driver implementation guide](https://msdn.microsoft.com/en-us/windows/hardware/drivers/stream/uvc-driver-implementation-checklist)
* [Microsoft extensions to USB Video Class 1.5 specification](https://msdn.microsoft.com/en-us/windows/hardware/drivers/stream/uvc-extensions-1-5)
* [Device transform manager (DTM) events](https://msdn.microsoft.com/en-us/library/windows/hardware/mt797660)
* [IMFDeviceTransform interface](https://msdn.microsoft.com/en-us/library/windows/hardware/mt797663)
* KSCategory_Xxx Device Interface Classes
    - [KSCATEGORY_SENSOR_CAMERA](https://msdn.microsoft.com/en-us/library/windows/hardware/mt796964)
    - [KSCATEGORY_VIDEO_CAMERA](https://msdn.microsoft.com/en-us/library/windows/hardware/mt796965)

### <a href="" id="bluetooth-1703"></a>Bluetooth

Windows 10 version 1703, now provides:

* Hands-Free Profile (HFP) 1.6 specification with Wideband speech on Windows 10 for desktop editions.
* Support for [Call Control APIs](https://docs.microsoft.com/en-us/uwp/api/Windows.ApplicationModel.Calls) on Windows 10 for desktop editions.
* Support for GATT Server, Bluetooth LE Peripheral and non-paired support for Bluetooth LE. See our [developer post](http://aka.ms/bluetoothgatt) for more details.

For more information about what's new for Bluetooth, see [Bluetooth](https://msdn.microsoft.com/en-us/windows/hardware/commercialize/design/component-guidelines/bluetooth) and [Bluetooth LE pre-pairing](https://msdn.microsoft.com/en-us/windows/hardware/commercialize/design/component-guidelines/bluetooth-prepairing).

### <a href="" id="networking-1703"></a>Networking

The following lists updates to Networking:

* [**Winsock Kernel**](https://msdn.microsoft.com/windows/hardware/drivers/network/winsock-kernel-socket-categories) - Includes a new type of socket called Stream Sockets, which support Linux networking applications on Windows. New functions and structures include [WskConnectEx](https://msdn.microsoft.com/library/windows/hardware/mt799884), [WskListen](https://msdn.microsoft.com/library/windows/hardware/mt799885), [WSK_CLIENT_STREAM_DISPATCH](https://msdn.microsoft.com/library/windows/hardware/mt799886), and [WSK_PROVIDER_STREAM_DISPATCH](https://msdn.microsoft.com/library/windows/hardware/mt799887).
* [**Mobile Broadband (MB)**](https://msdn.microsoft.com/windows/hardware/drivers/network/mobile-broadband--mb--design-guide) - Updates include improved [LTE attach features](https://msdn.microsoft.com/windows/hardware/drivers/network/mb-lte-attach-operations), support for [Multi-SIM Operations](https://msdn.microsoft.com/windows/hardware/drivers/network/mb-multi-sim-operations), support for [provisioning contexts](https://msdn.microsoft.com/windows/hardware/drivers/network/mb-provisioned-context-operations) into the modem, support for the [Selective Absorption Rate platform](https://msdn.microsoft.com/windows/hardware/drivers/network/mb-sar-platform-support), and support for [network blacklisting](https://msdn.microsoft.com/windows/hardware/drivers/network/mb-network-blacklist-operations).
* [**Mobile Operator Scenarios (MOs)**](https://msdn.microsoft.com/windows/hardware/drivers/mobilebroadband/apn-database) - New database format called [COSA FAQ](https://msdn.microsoft.com/windows/hardware/drivers/mobilebroadband/cosa---faq), for MOs to provision Windows Desktop MB devices. See these topics for more updates:
    * [Planning your COSA/APN database submission](https://msdn.microsoft.com/windows/hardware/drivers/mobilebroadband/planning-your-apn-database-submission)
    * [Submitting the COSA/APN database update](https://msdn.microsoft.com/windows/hardware/drivers/mobilebroadband/submitting-the-apn-database-update)
    * [Testing your COSA/APN database submission](https://msdn.microsoft.com/windows/hardware/drivers/mobilebroadband/testing-your-apn-database-submission)

### POS

New topics:

* [Bluetooth barcode scanner UUIDs](https://msdn.microsoft.com/en-us/library/windows/hardware/mt781262)
* [BarcodeSymbologyDecodeLenthType enumeration](https://msdn.microsoft.com/en-us/library/windows/hardware/mt781217)
* [BarcodeSymbologyAttributesData structure](https://msdn.microsoft.com/en-us/library/windows/hardware/mt781216)

Updated:

* New Gs1DWCode symbology to the [BarcodeSymbology enumeration](https://msdn.microsoft.com/en-us/library/windows/hardware/dn757474)

### <a href="" id="usb-1703"></a>USB

Windows 10 version 1703 provides a new class extension (UcmTcpciCx.sys) that supports the Universal Serial Bus Type-C Port Controller Interface Specification. A USB Type-C connector driver does not need to maintain any internal PD/Type-C state. The complexity of managing the USB Type-C connector and USB Power Delivery (PD) state machines is handled by the system. You only need to write a client driver that communicates hardware events to the system through the class extension. For more information, see [USB Type-C Controller Interface driver class extensions reference](https://msdn.microsoft.com/library/windows/hardware/mt805826).

## <a href="" id="version-1607"></a>Changes in Windows 10, version 1607

[Back to Top](#top)

This section describes new features for driver development in Windows 10, version 1607.

### Audio

New [Windows Audio Architecture](https://msdn.microsoft.com/library/windows/hardware/mt631182) topic.

New audio structures and properties to better support the Cortana experience, including [**KSPROPERTY\_AUDIO\_MIC\_SENSITIVITY**](https://msdn.microsoft.com/library/windows/hardware/mt761741), [**KSPROPERTY\_AUDIO\_MIC\_SNR**](https://msdn.microsoft.com/library/windows/hardware/mt761742) and [**KSAUDIO\_PACKETSIZE\_CONSTRAINTS2**](https://msdn.microsoft.com/library/windows/hardware/mt761740).

New topic that describes the new [PKEY\_AudioEndpoint\_Default\_VolumeInDb](https://msdn.microsoft.com/library/windows/hardware/mt709031) registry key. This INF key provides the user a better experience when appropriate gain or attenuation is applied to the audio signal.

### <a href="" id="camera-1607"></a>Camera

New and updated topics to support Windows Hello and face authentication:

-   [Windows Hello camera driver bring up guide](https://msdn.microsoft.com/library/windows/hardware/mt742030)

-   [Extended camera controls](https://msdn.microsoft.com/library/windows/hardware/mt742029) (updated)

-   [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FACEAUTH\_MODE**](https://msdn.microsoft.com/library/windows/hardware/mt742028)


### <a href="" id="location-1607"></a>Location

New GNSS Breadcrumb DDIs:

-   [**GNSS\_BREADCRUMB\_LIST**](https://msdn.microsoft.com/library/windows/hardware/mt767989)

-   [**GNSS\_BREADCRUMB\_V1**](https://msdn.microsoft.com/library/windows/hardware/mt767990)

-   [**GNSS\_BREADCRUMBING\_ALERT\_DATA**](https://msdn.microsoft.com/library/windows/hardware/mt767987)

-   [**GNSS\_BREADCRUMBING\_PARAM**](https://msdn.microsoft.com/library/windows/hardware/mt767988)

-   [**IOCTL\_GNSS\_LISTEN\_BREADCRUMBING\_ALERT**](https://msdn.microsoft.com/library/windows/hardware/mt767991)

-   [**IOCTL\_GNSS\_POP\_BREADCRUMBS**](https://msdn.microsoft.com/library/windows/hardware/mt767992)

-   [**IOCTL\_GNSS\_START\_BREADCRUMBING**](https://msdn.microsoft.com/library/windows/hardware/mt767993)

-   [**IOCTL\_GNSS\_STOP\_BREADCRUMBING**](https://msdn.microsoft.com/library/windows/hardware/mt767994)

### <a href="" id="print-1607"></a>Print

[JSConstraintsDebug](https://msdn.microsoft.com/library/windows/hardware/mt740375) - a command-line tool that provides debugging support for JavaScript Constraints while developing a V4 printer driver.


### <a href="" id="wlan-1607"></a>WLAN

New and updated topics for WLAN Device Driver Interface (WDI) version 1.0.21. For details, see [WDI doc change history](https://msdn.microsoft.com/library/windows/hardware/mt691980).

## <a href="" id="version-1507"></a>Changes in Windows 10

[Back to Top](#top)

This section describes new features for driver development in Windows 10.

### Bluetooth

New [Microsoft-defined Bluetooth HCI extensions](https://msdn.microsoft.com/library/windows/hardware/dn917903) have been added.

### Buses and Ports

Driver programming interfaces and in-box drivers for Simple Peripheral Bus (SPB) such as I2C and SPI, and GPIO are part of OneCoreUAP-based editions of Windows. Those drivers will run on both Windows 10 for desktop editions and Windows 10 Mobile, as well as other Windows 10 versions.

### <a href="" id="camera-1507"></a>Camera

The camera driver DDIs have converged into a Universal Windows driver model, including new [camera DDIs](https://msdn.microsoft.com/library/windows/hardware/dn937081). Additional features include:

-   [Digital video stabilization](https://msdn.microsoft.com/library/windows/hardware/dn936754)
-   [Variable frame rate](https://msdn.microsoft.com/library/windows/hardware/dn917971)
-   [Face detection](https://msdn.microsoft.com/library/windows/hardware/dn917937)
-   [Video high dynamic range (HDR)](https://msdn.microsoft.com/library/windows/hardware/dn936752)
-   [Optical stabilization](https://msdn.microsoft.com/library/windows/hardware/dn917954)
-   [Scene analysis: photo HDR, flash no flash, ultra low light](https://msdn.microsoft.com/library/windows/hardware/dn917934)
-   [Capture stats: metadata framework/attributes, histograms](https://msdn.microsoft.com/library/windows/hardware/dn917945)
-   [Smooth zoom](https://msdn.microsoft.com/library/windows/hardware/dn936756)
-   [Hardware optimization hints](https://msdn.microsoft.com/library/windows/hardware/dn917956)
-   [Camera profiles](https://msdn.microsoft.com/library/windows/hardware/dn897239)

### Cellular

[Cellular architecture and implementation](https://msdn.microsoft.com/library/windows/hardware/dn927266) for Windows 10 has been updated.

### Display

The [display driver model](https://msdn.microsoft.com/library/windows/hardware/ff570595) from Windows 8.1 and Windows Phone have converged into a unified model for Windows 10.

A new memory model is implemented that gives each GPU a per-process virtual address space. Direct addressing of video memory is still supported by WDDMv2 for graphics hardware that requires it, but that is considered a legacy case. IHVs are expected to develop new hardware that supports virtual addressing. Significant changes have been made to the DDI to enable this new memory model.

### <a href="" id="human-interface-device"></a>Human Interface Device (HID)

The new Virtual HID Framework (VHF) eliminates the need for writing a kernel-mode transport minidriver. The framework comprises a Microsoft-provided static library (Vhfkm.lib) that exposes programming elements used by your driver. It also includes a Microsoft-provided in-box driver (Vhf.sys) that enumerates one or more child devices and proceeds to build a virtual [Human Interface Device](https://msdn.microsoft.com/windows/hardware/drivers/hid/) (HID) tree.

-   [Write a HID source driver by using Virtual HID Framework (VHF)](https://msdn.microsoft.com/library/windows/hardware/dn925056)
-   [Virtual HID Framework Callback Functions](https://msdn.microsoft.com/library/windows/hardware/dn925049)
-   [Virtual HID Framework Methods](https://msdn.microsoft.com/library/windows/hardware/dn925053)
-   [Virtual HID Framework Structures](https://msdn.microsoft.com/library/windows/hardware/dn925054)

### <a href="" id="location-1507"></a>Location

The Global Navigation Satellite System (GNSS) driver DDIs have converged to a [GNSS Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn917815) (UMDF 2.0).

### <a href="" id="near-field-communication"></a>Near Field Communication (NFC)

The [NFC DDIs](https://msdn.microsoft.com/library/windows/hardware/jj866056) have a new converged driver model to support mobile and desktop solutions.

[NFC Class Extension](https://msdn.microsoft.com/library/windows/hardware/dn905534): A new NFC class extension driver is available. The NFC class extension driver implements all of the Windows-defined DDIs to interact with the NFC controller, secure elements, and remote RF endpoints.

### <a href="" id="networking-1507"></a>Networking

The new [PacketDirect Provider Interface (PDPI)](https://msdn.microsoft.com/library/windows/hardware/dn931858) is available as an extension to the existing NDIS miniport driver model. The PDPI provides an I/O model that allows applications to manage their own buffers, poll processors, and directly manage sending and receiving packets over a miniport adapter. The combination of these capabilities allow the application to completely control its own contexts leading to a much higher packet-per-second (pps) ratio.

### <a href="" id="print-1507"></a>Print

The print driver is updated with v4 Print driver improvements and changes to support wireless printing from mobile devices, as well as the following:

-   [V4 Driver Manifest](https://msdn.microsoft.com/library/windows/hardware/jj218737)

    Provides information on changes to the v4 print driver manifest to support the PWG Raster rendering filter, including updated DriverConfig and DriverRender directives, and an updated example manifest.

-   [WS-Discovery Mobile Printing Support](https://msdn.microsoft.com/library/windows/hardware/dn897455)

    Describes the WS-Discovery requirements to enable mobile printing from Windows 10 Mobile devices to Windows 10 Mobile compatible printers.

-   [**IXpsRasterizationFactory2 interface**](https://msdn.microsoft.com/library/windows/hardware/dn937110)

    Supports printer content conversion from XPS to PWG Raster using the XPS Rasterization Service. PWG Raster supports non-square DPIs.

-   [**Print Pipeline Property Bag**](https://msdn.microsoft.com/library/windows/hardware/ff561066)

    Added the PrintDeviceCapabilities property to enable XPS rendering filters to retrieve the new PrintDeviceCapabilities XML files from the Print filter pipeline property bag.

-   [GetWithArgument Request and Response Schemas](https://msdn.microsoft.com/library/windows/hardware/dn936869)

    Provides support for mobile printing with a formal definition and example for the GetWithArgument request and response bidirectional communications schemas.

-   [**IBidiSpl::SendRecv method**](https://msdn.microsoft.com/library/windows/hardware/dd144988)

    Adds support for mobile printing with the GetWithArgument bidirectional schema value.

### Smart Card

In this release, there is a new class extension module, Wudfsmcclassext.dll, which handles complex driver operations. Smart card hardware-specific tasks are handled by your client driver. There are new programming interfaces that your client driver can use to send information about the card to the class extension so that it can process requests. Those driver programming interfaces are part of OneCoreUAP-based editions of Windows.

-   [Smart card client driver event callback functions](https://msdn.microsoft.com/library/windows/hardware/dn946583)
-   [Smart card client driver support methods](https://msdn.microsoft.com/library/windows/hardware/dn946584)

### Storage

The new storage firmware update, updated storage protocol pass through, and expanded storage query interfaces are available. The storage firmware update IOCTL interface allows partners to update their storage device firmware. The updated storage pass through IOCTL interface supports newer protocols including non-volatile memory express (NVMe). The expanded storage query interface allows applications to query protocol-dependent information.

### System-Supplied Driver Interfaces

The [GUID\_DEVICE\_RESET\_INTERFACE\_STANDARD](https://msdn.microsoft.com/library/windows/hardware/dn928420) interface defines a standard way for function drivers to attempt to reset and recover a malfunctioning device.

### USB

Here are the new features for USB in Windows 10. For more information, see [Windows 10: What's new for USB](https://msdn.microsoft.com/library/windows/hardware/dn957037).

-   Native support for USB Type-C as defined in the USB 3.1 specification. If you are building a system with USB Type-C connectors, you can use the in-box [USB Type-C Connector System Software Interface (UCSI) driver](https://msdn.microsoft.com/library/windows/hardware/mt710944) or [write a USB Type-C connector driver.](https://msdn.microsoft.com/library/windows/hardware/mt595924).
-   The dual role feature allows a mobile device, such as a phone, a phablet or a tablet, to designate itself as being a *device* or a *host*. See [USB Dual Role Driver Stack Architecture](https://msdn.microsoft.com/library/windows/hardware/dn957036) for more information.
-   Support for writing a driver for USB emulated devices by using the [Microsoft-provided USB device emulation class extension (UdeCx)](https://msdn.microsoft.com/library/windows/hardware/mt595925).
-   Support for writing a driver for a host controller that is not xHCI specification-compliant or a virtual host controller. To write such a driver, see [Developing Windows drivers for USB host controllers](https://msdn.microsoft.com/library/windows/hardware/mt187811).
-   Support writing function controller driver by using USB function class extension (UFX). See [Developing Windows drivers for USB function controllers](https://msdn.microsoft.com/library/windows/hardware/mt187810).

### <a href="" id="wlan-1507"></a>WLAN

WDI (WLAN Device Driver Interface) is a new [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672) that converges the WLAN drivers on Windows 10 for desktop editions and Windows 10 Mobile.

[Back to Top](#top) 





