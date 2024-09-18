---
title: What's New in Driver Development for Windows 11, Version 24H2
description: This section describes new features for driver development in Windows 11, version 24H2.
ms.date: 09/18/2024
---

# <a name="top"></a>What's new in driver development for Windows 11, version 24H2

This section describes new features and updates for driver development in Windows 11, version 24H2. To target this version of Windows, you can use [WDK 10.0.26100.1](./download-the-wdk.md) (released May 22, 2024).

## WDK NuGet package support

The WDK NuGet package consists of essential libraries, headers, DLL, tools and metadata used for building Windows drivers that can be shared and supported by modern CI/CD pipelines. Users can access and consume the NuGet packages directly from nuget.org within Visual Studio. Using NuGet with the WDK provides a convenient solution for WDK acquisition and updates. It manages dependencies such as the SDK, to help keep the driver development tool chain up to date. For more information, see [Install the latest WDK using NuGet - Step by Step](install-the-wdk-using-nuget.md).

## ARM64 support

Starting from WDK version 10.0.26100.1, WDK now supports development, testing and deployment of drivers on ARM64 machines. The WDK/EWDK can be installed and run natively on ARM64 hardware, in addition to the previously supported emulation of x86 KMDF/UMDF2 drivers on ARM64 hardware. There is also support for debugging and deployment of drivers to an ARM64 target machine from both ARM64 and x64 host machines. The process of installing WDK/EWDK on ARM64 machines will automatically identify and install all the necessary dependencies including build tools, binaries and libraries.

## Audio

Updates to the [ACX audio class extensions overview](./audio/acx-audio-class-extensions-overview.md) and the [Windows 11 APIs for Audio Processing Objects](./audio/windows-11-apis-for-audio-processing-objects.md) articles including new information on the following:

- [ACX multi circuit composition](./audio/acx-multi-circuit-composition.md)

- [ACX multi stack cross driver communications](./audio/acx-multi-stack.md)

- [ACX audio data formats and data format lists](./audio/acx-data-formats.md)

- [ACX power management](./audio/acx-power-management.md)

- [ACX WDF driver lifetime management](./audio/acx-wdf-driver-lifetime-management.md)

## Camera and streaming media

Three new camera articles for Windows 11, version 24H2 (also applies to Windows 11, version 23H2):

- [Camera settings page](./stream/camera-settings-page.md) - Describes the features and operation of the camera settings page in Windows 11, and the default values framework that allows configuration of the camera configuration applied when an application starts the camera.

- [Camera companion apps](./stream/camera-companion-apps.md) - Describes companion apps, an extensibility feature for manufacturers of cameras to build custom applications that can configure the camera and adjust default image settings.

- [Network cameras](./stream/network-cameras.md) - Describes compatibility with ONVIF network cameras in Windows.

New camera KS Properties and DDIs:

- [KSPROPERTY_CAMERACONTROL_EXTENDED_FRAMERATE_THROTTLE](./stream/ksproperty-cameracontrol-extended-framerate-throttle.md)

- [KSPROPERTY_CAMERACONTROL_EXTENDED_FIELDOFVIEW2](./stream/ksproperty-cameracontrol-extended-fieldofview2.md)

- [KSPROPERTY_CAMERACONTROL_EXTENDED_FIELDOFVIEW2_CONFIGCAPS](./stream/ksproperty-cameracontrol-extended-fieldofview2-configcaps.md)

- [**KSCAMERA_EXTENDEDPROP_FIELDOFVIEW2_CONFIGCAPS**](/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-kscamera_extendedprop_fieldofview2_configcaps)

Updated UVC MSXUs for framerate throttle and FoV2 additions. For more information, see [Microsoft extensions to USB Video Class 1.5 specification](./stream/uvc-extensions-1-5.md).

## Display and graphics drivers

GPUs are increasingly used in artificial intelligence and machine learning scenarios due to their computational power, parallel processing capabilities, and efficient handling of large datasets. Several new features are added to Windows Display Driver Model (WDDM) version 3.2 as optimizations to GPU/NPU usage, especially in cloud-based scenarios.

- [Dirty bit tracking](./display/dirty-bit-tracking.md) enhances the performance of VRAM data transfer between physical hosts during the live migration of virtual machines.

- [Live migration of heterogeneous GPU-P compute devices](./display/live-migration-on-gpup-devices.md) is added. Significant content can now be transferred while virtualized resources are still active, reducing the pause time needed to complete a migration.

- A [GPU native fence synchronization object](./display/native-gpu-fence-objects.md) is added as an extension to the monitored fence object, supporting the following extra features:

  - GPU wait on monitored fence value, which allows for high performance engine-to-engine synchronization without requiring CPU round trips.
  
  - Conditional interrupt notification only for GPU fence signals that have CPU waiters, enabling substantial power savings.
  
  - Fence value storage in the GPU's local memory.

