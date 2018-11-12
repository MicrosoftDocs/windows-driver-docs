---
title: Implementation Issues for WavePci Devices
description: Implementation Issues for WavePci Devices
ms.assetid: c286d745-6e76-4540-98e6-a46ce1dd0f5d
keywords:
- WDM audio drivers WDK , WavePci
- audio drivers WDK , WavePci
- WavePci design guidelines WDK audio
- scatter/gather DMA WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Implementation Issues for WavePci Devices


## <span id="implementation_issues_for_wavepci_devices"></span><span id="IMPLEMENTATION_ISSUES_FOR_WAVEPCI_DEVICES"></span>


This section presents guidelines for hardware and software design that audio hardware vendors can use to improve the performance and reliability of their WavePci devices. All of these guidelines apply to audio devices and drivers that are designed to work with Microsoft Windows XP and later, but many also apply to earlier versions of Windows going back to Windows 98 Second Edition.

As discussed in [Wave Filters](wave-filters.md), the port class system driver, Portcls.sys, provides two different port drivers for wave rendering and capture devices:

-   WaveCyclic is less demanding of hardware and software, but its performance is limited by the software overhead of copying data between buffers.

-   WavePci is the performance-oriented alternative to WaveCyclic, but requires more sophisticated hardware and driver software.

Although the name WavePci implies an audio device that plugs into the PCI bus, in fact, the primary requirement for a WavePci device is that it contains a scatter/gather DMA controller capable of accessing data anywhere in system memory:

-   A typical WavePci device does reside on a PCI bus, but, in theory, at least, a WavePci miniport driver could be written for a device that resides on a system bus other than PCI (for example, AGP).

-   A wave device that resides on a PCI bus but lacks scatter/gather DMA can be represented by a WaveCyclic driver, but not by a WavePci driver.

Historically, some vendors have had difficulty in implementing fully functional WavePci devices. The two main problem areas are:

1.  Hardware design flaws that degrade performance.

2.  Driver implementation errors affecting performance or reliability.

This experience is distilled into the following topics, which address the key hardware and software design issues for WavePci devices:

[Hardware Requirements for WavePci Devices](hardware-requirements-for-wavepci-devices.md)

[Performance Issues for a WavePci Miniport Driver](performance-issues-for-a-wavepci-miniport-driver.md)

[Reliability Issues for a WavePci Miniport Driver](reliability-issues-for-a-wavepci-miniport-driver.md)

 

 




