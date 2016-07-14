---
Description: UAA Class Drivers
MS-HAID: 'audio.uaa\_class\_drivers'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: UAA Class Drivers
---

# UAA Class Drivers


In Windows Vista, Microsoft provides UAA class drivers for audio devices that connect to either an internal bus (PCI) or an external bus (IEEE 1394 or USB). To be supported by the UAA class driver for a particular bus, a device must conform to the UAA hardware specifications for that bus. For a device on an internal bus, the UAA hardware requirements document specifies the following:

-   The HD Audio controller's register set with the minor changes that are discussed in [UAA Extensions to the HD Audio Architecture](uaa-extensions-to-the-hd-audio-architecture.md).

-   The requirements for the HD Audio codec (to be published).

For information about the requirements for UAA devices on external buses or information about UAA class drivers, see the white paper titled *Universal Audio Architecture* at the [audio technology](http://go.microsoft.com/fwlink/p/?linkid=8751) website.

The remainder of this discussion refers only to the version of the UAA class driver that controls an audio device that connects to an internal bus, implements the HD Audio hardware registers, and controls a UAA-compliant HD Audio codec. This class driver is a child of the HD Audio bus driver and uses the bus driver's baseline HD Audio DDI to program the UAA-compliant hardware.

The UAA class driver for the HD Audio codec:

-   Provides the system with a device interface for an audio codec or codecs.

-   Collects information about the digital-to-audio converters, audio-to-digital converters, and jack-presence detection pins in the codecs that are present on the HD Audio Link.

-   Initializes the audio codec or codecs with third-party commands on startup.

-   Gets and sets audio properties in the audio codecs.

-   Provides a streaming interface (mapping a stream's cyclic buffer to user mode, setting up the codec and DMA engine, and handling properties such as link position).

-   Handles power management in the audio codecs.

This class driver does not provide:

-   A way of dynamically programming audio effects nodes in the codecs.

-   Combining functions across two or more codecs to form an aggregate audio or modem device.

-   Handling of general-purpose I/O (GPIO) pins on widgets unless they are explicitly defined in the UAA hardware requirements document.

-   A plug-in model for third-party code for either programming the codecs or providing software effects.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20UAA%20Class%20Drivers%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