- [User-mode work submission](./display/user-mode-work-submission.md) is an in-progress feature that isn't yet enabled for final use. This feature allows user-mode drivers to submit work directly to the GPU without kernel-mode intervention.

Other added WDDM 3.2 features include:

- The D3D12 video encoding DDI is extended to [support AV1 encoding](./display/video-encoding-d3d12-av1.md).

- The method that a user-mode or kernel-mode graphics driver uses to determine whether a particular [WDDM feature is supported and enabled](./display/querying-wddm-feature-support-and-enablement.md)

- [TDR (timeout detection and recovery) debugging is enhanced](./display/tdr-debuggability-improvements.md) to provide more information about the cause of a TDR event.

- [Allocation notification](./display/allocation-notification.md) is an in-progress feature that isn't yet enabled for final use. This feature allows kernel-mode drivers to receive notifications about an allocation that's about to undergo a paging eviction or promotion operation.

## File system and filter drivers

Starting in Windows 11, version 24H2:

- [Bind links](/windows/win32/bindlink/) can be used to bind a file system namespace to a local "virtual path" through the Bind Filter (*bindflt.sys*). Minifilters can choose to veto such bind links on the system's boot partition. For more information, see [Vetoing a bind link](./ifs/vetoing-a-bind-link.md).

- When opening a $INDEX_ALLOCATION attribute, [**NtCreateFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntcreatefile) now honors the state of the **FILE_NON_DIRECTORY_FILE** flag, whereas it previously didn't.

- *FltMgr* provides [Query on Create support for USN and file security information](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltrequestsecurityinfooncreatecompletion).

## Network drivers

- Starting in Windows 11, version 24H2, you can write a [User-Mode Driver Framework (UMDF) NetAdapterCx](netcx/user-mode-netcx.md) driver. The UMDF APIs in NetAdapterCx align with the KMDF versions, so you can convert your KMDF-based client driver to UMDF with little to no code changes.

- UDP Receive Segment Coalescing Offload (URO) is a new hardware offload feature that enables network interface cards (NICs) to coalesce UDP receive segments. For more information, see [UDP Receive Segment Coalescing Offload (URO)](network/udp-rsc-offload.md) and [NetAdapterCx URO](netcx/rsc-offload.md).

- [WiFiCx Wi-Fi 7](./netcx/wificx-wi-fi-7.md) introduces support for Wi-Fi 7 features, providing faster connectivity speeds, lower latency, and improved security. WiFiCx Wi-Fi 7 enables:
  
  - Multi-Link Operation (MLO) with roaming differentiation to leverage multiple simultaneous channels to the Wi-Fi access point (AP).
  
  - Enhanced capabilities for WPA3-SAE authentication and Opportunistic Wireless Encryption (OWE) with GCMP-256 cipher.

- [WiFiCx WPA3 SoftAP](./netcx/wificx-wpa3-softap.md) enables devices to set up a Soft Access Point (SoftAP) using the Wi-Fi Protected Access 3 - Simultaneous Authentication of Equals (WPA3-SAE) security protocol.

- [WiFiCx QoS R1](./netcx/qos-r1.md) introduces advanced traffic management capabilities for WiFiCx devices. QoS R1 enables prioritization of Wi-Fi data packets through Mirrored Stream Classification Service (MSCS) and QoS Mapping (DSCP-to-UP Mapping).

## Kernel

Four new *wdm.h* power management DDIs for Windows 11, version 24H2:

- **[PO_EFFECTIVE_POWER_MODE_CALLBACK](/windows-hardware/drivers/ddi/wdm/nc-wdm-po_effective_power_mode_callback)** callback function - Invoked with the current value of the power setting immediately after registration.

- **[PO_EFFECTIVE_POWER_MODE](/windows-hardware/drivers/ddi/wdm/ne-wdm-po_effective_power_mode)** enumeration - Enumerates the effective power modes.

- **[PoRegisterForEffectivePowerModeNotifications](/windows-hardware/drivers/ddi/wdm/nf-wdm-poregisterforeffectivepowermodenotifications)** function - Registers a callback to receive effective power mode change notifications.

- **[PoUnregisterFromEffectivePowerModeNotifications](/windows-hardware/drivers/ddi/wdm/nf-wdm-pounregisterfromeffectivepowermodenotifications)** function - Unregisters from effective power mode change notifications.

## Storage drivers

- A storport miniport driver can now read configuration data from more locations within the registry. For more information, see **[StorPortReadRegistryKey](/windows-hardware/drivers/ddi/storport/nf-storport-storportreadregistrykey)** and **[StorPortReadDriverRegistry](/windows-hardware/drivers/ddi/storport/nf-storport-storportreaddriverregistry)**.

