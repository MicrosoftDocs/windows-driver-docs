---
title: What's new in driver development
description: This section describes new features for driver development in Windows 10.
ms.assetid: 5502AAF9-2400-4338-A646-C746B29F9A44
---

# What's new in driver development


This section describes new features for driver development in Windows 10.

## What's new in driver development for Windows 10, version 1607


This section describes new features for driver development in Windows 10, version 1607.

### Open publishing

We're making the docs more community-driven. On many pages of the Windows driver documentation, you can suggest changes directly. Look for the **Contribute** button in the upper right corner of a page. It looks like this:

![screenshot of contribute button](contribute-button.png)

When you click **Contribute**, you'll arrive at the Markdown source file for that topic in a [GitHub repository](https://github.com/Microsoft/windows-driver-docs). You can click **Edit** and suggest changes right here.

For more details, see [CONTRIBUTING.md](https://github.com/Microsoft/windows-driver-docs/blob/staging/CONTRIBUTING.md) in the repo. And thanks for taking the time to improve the docs!

### Audio

New [Windows Audio Architecture](https://msdn.microsoft.com/library/windows/hardware/mt631182) topic.

New audio structures and properties to better support the Cortana experience, including [**KSPROPERTY\_AUDIO\_MIC\_SENSITIVITY**](https://msdn.microsoft.com/library/windows/hardware/mt761741), [**KSPROPERTY\_AUDIO\_MIC\_SNR**](https://msdn.microsoft.com/library/windows/hardware/mt761742) and [**KSAUDIO\_PACKETSIZE\_CONSTRAINTS2**](https://msdn.microsoft.com/library/windows/hardware/mt761740).

New topic that describes the new [PKEY\_AudioEndpoint\_Default\_VolumeInDb](https://msdn.microsoft.com/library/windows/hardware/mt709031) registry key. This INF key provides the user a better experience when appropriate gain or attenuation is applied to the audio signal.

### Camera

New and updated topics to support Windows Hello and face authentication:

-   [Windows Hello camera driver bring up guide](https://msdn.microsoft.com/library/windows/hardware/mt742030)

-   [Extended camera controls](https://msdn.microsoft.com/library/windows/hardware/mt742029) (updated)

-   [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FACEAUTH\_MODE**](https://msdn.microsoft.com/library/windows/hardware/mt742028)

### Debugger

New topic about [Debugging a UWP app using WinDbg](https://msdn.microsoft.com/library/windows/hardware/mt757092).

Updates to the 30 most-viewed developer bug check topics in [Bug Check Code Reference](https://msdn.microsoft.com/library/windows/hardware/hh994433).

### Location

New GNSS Breadcrumb DDIs:

-   [**GNSS\_BREADCRUMB\_LIST**](https://msdn.microsoft.com/library/windows/hardware/mt767989)

-   [**GNSS\_BREADCRUMB\_V1**](https://msdn.microsoft.com/library/windows/hardware/mt767990)

-   [**GNSS\_BREADCRUMBING\_ALERT\_DATA**](https://msdn.microsoft.com/library/windows/hardware/mt767987)

-   [**GNSS\_BREADCRUMBING\_PARAM**](https://msdn.microsoft.com/library/windows/hardware/mt767988)

-   [**IOCTL\_GNSS\_LISTEN\_BREADCRUMBING\_ALERT**](https://msdn.microsoft.com/library/windows/hardware/mt767991)

-   [**IOCTL\_GNSS\_POP\_BREADCRUMBS**](https://msdn.microsoft.com/library/windows/hardware/mt767992)

-   [**IOCTL\_GNSS\_START\_BREADCRUMBING**](https://msdn.microsoft.com/library/windows/hardware/mt767993)

-   [**IOCTL\_GNSS\_STOP\_BREADCRUMBING**](https://msdn.microsoft.com/library/windows/hardware/mt767994)

### Print

[JSConstraintsDebug](https://msdn.microsoft.com/library/windows/hardware/mt740375) - a command-line tool that provides debugging support for JavaScript Constraints while developing a V4 printer driver.

### Windows Driver Frameworks (WDF)

Windows 10, version 1607 includes Kernel-Mode Driver Framework (KMDF) version 1.19 and User-Mode Driver Framework (UMDF) version 2.19.

For info on what's included in these framework versions, see [What's New for WDF Drivers in Windows 10](https://msdn.microsoft.com/windows/hardware/drivers/wdf/what-s-new-for-wdf-drivers).

### WLAN

New and updated topics for WLAN Device Driver Interface (WDI) version 1.0.21. For details, see [WDI doc change history](https://msdn.microsoft.com/library/windows/hardware/mt691980).

## What's new in driver development for Windows 10


This section describes new features for driver development in Windows 10

### Universal Windows drivers

Starting in Windows 10, you can write a single driver that works on OneCoreUAP-based editions of Windows, such as Windows 10 for desktop editions (Home, Pro, Enterprise, and Education), Windows 10 Mobile, and Windows 10 IoT Core (IoT Core). Such a driver is called a Universal Windows driver. A Universal Windows driver calls a subset of the interfaces that are available to a Windows driver. For information about how to build, install, deploy, and debug a Universal Windows driver for Windows 10, see [Getting Started with Universal Windows drivers](https://msdn.microsoft.com/windows-drivers/develop/getting_started_with_universal_drivers).

When you build a Universal Windows driver using Microsoft Visual Studio 2015, Visual Studio automatically checks if the APIs that your driver calls are valid for a Universal Windows driver. You can also use the ApiValidator.exe as a standalone tool to perform this task. The ApiValidator.exe tool is part of the Windows Driver Kit (WDK) for Windows 10. For info, see [Validating Universal Windows drivers](https://msdn.microsoft.com/windows-drivers/develop/validating_universal_drivers).

Universal Windows drivers also require a special kind of INF file called a *universal INF*. A universal INF can use a subset of the directives and sections available to a legacy INF file. To learn more, see [Using a Universal INF File](https://msdn.microsoft.com/library/windows/hardware/dn941087). To see which sections and directives apply, see [INF File Sections and Directives](https://msdn.microsoft.com/library/windows/hardware/ff547433).

When you're ready, use the [InfVerif](https://msdn.microsoft.com/library/windows/hardware/dn929319) tool to test your driver's INF file. In addition to reporting INF syntax problems, the tool reports if the INF file will work with a Universal Windows driver.

You can also find information about which APIs you can call from a Universal Windows driver. This information is located in the Requirements block at the bottom of MSDN reference pages.

For example, you'll see a listing similar to this one that tells you if a given DDI is **Universal.**

![target platform set to universal in requirements block](targetplatform.png)

For more info, see [Target platform on MSDN driver reference pages](https://msdn.microsoft.com/windows-drivers/develop/windows_10_editions_for_universal_drivers).

### Bluetooth

New [Microsoft-defined Bluetooth HCI extensions](https://msdn.microsoft.com/library/windows/hardware/dn917903) have been added.

### Buses and Ports

Driver programming interfaces and in-box drivers for Simple Peripheral Bus (SPB) such as I2C and SPI, and GPIO are part of OneCoreUAP-based editions of Windows. Those drivers will run on both Windows 10 for desktop editions and Windows 10 Mobile, as well as other Windows 10 versions.

### Camera

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

### Debugging Tools for Windows

The following new commands are available in for the Windows debugger:

-   [**dx (Display NatVis Expression)**](https://msdn.microsoft.com/library/windows/hardware/dn936815) - A new debugger command which displays object information using the NatVis extension model.
-   [**.settings**](https://msdn.microsoft.com/library/windows/hardware/dn925473) - A new command that sets, modifies, displays, loads and saves settings in the Debugger.Settings namespace.

### Driver Verifier

Driver verifier includes new driver validation rules for the following technologies:

-   New [Rules for Audio Drivers](https://msdn.microsoft.com/library/windows/hardware/dn906757)
-   New [Rules for AVStream Drivers](https://msdn.microsoft.com/library/windows/hardware/dn906758)
-   Four new [Rules for KMDF Drivers](https://msdn.microsoft.com/library/windows/hardware/ff551709)
-   Three new [Rules for NDIS Drivers](https://msdn.microsoft.com/library/windows/hardware/ff551713)

### Human Interface Device (HID)

The new Virtual HID Framework (VHF) eliminates the need for writing a kernel-mode transport minidriver. The framework comprises a Microsoft-provided static library (Vhfkm.lib) that exposes programming elements used by your driver. It also includes a Microsoft-provided in-box driver (Vhf.sys) that enumerates one or more child devices and proceeds to build a virtual [Human Interface Device](https://msdn.microsoft.com/windows/hardware/drivers/hid/) (HID) tree.

-   [Write a HID source driver by using Virtual HID Framework (VHF)](https://msdn.microsoft.com/library/windows/hardware/dn925056)
-   [Virtual HID Framework Callback Functions](https://msdn.microsoft.com/library/windows/hardware/dn925049)
-   [Virtual HID Framework Methods](https://msdn.microsoft.com/library/windows/hardware/dn925053)
-   [Virtual HID Framework Structures](https://msdn.microsoft.com/library/windows/hardware/dn925054)

### Location

The Global Navigation Satellite System (GNSS) driver DDIs have converged to a [GNSS Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn917815) (UMDF 2.0).

### Near Field Communication (NFC)

The [NFC DDIs](https://msdn.microsoft.com/library/windows/hardware/jj866056) have a new converged driver model to support mobile and desktop solutions.

[NFC Class Extension](https://msdn.microsoft.com/library/windows/hardware/dn905534): A new NFC class extension driver is available. The NFC class extension driver implements all of the Windows-defined DDIs to interact with the NFC controller, secure elements, and remote RF endpoints.

### <a href="" id="networking-"></a>Networking

The new [PacketDirect Provider Interface (PDPI)](https://msdn.microsoft.com/library/windows/hardware/dn931858) is available as an extension to the existing NDIS miniport driver model. The PDPI provides an I/O model that allows applications to manage their own buffers, poll processors, and directly manage sending and receiving packets over a miniport adapter. The combination of these capabilities allow the application to completely control its own contexts leading to a much higher packet-per-second (pps) ratio.

### Power Management Framework (PoFx)

The power management framework (PoFx) enables a driver to define one or more sets of individually adjustable performance states for individual components within a device. The driver can use performance states to throttle a component's workload to provide just enough performance for its current needs. For more information, see [Component-Level Performance State Management](https://msdn.microsoft.com/library/windows/hardware/dn939352).

### Print

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

### Windows compatible hardware development boards

Windows is now supported on more affordable boards such as the Raspberry Pi 2. Become a part of our early adopter community and load Windows on that board. For more information, see [Windows compatible hardware development boards](https://msdn.microsoft.com/library/windows/hardware/dn914597).

### WLAN

WDI (WLAN Device Driver Interface) is a new [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672) that converges the WLAN drivers on Windows 10 for desktop editions and Windows 10 Mobile.

### WPP Software Tracing

[WPP Software Tracing](https://msdn.microsoft.com/library/windows/hardware/ff556204) introduces a new feature: Inflight Trace Recorder. If the driver enables WPP tracing and WPP Recorder, trace logging is turned on automatically and you can easily view messages without starting or stopping trace sessions. For more fine tuned control over the log, WPP Recorder allows a KMDF driver to create and manage custom buffers.

-   [WPP Recorder for logging traces](https://msdn.microsoft.com/library/windows/hardware/dn914610)
-   [**WppRecorderLogGetDefault**](https://msdn.microsoft.com/library/windows/hardware/dn895240)
-   [**WppRecorderLogCreate**](https://msdn.microsoft.com/library/windows/hardware/dn914615) (KMDF only)
-   [**WppRecorderDumpLiveDriverData**](https://msdn.microsoft.com/library/windows/hardware/dn914612)

 





