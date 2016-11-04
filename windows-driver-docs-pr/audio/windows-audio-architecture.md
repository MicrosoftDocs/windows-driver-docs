---
title: Windows Audio Architecture
description: This topic provided a high level summary of the Windows 10 audio architecture.
ms.assetid: 1FC95504-18AA-4F3B-8E96-005276699694
---

# Windows Audio Architecture


This topic provided a high level summary of the Windows 10 audio architecture.

## <span id="Windows_10_Audio_Stack_Diagram"></span><span id="windows_10_audio_stack_diagram"></span><span id="WINDOWS_10_AUDIO_STACK_DIAGRAM"></span>Windows 10 Audio Stack Diagram


This diagram provides a summary of the major elements of the Windows 10 audio stack.

![windows 10 audio stack diagram showing apps, audio engine, drivers and hardware ](images/audio-windows-10-stack-diagram.png)

## <span id="APIs"></span><span id="apis"></span><span id="APIS"></span>APIs


**Top level APIs**

The top level APIs are used for application development. These APIs are in currently in use and supported.

-   XAML [MediaElement class](https://msdn.microsoft.com/library/windows/apps/windows.ui.xaml.controls.mediaelement)(C#, VB, C++)
-   HTML [Audio object](https://msdn.microsoft.com/library/windows/apps/hh767373.aspx) and [Video object](https://msdn.microsoft.com/library/windows/apps/hh767390.aspx)&lt;tags&gt; (used by websites and Windows Web Apps)
-   [Windows.Media.Capture namespace](https://msdn.microsoft.com/library/windows/apps/xaml/windows.media.capture) (C#, VB, C++)
-   [Microsoft Media Foundation](https://msdn.microsoft.com/library/windows/desktop/ms694197) (C++)

These older APIs are deprecated.

-   [DirectShow](https://msdn.microsoft.com/library/windows/desktop/dd375454)
-   [DirectSound](https://msdn.microsoft.com/library/ee416960.aspx)
-   [PlaySound](https://msdn.microsoft.com/library/dd743680)
-   [Windows.Media.MediaControlContract](https://msdn.microsoft.com/library/windows/apps/dn706169)

**Low level APIs**

These lower level APIs are recommended for audio streaming.

-   [WASAPI](https://msdn.microsoft.com/library/windows/desktop/dd371455) (High performance, but more complicated)
-   [IXAudio2](https://msdn.microsoft.com/library/windows/desktop/ee415908) (Typically used for games)
-   [MIDI](https://msdn.microsoft.com/library/windows/desktop/dd742875)

This lower level API is recommended for enumeration.

-   [Windows.Devices.Enumeration](https://msdn.microsoft.com/library/windows/apps/br225459)

These APIs are not recommended for Windows applications.

-   [About MMDevice API](https://msdn.microsoft.com/library/windows/desktop/dd316556) (replaced by Windows.Devices.Enumeration)
-   [DeviceTopology API](https://msdn.microsoft.com/library/windows/desktop/dd370809)
-   [EndpointVolume API](https://msdn.microsoft.com/library/windows/desktop/dd370832)

## <span id="Audio_Engine"></span><span id="audio_engine"></span><span id="AUDIO_ENGINE"></span>Audio Engine


The audio engine consists of two related components, the Audio Device Graph (audiodg.exe), which loads the Audio Engine (audioeng.dll).

The audio engine:

-   Mixes and processes audio streams. For more information about how the audio engine uses buffers to transfer audio, see [Understanding the WaveRT Port Driver](understanding-the-wavert-port-driver.md).
-   Loads “Audio Processing Objects” (APOs), which are H/W-specific plugins that process the audio signal. For more information about APOs, see [Windows Audio Processing Objects](windows-audio-processing-objects.md).

## <span id="audio_service__audiosrv.dll_"></span><span id="AUDIO_SERVICE__AUDIOSRV.DLL_"></span>Audio Service (audiosrv.dll)


The audio service:

-   Is used to setup and control audio streams.
-   Implements Windows policies for background audio playback, ducking, etc.

## <span id="audio_endpoint_builder__audioendpointbuilder.exe_"></span><span id="AUDIO_ENDPOINT_BUILDER__AUDIOENDPOINTBUILDER.EXE_"></span>Audio Endpoint Builder (audioendpointbuilder.exe)


The Audio Endpoint Builder (audioendpointbuilder.exe):

-   Is used to discover new audio devices and create software audio endpoints. For more information about the algorithm that is used, see [Audio Endpoint Builder Algorithm](audio-endpoint-builder-algorithm.md).

## <span id="Audio_Drivers"></span><span id="audio_drivers"></span><span id="AUDIO_DRIVERS"></span>Audio Drivers


Audio drivers:

-   Follow the port-miniport model. For more information, see [WDM Audio Terminology](wdm-audio-terminology.md) and [Developing a WaveRT Miniport Driver](developing-a-wavert-miniport-driver.md).
-   Allow the audio stack to render and capture audio from several audio devices, including: integrated speakers and microphones, headsets/headphones, USB devices, Bluetooth devices, HDMI, etc.
-   The port-minport model corresponds to the Advanced Linux Sound Architecture – ALSA
-   For information on sample driver code, see [Sample Audio Drivers](sample-audio-drivers.md).

## <span id="Hardware"></span><span id="hardware"></span><span id="HARDWARE"></span>Hardware


The audio hardware that is present on any give device varies but can include:

-   Audio Codec
-   DSP (optional)
-   Integrated speakers, microphone, etc
-   External devices: USB audio devices, Bluetooth audio devices, HDMI audio, etc.
-   Signal processing can also be implemented in the H/W (e.g. the codec or the DSP), instead of or in addition to the APOs.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Windows%20Audio%20Architecture%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