- Stornvme supports more vendor-specific NVMe features and log pages. For more information, see the *[StorageAdapterProtocolSpecificPropertyEx](/windows-hardware/drivers/ddi/ntddstor/ne-ntddstor-storage_property_id)*, *[StorageDeviceProtocolSpecificPropertyEx](/windows-hardware/drivers/ddi/ntddstor/ne-ntddstor-storage_property_id)*, *[NVMeDataTypeLogPageEx](/windows-hardware/drivers/ddi/ntddstor/ne-ntddstor-_storage_protocol_nvme_data_type)*, and *[NVMeDataTypeFeatureEx](/windows-hardware/drivers/ddi/ntddstor/ne-ntddstor-_storage_protocol_nvme_data_type)* enum values. The [ntddstor.h](/windows-hardware/drivers/ddi/ntddstor/) header file contains usage guidance for these new property identifiers and data types as well as their associated input and output structures.

## Install

- **INF AddComClass directive**: An *AddComClass* directive is used within a `com-server-install-section` and registers a COM class.

- **INF AddComServer directive**: An *AddComServer* directive is used within a `DDInstall.COM` section and registers a COM server.

- **INF DDInstall.COM section**: The `DDInstall.COM` section contains one or more INF *AddComServer* directives that reference other INF-writer-defined sections in an INF file.

- The driver package INF registry conversion tool (`reg2inf.exe`) converts a registry key and its values or a COM .dll implementing a **[DllRegisterServer](/windows/win32/api/olectl/nf-olectl-dllregisterserver)** routine into a set of [INF AddReg directives](./install/inf-addreg-directive.md) or [INF DDInstall.COM section](./install/inf-ddinstall-com-section.md) for in-proc COM servers for inclusion into a driver package INF file.

## USB

- Support for USB superspeed information through **[IOCTL_USB_GET_NODE_CONNECTION_SUPERSPEEDPLUS_INFORMATION](/windows-hardware/drivers/ddi/usbioctl/ni-usbioctl-ioctl_usb_get_node_connection_superspeedplus_information)** and **[USB_NODE_CONNECTION_SUPERSPEEDPLUS_INFORMATION](/windows-hardware/drivers/ddi/usbioctl/ns-usbioctl-usb_node_connection_superspeedplus_information)**.

## Sensors

- Support for new human presence fields in proximity sensors through **[HUMAN_PRESENCE_DETECTION_TYPE](/windows-hardware/drivers/ddi/sensorsdef/ne-sensorsdef-human_presence_detection_type)** and **[PROXIMITY_SENSOR_CAPABILITIES](/windows-hardware/drivers/ddi/sensorsdef/ne-sensorsdef-proximity_sensor_capabilities)**.

- Humans presence updates include support for tracking multiple humans.

## Driver security  

Updates to the [Windows CodeQL rules](./devtest/codeql-windows-driver-rules.md) and updates to the [Driver security checklist](./driversecurity/driver-security-checklist.md).

## Windows debugging tools - WinDbg

Major new WinDbg features are listed here. For full details on the updates to WinDbg see [WinDbg Release Notes](./debuggercmds/windbg-release-notes.md). For general information about the debugging tools, see [What is WinDbg?](./debuggercmds/windbg-overview.md).

### Live Linux debugging

You can now live debug a Linux process. For more information, see these articles:

[Linux live remote process debugging](./debugger/linux-live-remote-process-debugging.md)

[Linux symbols and sources](./debugger/linux-dwarf-symbols.md)

### Other WinDbg updates and new features

- [Source Code Extended Access](./debugger/source-code-extended-access.md)

- [Open Enclave debugging](./debugger/open-enclave-debugging.md)

- [Ambiguous breakpoint resolution](./debugger/ambiguous-breakpoint-resolution.md)

- [WinDbg - Restricted Mode](./debugger/windbg-restricted-mode-preview.md)

- Improved [JavaScript Debugger Scripting - JavaScript Debugging](./debugger/javascript-debugger-scripting.md#javascript-debugging)

- Accessibility improvements

- Time Travel Debugging on ARM64

- Smart number selection and search

- New disassembly window

- Updates to [Supported Ethernet NICs for Network Kernel Debugging in Windows 11](./debugger/supported-ethernet-nics-for-network-kernel-debugging-in-windows-11.md)

- Expanded bug check information including new bug checks described in [Bug Check Code Reference](./debugger/bug-check-code-reference2.md)

## Related articles

For information on what was new for drivers in past Windows releases, see the following pages:

- [Driver development changes for Windows 11, version 23H2](driver-changes-for-windows-11-version-23h2.md)

- [Driver development changes for Windows 11, version 22H2](driver-changes-for-windows-11-version-22h2.md)

- [Driver development changes for Windows 11, version 21H2](driver-changes-for-windows-11-version-21h2.md)

- [Driver development changes for Windows Server 2022](driver-changes-for-windows-server-2022.md)

- [Driver development changes for Windows 10, version 2004](driver-changes-for-windows-10-version-2004.md)

[Back to Top](#top)
