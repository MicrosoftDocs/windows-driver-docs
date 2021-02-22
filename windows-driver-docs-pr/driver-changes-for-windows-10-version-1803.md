---
title: Driver development changes for Windows 10, version 1803
description: Learn about new features for driver development in Windows 10, such as support for Bluetooth Swift Pair.
ms.date: 04/28/2020
ms.localizationpriority: medium
---

# What's new in Windows 10, version 1803

This section describes new features and updates for driver development in Windows 10, version 1803 (Windows 10 April 2018 Update).

## <a name="acpi-1803"></a>ACPI

Windows 10, version 1803 includes updates to ACPI DDIs to support platform capabilities and physical device location.

## <a name="audio-1803"></a>Audio

The [voice activation](./audio/voice-activation.md) topic was updated to include additional information on APO requirements.

## <a name="bluetooth-1803"></a>Bluetooth

Windows 10, version 1803 introduces support for Swift Pair. Users no longer need to navigate the Settings App and find their peripheral to pair. Windows can now do this for them by popping a notification when a new peripheral is nearby and ready. There are two sets of requirements to ensure your peripheral works with Swift Pair. One set is for the peripheral’s behavior, and another for the structure and values in a Microsoft defined vendor advertisement section. For more information, see:

* [Bluetooth Swift Pair](/windows-hardware/design/component-guidelines/bluetooth-swift-pair)
* [Bluetooth Features and Recommendations](/windows-hardware/design/component-guidelines/bluetooth)

Windows 10, version 1803 supports Bluetooth version 5.0. For information about profile support, see [Bluetooth Version and Profile Support in Windows 10](./bluetooth/general-bluetooth-support-in-windows.md).

## <a name="camera-1803"></a>Camera

Updates to Camera driver development include:

* [DShow (DirectShow) Bridge implementation guidance for UVC devices](./stream/dshow-bridge-implementation-guidance-for-usb-video-class-devices.md) - Implementation guidance for configuring DShow Bridge for cameras and devices that comply with the USB Video Class (UVC) specification. The platform uses Microsoft OS Descriptors from the USB bus standard to configure DShow Bridge. The Extended Properties OS Descriptors are an extension of USB standard descriptors and are used by USB devices to return Windows specific device properties that are not enabled through standard specifications.
* [360 camera video capture](./stream/360-camera-video-capture.md) - Provides support for 360 camera preview, capture, and record with existing MediaCapture APIs. This enables the platform to expose spherical frame sources (for example, equirectangular frames ), enabling apps to detect and handle 360 video camera streams as well as to provide a 360 capture experience.

## Debugging

Changes to the Debugger for Windows 10, version 1803 include the following:

[WinDbg Preview Time Travel Debugging (TTD) hands on lab](./debugger/time-travel-debugging-walkthrough.md) - This lab introduces Time Travel Debugging (TTD), using a small sample program with a code flaw. TTD is used to debug, identify and root cause the issue.

## <a name="display-1803"></a>Display

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

## <a name="security-1803"></a>Driver security

Updates to [Windows Driver Security Guidance](./driversecurity/index.md)
and the [Driver security checklist](./driversecurity/driver-security-checklist.md), which provides a driver security checklist for driver developers.

## <a name="kernel-1803"></a>Windows kernel

This section describes the new and updated features for Windows kernel driver development in Windows 10, version 1803.

A set of new APIs has been added to the kit to enable third parties to create their own KDNET extensibility modules or KdSerial transport layers. For sample code, see “Kernel Transport Samples” (ddk\samples\kdserial and ddk\samples\kdnet) in the Debuggers folder.

Support was added to provide drivers with a sanctioned location (that the operating system knows about) where they can store file state.  With this approach, the system can associate files in that location with a device or driver.

There are distinct locations to store file states specific to the internals of a driver and specific to a device. For drivers that have file state, you can decide if the state written to disk is:

* Driver state ([IoGetDriverDirectory](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdriverdirectory)): global to the driver that might be controlling multiple devices), or

* Device state ([IoGetDeviceDirectory](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdevicedirectory)): specific to the driver-controlled single device and other devices might have different values for similar state.

Function drivers (FDO) can now negotiate additional power when their respective PCIe devices are in a D3Cold state. This includes:

