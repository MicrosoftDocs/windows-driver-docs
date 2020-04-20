---
title: What's new in driver development
description: This section describes new features for driver development in Windows 10.
ms.assetid: 5502AAF9-2400-4338-A646-C746B29F9A44
ms.date: 04/28/2020
ms.localizationpriority: medium
ms.custom: 19H1
---

# <a name="top"></a>What's new in driver development

This section provides information about the new features and updates to Windows driver development in Windows 10.

The following is a list of new feature highlights for driver development in Windows 10.

* [Windows 10, version 1903 WDK supports Visual Studio 2019](#wdk-supports-visual-studio-2019)
* [Windows Hardware Dev Center dashboard](#windows-hardware-dev-center-dashboard)
* [Debugging Tools for Windows](#debugging-tools-for-windows)
* [Device and Driver Installation](#device-and-driver-installation)
* [Windows Driver Frameworks](#windows-driver-frameworks-wdf)
* [Windows Compatible hardware development boards](#windows-compatible-hardware-development-boards)
* [Power Management Framework](#power-management-framework)
* [System-Supplied Driver Interfaces](#system-supplied-driver-interfaces)
* [WPP Software Tracing](#wpp-software-tracing)

The following table shows the feature updates in Windows 10, by driver technology and version.

| Driver  |[1903](#whats-new-in-windows-10-version-1903-latest)| [1809](#whats-new-in-windows-10-version-1809) |   [1803](#whats-new-in-windows-10-version-1803)    | [1709](#whats-new-in-windows-10-version-1709) |  [1703](#whats-new-in-windows-10-version-1703)  | [1607](#whats-new-in-windows-10-version-1607) |  [1507](#whats-new-in-windows-10-version-1507)  |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Audio  |  [![details](checkmark.png)](#audio-1903) |      [![details](checkmark.png)](#audio-1809)       |      [![details](checkmark.png)](#audio-1803)      |         [![details](checkmark.png)](#audio-1709)          |      [![details](checkmark.png)](#audio-1703)      |      [![details](checkmark.png)](#audio-1607)      |                   ![not available](minus.png)                   |
|               ACPI         |   ![not available](minus.png)    |             ![not available](minus.png)              |      [![details](checkmark.png)](#acpi-1803)       |          [![details](checkmark.png)](#acpi-1709)          |            ![not available](minus.png)             |          ![not available](minus.png)          |                   ![not available](minus.png)                   |
|             Biometric    |     ![not available](minus.png)   |             ![not available](minus.png)              |            ![not available](minus.png)             |       [![details](checkmark.png)](#biometric-1709)        |            ![not available](minus.png)             |          ![not available](minus.png)          |                   ![not available](minus.png)                   |
|             Bluetooth     |   ![not available](minus.png)     |     [![details](checkmark.png)](#bluetooth-1809)     |    [![details](checkmark.png)](#bluetooth-1803)    |                ![not available](minus.png)                |    [![details](checkmark.png)](#bluetooth-1703)    |          ![not available](minus.png)          |             [![details](checkmark.png)](#bluetooth-1507)             |
|          Buses and Ports          |   ![not available](minus.png)   |       ![not available](minus.png)              |            ![not available](minus.png)             |                ![not available](minus.png)                |            ![not available](minus.png)             |          ![not available](minus.png)          |          [![details](checkmark.png)](#buses-and-ports)          |
|              Camera       |    [![details](checkmark.png)](#camera-1903)    |             ![not available](minus.png)              |     [![details](checkmark.png)](#camera-1803)      |                ![not available](minus.png)                |     [![details](checkmark.png)](#camera-1703)      |   [![details](checkmark.png)](#camera-1607)   |            [![details](checkmark.png)](#camera-1507)            |
|             Cellular              |   ![not available](minus.png)   |       ![not available](minus.png)              |            ![not available](minus.png)             |                ![not available](minus.png)                |            ![not available](minus.png)             |          ![not available](minus.png)          |             [![details](checkmark.png)](#cellular)              |
|              Display          |  [![details](checkmark.png)](#display-1903) |      [![details](checkmark.png)](#display-1809)      |     [![details](checkmark.png)](#display-1803)     |        [![details](checkmark.png)](#display-1709)         |            ![not available](minus.png)             |          ![not available](minus.png)          |              [![details](checkmark.png)](#display-1507)              |
|          Driver security      |  ![not available](minus.png)  |             ![not available](minus.png)              |    [![details](checkmark.png)](#security-1803)     |                ![not available](minus.png)                |            ![not available](minus.png)             |          ![not available](minus.png)          |              ![not available](minus.png)              |
|      Hardware notifications    | ![not available](minus.png)  |             ![not available](minus.png)              |            ![not available](minus.png)             | [![details](checkmark.png)](#hardware-notifications-1709) |            ![not available](minus.png)             |          ![not available](minus.png)          |                   ![not available](minus.png)                   |
|   Human Interface Device (HID)    |    ![not available](minus.png)    |     ![not available](minus.png)              |            ![not available](minus.png)             |                ![not available](minus.png)                |            ![not available](minus.png)             |          ![not available](minus.png)          |      [![details](checkmark.png)](#human-interface-device)       |
|              Kernel          |   ![not available](minus.png)  |      [![details](checkmark.png)](#kernel-1809)       |     [![details](checkmark.png)](#kernel-1803)      |         [![details](checkmark.png)](#kernel-1709)         |     [![details](checkmark.png)](#kernel-1703)      |          ![not available](minus.png)          |                   ![not available](minus.png)                   |
|             Location       |   ![not available](minus.png)    |             ![not available](minus.png)              |            ![not available](minus.png)             |                ![not available](minus.png)                |            ![not available](minus.png)             |  [![details](checkmark.png)](#location-1607)  |           [![details](checkmark.png)](#location-1507)           |
|         Mobile broadband    |    [![details](checkmark.png)](#mobilebroadband-1903)  |  [![details](checkmark.png)](#mobilebroadband-1809)  | [![details](checkmark.png)](#mobilebroadband-1803) |    [![details](checkmark.png)](#mobilebroadband-1709)     | [![details](checkmark.png)](#mobilebroadband-1703) |          ![not available](minus.png)          |                   ![not available](minus.png)                   |
|     Near Field Communication      |    ![not available](minus.png)     |    ![not available](minus.png)              |            ![not available](minus.png)             |                ![not available](minus.png)                |            ![not available](minus.png)             |          ![not available](minus.png)          |     [![details](checkmark.png)](#near-field-communication)      |
|            Networking     |    [![details](checkmark.png)](#networking-1903)    |    [![details](checkmark.png)](#networking-1809)     |   [![details](checkmark.png)](#networking-1803)    |       [![details](checkmark.png)](#networking-1709)       |   [![details](checkmark.png)](#networking-1703)    |          ![not available](minus.png)          |          [![details](checkmark.png)](#networking-1507)          |
|                POS          |   ![not available](minus.png)   |             ![not available](minus.png)              |            ![not available](minus.png)             |                ![not available](minus.png)                |       [![details](checkmark.png)](#pos-1703)       |          ![not available](minus.png)          |                   ![not available](minus.png)                   |
|                PCI        |    ![not available](minus.png)    |             ![not available](minus.png)              |       [![details](checkmark.png)](#pci-1803)       |          [![details](checkmark.png)](#pci-1709)           |            ![not available](minus.png)             |          ![not available](minus.png)          |                   ![not available](minus.png)                   |
|               Print     |      [![details](checkmark.png)](#print-1903)    |             ![not available](minus.png)              |            ![not available](minus.png)             |                ![not available](minus.png)                |            ![not available](minus.png)             |   [![details](checkmark.png)](#print-1607)    |            [![details](checkmark.png)](#print-1507)             |
|      Pulse Width Modulation       |   ![not available](minus.png)  |        ![not available](minus.png)              |            ![not available](minus.png)             |          [![details](checkmark.png)](#pwm-1709)           |            ![not available](minus.png)             |          ![not available](minus.png)          |                   ![not available](minus.png)                   |
|              Sensors        |  [![details](checkmark.png)](#sensors-1903)    |      [![details](checkmark.png)](#sensors-1809)      |     [![details](checkmark.png)](#sensors-1803)     |                ![not available](minus.png)                |            ![not available](minus.png)             |          ![not available](minus.png)          |                   ![not available](minus.png)                   |
|            Smart Card     |    ![not available](minus.png)    |             ![not available](minus.png)              |            ![not available](minus.png)             |                ![not available](minus.png)                |            ![not available](minus.png)             |          ![not available](minus.png)          |            [![details](checkmark.png)](#smart-card)             |
|              Storage         |    [![details](checkmark.png)](#storage-1903)  |             ![not available](minus.png)              |            ![not available](minus.png)             |        [![details](checkmark.png)](#storage-1709)         |            ![not available](minus.png)             |          ![not available](minus.png)          |              [![details](checkmark.png)](#storage-1507)              |
| System-Supplied Driver Interfaces |   ![not available](minus.png)   |      ![not available](minus.png)              |            ![not available](minus.png)             |                ![not available](minus.png)                |            ![not available](minus.png)             |          ![not available](minus.png)          | [![details](checkmark.png)](#system-supplied-driver-interfaces) |
|                USB                |  ![not available](minus.png) |     [![details](checkmark.png)](#usb-1809)        |       [![details](checkmark.png)](#usb-1803)       |          [![details](checkmark.png)](#usb-1709)           |       [![details](checkmark.png)](#usb-1703)       |          ![not available](minus.png)          |                [![details](checkmark.png)](#usb-1507)                |
|               WI-FI           |  [![details](checkmark.png)](#wifi-1903)  |       [![details](checkmark.png)](#wifi-1809)        |      [![details](checkmark.png)](#wifi-1803)       |                ![not available](minus.png)                |            ![not available](minus.png)             |          ![not available](minus.png)          |                   ![not available](minus.png)                   |
|               WLAN         |    ![not available](minus.png)   |             ![not available](minus.png)              |            ![not available](minus.png)             |                ![not available](minus.png)                |            ![not available](minus.png)             |    [![details](checkmark.png)](#wlan-1607)    |             [![details](checkmark.png)](#wlan-1507)             |

## What's new in driver development for Windows 10

[Back to Top](#top)

This section provides highlights of new features for driver development in Windows 10.

### WDK supports Visual Studio 2019

Starting in Windows 10, version 1809, the Windows Driver Kit (WDK) supports Visual Studio 2019. This release of the WDK is not compatible with Visual Studio 2017.
Developers can continue working with Visual Studio 2017 by using releases 1709 thru 1809 of the WDK,  found in [Other WDK downloads](https://docs.microsoft.com/windows-hardware/drivers/other-wdk-downloads). To learn about what is new with Visual Studio 2019, see the [Visual Studio 2019 version 16.5 Release Notes](https://docs.microsoft.com/visualstudio/releases/2019/release-notes#whats-new-in-visual-studio-2019).

The following are a few of the notable changes in Visual Studio 2019 that Windows driver developers will see.

#### WDK GUI Driver Menu moved

In Visual Studio 2019 the WDK Driver menu has been moved to live under the Extension menu as seen below.

![screenshot of Visual Studio 2019 menu](images/vs-2019-driver-menu.png)

The WDK Driver menu in Visual Studio 2017 is located in the top menu options as seen below.

![screenshot of Visual Studio 2017 menu](images/vs-2017-menu.png)

#### Driver Templates discoverability

In Visual Studio 2019 the WDK Driver templates will be discoverable under Project Type, Drivers. The Driver Project Type will appear in the first official update release of Visual Studio 2019. Until then the Driver templates can be discovered by searching for them in the search menu.

![screenshot of Visual Studio 2019 driver templates](images/vs-2019-driver-template.png)

The WDK Driver templates were previously found in Visual Studio 2017 under New Projects> Visual C++> Windows Driver as seen below.

![screenshot of Visual Studio 2017 driver templates](images/vs-2017-driver-template.png)




### Windows compatible hardware development boards

Windows is now supported on more affordable boards such as the Raspberry Pi 2. Become a part of our early adopter community and load Windows on that board. For more information, see [Windows compatible hardware development boards](https://docs.microsoft.com/windows-hardware/drivers/gettingstarted/windows-compatible-hardware-development-boards).



## What's new in Windows 10, version 2004 (latest)

This section describes new features and updates for driver development in Windows 10, version 2004 (Windows 10 May 2020 Update).

[Back to Top](#top)

### Windows Drivers

Windows 10, version 2004 is a transition release for universal drivers. In this release, universal drivers still exist, but are being replaced by Windows Drivers. A Windows Driver is a universal driver with a few additional requirements.

Windows Drivers are distinguished from Windows Desktop Drivers. While Windows Drivers run on Windows 10X and Windows 10 Desktop editions,  Windows Desktop Drivers run only on Windows 10 Desktop editions.

No changes are required to universal drivers for the version 2004 release, but documentation is available now so that you can plan ahead for upcoming changes.

For information about how to build, install, deploy, and debug a Windows Driver, see [Getting Started with Universal Windows drivers](https://docs.microsoft.com/windows-hardware/drivers/develop/getting-started-with-windows-drivers).

## What's new in Windows 10, version 1903

This section describes new features and updates for driver development in Windows 10, version 1903 (Windows 10 April 2019 Update).

[Back to Top](#top)

### <a name="audio-1903"></a>Audio

The following is a list of new and updated Audio features in Windows 10, version 1903:

* New reference topics on the Audio OEM Adapter used for Voice Activation in the new [eventdetectoroemadapter.h](https://docs.microsoft.com/windows-hardware/drivers/ddi/eventdetectoroemadapter/) header.
* New Far Field Audio information: 
    * [PKEY_Devices_AudioDevice_Microphone_IsFarField](https://docs.microsoft.com/windows-hardware/drivers/audio/pkey-devices-audiodevice-microphone-isfarfield)
    * [KSPROPSETID_InterleavedAudio](https://docs.microsoft.com/windows-hardware/drivers/audio/kspropsetid-interleavedaudio)
    * [KSPROPERTY_INTERLEAVEDAUDIO_FORMATINFORMATION](https://review.docs.microsoft.com/windows-hardware/drivers/audio/ksproperty-interleavedaudio-formatinformation)
    
* New jack description information in [USB Audio 2.0 Drivers](https://docs.microsoft.com/windows-hardware/drivers/audio/usb-2-0-audio-drivers).

### <a name="camera-1903"></a>Camera

New Camera driver documentation and features added in Windows 10, version 1903 include:

* New [IR Torch](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-extended-irtorchmode) extended property control to set an IR camera's infrared torch power level and duty cycle.
* New [KSCATEGORY_NETWORK_CAMERA](https://docs.microsoft.com/windows-hardware/drivers/install/kscategory-network-camera) device.
* New and updated [USB Video Class (UVC) 1.5 extension](https://docs.microsoft.com/windows-hardware/drivers/stream/uvc-extensions-1-5) documentation for the following control selectors:
  * MSXU_CONTROL_FACE_AUTHENTICATION
  * MSXU_CONTROL_METADATA
  * MSUX_CONTROL_IR_TORCH


#### Debugging

Changes to the Debugger for Windows 10, version 1903 include the following:

* New stop codes were added to allow better tracking on unique failure types in the Windows operating system. In addition a number of existing bug check topics were expanded and updated. For more information, see [Bug Check Code Reference](https://docs.microsoft.com/windows-hardware/drivers/debugger/bug-check-code-reference2).

* Updates to KDNET topics to improve ease of use, for example in new [Setting Up KDNET Network Kernel Debugging Automatically](https://docs.microsoft.com/windows-hardware/drivers/debugger/setting-up-a-network-debugging-connection-automatically)

* Updates to IP V6 KDNET support.

* New [JavaScript Debugging](https://docs.microsoft.com/windows-hardware/drivers/debugger/javascript-debugger-scripting) topic

### <a name="display-1903"></a>Display

Updates to Display driver development in Windows 10, version 1903 include the following:

* **Super Wet Ink** New DDIs were added to enable front buffer rendering. See [D3DWDDM2_6DDI_SCANOUT_FLAGS](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3d10umddi/ne-d3d10umddi-d3dwddm2_6ddi_scanout_flags) and [PFND3DWDDM2_6DDI_PREPARE_SCANOUT_TRANSFORMATION](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3dwddm2_6ddi_prepare_scanout_transformation).

* **Variable Rate Shading** Enables allocation of rendering performance/power at varying rates across rendered images. See [PFND3D12DDI_RS_SET_SHADING_RATE_0062](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3d12umddi/nc-d3d12umddi-pfnd3d12ddi_rs_set_shading_rate_0062) and [D3D12DDI_SHADING_RATE_0062](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3d12umddi/ne-d3d12umddi-d3d12ddi_shading_rate_0062).

* **Collect Diagnostic Info** Allows the OS to collect a private data from drivers for graphics adapters which consist of both rendering and display functions. See [DXGKDDI_COLLECTDIAGNOSTICINFO](https://docs.microsoft.com/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_collectdiagnosticinfo).

* **Background Processing** Allows user mode drivers to express desired threading behavior, and the runtime to control/monitor it. User mode drivers would spin up background threads and assign the threads as low a priority as possible, and rely on the NT scheduler to ensure these threads don’t disrupt the critical-path threads, generally with success. See [PFND3D12DDI_QUEUEPROCESSINGWORK_CB_0062](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3d12umddi/nc-d3d12umddi-pfnd3d12ddi_queueprocessingwork_cb_0062).

* **Driver Hot Update** Reduce server downtime as much as possible when an OS component needs to be updated. See [DXGKDDI_SAVEMEMORYFORHOTUPDATE](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkcb_savememoryforhotupdate) and [DXGKDDI_RESTOREMEMORYFORHOTUPDATE](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_restorememoryforhotupdate).

### <a name="networking-1903"></a>Networking

#### NetAdapterCx

In the NetAdapter WDF class extension (NetAdapterCx), Net ring buffers have been replaced by Net rings, which have a new interface for sending and receiving network data using net ring iterators. The following is a list of new topics:

* [Introduction to net rings](https://docs.microsoft.com/windows-hardware/drivers/netcx/introduction-to-net-rings)
* [Sending network data with net rings](https://docs.microsoft.com/windows-hardware/drivers/netcx/sending-network-data-with-net-rings) with a new animation that illustrates how to send data
* [Receiving network data with net rings](https://docs.microsoft.com/windows-hardware/drivers/netcx/receiving-network-data-with-net-rings) with a new animation that illustrates how to receive data
* [Canceling network data with net rings](https://docs.microsoft.com/windows-hardware/drivers/netcx/canceling-network-data-with-net-rings)

New headers that support this feature include the following:

* [Ring.h](https://docs.microsoft.com/windows-hardware/drivers/ddi/ring/index)
* [Ringcollection.h](https://docs.microsoft.com/windows-hardware/drivers/ddi/ringcollection/index)
* [Netringiterator.h](https://docs.microsoft.com/windows-hardware/drivers/ddi/netringiterator/index)

The following is a list of NetAdapterCx content updates:

* Default adapter objects have been removed in favor of a single adapter object type. The following topics have been updated accordingly:

  * [Summary of NetAdapterCx objects](https://docs.microsoft.com/windows-hardware/drivers/netcx/summary-of-netadaptercx-objects)
  * [Device and adapter initialization](https://docs.microsoft.com/windows-hardware/drivers/netcx/device-and-adapter-initialization)

* Hardware offload and packet extension DDIs have been reorganized into new headers:

  * [Checksum.h](https://docs.microsoft.com/windows-hardware/drivers/ddi/checksum/index)
  * [Checksumtypes.h](https://docs.microsoft.com/windows-hardware/drivers/ddi/checksumtypes/index)
  * [Extension.h](https://docs.microsoft.com/windows-hardware/drivers/ddi/extension/index)
  * [Lso.h](https://docs.microsoft.com/windows-hardware/drivers/ddi/lso/index)
  * [Lsotypes.h](https://docs.microsoft.com/windows-hardware/drivers/ddi/lsotypes/index)
  * [Rsc.h](https://docs.microsoft.com/windows-hardware/drivers/ddi/rsc/index)
  * [Rsctypes.h](https://docs.microsoft.com/windows-hardware/drivers/ddi/rsctypes/index)

* Fundamental networking data structures, packets and fragments, have been updated and put into new headers:

  * [Packet.h](https://docs.microsoft.com/windows-hardware/drivers/ddi/packet/index)
  * [Fragment.h](https://docs.microsoft.com/windows-hardware/drivers/ddi/fragment/index)

* Overhauled [Transmit and receive queues](https://docs.microsoft.com/windows-hardware/drivers/netcx/transmit-and-receive-queues) topic to include callback samples and major operations for packet queues.

#### Mobile operator scenarios

New Mobile Plans content for mobile operators to sell plans to customers directly on Windows 10 devices, through the Mobile Plans app:

* [Mobile Plans](https://docs.microsoft.com/windows-hardware/drivers/mobilebroadband/mobile-plans)

### <a name="mobilebroadband-1903"></a>Mobile broadband

The following features were added to Mobile broadband in Windows 10, version 1903:

* New [SIM card (UICC) file/application system access](https://docs.microsoft.com/windows-hardware/drivers/network/mb-uicc-application-and-file-system-access) feature
* New [Cellular Time Information (NITZ)](https://docs.microsoft.com/windows-hardware/drivers/network/mb-nitz-support) feature.
* New [modem logging with DSS](https://docs.microsoft.com/windows-hardware/drivers/network/mb-modem-logging-with-dss) feature.
* New [5G data class support](https://docs.microsoft.com/windows-hardware/drivers/network/mb-5g-data-class-support) feature.

### Power Management Framework

The power management framework (PoFx) enables a driver to define one or more sets of individually adjustable performance states for individual components within a device. The driver can use performance states to throttle a component's workload to provide just enough performance for its current needs. For more information, see [Component-Level Performance State Management](https://docs.microsoft.com/windows-hardware/drivers/kernel/component-level-performance-management).

Windows 10, version 1903 includes support for the [Directed Power Management Framework (DFx)](https://docs.microsoft.com/windows-hardware/drivers/kernel/introduction-to-the-directed-power-management-framework).  Related reference documentation includes the following:

* [PO_FX_DEVICE_V3](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/ns-wdm-po_fx_device_v3)
* [PO_FX_DIRECTED_POWER_DOWN_CALLBACK callback function](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nc-wdm-po_fx_directed_power_down_callback)
* [PO_FX_DIRECTED_POWER_UP_CALLBACK callback function](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nc-wdm-po_fx_directed_power_up_callback)
* [PoFxCompleteDirectedPowerDown](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-pofxcompletedirectedpowerdown) function

For information about testing for DFx, please see the following pages:

* [Directed FX Single Device Test](https://docs.microsoft.com/windows-hardware/test/hlk/testref/34cfdfa6-7826-443c-9717-bc28c3166092)
* [Directed FX System Verification Test](https://docs.microsoft.com/windows-hardware/test/hlk/testref/def16163-9118-4d4a-b559-37873befa12e)
* [PwrTest DirectedFx Scenario](devtest/pwrtest-directedfx-scenario.md)

### <a name="print-1903"></a>Print

New Print driver documentation and features added in Windows 10, version 1903 include:

* New USB print IOCTLs:

  * [IOCTL_USBPRINT_GET_INTERFACE_TYPE](https://docs.microsoft.com/windows-hardware/drivers/ddi/usbprint/ni-usbprint-ioctl_usbprint_get_interface_type)
  * [IOCTL_USBPRINT_GET_PROTOCOL](https://docs.microsoft.com/windows-hardware/drivers/ddi/usbprint/ni-usbprint-ioctl_usbprint_get_protocol)
  * [IOCTL_USBPRINT_SET_PROTOCOL](https://docs.microsoft.com/windows-hardware/drivers/ddi/usbprint/ni-usbprint-ioctl_usbprint_set_protocol)

* New **fpRegeneratePrintDeviceCapabilities** [PRINTPROVIDER](https://docs.microsoft.com/windows-hardware/drivers/ddi/winsplp/ns-winsplp-_printprovidor) structure member and updated documentation.

### <a name="sensors-1903"></a>Sensors

New features in sensor driver development in Windows 10, version 1903 include a [MALT (Microsoft Ambient Light Tool) tool](https://docs.microsoft.com/windows-hardware/drivers/sensors/testing-malt-building-a-light-testing-tool) for testing and calibrating screen brightness.

There were also updates to the Ambient Color OEM whitepaper.

### <a name="storage-1903"></a>Storage

The following Storage features were added in Windows 10, version 1903:

* New Storport APIs for logging device failure and hardware protocol errors in ETW events and to query for platform D3 desired behavior
* New API to set the properties of a storage device or adapter
* For file systems, new DDIs were added to support retrieving extended attributes (EA) information upon create completion, allowing mini-filters to alter the ECP payload to change what higher filters see

### Windows Driver Frameworks (WDF)

In Windows 10, version 1903, the Windows Driver Framework (WDF) includes Kernel-Mode Driver Framework (KMDF) version 1.29 and User-Mode Driver Framework (UMDF) version 2.29.

For info on what's included in these framework versions, see [What's New for WDF Drivers in Windows 10](https://docs.microsoft.com/windows-hardware/drivers/wdf/).
To see what was added in previous versions of WDF, see [KMDF Version History](https://docs.microsoft.com/windows-hardware/drivers/wdf/kmdf-version-history) and [UMDF Version History](https://docs.microsoft.com/windows-hardware/drivers/wdf/umdf-version-history).

### Windows Hardware Error Architecture (WHEA)

Windows 10, version 1903 includes a simplified interface to WHEA.  For more info, see the following pages:

* [**WheaAddErrorSourceDeviceDriver**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntddk/nf-ntddk-wheaadderrorsourcedevicedriver)
* [**WheaReportHwErrorDeviceDriver**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntddk/nf-ntddk-wheareporthwerrordevicedriver)
* [**WheaRemoveErrorSourceDeviceDriver**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntddk/nf-ntddk-whearemoveerrorsourcedevicedriver)
* [**WHEA_ERROR_SOURCE_CONFIGURATION_DEVICE_DRIVER**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntddk/ns-ntddk-whea_error_source_configuration_device_driver)
* [*WHEA_ERROR_SOURCE_READY_DEVICE_DRIVER*](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntddk/nc-ntddk-_whea_error_source_ready_device_driver)
* [*WHEA_ERROR_SOURCE_UNINITIALIZE_DEVICE_DRIVER*](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntddk/nc-ntddk-_whea_error_source_uninitialize_device_driver)
* [*WHEA_ERROR_SOURCE_INITIALIZE_DEVICE_DRIVER*](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntddk/nc-ntddk-_whea_error_source_initialize_device_driver)

### <a name="wifi-1903"></a>Wi-fi

New Wi-fi driver development documentation and features include:

* New Fine Timing Measurement (FTM) feature
* New [WPA3-SAE Authentication](https://docs.microsoft.com/windows-hardware/drivers/network/wpa3-sae-authentication) feature
* New Multiband Operation (MBO) support to improve roaming performance in enterprise scenarios
* New beacon report offloading support
* For OID commands, NDIS status indications, and TLVs for these new features, see [WDI doc change history](https://docs.microsoft.com/windows-hardware/drivers/network/wdi-doc-change-history)

The following topics were updated for Windows 10, version 1903:

* [WDI_AUTH_ALGORITHM](https://docs.microsoft.com/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_auth_algorithm) - added support for WPA3-SAE authentication
* [OID_WDI_TASK_P2P_SEND_REQUEST_ACTION_FRAME](https://docs.microsoft.com/windows-hardware/drivers/network/oid-wdi-task-p2p-send-request-action-frame) and [OID_WDI_TASK_P2P_SEND_RESPONSE_ACTION_FRAME](https://docs.microsoft.com/windows-hardware/drivers/network/oid-wdi-task-p2p-send-response-action-frame) - added additional validation of outgoing Point to Point (P2P) action frames

## What's new in Windows 10, version 1809

This section describes new features and updates for driver development in Windows 10, version 1809 (Windows 10 October 2018 Update).

[Back to Top](#top)

### <a name="audio-1809"></a>Audio

Documentation on the new [sidebandaudio](https://docs.microsoft.com/windows-hardware/drivers/ddi/sidebandaudio/) and [usbsidebandaudio](https://docs.microsoft.com/windows-hardware/drivers/ddi/usbsidebandaudio/) headers is  now available.

### <a name="bluetooth-1809"></a>Bluetooth

* HCI_VS_MSFT_Read_Supported_Features has been updated to include a new flag for secure simple pairing process. See, [Microsoft-defined Bluetooth HCI commands and events](https://docs.microsoft.com/windows-hardware/drivers/bluetooth/microsoft-defined-bluetooth-hci-commands-and-events#hcivsmsftreadsupportedfeatures).

* New QDID for Windows 10, version 1809 is available here: [108589](https://launchstudio.bluetooth.com/ListingDetails/55701). For a complete list of QD ID for all releases, see [Bluetooth](https://docs.microsoft.com/windows-hardware/design/component-guidelines/bluetooth).

### Windows Hardware Dev Center dashboard

In Windows 10, version 1809, we added new and improved functionality in the way of [Hardware APIs](https://docs.microsoft.com/windows-hardware/drivers/dashboard/dashboard-api) for developers, IHVs, and OEMs to track and submit driver packages to the Windows hardware dashboard.

Use the shipping label REST APIs to create and manage shipping labels, the method by which you distribute your drivers.

* [Manage Shipping Labels](https://docs.microsoft.com/windows-hardware/drivers/dashboard/manage-shipping-labels)
* [Get shipping label data](https://docs.microsoft.com/windows-hardware/drivers/dashboard/get-shipping-labels)

Use the asynchronous custom report methods to access reporting data for driver errors and OEM hardware errors. You can define reporting templates based on your needs, set a schedule and you will have data delivered to you at regular intervals.

* [Schedule custom reports for your driver failure details](https://docs.microsoft.com/windows-hardware/drivers/dashboard/schedule-custom-reports-for-driver-failure-details)

### Debugging

Changes to the Debugger for Windows 10, version 1809 include the following:

* **New Debugger Data Model API** – A new object oriented debugger data model interface to support debugger automation is now available using the dbgmodel.h header. The debugger data model is an extensible object model that is central to the way in which new debugger extensions (including those in JavaScript, NatVis, and C++) both consume information from the debugger and produce information that can be accessed from the debugger as well as other extensions. Constructs which are written to the data model APIs are available in the debugger's dx expression evaluator as well as from JavaScript extensions or C++ extensions. Documentation will be available at: [Overview of the Debugger Data Model C++ Interface](debugger/data-model-cpp-overview.md)  and the [dbgmodel.h](https://docs.microsoft.com/windows-hardware/drivers/ddi/dbgmodel/) header reference topics.

* **IPv6** - We are adding support for IPv6 to KDNET. To make room for the larger headers required for IPv6, we decreased the payload size of packets. As a result, we’re declaring a new version of the KDNET protocol, so that host PCs running the latest version of the debugger can be used to debug target PCs that only support IPv4. There is a version of WinDbg Preview available at [https://aka.ms/windbgpreview](https://aka.ms/windbgpreview) that supports IPv6. Follow the Debugging Tools for Windows blog for updates on KDNET IPv6 support and see [Setting Up KDNET Network Kernel Debugging Manually](https://docs.microsoft.com/windows-hardware/drivers/debugger/setting-up-a-network-debugging-connection) for more details.

### Device and Driver Installation

In Windows 10, version 1809, the following content was added:

* [INF AddEventProvider Directive](https://docs.microsoft.com/windows-hardware/drivers/install/inf-addeventprovider-directive)
* [INF DDInstall.Events Section](https://docs.microsoft.com/windows-hardware/drivers/install/inf-ddinstall-events-section)

The following was updated:

* [Early Launch AntiMalware Requirements](https://docs.microsoft.com/windows-hardware/drivers/install/elam-driver-requirements)
* [Kernel-Mode Code Signing Requirements](https://docs.microsoft.com/windows-hardware/drivers/install/kernel-mode-code-signing-requirements--windows-vista-and-later-)

### <a name="display-1809"></a>Display

Updates to Display driver development in Windows 10, version 1809 include the following:

* **Raytracing** New Direct3D DDI's were created in parallel of Direct3D API's, in order to support hardware-accelerated raytracing. Example DDIs include: [PFND3D12DDI_BUILD_RAYTRACING_ACCELERATION_STRUCTURE_0054](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3d12umddi/nc-d3d12umddi-pfnd3d12ddi_build_raytracing_acceleration_structure_0054), [PFND3D12DDI_COPY_RAYTRACING_ACCELERATION_STRUCTURE_0054](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3d12umddi/nc-d3d12umddi-pfnd3d12ddi_copy_raytracing_acceleration_structure_0054). For more info about raytracing, see [Announcing Microsoft DirectX Raytracing](https://devblogs.microsoft.com/directx/announcing-microsoft-directx-raytracing/).

* **Universal Driver Requirements** WDDM 2.5 drivers will need to ensure their DirectX11 UMD, DirectX12 UMD, KMDs, and any other DLL loaded by these components, adhere to the Universal API.

* **SRV-Only Tiled Resource Tier 3** In Windows 10, version 1809, Tiled Resource Tier 3 capabilities can be supported less-orthogonally by GPUs. Direct3D12 now supports sparse volume textures without requiring unordered-access and render-target operations. SRV-Only Tiled Resource Tier 3 is a conceptual tier that fits between Tier 2 and Tier 3. Hardware support is optional, just like orthogonal Tiled Resource Tier 3 support currently is. But, supporting SRV-Only Tiled Resource Tier 3 is a super-set tier that requires support for Tiled Resource Tier 2.

   Drivers that already advertise support for orthogonal Tiled Resource Tier 3 merely have to update their drivers to support the latest “options caps” DDI structure version. The runtime will advertise SRV-Only Tiled Resource Tier 3 support to applications for any hardware that already supports orthogonal Tiled Resource Tier 3.

* **Render Pass** The Render Pass feature was added to:

  * Allow new APIs to be run on existing drivers.
  * Allow user mode drivers to choose optimal rendering path without heavy CPU penalty.

* **Meta-commands** A Meta-command is Direct3D12 object that represents an IHV-accelerated algorithm. It’s an opaque reference to a command generator implemented by the driver. Meta-command updates include Descriptor Table Binding and Texture binding. See [D3D12DDI_META_COMMAND_PARAMETER_TYPE](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3d12umddi/ne-d3d12umddi-d3d12ddi_meta_command_parameter_type) and [D3D12DDIARG_META_COMMAND_PARAMETER_DESC](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddiarg_meta_command_parameter_desc).

  Enable Compute Algorithms to use Texture Resources (swizzled memory)
  * Enable Graphics Pipeline Algorithms

* **HDR Brightness Compensation** A new SDR brightness boost was introduced to raise the reference white of SDR content to the user-desired value, allowing SDR content to be reproduced to a typical 200-240 nits, which is equivalent to what users have expected for SDR displays. SDR brightness boost affects overall Brightness3 behavior in two ways:

  1. This boost is applied pre-blend only on SDR content. HDR content is not affected. Meanwhile, for most laptop/brightness3 scenarios, users expect all content (SDR and HDR) to be adjusted.
  2. When the Brightness3 stack in the OS determines the desired nits value, it is not aware of the already applied SDR boost.

     The driver must then apply a compensation to the desired nits value coming from Brightness3 DDIs for HDR. Since Graphics drivers (and downstream TCON etc.) will be modifying the pixel values of the content to get desired nits value, there should also be a compensation applied to the HDR content metadata as provided by the applications via [D3DDDI_HDR_METADATA_HDR10](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3dukmdt/ns-d3dukmdt-_d3dddi_hdr_metadata_hdr10) or OS defaults via [DxgkDdiSetTargetAdjustedColorimetry](https://docs.microsoft.com/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_settargetadjustedcolorimetry). Since Graphics driver (TCONs) are responsible for modifying the pixel data, it is the driver’s responsibility to compensate the HDR content metadata.

* **HDR Pixel Format Support** This kernel mode device driver interface (DDI) change is part of WDDM 2.5 to expose new capabilities to be reported by driver/device, providing information regarding the HDR functionality supported by the driver/device.

   Currently, OS determines if the driver/device supports HDR based on the *HighColorSpace* bit of the [DXGK_MONITORLINKINFO_CAPABILITIES](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_dxgk_monitorlinkinfo_capabilities) structure as read from [DdiUpdateMonitorLinkInfo](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_updatemonitorlinkinfo). The *HighColorSpace* bit gives a combination of driver/link/monitor capability to run in HDR mode.

    The HDR capabilities reporting by the driver now includes a Driver/Device level capabilities, which will let OS know if the Driver/Device supports true HDR (i.e. FP16HDR), or only supports a limited form of HDR (i.e. ARGB10HDR), as defined below:

  * FP16HDR: Driver/device can take FP16 pixel format surfaces with scRGB/CCCS colorspace and apply PQ/2084 encoding and BT.2020 primaries during scanout pipeline to convert output signal to HDR10.
  * ARGB10HDR: Driver/device can take ARGB10 pixel format surfaces which are already PQ/2084 encoded and scan out HDR10 signal. Driver/device can’t handle FP16HDR as defined above or cannot handle the extended numeric range of scRGB FP16.

    Graphics drivers can only report support for either FP16HDR or ARGB10HDR as they are not really superset/subset configurations and OS will fail the Start Adapter if both are reported as supported at the same time. See [DXGK_MONITORLINKINFO_CAPABILITIES](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_dxgk_monitorlinkinfo_capabilities) and [_DXGK_DISPLAY_DRIVERCAPS_EXTENSION](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_display_drivercaps_extension).

* **SDR White Level** A kernel mode device driver interface change includes adding new parameters to existing DDIs to let the Graphics drivers know the “SDR white level” value that is being applied by the OS compositor for all the SDR content, for a display which is running in HDR mode. See _DXGK_COLORIMETRY.

### <a name="kernel-1809"></a>Windows kernel

Several new APIs have been added in the core kernel:

* [RtlQueryRegistryValueWithFallback function](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntddk/nf-ntddk-rtlqueryregistryvaluewithfallback): Querying the registry value entry by using a fallback handle in absence of a primary handle.
* [PsGetSiloContainerId function](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntddk/nf-ntddk-psgetsilocontainerid) and [PsGetThreadServerSilo function](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntddk/nf-ntddk-psgetthreadserversilo)
* New information classes added to: [_FILE_INFORMATION_CLASS](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/ne-wdm-_file_information_class)
  * FileLinkInformationExBypassAccessCheck
  * FileCaseSensitiveInformationForceAccessCheck
  * FileStorageReserveIdInformation
    * FileLinkInformationEx
* Extended version of NtCreateSection added [NtCreateSectionEx function](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntcreatesectionex) to indicate that this is actually an AWE section.
* New Ex macros grant direct access to actual push lock APIs exported by Ntoskernel.
  * [ExAcquirePushLockExclusive macro](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-exacquirepushlockexclusive)
  * [ExAcquirePushLockShared macro](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-exacquirepushlockshared)
  * [ExInitializePushLock function](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-exinitializepushlock)
  * [ExReleasePushLockExclusive macro](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-exreleasepushlockexclusive)
  * [ExReleasePushLockShared macro](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-exreleasepushlockshared)
* [KzLowerIrql](https://review.docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-kzlowerirql) and [KzRaiseIrql](https://review.docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-kzraiseirql) were moved to a supported extern forceinline for kernel components targeting Windows 8 and later versions, instead of relying on the forwarders to instantiate a special case of the inline functions.
* Flattening Portal Bridge (FPB) for PCI is now supported. For more information, see the [Official Specification](https://pcisig.com/sites/default/files/specification_documents/ECN_FPB_9_Feb_2017.pdf). The new APIs (_PCI_FPB_*) are declared in [Ntddk.h](https://review.docs.microsoft.com/windows-hardware/drivers/ddi/ntddk/).

### <a name="networking-1809"></a>Networking

#### NetAdapterCx

* New [INF files for NetAdapterCx client drivers](https://docs.microsoft.com/windows-hardware/drivers/netcx/inf-files-for-netadaptercx-client-drivers) topic.
* Transmit and receive queues have been consolidated into one object type called a packet queue, to simplify the API surface. A new section called [Polling model](https://docs.microsoft.com/windows-hardware/drivers/netcx/transmit-and-receive-queues#polling-model) has been added to the [Transmit and receive queues](https://docs.microsoft.com/windows-hardware/drivers/netcx/transmit-and-receive-queues) topic.
* [Hardware offloads](https://docs.microsoft.com/windows-hardware/drivers/netcx/netadaptercx-hardware-offloads) have been added to NetAdapterCx, which also automates the registration of associated packet extensions for client drivers.
* Network interfaces are now decoupled from the driver's WDF device object. The *EvtNetAdapterSetCapabilities* callback function was removed to support this. NetAdapterCx client drivers can now have multiple network interfaces, including a default one.

   Topics updated to support network interface/device object decoupling include the following:

  * [Summary of NetAdapterCx objects](https://docs.microsoft.com/windows-hardware/drivers/netcx/summary-of-netadaptercx-objects)
  * [Device and adapter initialization](https://docs.microsoft.com/windows-hardware/drivers/netcx/device-and-adapter-initialization)
  * [Power-up sequence for a NetAdapterCx client driver](https://docs.microsoft.com/windows-hardware/drivers/netcx/power-up-sequence-for-a-netadaptercx-client-driver)
  * [Power-down sequence for a NetAdapterCx client driver](https://docs.microsoft.com/windows-hardware/drivers/netcx/power-down-sequence-for-a-netadaptercx-client-driver)

* DDIs supporting [NetAdapterCx Receive side scaling (RSS)](https://docs.microsoft.com/windows-hardware/drivers/netcx/netadaptercx-receive-side-scaling-rss-) have been simplified.
* Packet context token helper macros have been removed.

#### NDIS

[Receive side scaling version 2 (RSSv2)](https://docs.microsoft.com/windows-hardware/drivers/network/receive-side-scaling-version-2-rssv2-) has been updated to version 1.01.

### <a name="mobilebroadband-1809"></a>Mobile broadband

* New [OID](https://docs.microsoft.com/windows-hardware/drivers/network/oid-wwan-mpdp) and DDIs to support multiple packet data protocol (MPDP) interfaces for MBB devices.
* New [Device-based Reset and Recovery](https://docs.microsoft.com/windows-hardware/drivers/network/mb-device-based-reset-and-recovery) feature for more robust reset recovery for MBB devices and drivers.

#### Mobile Broadband WDF class extension (MBBCx)

MBBCx power management methods have been simplified.

Though preview content for MBBCx was available in Windows 10, version 1803, MBBCx now ships in the Windows 10, version 1809 version of the WDK.

#### Mobile operators

The [AutoConnectOrder setting](https://docs.microsoft.com/windows-hardware/drivers/mobilebroadband/desktop-cosa-apn-database-settings#apn-database-and-desktop-cosa-settings) is now supported in desktop COSA.

### <a name="sensors-1809"></a>Sensors

Support for auto Brightness feature:

The PKEY_SensorData_IsValid data field has been added to support auto brightness in sensors.

See [Light sensor data fields](https://docs.microsoft.com/windows-hardware/drivers/sensors/light-sensor-data-fields) for more info.

### Universal Drivers in Windows 10, version 1809

Starting in Windows 10, version 1809, Windows supports flexible linking, which enables you to use a single binary to target OneCore and Desktop SKUs.
To enable flexible linking, use the following new SDK API:

* [IsApiSetImplemented](https://docs.microsoft.com/windows/desktop/api/apiquery2/nf-apiquery2-isapisetimplemented)

This existing topic has been enhanced to describe how to use flexible linking to comply with the U requirement of the [DCHU driver design principles](https://docs.microsoft.com/windows-hardware/drivers/develop/getting-started-with-universal-drivers#design-principles):

* [Building for OneCore](https://docs.microsoft.com/windows-hardware/drivers/develop/building-for-onecore)


### <a name="usb-1809"></a>USB

**New feature for USB Type-C driver developers:**

If  your hardware is UCSI compliant and requires communication over a non-ACPI transport, you can utilize the new class extension &mdash; (UcmUcsiCx.sys). This implements the UCSI specification in a transport agnostic way. With minimal amount of code, your driver, which is a client to UcmUcsiCx, can communicate with the USB Type-C hardware over non-ACPI transport. This topic describes the services provided by the UCSI class extension and the expected behavior of the client driver.

* [Write a UCSI client driver](https://docs.microsoft.com/windows-hardware/drivers/usbcon/write-a-ucsi-driver)
* [UcmUcsiCx class extensions reference](https://docs.microsoft.com/windows-hardware/drivers/ddi/_usbref/#type-c-driver-reference)
* [UcmUcsiCx client driver sample](https://github.com/Microsoft/Windows-driver-samples/tree/master/usb/UcmUcsiAcpiSample)

**New feature for USB Type-C driver developers that allows you to monitor the activities of USB Type-C connectors and/or get involved in policy decisions on USB Type-C connectors.**

For example, control their device’s charging based on thermal conditions, so that the device won’t be overheated.

* [Write a USB Type-C Policy Manager client driver](https://www.microsoft.com/windows-hardware/drivers/usbcon/policy-manager-client)
* New APIs are available in [Usbpmapi.h](https://docs.microsoft.com/windows-hardware/drivers/ddi/usbpmapi/)

**New versions of the class extensions available for emulated USB devices (UDE) -- 1.1 and USB host controller (Ucx) 1.5:**

Emulated devices now support better reset recovery through function (FLDR) and platform (PLDR) resets. The client driver can now inform the system that the device needs a reset  and the type of reset: function or platform.

* [UdecxWdfDeviceNeedsReset function](https://docs.microsoft.com/windows-hardware/drivers/ddi/udecxwdfdevice/nf-udecxwdfdevice-udecxwdfdeviceneedsreset)

The host controller can also opt for FLDR and PLDR resets through:

* [EVT_UCX_USBDEVICE_DISABLE](https://docs.microsoft.com/windows-hardware/drivers/ddi/ucxusbdevice/nc-ucxusbdevice-evt_ucx_usbdevice_disable)

### <a name="wifi-1809"></a>Wi-fi

The WLAN device driver interface (WDI) spec has been updated to version 1.1.7.

* Added support for the latest 802.11ax PHY type for WDI drivers.
* Added support for unsolicited device service indications.

## What's new in Windows 10, version 1803

This section describes new features and updates for driver development in Windows 10, version 1803 (Windows 10 April 2018 Update).

[Back to Top](#top)

### <a name="acpi-1803"></a>ACPI

Windows 10, version 1803 includes updates to ACPI DDIs to support platform capabilities and physical device location.

### <a name="audio-1803"></a>Audio

The [voice activation](https://docs.microsoft.com/windows-hardware/drivers/audio/voice-activation) topic was updated to include additional information on APO requirements.

### <a name="bluetooth-1803"></a>Bluetooth

Windows 10, version 1803 introduces support for Swift Pair. Users no longer need to navigate the Settings App and find their peripheral to pair. Windows can now do this for them by popping a notification when a new peripheral is nearby and ready. There are two sets of requirements to ensure your peripheral works with Swift Pair. One set is for the peripheral’s behavior, and another for the structure and values in a Microsoft defined vendor advertisement section. For more information, see:

* [Bluetooth Swift Pair](https://docs.microsoft.com/windows-hardware/design/component-guidelines/bluetooth-swift-pair)
* [Bluetooth Features and Recommendations](https://docs.microsoft.com/windows-hardware/design/component-guidelines/bluetooth)

Windows 10, version 1803 supports Bluetooth version 5.0. For information about profile support, see [Bluetooth Version and Profile Support in Windows 10](https://docs.microsoft.com/windows-hardware/drivers/bluetooth/general-bluetooth-support-in-windows).

### <a name="camera-1803"></a>Camera

Updates to Camera driver development include:

* [DShow (DirectShow) Bridge implementation guidance for UVC devices](https://docs.microsoft.com/windows-hardware/drivers/stream/dshow-bridge-implementation-guidance-for-usb-video-class-devices) - Implementation guidance for configuring DShow Bridge for cameras and devices that comply with the USB Video Class (UVC) specification. The platform uses Microsoft OS Descriptors from the USB bus standard to configure DShow Bridge. The Extended Properties OS Descriptors are an extension of USB standard descriptors and are used by USB devices to return Windows specific device properties that are not enabled through standard specifications.
* [360 camera video capture](https://docs.microsoft.com/windows-hardware/drivers/stream/360-camera-video-capture) - Provides support for 360 camera preview, capture, and record with existing MediaCapture APIs. This enables the platform to expose spherical frame sources (for example, equirectangular frames ), enabling apps to detect and handle 360 video camera streams as well as to provide a 360 capture experience.

#### Debugging

Changes to the Debugger for Windows 10, version 1803 include the following:

[WinDbg Preview Time Travel Debugging (TTD) hands on lab](https://docs.microsoft.com/windows-hardware/drivers/debugger/time-travel-debugging-walkthrough) - This lab introduces Time Travel Debugging (TTD), using a small sample program with a code flaw. TTD is used to debug, identify and root cause the issue.

### <a name="display-1803"></a>Display

The following are updates to Display driver development in Windows 10, version 1803:

* **Indirect Display UMDF class extension** - The Indirect Display driver can pass the SRM to the rendering GPU and have a mechanism to query the SRM version being used.

* **IOMMU hardware-based GPU isolation support** - Increases security by restricting GPU access to system memory.

* **GPU paravirtualization support** - Enables display drivers to provide rendering capabilities to Hyper-V virtualized environments.

* **Brightness** - A new brightness interface to support multiple displays that can be set to calibrated nit-based brightness levels.

* **D3D11 bitstream encryption** - Additional GUIDS and parameters to D3D11 to support exposing CENC, CENS, CBC1, and CBCS with 8 or 16 byte initialization vectors.

* **D3D11 and D3D12 video decode histogram** - A luminance histogram allows the media team to leverage fixed function hardware for histogram to improve tone mapping quality for HDR/EDR scenarios. Fixed function hardware is useful when GPU is already saturated in these scenarios and to enable parallel processing. This feature is optional and should only be implemented if fixed function hardware is available. This feature should not be implemented with 3D or Compute.

* **D3D12 video decode** now supports Decode Tier II, indicating driver supports *Array of Textures* that enable applications to amortize allocation cost and reduce peak memory usage during resolution change.

* **Tiled resource tier and LDA atomics** - A new cross node sharing tier to add support for atomic shader instructions working across linked adapter (LDA) nodes. This improves ISVs ability to implement multiple GPU rendering techniques like split frame rendering (SFR) and clearly advances the capabilities over what is possible in D3D11.

* **GPU dithering support** - Drivers can report the ability to perform dithering on the wire signal for a given timing mode. This allows the OS to explicitly request dithering in scenarios where a higher effective bit depth is needed than is physically available on the monitor link, for example for HDR10 over HDMI 2.0.

* **Post-processing color enhancement override** - Adds the ability for the OS to request that the driver temporarily disable any post-processing that enhances or alters display colors. This is to support scenarios where specific applications want to enforce colorimetrically accurate color behavior on the display, and safely coexist with OEM or IHV-proprietary display color enhancements.

* **Direct3D12 and Video** - New API and DDI to provide access to the following capabilities:
  * Hardware accelerated video decoding
  * Content Protection
  * Video processing

* **DisplayID** - A new DDI, designed to allow the VESA’s DisplayID descriptor to be queried from a display controlled by a graphics adapter and shall support DisplayID v1.3 and DisplayID v2.0. The DDI is an extension of existing DxgkDdiQueryAdapterInfo DDI and shall be supported by all drivers with DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM2_3, including kernel mode display only drivers and indirect display drivers.

* **GPU performance data** - Extensions to DdiQueryAdapterInfo will expose information such as temperature, fan speed, clock speeds for engines and memory, memory bandwidth, power draw, and voltages

* Miscellaneous - A new SupportContextlessPresent driver cap to help IHV onboard new driver.

* Improvements to External/Removable GPU support in the OS. As a first step to add better support, Dxgkrnl needs to determine if a GPU is “detachable”, i.e. hot-pluggable. For RS4 we would like to leverage the driver’s knowledge about this instead of building our own infrastructure. For this purpose, we are adding a “Detachable” bit to DXGK_ DRIVERCAPS struct. Driver will set this bit during adapter initialization if the adapter is hot-pluggable.

* **Display Diagnostics** - Kernel mode device driver interface (DDI) changes to allow the driver for a display controller to report diagnostic events to the OS.  This provides a channel through which the driver can log events which would otherwise be invisible to the OS as the events are not a response to an OS request or something the OS needs to react to.

* **Shared graphics power components** - Allows non-graphics drivers to participate in the power management of a graphics device.  A non-graphics driver will use a driver interface to manage one or more of these shared power components in coordination with the graphics driver.

* **Shared texture improvements** - Includes increasing the types of textures that can be shared across processes and D3D devices. This design enables the frame server OS component to support monochrome with minimal memory copying.

### <a name="security-1803"></a>Driver security

Updates to [Windows Driver Security Guidance](https://docs.microsoft.com/windows-hardware/drivers/driversecurity/)
and the [Driver security checklist](https://docs.microsoft.com/windows-hardware/drivers/driversecurity/driver-security-checklist), which provides a driver security checklist for driver developers.

### <a name="kernel-1803"></a>Windows kernel

This section describes the new and updated features for Windows kernel driver development in Windows 10, version 1803.

A set of new APIs has been added to the kit to enable third parties to create their own KDNET extensibility modules or KdSerial transport layers. For sample code, see “Kernel Transport Samples” (ddk\samples\kdserial and ddk\samples\kdnet) in the Debuggers folder.

Support was added to provide drivers with a sanctioned location (that the operating system knows about) where they can store file state.  With this approach, the system can associate files in that location with a device or driver.

There are distinct locations to store file states specific to the internals of a driver and specific to a device. For drivers that have file state, you can decide if the state written to disk is:

* Driver state ([IoGetDriverDirectory](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdriverdirectory)): global to the driver that might be controlling multiple devices), or

* Device state ([IoGetDeviceDirectory](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdevicedirectory)): specific to the driver-controlled single device and other devices might have different values for similar state.

Function drivers (FDO) can now negotiate additional power when their respective PCIe devices are in a D3Cold state. This includes:

* Auxiliary power requirement [D3COLD_REQUEST_AUX_POWER](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nc-wdm-d3cold_request_aux_power).
* Core power rail [D3COLD_REQUEST_CORE_POWER_RAIL](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nc-wdm-d3cold_request_core_power_rail).
* Requirement for a fixed delay time between the message is received at the PCI Express Downstream Port and the time the platform asserts PERST# to the slot during the corresponding endpoint’s or PCI Express Upstream Port’s transition to D3cold while the system is in an ACPI operational state. See [D3COLD_REQUEST_PERST_DELAY](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nc-wdm-d3cold_request_perst_delay).

NT services and kernel-mode and user-mode drivers can raise a custom trigger for a device by using the [RtlRaiseCustomSystemEventTrigger](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntddk/nf-ntddk-rtlraisecustomsystemeventtrigger) function. A custom trigger, owned by the driver developer, notifies system event broker to start an associated background task with it, which is identified by a custom trigger identifier.

You can now register for active session change notification and get a callback when the notification is fired. As part of this notification, some data is also shared with the caller. This associated data is delivered via the [PO_SPR_ACTIVE_SESSION_DATA structure](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntpoapi/ns-ntpoapi-_po_spr_active_session_data).

### <a name="networking-1803"></a>Networking

This section outlines new features and improvements for Windows Networking driver development in Windows 10, version 1803.

#### NDIS and NetAdapterCx

Updates to NDIS include:

* [Receive side scaling V2](https://docs.microsoft.com/windows-hardware/drivers/network/receive-side-scaling-version-2-rssv2-in-ndis-6-80) has been updated with further details about steering parameters
* The [Synchronous OID interface](https://docs.microsoft.com/windows-hardware/drivers/network/synchronous-oid-request-interface-in-ndis-6-80) now supports NDIS light weight filter drivers

The following topics are new for the Network Adapter WDF class extension (NetAdapterCx):

* [Introduction to NetAdapterCx 1.2](https://docs.microsoft.com/windows-hardware/drivers/netcx/introduction-to-netadaptercx-1-2)
* [Packet descriptors and extensions](https://docs.microsoft.com/windows-hardware/drivers/netcx/packet-descriptors-and-extensions)
* [Network data buffer management](https://docs.microsoft.com/windows-hardware/drivers/netcx/network-data-buffer-management)
* [NetAdapterCx receive side scaling (RSS)](https://docs.microsoft.com/windows-hardware/drivers/netcx/netadaptercx-receive-side-scaling-rss-)

Additionally, new topics are available for a preview-only feature, the Mobile Broadband class extension (MBBCx), which uses the NetAdapterCx model for mobile broadband connectivity.

* [Mobile Broadband Class Extension (MBBCx)](https://docs.microsoft.com/windows-hardware/drivers/netcx/mobile-broadband-mbb-wdf-class-extension-mbbcx-)
  * [Writing an MBBCx client driver](https://docs.microsoft.com/windows-hardware/drivers/netcx/writing-an-mbbcx-client-driver)
  * [MBBCx API reference](https://docs.microsoft.com/windows-hardware/drivers/netcx/mbbcx-api-reference)

### <a name="mobilebroadband-1803"></a>Mobile broadband

In mobile broadband, a new topic detailing [MB low level UICC access](https://docs.microsoft.com/windows-hardware/drivers/network/mb-low-level-uicc-access) is available.

#### Mobile operators

New Hotspot and AppID settings are now a part of [desktop COSA](https://docs.microsoft.com/windows-hardware/drivers/mobilebroadband/desktop-cosa-apn-database-settings#desktop-cosa-only-settings). Mobile operators are strongly encouraged to transition from broadband app experience apps with [Sysdev metadata packages](https://docs.microsoft.com/windows-hardware/drivers/mobilebroadband/service-metadata) to [MO UWP Apps](https://docs.microsoft.com/windows-hardware/drivers/mobilebroadband/uwp-mobile-broadband-apps) and the [COSA database](https://docs.microsoft.com/windows-hardware/drivers/mobilebroadband/desktop-cosa-apn-database-settings).

### <a name="pci-1803"></a>PCIe

New ACPI _DSD methods have been added to support these Modern Standby and PCI hot plug scenarios:

* Directed Deepest Runtime Idle Power State (DDRIPS) support on PCIe Root Ports
* Identifying PCIe Root Ports supporting hot plug in D3
* Identifying externally exposed PCIe Root Ports

For information, see [ACPI Interface: Device Specific Data (_DSD) for PCIe Root Ports](https://docs.microsoft.com/windows-hardware/drivers/pci/dsd-for-pcie-root-ports).

### <a name="sensors-1803"></a>Sensors

The [SENSOR_CONNECTION_TYPES enumeration](https://docs.microsoft.com/windows-hardware/drivers/ddi/sensorsdef/ne-sensorsdef-sensor_connection_types) was added to clarify connection type properties.

### <a name="usb-1803"></a>USB

New APIs were added to simulate detach for shared connectors. If a USB device is attached to a host or has shared connector while the stack is being removed while the device is attached to a host or has shared connectors, you can simulate a detach event. At this point all attach/detach notification mechanisms are disabled. For more information, see [UfxDeviceNotifyFinalExit function](https://docs.microsoft.com/windows-hardware/drivers/ddi/ufxclient/nf-ufxclient-ufxdevicenotifyfinalexit).

### <a name="wifi-1803"></a>Wi-fi

Updates to Wi-fi driver development include a new [TLV for the Nic Auto Power Saver (NAPS) advanced power management feature](https://docs.microsoft.com/windows-hardware/drivers/network/wdi-tlv-os-power-management-features) and updates to the platform level device recovery service (PLDR).



[Back to Top](#top)

## Deprecated features

The following table describes Windows driver development features that have been removed in Windows 10.

| Driver technology | Feature | Deprecated in |
|---|---|---|
| GNSS/Location | [Geolocation driver sample for Windows 8.1](https://docs.microsoft.com/windows-hardware/drivers/gnss/sensors-geolocation-driver-sample) and related documentation | Windows 10, version 1709 |
| Mobile Operator Scenarios (Networking) | [AllowStandardUserPinUnlock](https://docs.microsoft.com/windows-hardware/drivers/mobilebroadband/allowstandarduserpinunlock) | Windows 10, version 1709 |
| Scan/Image | [WSD (Web Services for Devices) Challenger](https://docs.microsoft.com/windows-hardware/drivers/image/challenging-a-disconnected-scanner-with-the-wsd-challenger) functionality and related documentation | Windows 10, version 1709 |
|Mobile Operators| Mobile broadband app experience apps with Sysdev metadata packages are deprecated in favor of MO UWP APPS and COSA. | Windows 10, version 1803|
