---
title: What's new in driver development
description: This section describes new features for driver development in Windows 10.
ms.date: 05/28/2021
ms.localizationpriority: medium
---

# <a name="top"></a>What's new in driver development

This section describes new features and updates for driver development in Windows Server 2022.

## Kernel 

### DMA/MDL updates

New API pages:

* [*PCREATE_COMMON_BUFFER_FROM_MDL*](/windows-hardware/drivers/ddi/wdm/nc-wdm-pcreate-common-buffer-from-mdl) callback function
* [**DMA_COMMON_BUFFER_EXTENDED_CONFIGURATION_TYPE**](/windows-hardware/drivers/ddi/wdm/ne-wdm-_dma_common_buffer_extended_configuration_type) enumeration
* [**DMA_COMMON_BUFFER_EXTENDED_CONFIGURATION_ACCESS_TYPE**](/windows-hardware/drivers/ddi/wdm/ne-wdm-dma_common_buffer_extended_configuration_access_type) enumeration
* [**DMA_COMMON_BUFFER_EXTENDED_CONFIGURATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-dma_common_buffer_extended_configuration) structure

Updated:

* [**DMA_OPERATIONS**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_dma_operations) structure (new field **CreateCommonBufferFromMdl**)

### NUMA (Non-Uniform Memory Access)

New API pages:

* [**KeQueryNodeActiveAffinity2**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kequerynodeactiveaffinity2)
* [**KeQueryNodeActiveProcessorCount**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kequerynodeactiveprocessorcount)

Updated:

* [**KeQueryNodeActiveAffinity**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kequerynodeactiveaffinity)
* [**xKeQueryLogicalProcessorRelationship**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kequerylogicalprocessorrelationship)


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

## Debugger

For information on what is new on the WinDbg Preview debugger, see [WinDbg Preview - What's New](./debugger/windbg-what-is-new-preview.md). Highlights include:

- [Portable PDB Symbols](./debugger/symbols-portable-pdb.md) support.
- [Support for Open Enclave debugging](./debugger/open-enclave-debugging.md)- WinDbg Preview can now debug Open Enclave (OE) applications.
- For user mode time travel debugging, a new timeline window displays a visual representation of important events in your trace: exceptions, breakpoints, function calls, and memory accesses. For more information, see [WinDbg Preview - Timeline](./debugger/windbg-timeline-preview.md).

Updates and addtions to debug transport topics, such as [Setting Up KDNET Network Kernel Debugging Automatically](./debugger/setting-up-a-network-debugging-connection-automatically.md), [Setting Up Kernel-Mode Debugging over USB EEM on an ARM device using KDNET](./debugger/setting-up-kernel-mode-debugging-over-usb-eem-arm-kdnet.md) and [Setting Up 2PF Kernel-Mode Debugging using KDNET](./debugger/setting-up-kernel-mode-debugging-using-2pf.md).

Bugcheck stop code topic addtions and updates, including listing live dump codes in a new section - 
[Kernel Live Dump Code Reference](./debugger/bug-check-code-reference-live-dump.md).


## Driver Quality

New [CodeQL and the Static Tools Logo Test](./devtest/static-tools-and-codeql.md) and [Supplemental Windows Driver CodeQL Queries](./devtest/codeql-windows-driver-rules.md).

Updates and additions to Driver Verfier rules, for example the new [DoubleFetch rule](./devtest/wdm-doublefetch.md). 

## Driver Security

Updates to the [Driver Security Checklist](./driversecurity/driver-security-checklist.md).

## Audio

Updated and new topics including:

- [Default Audio Endpoint Selection Starting in Windows 10](./audio/default-audio-endpoint-selection.md)
- [Multiple Voice Assistant](./audio/voice-activation-mva.md)
- [Voice Activation](./audio/voice-activation.md)
- [Low Latency Audio](./audio/low-latency-audio.md)

New online help for the [KsStudio Utility](./audio/ksstudio-utility.md).

## Related Topics

For information on what was new for drivers in past Windows releases, see the following pages:

* [Driver development changes for Windows 10, version 2004](driver-changes-for-windows-10-version-2004.md)
* [Driver development changes for Windows 10, version 1903](driver-changes-for-windows-10-version-1903.md)
* [Driver development changes for Windows 10, version 1809](driver-changes-for-windows-10-version-1809.md)
* [Driver development changes for Windows 10, version 1803](driver-changes-for-windows-10-version-1803.md)

[Back to Top](#top)
