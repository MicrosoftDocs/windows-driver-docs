---
title: Implementation Issues for WavePci Devices
description: Implementation Issues for WavePci Devices
ms.assetid: c286d745-6e76-4540-98e6-a46ce1dd0f5d
keywords: ["WDM audio drivers WDK , WavePci", "audio drivers WDK , WavePci", "WavePci design guidelines WDK audio", "scatter/gather DMA WDK audio"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Implementation%20Issues%20for%20WavePci%20Devices%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




