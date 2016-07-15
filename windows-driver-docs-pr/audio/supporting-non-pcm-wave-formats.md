---
Description: 'Supporting Non-PCM Wave Formats'
MS-HAID: 'audio.supporting\_non\_pcm\_wave\_formats'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: 'Supporting Non-PCM Wave Formats'
---

# Supporting Non-PCM Wave Formats


## <span id="supporting_non_pcm_wave_formats"></span><span id="SUPPORTING_NON_PCM_WAVE_FORMATS"></span>


In Microsoft Windows 2000 and Windows 98, the WDM audio framework did not allow Windows clients to use the standard audio APIs (waveOut, DirectSound, and DirectShow) to play non-PCM audio data through the PortCls system driver.

This limitation has been removed in Microsoft Windows XP and later, and Windows Millennium Edition, which can play audio data encoded in a non-PCM format such as AC-3 or WMA Pro. In addition, a hot-fix package is available for Windows 98 SE that contains all fixes necessary to play non-PCM data through the waveOut and DirectSound APIs. Service Pack 2 for Windows 2000 also contains these fixes.

This section describes limitations in earlier versions of Windows that prevented clients from playing non-PCM audio, and presents a set of guidelines for adapting a WDM audio driver to support non-PCM data formats on more recent versions of Windows.

Additionally, this section describes the new subformat GUIDs in Windows 7 that provide support for compressed audio formats.

This section includes the following topics:

[Background of Non-PCM Support](background-of-non-pcm-support.md)

[Requirements for a Non-PCM Pin Factory](requirements-for-a-non-pcm-pin-factory.md)

[Subformat GUIDs for Compressed Audio Formats](subformat-guids-for-compressed-audio-formats.md)

[Converting Between Format Tags and Subformat GUIDs](converting-between-format-tags-and-subformat-guids.md)

[KS Topology Considerations](ks-topology-considerations.md)

[Specifics for waveOut Clients](specifics-for-waveout-clients.md)

[Specifics for DirectSound Clients](specifics-for-directsound-clients.md)

[S/PDIF Pass-Through Transmission of Non-PCM Streams](s-pdif-pass-through-transmission-of-non-pcm-streams.md)

[Specifying AC-3 Data Ranges](specifying-ac-3-data-ranges.md)

[Specifying WMA Pro Data Ranges](specifying-wma-pro-data-ranges.md)

[USB Audio Support for Non-PCM Formats](usb-audio-support-for-non-pcm-formats.md)

[Additional Requirements for Windows 98](additional-requirements-for-windows-98.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Supporting%20Non-PCM%20Wave%20Formats%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")


