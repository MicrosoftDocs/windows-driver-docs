---
title: What's new in driver development
description: This section describes new features for driver development in Windows 10.
ms.date: 05/24/2021
ms.localizationpriority: medium
---

# <a name="top"></a>What's new in driver development

This section describes new features and updates for driver development in Windows Server 2022.

## Kernel DMA/MDL updates

New API pages:

* [*PCREATE_COMMON_BUFFER_FROM_MDL*](/windows-hardware/drivers/ddi/wdm/nc-wdm-pcreate-common-buffer-from-mdl) callback function
* [**DMA_COMMON_BUFFER_EXTENDED_CONFIGURATION_TYPE**](/windows-hardware/drivers/ddi/wdm/ne-wdm-_dma_common_buffer_extended_configuration_type) enumeration
* [**DMA_COMMON_BUFFER_EXTENDED_CONFIGURATION_ACCESS_TYPE**](/windows-hardware/drivers/ddi/wdm/ne-wdm-dma_common_buffer_extended_configuration_access_type) enumeration
* [**DMA_COMMON_BUFFER_EXTENDED_CONFIGURATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-dma_common_buffer_extended_configuration) structure

Updated:

* [**DMA_OPERATIONS**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_dma_operations) structure (new field **CreateCommonBufferFromMdl**)

## NetAdapterCx

* The new [NetAdapterCx platform-level device reset (PLDR)](./netcx/platform-level-device-reset.md) feature provides an effective way to reset and recover malfunctioning network devices without rebooting the system.

* NetAdapterCx support for the following hardware offloads has been updated:

    * [Checksum offload](./netcx/checksum-offload.md)

    *  [Generic send offload (GSO)](./netcx/gso-offload.md)

    * [Receive Segment Coalescing (RSC)](./netcx/rsc-offload.md)

## Networking

New network driver documentation and features include:

* The new [NDIS packet timestamping](./network/overview-of-ndis-packet-timestamping.md) feature supports the hardware timestamping capability of a network interface card (NIC) for the Precision Time Protocol (PTP) version 2.

* The new [NDIS Poll Mode](/windows-hardware/drivers/ddi/poll) feature is an OS controlled polling execution model that drives the network interface datapath.

* The [Virtual Machine Multiple Queues (VMMQ)](./network/overview-of-virtual-machine-multiple-queues.md) NIC offload technology extends Native RSS (RSSv1) to a Hyper-V virtual environment.

## Windows Driver Frameworks (WDF)

In Windows Server 2022, the Windows Driver Framework (WDF) includes Kernel-Mode Driver Framework (KMDF) version 1.33 and User-Mode Driver Framework (UMDF) version 2.33.

For info on what's included in these framework versions, see [What's New for WDF Drivers in Windows 10](./wdf/index.md).
To see what was added in previous versions of WDF, see:

* [KMDF Version History](./wdf/kmdf-version-history.md)
* [UMDF Version History](./wdf/umdf-version-history.md)

## Related Topics

For information on what was new for drivers in past Windows releases, see the following pages:

* [Driver development changes for Windows 10, version 2004](driver-changes-for-windows-10-version-2004.md)
* [Driver development changes for Windows 10, version 1903](driver-changes-for-windows-10-version-1903.md)
* [Driver development changes for Windows 10, version 1809](driver-changes-for-windows-10-version-1809.md)
* [Driver development changes for Windows 10, version 1803](driver-changes-for-windows-10-version-1803.md)

[Back to Top](#top)

## Deprecated features

The following table describes Windows driver development features that have been removed in Windows 10.

| Driver technology | Feature | Deprecated in |
|---|---|---|
| GNSS/Location | [Geolocation driver sample for Windows 8.1](./gnss/sensors-geolocation-driver-sample.md) and related documentation | Windows 10, version 1709 |
| Mobile Operator Scenarios (Networking) | [AllowStandardUserPinUnlock](./mobilebroadband/allowstandarduserpinunlock.md) | Windows 10, version 1709 |
| Scan/Image | [WSD (Web Services for Devices) Challenger](./image/challenging-a-disconnected-scanner-with-the-wsd-challenger.md) functionality and related documentation | Windows 10, version 1709 |
|Mobile Operators| Mobile broadband app experience apps with Sysdev metadata packages are deprecated in favor of MO UWP APPS and COSA. | Windows 10, version 1803|
