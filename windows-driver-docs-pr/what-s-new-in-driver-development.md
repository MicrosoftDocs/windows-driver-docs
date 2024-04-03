---
title: What's New in Driver Development for Windows 11, Version 24H2
description: This section describes new features for driver development in Windows 11, version 24H2.
ms.date: 04/02/2024
---

# <a name="top"></a>What's new in driver development for Windows 11, version 24H2

This section describes new features and updates for driver development in Windows 11, version 24H2. To target this version of Windows, you can use [WDK xx.x.xxxxx.xxxx](./download-the-wdk.md) (released April 8, 2024).

## Audio

## Bluetooth Low Energy (LE) Audio

## Camera and streaming media

Three new camera articles for Windows 11, version 24H2 (also applies to Windows 11, version 23H2):

- [Camera settings page](./stream/camera-settings-page.md) - Describes the features and operation of the camera settings page in Windows 11, and the default values framework that allows configuration of the camera configuration applied when an application starts the camera.

- [Camera companion apps](./stream/camera-companion-apps.md)

- [Network cameras](./stream/network-cameras.md)

## Display and graphics drivers

GPUs are increasingly used in artificial intelligence and machine learning scenarios due to their computational power, parallel processing capabilities, and efficient handling of large datasets. Several new features are added to Windows Display Driver Model (WDDM) version 3.2 as optimizations to GPU/NPU usage, especially in cloud-based scenarios.

- [Dirty bit tracking](./display/dirty-bit-tracking.md) enhances the performance of VRAM data transfer between physical hosts during the live migration of virtual machines.

- [Live migration of heterogeneous GPU-P compute devices](./display/live-migration-on-gpup-devices.md) has been added. Significant content can now be transferred while virtualized resources are still active, reducing the pause time needed to complete a migration.

<<<<<<< HEAD
- A [GPU native fence synchronization object](./display/gpu-fence-synchronization-object.md) is added as an extension to the monitored fence object, supporting the following additional features:
=======
- A [GPU native fence synchronization object](./display/native-gpu-fence-objects.md) is added as an extension to the monitored fence object, supporting the following additional features:
>>>>>>> release-copper

  - GPU wait on monitored fence value, which allows for high performance engine-to-engine synchronization without requiring CPU round trips.
  - Conditional interrupt notification only for GPU fence signals that have CPU waiters, enabling substantial power savings.
  - Fence value storage in the GPU's local memory.

Other added WDDM 3.2 features:

- The method that a user-mode or kernel-mode graphics driver uses to determine whether a particular WDDM feature is enabled has been updated. For more information, see [Querying WDDM feature support and enablement](./display/querying-wddm-feature-support-and-enablement.md).

- TDR (timeout detection and recovery) debugging has been enhanced to provide more information about the cause of a TDR event. For more information, see [TDR debuggability improvements](./display/tdr-debuggability-improvements.md).

## Dynamic lighting

## File system and filter drivers

- Starting in Windows 11, version 24H2, [bind links](/windows/win32/bindlink/) can be used to bind a file system namespace to a local "virtual path" through the Bind Filter (*bindflt.sys*). Minifilters can choose to veto such bind links on the system's boot partition. For more information, see [Vetoing a bind link](./ifs/vetoing-a-bind-link.md).

- *FltMgr* now provides [Query on Create support for USN and file security information](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltrequestsecurityinfooncreatecompletion).

## Human presence sensors

## Network drivers

Starting in Windows 11, version 24H2, you can write a [User-Mode Driver Framework (UMDF) NetAdapterCx](netcx/user-mode-netcx.md) driver. The UMDF APIs in NetAdapterCx align with the KMDF versions, so you can convert your KMDF-based client driver to UMDF with little to no code changes.

UDP Receive Segment Coalescing Offload (URO) is a new hardware offload feature that enables network interface cards (NICs) to coalesce UDP receive segments.  For more information, see [UDP Receive Segment Coalescing Offload (URO)](network/udp-rsc-offload.md) and [NetAdapterCx URO](netcx/rsc-offload.md).

## Kernel

Four new *wdm.h* power management DDIs for Windows 11, version 24H2:

- **[PO_EFFECTIVE_POWER_MODE_CALLBACK](/windows-hardware/drivers/ddi/wdm/nc-wdm-po_effective_power_mode_callback)** callback function - Invoked with the current value of the power setting immediately after registration.

- **[PO_EFFECTIVE_POWER_MODE](/windows-hardware/drivers/ddi/wdm/ne-wdm-po_effective_power_mode)** enumeration - Enumerates the effective power modes.

- **[PoRegisterForEffectivePowerModeNotifications](/windows-hardware/drivers/ddi/wdm/nf-wdm-poregisterforeffectivepowermodenotifications)** function - Registers a callback to receive effective power mode change notifications.

- **[PoUnregisterFromEffectivePowerModeNotifications](/windows-hardware/drivers/ddi/wdm/nf-wdm-pounregisterfromeffectivepowermodenotifications)** function - Unregisters from effective power mode change notifications.

## Storage drivers

A storport miniport driver can now read configuration data from more locations within the registry. For more information, see **[StorPortReadRegistryKey](/windows-hardware/drivers/ddi/storport/nf-storport-storportreadregistrykey)** and **[StorPortReadDriverRegistry](/windows-hardware/drivers/ddi/storport/nf-storport-storportreaddriverregistry)**.

Stornvme supports more vendor-specific NVMe features and log pages. For more information, see the *[StorageAdapterProtocolSpecificPropertyEx](/windows-hardware/drivers/ddi/ntddstor/ne-ntddstor-storage_property_id)*, *[StorageDeviceProtocolSpecificPropertyEx](/windows-hardware/drivers/ddi/ntddstor/ne-ntddstor-storage_property_id)*, *[NVMeDataTypeLogPageEx](/windows-hardware/drivers/ddi/ntddstor/ne-ntddstor-_storage_protocol_nvme_data_type)*, and *[NVMeDataTypeFeatureEx](/windows-hardware/drivers/ddi/ntddstor/ne-ntddstor-_storage_protocol_nvme_data_type)* enum values. The [ntddstor.h](/windows-hardware/drivers/ddi/ntddstor/) header file contains usage guidance for these new property identifiers and data types as well as their associated input and output structures.

## USB

## Getting started

## Driver security  

## Windows debugging tools

## Related Topics

For information on what was new for drivers in past Windows releases, see the following pages:

- [Driver development changes for Windows 11, version 22H2](driver-changes-for-windows-11-version-22h2.md)
- [Driver development changes for Windows 11, version 21H2](driver-changes-for-windows-11-version-21h2.md)
- [Driver development changes for Windows Server 2022](driver-changes-for-windows-server-2022.md)
- [Driver development changes for Windows 10, version 2004](driver-changes-for-windows-10-version-2004.md)

[Back to Top](#top)
