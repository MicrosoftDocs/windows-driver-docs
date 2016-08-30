---
title: What's new in driver development
description: This section describes new features for driver development in Windows 10.
ms.assetid: 5502AAF9-2400-4338-A646-C746B29F9A44
---

# What's new in driver development


This section describes new features for driver development in Windows 10.

## Universal Windows drivers


Starting in Windows 10, you can write a single driver that works on OneCoreUAP-based editions of Windows, such as Windows 10 for desktop editions (Home, Pro, Enterprise, and Education), Windows 10 Mobile, and Windows 10 IoT Core (IoT Core). Such a driver is called a Universal Windows driver. A Universal Windows driver calls a subset of the interfaces that are available to a Windows driver. For information about how to build, install, deploy, and debug a Universal Windows driver for Windows 10, see [Getting Started with Universal Windows drivers](https://msdn.microsoft.com/windows-drivers/develop/getting_started_with_universal_drivers).

When you build a Universal Windows driver using Microsoft Visual Studio 2015, Visual Studio automatically checks if the APIs that your driver calls are valid for a Universal Windows driver. You can also use the ApiValidator.exe as a standalone tool to perform this task. The ApiValidator.exe tool is part of the Windows Driver Kit (WDK) for Windows 10. For info, see [Validating Universal Windows drivers](https://msdn.microsoft.com/windows-drivers/develop/validating_universal_drivers).

Universal Windows drivers also require a special kind of INF file called a *universal INF*. A universal INF can use a subset of the directives and sections available to a legacy INF file. To learn more, see [Using a Universal INF File](devinst.using_a_configurable_inf_file). To see which sections and directives apply, see [INF File Sections and Directives](devinst.inf_file_sections_and_directives).

When you're ready, use the [InfVerif](devtest.infverif) tool to test your driver's INF file. In addition to reporting INF syntax problems, the tool reports if the INF file will work with a Universal Windows driver.

You can also find information about which APIs you can call from a Universal Windows driver. This information is located in the Requirements block at the bottom of MSDN reference pages.

For example, you'll see a listing similar to this one that tells you if a given DDI is **Universal.**

![target platform set to universal in requirements block](images/targetplatform.png)

For more info, see [Target platform on MSDN driver reference pages](https://msdn.microsoft.com/windows-drivers/develop/windows_10_editions_for_universal_drivers).

## Bluetooth


New [Microsoft-defined Bluetooth HCI extensions](bltooth.bluetooth_microsoft-defined_hci_extensions) have been added.

## Buses and Ports


Driver programming interfaces and in-box drivers for Simple Peripheral Bus (SPB) such as I2C and SPI, and GPIO are part of OneCoreUAP-based editions of Windows. Those drivers will run on both Windows 10 for desktop editions and Windows 10 Mobile, as well as other Windows 10 versions.

## Camera


The camera driver DDIs have converged into a Universal Windows driver model, including new [camera DDIs](stream.windows_10_technical_preview_camera_drivers_reference). Additional features include:

-   [Digital video stabilization](stream.ksproperty_cameracontrol_extended_videostabilization)
-   [Variable frame rate](stream.ksproperty_cameracontrol_extended_vfr)
-   [Face detection](stream.ksproperty_cameracontrol_extended_facedetection)
-   [Video high dynamic range (HDR)](stream.ksproperty_cameracontrol_extended_videohdr)
-   [Optical stabilization](stream.ksproperty_cameracontrol_extended_ois)
-   [Scene analysis: photo HDR, flash no flash, ultra low light](stream.ksproperty_cameracontrol_extended_advancedphoto)
-   [Capture stats: metadata framework/attributes, histograms](stream.ksproperty_cameracontrol_extended_histogram)
-   [Smooth zoom](stream.ksproperty_cameracontrol_extended_zoom)
-   [Hardware optimization hints](stream.ksproperty_cameracontrol_extended_optimizationhint_)
-   [Camera profiles](stream.camera_driver_functions)

## Cellular


[Cellular architecture and implementation](netvista.cellular_architecture_and_driver_model) for Windows 10 has been updated.

## Display


The [display driver model](display.windows_vista_display_driver_model_reference) from Windows 8.1 and Windows Phone have converged into a unified model for Windows 10.

A new memory model is implemented that gives each GPU a per-process virtual address space. Direct addressing of video memory is still supported by WDDMv2 for graphics hardware that requires it, but that is considered a legacy case. IHVs are expected to develop new hardware that supports virtual addressing. Significant changes have been made to the DDI to enable this new memory model.

## Debugging Tools for Windows


The following new commands are available in for the Windows debugger:

-   [**dx (Display NatVis Expression)**](debugger.dx__display_visualizer_variables_) - A new debugger command which displays object information using the NatVis extension model.
-   [**.settings**](debugger._settings__set_debug_settings_) - A new command that sets, modifies, displays, loads and saves settings in the Debugger.Settings namespace.

## Driver Verifier


Driver verifier includes new driver validation rules for the following technologies:

-   New [Rules for Audio Drivers](devtest.rules_for_audio_drivers)
-   New [Rules for AVStream Drivers](devtest.rules_for_avstream_drivers)
-   Four new [Rules for KMDF Drivers](devtest.sdv_rules_for_kmdf_drivers)
-   Three new [Rules for NDIS Drivers](devtest.sdv_rules_for_ndis_drivers)

## Human Interface Device (HID)


The new Virtual HID Framework (VHF) eliminates the need for writing a kernel-mode transport minidriver. The framework comprises a Microsoft-provided static library (Vhfkm.lib) that exposes programming elements used by your driver. It also includes a Microsoft-provided in-box driver (Vhf.sys) that enumerates one or more child devices and proceeds to build a virtual [Human Interface Device](hid.portal) (HID) tree.

-   [Write a HID source driver by using Virtual HID Framework (VHF)](hid.virtual_hid_framework__vhf_)
-   [Virtual HID Framework Callback Functions](hid.virtual_hid_framework_callback_functions)
-   [Virtual HID Framework Methods](hid.virtual_hid_framework_methods)
-   [Virtual HID Framework Structures](hid.virtual_hid_framework_structures)

## Location


The Global Navigation Satellite System (GNSS) driver DDIs have converged to a [GNSS Universal Windows driver model](sensors.universal_gnss_driver_for_windows_10) (UMDF 2.0).

## Near Field Communication (NFC)


The [NFC DDIs](nfpdrivers.design_guide) have a new converged driver model to support mobile and desktop solutions.

[NFC Class Extension](nfpdrivers.nfc_class_extension_): A new NFC class extension driver is available. The NFC class extension driver implements all of the Windows-defined DDIs to interact with the NFC controller, secure elements, and remote RF endpoints.

## <a href="" id="networking-"></a>Networking


The new [PacketDirect Provider Interface (PDPI)](netvista.packet_direct_reference) is available as an extension to the existing NDIS miniport driver model. The PDPI provides an I/O model that allows applications to manage their own buffers, poll processors, and directly manage sending and receiving packets over a miniport adapter. The combination of these capabilities allow the application to completely control its own contexts leading to a much higher packet-per-second (pps) ratio.

## Power Management Framework (PoFx)


The power management framework (PoFx) enables a driver to define one or more sets of individually adjustable performance states for individual components within a device. The driver can use performance states to throttle a component's workload to provide just enough performance for its current needs. For more information, see [Component-Level Performance State Management](kernel.component-level_performance_management).

## Print


The print driver is updated with v4 Print driver improvements and changes to support wireless printing from mobile devices, as well as the following:

-   [V4 Driver Manifest](print.v4_driver_manifest)

    Provides information on changes to the v4 print driver manifest to support the PWG Raster rendering filter, including updated DriverConfig and DriverRender directives, and an updated example manifest.

-   [WS-Discovery Mobile Printing Support](print.ws-discovery_mobile_printing_support)

    Describes the WS-Discovery requirements to enable mobile printing from Windows 10 Mobile devices to Windows 10 Mobile compatible printers.

-   [**IXpsRasterizationFactory2 interface**](print.ixpsrasterizationfactory2)

    Supports printer content conversion from XPS to PWG Raster using the XPS Rasterization Service. PWG Raster supports non-square DPIs.

-   [**Print Pipeline Property Bag**](print.print_pipeline_property_bag)

    Added the PrintDeviceCapabilities property to enable XPS rendering filters to retrieve the new PrintDeviceCapabilities XML files from the Print filter pipeline property bag.

-   [GetWithArgument Request and Response Schemas](print.getwithargument_request_and_response_schemas)

    Provides support for mobile printing with a formal definition and example for the GetWithArgument request and response bidirectional communications schemas.

-   [**IBidiSpl::SendRecv method**](print.ibidispl_ibidispl__sendrecv)

    Adds support for mobile printing with the GetWithArgument bidirectional schema value.

## Smart Card


In this release, there is a new class extension module, Wudfsmcclassext.dll, which handles complex driver operations. Smart card hardware-specific tasks are handled by your client driver. There are new programming interfaces that your client driver can use to send information about the card to the class extension so that it can process requests. Those driver programming interfaces are part of OneCoreUAP-based editions of Windows.

-   [Smart card client driver event callback functions](smartcrd.smart_card_client_driver_callback_functions)
-   [Smart card client driver support methods](smartcrd.smart_card_client_driver_functions)

## Storage


The new storage firmware update, updated storage protocol pass through, and expanded storage query interfaces are available. The storage firmware update IOCTL interface allows partners to update their storage device firmware. The updated storage pass through IOCTL interface supports newer protocols including non-volatile memory express (NVMe). The expanded storage query interface allows applications to query protocol-dependent information.

## System-Supplied Driver Interfaces


The [GUID\_DEVICE\_RESET\_INTERFACE\_STANDARD](kernel.guid_device_reset_interface_standard) interface defines a standard way for function drivers to attempt to reset and recover a malfunctioning device.

## USB


USB Dual Role controllers are now supported in Windows 10. The dual role feature allows a mobile device, such as a phone, a phablet or a tablet, to designate itself as being a *device* or a *host*. See [USB Dual Role Driver Stack Architecture](buses.usb_dual_role_driver_stack_architecture) for more information.

## Windows compatible hardware development boards


Windows is now supported on more affordable boards such as the Raspberry Pi 2. Become a part of our early adopter community and load Windows on that board. For more information, see [Windows compatible hardware development boards](wdkgetstart.windows_compatible_hardware_development_boards).

## WLAN


WDI (WLAN Device Driver Interface) is a new [WLAN Universal Windows driver model](netvista.wifi_universal_driver_model) that converges the WLAN drivers on Windows 10 for desktop editions and Windows 10 Mobile.

## WPP Software Tracing


[WPP Software Tracing](devtest.wpp_software_tracing) introduces a new feature: Inflight Trace Recorder. If the driver enables WPP tracing and WPP Recorder, trace logging is turned on automatically and you can view easily messages without starting or stopping trace sessions. To get better control over the log bugger, WPP Recorder allows a KMDF driver to create and manage custom buffers.

-   [WPP Recorder for logging traces](devtest.using_wpp_recorder)
-   [**WppRecorderLogGetDefault**](devtest.wpprecorderloggetdefault)
-   [**WppRecorderLogCreate**](devtest.wpprecorderlogcreate) (KMDF only)
-   [**WppRecorderDumpLiveDriverData**](devtest.wpprecorderdumplivedriverdata)

 
