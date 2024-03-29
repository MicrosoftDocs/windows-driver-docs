---
title: What's New in Driver Development for Windows 11, Version 24H2
description: This section describes new features for driver development in Windows 11, version 24H2.
ms.date: 03/28/2024
---

# <a name="top"></a>What's new in driver development for Windows 11, version 24H2

This section describes new features and updates for driver development in Windows 11, version 24H2. To target this version of Windows, you can use [WDK xx.x.xxxxx.xxxx](./download-the-wdk.md) (released April 8, 2024).

## Audio

## Bluetooth Low Energy (LE) Audio

## Camera and streaming media

## Display and graphics drivers

GPUs are increasingly used in artificial intelligence and machine learning scenarios due to their computational power, parallel processing capabilities, and efficient handling of large datasets. Several new features are added to Windows Display Driver Model (WDDM) version 3.2 as optimizations to GPU/NPU usage, especially in cloud-based scenarios.

* [Dirty bit tracking](./display/dirty-bit-tracking.md) enhances the performance of VRAM data transfer between physical hosts during the live migration of virtual machines.

* [Live migration of heterogeneous GPU-P compute devices](.display/live-migration-on-gpup-devices.md) has been added. Significant content can now be transferred while virtualized resources are still active, reducing the pause time needed to complete a migration.

* A [GPU native fence synchronization object](.display/gpu-fence-synchronization-object.md) is added as an extension to the monitored fence object, supporting the following additional features:

  * GPU wait on monitored fence value, which allows for high performance engine-to-engine synchronization without requiring CPU round trips.
  * Conditional interrupt notification only for GPU fence signals that have CPU waiters, enabling substantial power savings.
  * Fence value storage in the GPU's local memory.

Additionally, the method that a user-mode or kernel-mode graphics driver uses to determine whether a particular WDDM feature is enabled has been updated. For more information, see [Querying WDDM feature support and enablement](./display/querying-wddm-feature-support-and-enablement.md).

## Dynamic lighting

## File system and filter drivers

* Starting in Windows 11, version 24H2, [bind links](/windows/win32/bindlink/) can be used to bind a file system namespace to a local "virtual path" through the Bind Filter (*bindflt.sys*). Minifilters can choose to veto such bind links on the system's boot partition. For more information, see [Vetoing a bind link](./ifs/vetoing-a-bind-link.md).

* *FltMgr* now provides [Query on Create support for USN and file security information](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltrequestsecurityinfooncreatecompletion).

## Human presence sensors

## Network drivers

UDP Receive Segment Coalescing Offload (URO) is a new hardware offload feature that enables network interface cards (NICs) to coalesce UDP receive segments.  For more information, see [UDP Receive Segment Coalescing Offload (URO)](./network/udp-rsc-offload.md) and [NetAdapterCx URO](./netcx/rsc-offload.md).

## Print devices

## Storage drivers

## USB

## Getting started

## Driver security  

## Windows debugging tools

## Related Topics

For information on what was new for drivers in past Windows releases, see the following pages:

* [Driver development changes for Windows 11, version 22H2](driver-changes-for-windows-11-version-22h2.md)
* [Driver development changes for Windows 11, version 21H2](driver-changes-for-windows-11-version-21h2.md)
* [Driver development changes for Windows Server 2022](driver-changes-for-windows-server-2022.md)
* [Driver development changes for Windows 10, version 2004](driver-changes-for-windows-10-version-2004.md)

[Back to Top](#top)