* Auxiliary power requirement [D3COLD_REQUEST_AUX_POWER](/windows-hardware/drivers/ddi/wdm/nc-wdm-d3cold_request_aux_power).
* Core power rail [D3COLD_REQUEST_CORE_POWER_RAIL](/windows-hardware/drivers/ddi/wdm/nc-wdm-d3cold_request_core_power_rail).
* Requirement for a fixed delay time between the message is received at the PCI Express Downstream Port and the time the platform asserts PERST# to the slot during the corresponding endpoint’s or PCI Express Upstream Port’s transition to D3cold while the system is in an ACPI operational state. See [D3COLD_REQUEST_PERST_DELAY](/windows-hardware/drivers/ddi/wdm/nc-wdm-d3cold_request_perst_delay).

NT services and kernel-mode and user-mode drivers can raise a custom trigger for a device by using the [RtlRaiseCustomSystemEventTrigger](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-rtlraisecustomsystemeventtrigger) function. A custom trigger, owned by the driver developer, notifies system event broker to start an associated background task with it, which is identified by a custom trigger identifier.

You can now register for active session change notification and get a callback when the notification is fired. As part of this notification, some data is also shared with the caller. This associated data is delivered via the [PO_SPR_ACTIVE_SESSION_DATA structure](/windows-hardware/drivers/ddi/ntpoapi/ns-ntpoapi-_po_spr_active_session_data).

## <a name="networking-1803"></a>Networking

This section outlines new features and improvements for Windows Networking driver development in Windows 10, version 1803.

## NDIS and NetAdapterCx

Updates to NDIS include:

* [Receive side scaling V2](./network/receive-side-scaling-version-2-rssv2-in-ndis-6-80.md) has been updated with further details about steering parameters
* The [Synchronous OID interface](./network/synchronous-oid-request-interface-in-ndis-6-80.md) now supports NDIS light weight filter drivers

The following topics are new for the Network Adapter WDF class extension (NetAdapterCx):

* [Introduction to NetAdapterCx 1.2](./netcx/index.md)
* [Packet descriptors and extensions](./netcx/packet-descriptors-and-extensions.md)
* [Network data buffer management](./netcx/network-data-buffer-management.md)
* [NetAdapterCx receive side scaling (RSS)](./netcx/netadaptercx-receive-side-scaling-rss-.md)

Additionally, new topics are available for a preview-only feature, the Mobile Broadband class extension (MBBCx), which uses the NetAdapterCx model for mobile broadband connectivity.

* [Mobile Broadband Class Extension (MBBCx)](./netcx/mobile-broadband-mbb-wdf-class-extension-mbbcx.md)
  * [Writing an MBBCx client driver](./netcx/writing-an-mbbcx-client-driver.md)
  * [MBBCx API reference](/windows-hardware/drivers/ddi/_netvista/)

## <a name="mobilebroadband-1803"></a>Mobile broadband

In mobile broadband, a new topic detailing [MB low level UICC access](./network/mb-low-level-uicc-access.md) is available.

## Mobile operators

New Hotspot and AppID settings are now a part of [desktop COSA](./mobilebroadband/desktop-cosa-apn-database-settings.md#desktop-cosa-only-settings). Mobile operators are strongly encouraged to transition from broadband app experience apps with [Sysdev metadata packages](./mobilebroadband/service-metadata.md) to [MO UWP Apps](./mobilebroadband/uwp-mobile-broadband-apps.md) and the [COSA database](./mobilebroadband/desktop-cosa-apn-database-settings.md).

## <a name="pci-1803"></a>PCIe

New ACPI _DSD methods have been added to support these Modern Standby and PCI hot plug scenarios:

* Directed Deepest Runtime Idle Power State (DDRIPS) support on PCIe Root Ports
* Identifying PCIe Root Ports supporting hot plug in D3
* Identifying externally exposed PCIe Root Ports

For information, see [ACPI Interface: Device Specific Data (_DSD) for PCIe Root Ports](./pci/dsd-for-pcie-root-ports.md).

## <a name="sensors-1803"></a>Sensors

The [SENSOR_CONNECTION_TYPES enumeration](/windows-hardware/drivers/ddi/sensorsdef/ne-sensorsdef-sensor_connection_types) was added to clarify connection type properties.

## <a name="usb-1803"></a>USB

New APIs were added to simulate detach for shared connectors. If a USB device is attached to a host or has shared connector while the stack is being removed while the device is attached to a host or has shared connectors, you can simulate a detach event. At this point all attach/detach notification mechanisms are disabled. For more information, see [UfxDeviceNotifyFinalExit function](/windows-hardware/drivers/ddi/ufxclient/nf-ufxclient-ufxdevicenotifyfinalexit).

## <a name="wifi-1803"></a>Wi-fi

Updates to Wi-fi driver development include a new [TLV for the Nic Auto Power Saver (NAPS) advanced power management feature](./network/wdi-tlv-os-power-management-features.md) and updates to the platform level device recovery service (PLDR).
