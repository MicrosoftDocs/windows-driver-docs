---
title: High Definition Audio DDI
description: High Definition Audio DDI
keywords:
- HD Audio
- High Definition Audio (HD Audio)
- WDM audio drivers WDK , HD Audio
- audio drivers WDK , HD Audio
- Intel High Definition Audio Specification
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# High Definition Audio DDI


In Windows Vista, Microsoft will provide the following two drivers as part of the operating system:

-   A bus driver for managing an Intel High Definition Audio (HD Audio) bus interface controller.

-   A [Universal Audio Architecture](universal-audio-architecture.md) (UAA) class driver for managing a UAA-compliant audio codec (or possibly more than one codec) that is connected to an HD Audio controller.

Microsoft also will develop a similar HD Audio bus driver and UAA HD Audio class driver for systems that run Windows Server 2003, and Windows XP. For information about the HD Audio controller architecture, see the Intel High Definition Audio Specification at the [Intel HD Audio](https://www.intel.com/content/www/us/en/standards/intel-standards-and-initiatives.html) website. For an overview of Microsoft's UAA, see the white paper [Universal Audio Architecture](/previous-versions/windows/hardware/design/dn640534(v=vs.85)) website.

The HD Audio bus driver implements the HD Audio device driver interface (DDI), which kernel-mode audio and modem drivers use to communicate with hardware codecs that are attached to the HD Audio controller. The HD Audio bus driver exposes the HD Audio DDI to its children, which are instances of the audio and modem drivers that manage the codecs.

The version of the HD Audio bus driver that runs on Windows Server 2003 and Windows XP supports three variants of the HD Audio DDI:

-   A DDI that is defined by the [**HDAUDIO\_BUS\_INTERFACE**](/windows-hardware/drivers/ddi/hdaudio/ns-hdaudio-_hdaudio_bus_interface) structure. This DDI is identical to the HD Audio DDI in Windows Vista.

-   A DDI that is defined by the [**HDAUDIO\_BUS\_INTERFACE\_V2**](/windows-hardware/drivers/ddi/hdaudio/ns-hdaudio-_hdaudio_bus_interface_v2) structure. This DDI is available in Windows Vista and later versions of Windows.

-   A DDI that is defined by the [**HDAUDIO\_BUS\_INTERFACE\_BDL**](/windows-hardware/drivers/ddi/hdaudio/ns-hdaudio-_hdaudio_bus_interface_bdl) structure. This DDI is available in Windows XP and later versions of Windows.

The differences between the three DDIs are minor and are discussed in [Differences Between the HD Audio DDI Versions](differences-between-the-hd-audio-ddi-versions.md).

In Windows Vista, the HD Audio bus driver supports the DDI that is defined by the HDAUDIO\_BUS\_INTERFACE and the HDAUDIO\_BUS\_INTERFACE\_V2 structures.

In Windows Vista, Windows Server 2003 and Windows XP, the UAA class driver uses the DDI defined by the HDAUDIO\_BUS\_INTERFACE structure to manage UAA-compliant audio codecs. In addition, hardware vendors can choose to write custom device drivers that use one or both of these DDIs to manage their audio and modem codecs.

Hardware vendors should design their audio codecs to conform to the UAA hardware requirements document (to be published). In the absence of a custom audio driver from the vendor, users can rely on the system-supplied UAA HD Audio class driver to manage their UAA-compliant audio codecs. However, an audio codec might contain proprietary features that are accessible only through the vendor's custom driver.

This section describes the following information for both versions of the HD Audio DDI:

-   A background discussion of Intel's HD Audio architecture and Microsoft's UAA HD Audio class driver.

-   Programming guidelines for using both versions of the HD Audio DDI to control audio and modem codecs.

This section includes:

[HD Audio and UAA](hd-audio-and-uaa.md)

[HD Audio DDI Programming Guidelines](programming-guidelines.md)

 

