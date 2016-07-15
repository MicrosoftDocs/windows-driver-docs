---
Description: Custom Audio Drivers
MS-HAID: 'audio.custom\_audio\_drivers'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Custom Audio Drivers
---

# Custom Audio Drivers


Audio devices that are not UAA-compatible require vendor-supplied custom drivers. In addition, a UAA-compatible audio adapter can incorporate proprietary features that are not supported by the UAA class drivers; these features are accessible to applications only if the vendor provides a custom audio driver. Only the standard UAA features are accessible through the system-supplied UAA drivers. For information about UAA-supported features, see the white paper titled Universal Audio Architecture on the [audio technology](http://go.microsoft.com/fwlink/p/?linkid=8751) page on the WHDC website.

Two options are available to hardware vendors for writing custom audio drivers: developing a custom audio-adapter driver for use with the PortCls system driver (Portcls.sys), or developing a custom minidriver for use with the AVStream class system driver (Ks.sys).

Most custom drivers for audio adapters use PortCls, which is supplied as part of the operating system. The PortCls system driver (Portcls.sys) contains a built-in audio-driver infrastructure that makes the task of writing a custom audio driver easier. PortCls implements several port drivers, each of which is specialized to manage the generic functions of a particular type of wave, MIDI, or mixer device. After selecting an appropriate set of port drivers to manage the audio functions on the audio adapter, the vendor develops a complementary set of miniport drivers that work in conjunction with the selected port drivers and control the hardware-dependent features of the audio devices.

The vendor can also support an audio device by developing a custom AVStream class minidriver. The minidriver works in conjunction with the AVStream class system driver, which is supplied as part of the operating system. Implementing an AVStream driver is more difficult than using PortCls, but doing so might still be appropriate for devices that integrate audio and video. An AVStream driver might also be necessary for an existing USB or IEEE 1394 audio device that fails to comply with the requirements of the system-supplied USBAudio or AVCAudio class system driver.

For nearly all PCI audio adapters that require vendor-supplied custom drivers, vendors should choose PortCls.

The AVStream class system driver (Ks.sys) lacks most of the audio-specific support functions that exist in PortCls.

For more information about PortCls, see [Introduction to Port Class](introduction-to-port-class.md). For more information about AVStream, see [AVStream Overview](stream.avstream_overview).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Custom%20Audio%20Drivers%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")


