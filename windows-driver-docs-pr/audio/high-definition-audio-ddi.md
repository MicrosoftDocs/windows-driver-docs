---
Description: High Definition Audio DDI
MS-HAID: 'audio.high\_definition\_audio\_ddi'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: High Definition Audio DDI
---

# High Definition Audio DDI


In Windows Vista, Microsoft will provide the following two drivers as part of the operating system:

-   A bus driver for managing an Intel High Definition Audio (HD Audio) bus interface controller.

-   A [Universal Audio Architecture](universal-audio-architecture.md) (UAA) class driver for managing a UAA-compliant audio codec (or possibly more than one codec) that is connected to an HD Audio controller.

Microsoft also will develop a similar HD Audio bus driver and UAA HD Audio class driver for systems that run Windows Server 2003, and Windows XP. For information about the HD Audio controller architecture, see the Intel High Definition Audio Specification at the [Intel HD Audio](http://go.microsoft.com/fwlink/p/?linkid=42508) website. For an overview of Microsoft's UAA, see the white paper titled Universal Audio Architecture at the [audio technology](http://go.microsoft.com/fwlink/p/?linkid=8751) website.

The HD Audio bus driver implements the HD Audio device driver interface (DDI), which kernel-mode audio and modem drivers use to communicate with hardware codecs that are attached to the HD Audio controller. The HD Audio bus driver exposes the HD Audio DDI to its children, which are instances of the audio and modem drivers that manage the codecs.

The version of the HD Audio bus driver that runs on Windows Server 2003 and Windows XP supports three variants of the HD Audio DDI:

-   A DDI that is defined by the [**HDAUDIO\_BUS\_INTERFACE**](audio.hdaudio_bus_interface) structure. This DDI is identical to the HD Audio DDI in Windows Vista.

-   A DDI that is defined by the [**HDAUDIO\_BUS\_INTERFACE\_V2**](audio.hdaudio_bus_interface_v2) structure. This DDI is available in Windows Vista and later versions of Windows.

-   A DDI that is defined by the [**HDAUDIO\_BUS\_INTERFACE\_BDL**](audio.hdaudio_bus_interface_bdl) structure. This DDI is available in Windows XP and later versions of Windows.

The differences between the three DDIs are minor and are discussed in [Differences Between the HD Audio DDI Versions](differences-between-the-hd-audio-ddi-versions.md).

In Windows Vista, the HD Audio bus driver supports the DDI that is defined by the HDAUDIO\_BUS\_INTERFACE and the HDAUDIO\_BUS\_INTERFACE\_V2 structures.

In Windows Vista, Windows Server 2003 and Windows XP, the UAA class driver uses the DDI defined by the HDAUDIO\_BUS\_INTERFACE structure to manage UAA-compliant audio codecs. In addition, hardware vendors can choose to write custom device drivers that use one or both of these DDIs to manage their audio and modem codecs.

Hardware vendors should design their audio codecs to conform to the UAA hardware requirements document (to be published). In the absence of a custom audio driver from the vendor, users can rely on the system-supplied UAA HD Audio class driver to manage their UAA-compliant audio codecs. However, an audio codec might contain proprietary features that are accessible only through the vendor's custom driver.

This section describes the following information for both versions of the HD Audio DDI:

-   A background discussion of Intel's HD Audio architecture and Microsoft's UAA HD Audio class driver.

-   Programming guidelines for using both versions of the HD Audio DDI to control audio and modem codecs.

This section includes:

[HD Audio and UAA](hd-audio-and-uaa.md)

[Programming Guidelines](programming-guidelines.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20High%20Definition%20Audio%20DDI%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



