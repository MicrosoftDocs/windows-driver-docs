---
title: Sample Audio Drivers
description: Sample Audio Drivers
ms.assetid: bea50e70-e1ec-4a66-9bfc-8bd644b07ce7
keywords:
- WDM audio drivers WDK , sample drivers
- audio drivers WDK , sample drivers
- sample drivers WDK audio
- Ac97 sample audio driver WDK audio
- Dmusuart sample audio driver WDK audio
- Fmsynth sample audio driver WDK audio
- Gfx sample audio driver WDK audio
- Mpu401 sample audio driver WDK audio
- Msvad sample audio driver WDK audio
- Sb16 sample audio driver WDK audio
- Stdunk sample audio driver WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Sample Audio Drivers


## <span id="SYSVAD_Audio_Sample"></span><span id="sysvad_audio_sample"></span><span id="SYSVAD_AUDIO_SAMPLE"></span>SYSVAD Audio Sample


**System Virtual Audio Device Driver Sample (SYSVAD)**

The SYSVAD driver highlights many important features of the WDM audio architecture. These are working implementations with source code that can serve as a starting point for writing a custom driver for a proprietary audio device.

The *sysvad* solution file contains the following projects.

-   **TabletAudioSample**

    The *TabletAudioSample* project demonstrates how to develop a WDM audio driver that exposes support for multiple audio devices. Some of these audio devices are embedded (speakers, mic arrays) in the system while others are pluggable (headphone speaker/mic, Bluetooth headsets speaker/mic). The driver uses WaveRT and audio offloading for rendering devices. The driver uses a "virtual audio device" instead of an actual hardware-based adapter and highlights the different aspects of the audio offloading WDM audio driver architecture. For more information about the Windows audio engine, see [Hardware-Offloaded Audio Processing (Windows Drivers)](hardware-offloaded-audio-processing.md).

-   **PhoneAudioSample**

    The *PhoneAudioSample* project is very similar to the *TabletAudioSample* project. It includes optimizations for mobile devices.

-   **EndpointsCommon**

    The *EndpointsCommon* project contains common code to both the tablet and phone. For more information, see [Universal Windows Drivers for Audio](audio-universal-drivers.md).

-   **SwapAPO**

    The *SwapAPO* project demonstrates how to develop audio processing objects. It includes sample code that demonstrates how to register and unregister audio processing objects, and also shows how to customize a Control Panel property page to reflect the available features in the processing object. For more information, see [Windows Audio Processing Objects](windows-audio-processing-objects.md).

-   **KeywordDetectorAdapter**

    The *KeywordDetectorAdapter* project demonstrates how to develop a keyword detector adapter. For more information, see [Voice Activation](voice-activation.md).

**Download and extract the Sysvad audio sample from GitHub**

The SYSVAD audio sample is available on the [Windows Driver Samples GitHub](https://github.com/Microsoft/Windows-driver-samples).

You can browse the Sysvad audio sample here:

<https://github.com/Microsoft/Windows-driver-samples/tree/master/audio/sysvad>

Follow these steps to download and open the SYSVAD sample.

a. You can use GitHub tools to work with the samples. You can also download the universal driver samples in one zip file.

<https://github.com/Microsoft/Windows-driver-samples/archive/master.zip>

b. Download the master.zip file to your local hard drive.

c. Right click *Windows-driver-samples-master.zip*, and choose **Extract All**. Specify a new folder, or browse to an existing one that will store the extracted files. For example, you could specify *C:\\DriverSamples\\* as the new folder into which the files will be extracted.

d. After the files are extracted, navigate to the following subfolder.

*C:\\DriverSamples\\Audio\\Sysvad*

**Open the driver solution in Visual Studio**

In Microsoft Visual Studio, Click **File** &gt; **Open** &gt; **Project/Solution...** and navigate to the folder that contains the extracted files (for example, *C:\\DriverSamples\\Audio\\Sysvad*). Double-click the *Sysvad* solution file to open it.

In Visual Studio locate the Solution Explorer. (If this is not already open, choose **Solution Explorer** from the **View** menu.) In Solution Explorer, you can see one solution that has six projects.

## <span id="sample_audio_drivers"></span><span id="SAMPLE_AUDIO_DRIVERS"></span>Archived Audio Samples


These audio samples support previous versions of the Microsoft Windows Driver Kit (WDK). They are available as part of the zip file download available [here](https://go.microsoft.com/fwlink/p/?LinkId=618052).

-   **Microsoft Virtual Audio Device Driver Sample (Msvad)**

-   **AC97 Driver (Ac97)**

-   **DirectMusic UART Driver Sample (Dmusuart)**

-   **DirectMusic Software Synthesizer Sample (ddksynth)**

-   **FM Synthesizer (Fmsynth)**

-   **Audio Adapters Samples**

**Audio Processing Codec Samples**

-   **Msfilter Sample Codec (MsFilter)**

-   **Msgsm610 Sample Codec (gsm610)**

For details, see the readme documentation that accompanies each of these samples in the WDK.

For information on the WDK samples, see [Windows Driver Kit Samples Pack (Windows Drivers).](https://msdn.microsoft.com/library/windows/hardware/ff554118)

 

 




