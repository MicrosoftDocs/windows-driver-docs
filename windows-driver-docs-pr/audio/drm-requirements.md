---
title: DRM Requirements
description: DRM Requirements
ms.assetid: 312b943b-f280-4b29-a5d4-e78c7088bb22
keywords: ["WHQL testing WDK audio", "Digital Rights Management WDK audio , compliance testing", "DRM WDK audio , compliance testing", "compliance testing WDK audio", "testing DRM compliance WDK audio", "Designed for Windows XP logo test WDK audio", "logo tests WDK audio"]
---

# DRM Requirements


## <span id="drm_requirements"></span><span id="DRM_REQUIREMENTS"></span>


This section presents the requirements that an audio miniport driver must meet to pass DRM-compliance testing by Microsoft Windows Hardware Quality Lab (WHQL). These requirements apply specifically to WaveCyclic and WavePci [audio miniport drivers](audio-miniport-drivers.md), which are hardware-specific counterparts to the WavePci and WaveCyclic port drivers in the Port Class Library (Portcls.sys). DRM-compliance testing is not currently available for USB drivers.

In Windows Me and in Windows XP and later, only trusted audio drivers can play DRM-protected content. Windows identifies a trusted driver by means of a DRM-specific digital signature that is stored in the driver's .cat (catalog) files. Microsoft issues a DRM signature only for a driver that passes the DRM-compliance test as part of the hardware-compatibility testing administered by WHQL.

For Windows Me drivers, the DRM-compliance test is optional and is performed only at the hardware vendor's request. The DRM signature is separate from and in addition to the Windows-logo signature. Note that a driver that passes the Windows-logo test but not the DRM-compliance test still can play content that is not protected by DRM security.

For Windows XP and later, however, the DRM-compliance test is a required part of WHQL testing. A driver must pass the DRM-compliance test in order to qualify for the "Designed for Windows XP" logo.

The DRM-compliance test requires a trusted audio driver to do the following:

-   The audio miniport driver must implement the [IDrmAudioStream](https://msdn.microsoft.com/library/windows/hardware/ff536568) interface in its stream objects, which must return an object of type IDrmAudioStream if queried for IID\_IDrmAudioStream.

-   When copy protection is requested ([**DRMRIGHTS**](https://msdn.microsoft.com/library/windows/hardware/ff536355).**CopyProtect** = **TRUE**), the audio driver must disable the ability to capture the stream currently being played back. This means that the driver must not save the unprotected digital content to any form of nonvolatile storage, which includes hard disk, EEPROM, memory card, and memory stick. Also, the driver must disable the capture multiplexer on an output D/A converter and otherwise prevent the loopback of digital content.

-   When an audio driver is asked to disable the digital audio output on the device (DRMRIGHTS.**DigitalOutputDisable** = **TRUE**), it must disable all digital audio outputs that are capable of transmitting content over a standard interface through a standard interconnection scheme. Digital outputs include--but are not strictly limited to--S/PDIF, IEEE 1394, parallel, serial, modem, and network ports. (This requirement does not currently apply to USB.)

-   When handling secure content, an audio driver must never attach an untrusted driver to its stack. In other words, the audio driver must rely only on other components that also contain DRM signatures. The driver must never facilitate the transfer of audio data to any component that does not have a DRM signature. In particular, if a driver passes digital content to another component, the driver must use the DRM APIs in the kernel to inform the [DRMK system driver](kernel-mode-wdm-audio-components.md#drmk_system_driver) of this fact.

In addition to passing the DRM-compliance test, the audio device and driver must not allow a user to select a mode of operation that defeats or subverts the DRM components in the kernel. Specifically, the driver must not provide registry settings, user control panels, or other means of disabling the DRM functions.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20DRM%20Requirements%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


