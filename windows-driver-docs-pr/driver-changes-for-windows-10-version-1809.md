---
title: Driver development changes for Windows 10, version 1809
description: Learn about new features for driver development in Windows 10, version 1809 (Windows 10 October 2018 update).
ms.date: 04/28/2020
ms.localizationpriority: medium
---

# What's new in Windows 10, version 1809

This section describes new features and updates for driver development in Windows 10, version 1809 (Windows 10 October 2018 Update).

## <a name="audio-1809"></a>Audio

Documentation on the new [sidebandaudio](/windows-hardware/drivers/ddi/sidebandaudio/) and [usbsidebandaudio](/windows-hardware/drivers/ddi/usbsidebandaudio/) headers is  now available.

## <a name="bluetooth-1809"></a>Bluetooth

* HCI_VS_MSFT_Read_Supported_Features has been updated to include a new flag for secure simple pairing process. See, [Microsoft-defined Bluetooth HCI commands and events](./bluetooth/microsoft-defined-bluetooth-hci-commands-and-events.md#hci_vs_msft_read_supported_features).

* New QDID for Windows 10, version 1809 is available here: [108589](https://launchstudio.bluetooth.com/ListingDetails/55701). For a complete list of QD ID for all releases, see [Bluetooth](/windows-hardware/design/component-guidelines/bluetooth).

## Windows Hardware Dev Center dashboard

In Windows 10, version 1809, we added new and improved functionality in the way of [Hardware APIs](./dashboard/dashboard-api.md) for developers, IHVs, and OEMs to track and submit driver packages to the Windows hardware dashboard.

Use the shipping label REST APIs to create and manage shipping labels, the method by which you distribute your drivers.

* [Manage Shipping Labels](./dashboard/manage-shipping-labels.md)
* [Get shipping label data](./dashboard/get-shipping-labels.md)

Use the asynchronous custom report methods to access reporting data for driver errors and OEM hardware errors. You can define reporting templates based on your needs, set a schedule and you will have data delivered to you at regular intervals.

* [Schedule custom reports for your driver failure details](./dashboard/dashboard-api.md)

## Debugging

Changes to the Debugger for Windows 10, version 1809 include the following:

* **New Debugger Data Model API** – A new object oriented debugger data model interface to support debugger automation is now available using the dbgmodel.h header. The debugger data model is an extensible object model that is central to the way in which new debugger extensions (including those in JavaScript, NatVis, and C++) both consume information from the debugger and produce information that can be accessed from the debugger as well as other extensions. Constructs which are written to the data model APIs are available in the debugger's dx expression evaluator as well as from JavaScript extensions or C++ extensions. Documentation will be available at: [Overview of the Debugger Data Model C++ Interface](debugger/data-model-cpp-overview.md)  and the [dbgmodel.h](/windows-hardware/drivers/ddi/dbgmodel/) header reference topics.

* **IPv6** - We are adding support for IPv6 to KDNET. To make room for the larger headers required for IPv6, we decreased the payload size of packets. As a result, we’re declaring a new version of the KDNET protocol, so that host PCs running the latest version of the debugger can be used to debug target PCs that only support IPv4. There is a version of WinDbg Preview available at [https://aka.ms/windbgpreview](https://aka.ms/windbgpreview) that supports IPv6. Follow the Debugging Tools for Windows blog for updates on KDNET IPv6 support and see [Setting Up KDNET Network Kernel Debugging Manually](./debugger/setting-up-a-network-debugging-connection.md) for more details.

## Device and Driver Installation

In Windows 10, version 1809, the following content was added:

* [INF AddEventProvider Directive](./install/inf-addeventprovider-directive.md)
* [INF DDInstall.Events Section](./install/inf-ddinstall-events-section.md)

The following was updated:

* [Early Launch AntiMalware Requirements](./install/elam-driver-requirements.md)
* [Kernel-Mode Code Signing Requirements](./install/kernel-mode-code-signing-requirements--windows-vista-and-later-.md)

## <a name="display-1809"></a>Display

Updates to Display driver development in Windows 10, version 1809 include the following:

* **Raytracing** New Direct3D DDI's were created in parallel of Direct3D API's, in order to support hardware-accelerated raytracing. Example DDIs include: [PFND3D12DDI_BUILD_RAYTRACING_ACCELERATION_STRUCTURE_0054](/windows-hardware/drivers/ddi/d3d12umddi/nc-d3d12umddi-pfnd3d12ddi_build_raytracing_acceleration_structure_0054), [PFND3D12DDI_COPY_RAYTRACING_ACCELERATION_STRUCTURE_0054](/windows-hardware/drivers/ddi/d3d12umddi/nc-d3d12umddi-pfnd3d12ddi_copy_raytracing_acceleration_structure_0054). For more info about raytracing, see [Announcing Microsoft DirectX Raytracing](https://devblogs.microsoft.com/directx/announcing-microsoft-directx-raytracing/).

* **Universal Driver Requirements** WDDM 2.5 drivers will need to ensure their DirectX11 UMD, DirectX12 UMD, KMDs, and any other DLL loaded by these components, adhere to the Universal API.

* **SRV-Only Tiled Resource Tier 3** In Windows 10, version 1809, Tiled Resource Tier 3 capabilities can be supported less-orthogonally by GPUs. Direct3D12 now supports sparse volume textures without requiring unordered-access and render-target operations. SRV-Only Tiled Resource Tier 3 is a conceptual tier that fits between Tier 2 and Tier 3. Hardware support is optional, just like orthogonal Tiled Resource Tier 3 support currently is. But, supporting SRV-Only Tiled Resource Tier 3 is a super-set tier that requires support for Tiled Resource Tier 2.

   Drivers that already advertise support for orthogonal Tiled Resource Tier 3 merely have to update their drivers to support the latest “options caps” DDI structure version. The runtime will advertise SRV-Only Tiled Resource Tier 3 support to applications for any hardware that already supports orthogonal Tiled Resource Tier 3.

* **Render Pass** The Render Pass feature was added to:

  * Allow new APIs to be run on existing drivers.
  * Allow user mode drivers to choose optimal rendering path without heavy CPU penalty.

* **Meta-commands** A Meta-command is Direct3D12 object that represents an IHV-accelerated algorithm. It’s an opaque reference to a command generator implemented by the driver. Meta-command updates include Descriptor Table Binding and Texture binding. See [D3D12DDI_META_COMMAND_PARAMETER_TYPE](/windows-hardware/drivers/ddi/d3d12umddi/ne-d3d12umddi-d3d12ddi_meta_command_parameter_type) and [D3D12DDIARG_META_COMMAND_PARAMETER_DESC](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddiarg_meta_command_parameter_desc).

  Enable Compute Algorithms to use Texture Resources (swizzled memory)
  * Enable Graphics Pipeline Algorithms

* **HDR Brightness Compensation** A new SDR brightness boost was introduced to raise the reference white of SDR content to the user-desired value, allowing SDR content to be reproduced to a typical 200-240 nits, which is equivalent to what users have expected for SDR displays. SDR brightness boost affects overall Brightness3 behavior in two ways:

  1. This boost is applied pre-blend only on SDR content. HDR content is not affected. Meanwhile, for most laptop/brightness3 scenarios, users expect all content (SDR and HDR) to be adjusted.
  2. When the Brightness3 stack in the OS determines the desired nits value, it is not aware of the already applied SDR boost.

     The driver must then apply a compensation to the desired nits value coming from Brightness3 DDIs for HDR. Since Graphics drivers (and downstream TCON etc.) will be modifying the pixel values of the content to get desired nits value, there should also be a compensation applied to the HDR content metadata as provided by the applications via [D3DDDI_HDR_METADATA_HDR10](/windows-hardware/drivers/ddi/d3dukmdt/ns-d3dukmdt-_d3dddi_hdr_metadata_hdr10) or OS defaults via [DxgkDdiSetTargetAdjustedColorimetry](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_settargetadjustedcolorimetry). Since Graphics driver (TCONs) are responsible for modifying the pixel data, it is the driver’s responsibility to compensate the HDR content metadata.

* **HDR Pixel Format Support** This kernel mode device driver interface (DDI) change is part of WDDM 2.5 to expose new capabilities to be reported by driver/device, providing information regarding the HDR functionality supported by the driver/device.

   Currently, OS determines if the driver/device supports HDR based on the *HighColorSpace* bit of the [DXGK_MONITORLINKINFO_CAPABILITIES](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_dxgk_monitorlinkinfo_capabilities) structure as read from [DdiUpdateMonitorLinkInfo](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_updatemonitorlinkinfo). The *HighColorSpace* bit gives a combination of driver/link/monitor capability to run in HDR mode.

    The HDR capabilities reporting by the driver now includes a Driver/Device level capabilities, which will let OS know if the Driver/Device supports true HDR (i.e. FP16HDR), or only supports a limited form of HDR (i.e. ARGB10HDR), as defined below:

  * FP16HDR: Driver/device can take FP16 pixel format surfaces with scRGB/CCCS colorspace and apply PQ/2084 encoding and BT.2020 primaries during scanout pipeline to convert output signal to HDR10.
  * ARGB10HDR: Driver/device can take ARGB10 pixel format surfaces which are already PQ/2084 encoded and scan out HDR10 signal. Driver/device can’t handle FP16HDR as defined above or cannot handle the extended numeric range of scRGB FP16.

    Graphics drivers can only report support for either FP16HDR or ARGB10HDR as they are not really superset/subset configurations and OS will fail the Start Adapter if both are reported as supported at the same time. See [DXGK_MONITORLINKINFO_CAPABILITIES](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_dxgk_monitorlinkinfo_capabilities) and [_DXGK_DISPLAY_DRIVERCAPS_EXTENSION](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_display_drivercaps_extension).

* **SDR White Level** A kernel mode device driver interface change includes adding new parameters to existing DDIs to let the Graphics drivers know the “SDR white level” value that is being applied by the OS compositor for all the SDR content, for a display which is running in HDR mode. See _DXGK_COLORIMETRY.

## <a name="kernel-1809"></a>Windows kernel

Several new APIs have been added in the core kernel:

* [RtlQueryRegistryValueWithFallback function](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-rtlqueryregistryvaluewithfallback): Querying the registry value entry by using a fallback handle in absence of a primary handle.
* [PsGetSiloContainerId function](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-psgetsilocontainerid) and [PsGetThreadServerSilo function](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-psgetthreadserversilo)
* New information classes added to: [_FILE_INFORMATION_CLASS](/windows-hardware/drivers/ddi/wdm/ne-wdm-_file_information_class)
  * FileLinkInformationExBypassAccessCheck
  * FileCaseSensitiveInformationForceAccessCheck
  * FileStorageReserveIdInformation
    * FileLinkInformationEx
* Extended version of NtCreateSection added [NtCreateSectionEx function](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntcreatesectionex) to indicate that this is actually an AWE section.
* New Ex macros grant direct access to actual push lock APIs exported by Ntoskernel.
  * [ExAcquirePushLockExclusive macro](/windows-hardware/drivers/ddi/wdm/nf-wdm-exacquirepushlockexclusive)
  * [ExAcquirePushLockShared macro](/windows-hardware/drivers/ddi/wdm/nf-wdm-exacquirepushlockshared)
  * [ExInitializePushLock function](/windows-hardware/drivers/ddi/wdm/nf-wdm-exinitializepushlock)
  * [ExReleasePushLockExclusive macro](/windows-hardware/drivers/ddi/wdm/nf-wdm-exreleasepushlockexclusive)
  * [ExReleasePushLockShared macro](/windows-hardware/drivers/ddi/wdm/nf-wdm-exreleasepushlockshared)
* [KzLowerIrql](/windows-hardware/drivers/ddi/wdm/nf-wdm-kzlowerirql) and [KzRaiseIrql](/windows-hardware/drivers/ddi/wdm/nf-wdm-kzraiseirql) were moved to a supported extern forceinline for kernel components targeting Windows 8 and later versions, instead of relying on the forwarders to instantiate a special case of the inline functions.
* Flattening Portal Bridge (FPB) for PCI is now supported. For more information, see [PCI-SIG](https://pcisig.com) for the Official Specification. The new APIs (_PCI_FPB_*) are declared in [Ntddk.h](/windows-hardware/drivers/ddi/ntddk/).

## <a name="networking-1809"></a>Networking

## NetAdapterCx

* New [INF files for NetAdapterCx client drivers](./netcx/inf-files-for-netadaptercx-client-drivers.md) topic.
* Transmit and receive queues have been consolidated into one object type called a packet queue, to simplify the API surface. A new section called [Polling model](./netcx/transmit-and-receive-queues.md#polling-model) has been added to the [Transmit and receive queues](./netcx/transmit-and-receive-queues.md) topic.
* [Hardware offloads](./netcx/introduction-to-hardware-offloads.md) have been added to NetAdapterCx, which also automates the registration of associated packet extensions for client drivers.
* Network interfaces are now decoupled from the driver's WDF device object. The *EvtNetAdapterSetCapabilities* callback function was removed to support this. NetAdapterCx client drivers can now have multiple network interfaces, including a default one.

   Topics updated to support network interface/device object decoupling include the following:

  * [Summary of NetAdapterCx objects](./netcx/summary-of-netadaptercx-objects.md)
  * [Device and adapter initialization](./netcx/device-and-adapter-initialization.md)
  * [Power-up sequence for a NetAdapterCx client driver](./netcx/power-up-sequence-for-a-netadaptercx-client-driver.md)
  * [Power-down sequence for a NetAdapterCx client driver](./netcx/power-down-sequence-for-a-netadaptercx-client-driver.md)

* DDIs supporting [NetAdapterCx Receive side scaling (RSS)](./netcx/netadaptercx-receive-side-scaling-rss-.md) have been simplified.
* Packet context token helper macros have been removed.

## NDIS

[Receive side scaling version 2 (RSSv2)](./network/receive-side-scaling-version-2-rssv2-.md) has been updated to version 1.01.

## <a name="mobilebroadband-1809"></a>Mobile broadband

* New [OID](./network/oid-wwan-mpdp.md) and DDIs to support multiple packet data protocol (MPDP) interfaces for MBB devices.
* New [Device-based Reset and Recovery](./network/mb-device-based-reset-and-recovery.md) feature for more robust reset recovery for MBB devices and drivers.

## Mobile Broadband WDF class extension (MBBCx)

MBBCx power management methods have been simplified.

Though preview content for MBBCx was available in Windows 10, version 1803, MBBCx now ships in the Windows 10, version 1809 version of the WDK.

## Mobile operators

The [AutoConnectOrder setting](./mobilebroadband/desktop-cosa-apn-database-settings.md#apn-database-and-desktop-cosa-settings) is now supported in desktop COSA.

## <a name="sensors-1809"></a>Sensors

Support for auto Brightness feature:

The PKEY_SensorData_IsValid data field has been added to support auto brightness in sensors.

See [Light sensor data fields](./sensors/light-sensor-data-fields.md) for more info.

## Universal Drivers in Windows 10, version 1809

Starting in Windows 10, version 1809, Windows supports flexible linking, which enables you to use a single binary to target OneCore and Desktop SKUs.
To enable flexible linking, use the following new SDK API:

* [IsApiSetImplemented](/windows/win32/api/apiquery2/nf-apiquery2-isapisetimplemented)

This existing topic has been enhanced to describe how to use flexible linking to comply with the U requirement of the [DCHU driver design principles](./develop/dch-principles-best-practices.md):

* [Building for OneCore](./develop/building-for-onecore.md)


## <a name="usb-1809"></a>USB

**New feature for USB Type-C driver developers:**

If  your hardware is UCSI compliant and requires communication over a non-ACPI transport, you can utilize the new class extension &mdash; (UcmUcsiCx.sys). This implements the UCSI specification in a transport agnostic way. With minimal amount of code, your driver, which is a client to UcmUcsiCx, can communicate with the USB Type-C hardware over non-ACPI transport. This topic describes the services provided by the UCSI class extension and the expected behavior of the client driver.

* [Write a UCSI client driver](./usbcon/write-a-ucsi-driver.md)
* [UcmUcsiCx class extensions reference](/windows-hardware/drivers/ddi/_usbref/#type-c-driver-reference)
* [UcmUcsiCx client driver sample](https://github.com/Microsoft/Windows-driver-samples/tree/master/usb/UcmUcsiAcpiSample)

**New feature for USB Type-C driver developers that allows you to monitor the activities of USB Type-C connectors and/or get involved in policy decisions on USB Type-C connectors.**

For example, control their device’s charging based on thermal conditions, so that the device won’t be overheated.

* [Write a USB Type-C Policy Manager client driver](./usbcon/policy-manager-client.md)
* New APIs are available in [Usbpmapi.h](/windows-hardware/drivers/ddi/usbpmapi/)

**New versions of the class extensions available for emulated USB devices (UDE) -- 1.1 and USB host controller (Ucx) 1.5:**

Emulated devices now support better reset recovery through function (FLDR) and platform (PLDR) resets. The client driver can now inform the system that the device needs a reset  and the type of reset: function or platform.

* [UdecxWdfDeviceNeedsReset function](/windows-hardware/drivers/ddi/udecxwdfdevice/nf-udecxwdfdevice-udecxwdfdeviceneedsreset)

The host controller can also opt for FLDR and PLDR resets through:

* [EVT_UCX_USBDEVICE_DISABLE](/windows-hardware/drivers/ddi/ucxusbdevice/nc-ucxusbdevice-evt_ucx_usbdevice_disable)

## <a name="wifi-1809"></a>Wi-fi

The WLAN device driver interface (WDI) spec has been updated to version 1.1.7.

* Added support for the latest 802.11ax PHY type for WDI drivers.
* Added support for unsolicited device service indications.
