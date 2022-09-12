---
title: Multiple Voice Assistant
description: The Multiple Voice Assistant platform provides support for additional voice assistants beyond Cortana. 
ms.date: 09/08/2020
---

# Multiple Voice Assistant

The Multiple Voice Assistant platform provides support for additional voice assistants beyond Cortana. This allows other assistants be available on Windows devices such as PCs and wearables like HoloLens. Multiple voice assistants can be active on the same device using a set of supported keyword patterns.

For information about implementing Windows Cortana, see [Voice Activation](voice-activation.md).

> [!NOTE]
> Multiple Voice Assistant is supported starting with Windows 10 Version 1903.
>

## Voice Activation

Voice activation is a feature that enables users to invoke a speech recognition engine from various device power states by saying a specific phrase.

Implementing voice activation is a significant project and is a task completed by SoC vendors. OEMs can contact their SoC vendor for information on their SoC's implementation of voice activation.

Voice activation allows users to quickly engage the voice assistant experience outside of their active context (i.e., what is currently on screen) by using their voice. Users often want to be able to instantly access an experience without having to physically interact with or touch a device. For an Xbox user this may be from not wanting to find and connect a controller. For PC users, they might want rapid access to an experience without having to perform multiple mouse, touch and/or keyboard actions, as in the case of a computer in the kitchen.

Voice activation is powered by a keyword spotter (KWS) which reacts if the key phrase is detected. Key phrases may include key words such as "Hey Contoso." *Keyword detection* describes the detection of the keyword by either hardware or software.
Key phrases may be uttered by themselves ("Hey Contoso") as a staged command, or followed by a speech action composing a chained command ("Hey Contoso, where is my next meeting?")

Microsoft provides an OS default keyword spotter (software keyword spotter) to provide voice assistant experience in cases where hardware keyword detection is unavailable. While this is currently available for Cortana, additional Microsoft configuration may be needed to onboard other voice assistants to do two-stage keyword detection. For more information contact `AskMVA@Microsoft.com`.  

If KWS is to wake the device from a low powered state, the solution is known as Wake-on-Voice (WoV). For more information, see [Wake on Voice](#wake-on-voice).

## Glossary of Terms

This glossary summarizes terms related to voice activation.

|Term|Example/definition|
|----|----|
| Staged Command | Example: Hey Contoso <pause, wait for assistant UI> What's the weather? This is sometimes referred to as "two-shot command" or "keyword-only" |
| Chained Command | Example: Hey Contoso what's the weather? This is sometimes referred to as a "one-shot command" |
| Voice Activation | Example: "Hey Contoso" The scenario where keyword is detected in a predefined activation key phrase |
| Wake-on-Voice (WoV) | Technology that enables voice activation from a screen off, lower power state, to a screen on full power state |
|WoV from Modern Standby| Wake-on-Voice from a Modern Standby (S0ix) screen off state to a screen on full power (S0) state |
| Modern Standby | Windows Low Power Idle infrastructure - successor to Connected Standby (CS) in Windows 10. The first state of modern standby is when the screen is off. The deepest sleep state is when in DRIPS/Resiliency. For more information, see [Modern Standby](/windows-hardware/design/device-experiences/modern-standby)|
| KWS | Keyword spotter – the algorithm that provides the detection of "Hey Contoso" |
| SW KWS | Software keyword spotter – an implementation of KWS that runs on the host (CPU). For "Hey Cortana", SW KWS is included as part of Windows. |
| HW KWS | Hardware keyword spotter – an implementation of KWS that runs offloaded on hardware |
| Burst buffer | A circular buffer used to store PCM data that can be bursted up in the event of a KWS detection, so that all audio that triggered a KWS detection is included |
| Event detector OEM Adapter | A user mode component that acts as an intermediary between the Windows voice assistant stack and driver |
| Model | The acoustic model data file used by the KWS algorithm. The data file is static. Models are localized, one per locale.|
| MVA | Multiple Voice Agent - new HWKWS DDI which supports multiple agents |
| SVA | Single Voice Agent - previous HWKWS DDI which only supports a single agent (Cortana) |

## Integrating a Hardware Keyword Spotter

To implement a hardware keyword spotter (HW KWS) SoC vendors must complete the following tasks.

- Create a custom keyword detector based on the SYSVAD sample described later in this topic. You will implement these methods in a COM DLL, described in [IEvent Detector OEM Adapter Interface](/windows-hardware/drivers/ddi/eventdetectoroemadapter/nn-eventdetectoroemadapter-ieventdetectoroemadapter).
- Implement WAVE RT enhancements described in [WAVERT Enhancements](#wavert-enhancements).
- Provide INF file entries to describe any custom APOs used for keyword detection.
  - [PKEY\_FX\_KeywordDetector\_StreamEffectClsid](./pkey-fx-keyworddetector-streameffectclsid.md)
  - [PKEY\_FX\_KeywordDetector\_ModeEffectClsid](./pkey-fx-keyworddetector-modeeffectclsid.md)
  - [PKEY\_FX\_KeywordDetector\_EndpointEffectClsid](./pkey-fx-keyworddetector-endpointeffectclsid.md)
  - [PKEY\_SFX\_KeywordDetector\_ProcessingModes\_Supported\_For\_Streaming](./pkey-sfx-keyworddetector-processingmodes-supported-for-streaming.md)
  - [PKEY\_MFX\_KeywordDetector\_ProcessingModes\_Supported\_For\_Streaming](./pkey-mfx-keyworddetector-processingmodes-supported-for-streaming.md)
  - [PKEY\_EFX\_KeywordDetector\_ProcessingModes\_Supported\_For\_Streaming](./pkey-efx-keyworddetector-processingmodes-supported-for-streaming.md)
- Review the hardware recommendations and test guidance in [Audio Device Recommendation](/windows-hardware/design/component-guidelines/audio). This topic provides guidance and recommendations for the design and development of audio input devices intended for use with Microsoft's Speech Platform.
- Support both staged and chained commands.
- Meet locale requirements of voice assistants
- The APOs (Audio Processing Objects) must provide the following effects:
  - AEC
  - AGC
  - NS
- Effects for Speech processing mode must be reported by the MFX APO.
- The APO may perform format conversion as MFX.
- The APO must output the following format:
  - 16 kHz, mono, FLOAT.
- Optionally design any custom APOs to enhance the audio capture process. For more information, see [Windows Audio Processing Objects](windows-audio-processing-objects.md).

Hardware-offloaded keyword spotter (HW KWS) WoV Requirements

- HW KWS WoV is supported during S0 Working state and S0 sleep state also known as Modern Standby.
- HW KWS WoV is not supported from S3.  

### AEC

AEC can be performed by the DSP at the time the burst audio is captured, or it can be done at a later time via a software APO. In order to perform a software AEC with KWS burst data, it is necessary to have the corresponding loopback audio from the time the burst data was captured. To do this a custom audio format for the burst output was created which interleaves the loopback audio into the burst audio data.

Starting with Windows version 20H1, the Microsoft AEC APO is aware of this interleaved format and can use it to perform the AEC. For more information, see [KSPROPERTY_INTERLEAVEDAUDIO_FORMATINFORMATION](./ksproperty-interleavedaudio-formatinformation.md).

### Validation

Validate HW support for [KSPROPSETID_SoundDetector2](kspropsetid-sounddetector2.md) properties with [Voice Activation Manager 2 tests](/windows-hardware/test/hlk/testref/5119a80f-8aae-49bb-aa59-8eaa7e7b1fad).

## Sample Code Overview

There is sample code for an audio driver that implements voice activation on GitHub as part of the SYSVAD virtual audio adapter sample. It is recommended to use [this code](https://github.com/Microsoft/Windows-driver-samples/tree/main/audio/sysvad/) as a starting point.

For more information about the SYSVAD sample audio driver, see [Sample Audio Drivers](./sample-audio-drivers.md).

## Keyword Recognition System Information

### Voice Activation Audio Stack Support

The audio stack external interfaces for enabling Voice Activation serves as the communication pipeline for the speech platform and the audio drivers. The external interfaces are divided into three parts.

- [*Event detector Device Driver Interface (DDI)*](/windows-hardware/drivers/ddi/eventdetectoroemadapter/nn-eventdetectoroemadapter-ieventdetectoroemadapter). The Event detector Device Driver Interface is responsible for configuring and arming the HW Keyword Spotter (KWS).  It is also used by the driver to notify the system of a detection event.
- [*IEvent Detector OEM Adapter DLL*](/windows-hardware/drivers/ddi/eventdetectoroemadapter/nn-eventdetectoroemadapter-ieventdetectoroemadapter). This DLL implements a COM interface to adapt the driver specific opaque data for use by the OS to assist with keyword detection.
- *WaveRT streaming enhancements*. The enhancements enable the audio driver to burst stream the buffered audio data from the keyword detection.

### Audio Endpoint Properties

Audio endpoint graph building occurs normally. The graph is prepared to handle faster than real time capture. Timestamps on captured buffers remain true. Specifically, the timestamps will correctly reflect data that was captured in the past and buffered, and is now bursting.

### Theory of Operation

The driver exposes a KS filter for its capture device as usual. This filter supports several KS properties and a KS event to configure, enable and signal a detection event. The filter also includes an additional pin factory identified as a keyword spotter (KWS) pin. This pin is used to stream audio from the keyword spotter.

The property is: [**KSPROPSETID_SoundDetector2**](kspropsetid-sounddetector2.md)

All [**KSPROPSETID_SoundDetector2**](kspropsetid-sounddetector2.md) properties are called with a [KSSOUNDDETECTORPROPERTY](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-kssounddetectorproperty)  data structure. This data structure contains a KSPROPERTY and the event id for the keyword to be armed, reset, detected, etc.

- Supported keyword types - [**KSPROPERTY\_SOUNDDETECTOR\_PATTERNS**](./ksproperty-sounddetector.md). This property is set by the operating system to configure the keywords to be detected.
- List of keyword patterns GUIDs - [**KSPROPERTY\_SOUNDDETECTOR\_SUPPORTEDPATTERNS**](./ksproperty-sounddetector.md). This property is used to get a list of GUIDs that identify the types of supported patterns.
- Armed - [**KSPROPERTY\_SOUNDDETECTOR\_ARMED**](./ksproperty-sounddetector.md). This read/write property is a simply Boolean status indicating whether the detector is armed. The OS sets this to engage the keyword detector. The OS can clear this to disengage. The driver automatically clears this when keyword patterns are set and also after a keyword is detected. (The OS must rearm.)
- Match result - [**KSPROPERTY\_SOUNDDETECTOR\_RESET**](ksproperty-sounddetector-reset.md) is used to reset the sound detector at startup time.

At keyword detection time, a PNP notification containing KSNOTIFICATIONID_SoundDetector is sent. NOTE: this is not a KSEvent, but rather a PNP event which is sent, with a payload, via IoReportTargetDeviceChangeAsynchronous.

KSNOTIFICATIONID_SoundDetector is defined in ksmedia.h as shown here.

```cpp
// The payload of this notification is a SOUNDDETECTOR_PATTERNHEADER
#define STATIC_KSNOTIFICATIONID_SoundDetector\
    0x6389d844, 0xbb32, 0x4c4c, 0xa8, 0x2, 0xf4, 0xb4, 0xb7, 0x7a, 0xfe, 0xad
DEFINE_GUIDSTRUCT("6389D844-BB32-4C4C-A802-F4B4B77AFEAD", KSNOTIFICATIONID_SoundDetector);
#define KSNOTIFICATIONID_SoundDetector DEFINE_GUIDNAMED(KSNOTIFICATIONID_SoundDetector)
```

### Sequence of Operation

#### System Startup

1. The OS sends a [**KSPROPERTY\_SOUNDDETECTOR\_RESET**](ksproperty-sounddetector-reset.md) to clear any previous detector state, resetting all detectors to disarmed and clearing previous patterns set.
2. The OS queries [**KSPROPERTY\_SOUNDDETECTOR\_PATTERNS**](./ksproperty-sounddetector.md) to retrieve the clsid for the event detector OEM adapter.
3. The OS uses the event detector oem adapter to retrieve the list of supported keywords and languages.
4. The OS registers for custom PNP notifications sent by the driver
5. The OS sets the required keyword pattern(s).
6. The OS arms the detector(s)

### Internal Driver and Hardware Operation

While the detector is armed, the hardware can be continuously capturing and buffering audio data in a small FIFO buffer. (The size of this FIFO buffer is determined by requirements outside of this document, but might typically be hundreds of milliseconds to several seconds.) The detection algorithm operates on the data streaming through this buffer. The design of the driver and hardware are such that while armed there is no interaction between the driver and hardware and no interrupts to the "application" processors until a keyword is detected. This allows the system to reach a lower power state if there is no other activity.

When the hardware detects a keyword, it generates an interrupt. While waiting for the driver to service the interrupt, the hardware continues to capture audio into the buffer, ensuring no data after the keyword is lost, within buffering limits.

### Keyword Timestamps

After detecting a keyword, all voice activation solutions must buffer all of the spoken keyword, including 1.6s before the start of the keyword. The audio driver must provide timestamps identifying the start and end of the key phrase in the stream.

In order to support the keyword start/end timestamps, DSP software may need to internally timestamp events based on a DSP clock. Once a keyword is detected, the DSP software interacts with the driver to prepare a KS event. The driver and DSP software will need to map the DSP timestamps to a Windows performance counter value. The method of doing this is specific to the hardware design. One possible solution is for the driver to read current performance counter, query the current DSP timestamp, read current performance counter again, and then estimate a correlation between performance counter and DSP time. Then given the correlation, the driver can map the keyword DSP timestamps to Windows performance counter timestamps.

## IEvent Detector OEM Adapter Interface

The OEM supplies a COM object implementation that acts as an intermediary between the OS and the driver, helping to compute or parse the opaque data that is written and read to the audio driver through [**KSPROPERTY\_SOUNDDETECTOR\_PATTERNS**](./ksproperty-sounddetector-patterns.md) and [**KSPROPERTY\_SOUNDDETECTOR\_MATCHRESULT**](./ksproperty-sounddetector-matchresult.md).

The CLSID of the COM object is a detector pattern type GUID returned by the [**KSPROPERTY\_SOUNDDETECTOR\_SUPPORTEDPATTERNS**](./ksproperty-sounddetector-supportedpatterns.md). The OS calls CoCreateInstance passing the pattern type GUID to instantiate the appropriate COM object that is compatible with keyword pattern type and calls methods on the object's IEventDetectorOemAdapter interface.

### COM Threading Model requirements

The OEM's implementation may choose any of the COM threading models.

### IEventDetectorOemAdapter

The interface design attempts to keep the object implementation stateless. In other words, the implementation should require no state to be stored between method calls. In fact, internal C++ classes likely do not need any member variables beyond those required to implement a COM object in general.

### Methods

Implement the following methods.

- [**IEventDetectorOemAdapter::BuildArmingPatternData**](/windows-hardware/drivers/ddi/eventdetectoroemadapter/nf-eventdetectoroemadapter-ieventdetectoroemadapter-buildarmingpatterndata)
- [**IEventDetectorOemAdapter::ComputeAndAddUserModelData**](/windows-hardware/drivers/ddi/eventdetectoroemadapter/nf-eventdetectoroemadapter-ieventdetectoroemadapter-computeandaddusermodeldata)
- [**IEventDetectorOemAdapter::GetCapabilities**](/windows-hardware/drivers/ddi/eventdetectoroemadapter/nf-eventdetectoroemadapter-ieventdetectoroemadapter-getcapabilities)
- [**IEventDetectorOemAdapter::GetCapabilitiesForLanguage**](/windows-hardware/drivers/ddi/eventdetectoroemadapter/nf-eventdetectoroemadapter-ieventdetectoroemadapter-getcapabilitiesforlanguage)
- [**IEventDetectorOemAdapter::ParseDetectionResultData**](/windows-hardware/drivers/ddi/eventdetectoroemadapter/nf-eventdetectoroemadapter-ieventdetectoroemadapter-parsedetectionresultdata)
- [**IEventDetectorOemAdapter::ReportOSDetectionResult**](/windows-hardware/drivers/ddi/eventdetectoroemadapter/nf-eventdetectoroemadapter-ieventdetectoroemadapter-parsedetectionresultdata)
- [**IEventDetectorOemAdapter::VerifyUserEventData**](/windows-hardware/drivers/ddi/eventdetectoroemadapter/nf-eventdetectoroemadapter-ieventdetectoroemadapter-verifyusereventdata)

## WAVERT Enhancements

Miniport interfaces are defined to be implemented by WaveRT miniport drivers. These interfaces provide methods to either simplify the audio driver, improve OS audio pipeline performance and reliability, or support new scenarios. A new PnP device interface property is defined allowing the driver to provide a static expressions of its buffer size constraints to the OS.

### Buffer Sizes

A driver operates under various constraints when moving audio data between the OS, the driver, and the hardware. These constraints may be due to the physical hardware transport that moves data between memory and hardware, and/or due to the signal processing modules within the hardware or associated DSP.

HW-KWS solutions must support audio capture sizes of at least 100ms and up to 200ms.

The driver expresses the buffer size constraints by setting the DEVPKEY\_KsAudio\_PacketSize\_Constraints2 device property on the KSCATEGORY\_AUDIO PnP device interface of the KS filter that has the KS streaming pin(s). This property should remain valid and stable while the KS filter interface is enabled. The OS can read this value at any time without having to open a handle to the driver and call on the driver.

### DEVPKEY\_KsAudio\_PacketSize\_Constraints2

The DEVPKEY\_KsAudio\_PacketSize\_Constraints2 property value contains a [**KSAUDIO\_PACKETSIZE\_CONSTRAINTS2**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ksaudio_packetsize_constraints2) structure describing the physical hardware constraints (i.e. due to the mechanics of transferring data from the WaveRT buffer to the audio hardware). The structure includes an array of 0 or more [**KSAUDIO\_PACKETSIZE\_PROCESSINGMODE\_CONSTRAINT**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ksaudio_packetsize_signalprocessingmode_constraint) structures describing constraints specific to any signal processing modes. The driver sets this property before calling [**PcRegisterSubdevice**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcregistersubdevice) or otherwise enabling its KS filter interface for its streaming pins.

### IMiniportWaveRTInputStream

A driver implements this interface for better coordination of audio dataflow from the driver to OS. If this interface is available on a capture stream, the OS uses methods on this interface to access data in the WaveRT buffer. For more information see, [**IMiniportWaveRTInputStream::GetReadPacket**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportwavertinputstream-getreadpacket)

### IMiniportWaveRTOutputStream

A WaveRT miniport optionally implements this interface to be advised of write progress from the OS and to return precise stream position. For more information see [**IMiniportWaveRTOutputStream::SetWritePacket**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportwavertoutputstream-setwritepacket), [**IMiniportWaveRTOutputStream::GetOutputStreamPresentationPosition**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportwavertoutputstream-getoutputstreampresentationposition) and [**IMiniportWaveRTOutputStream::GetPacketCount**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportwavertoutputstream-getpacketcount).

### Performance counter timestamps

Several of the driver routines return Windows performance counter timestamps reflecting the time at which samples are captured or presented by the device.

In devices that have complex DSP pipelines and signal processing, calculating an accurate timestamp may be challenging and should be done thoughtfully. The timestamps should not simply reflect the time at which samples were transferred to or from the OS to the DSP.

- Within the DSP, track sample timestamps using some internal DSP wall clock.
- Between the driver and DSP, calculate a correlation between the Windows performance counter and the DSP wall clock. Procedures for this can range from very simple (but less precise) to fairly complex or novel (but more precise).
- Factor in any constant delays due to signal processing algorithms or pipeline or hardware transports, unless these delays are otherwise accounted for.

### Burst Read Operation

This section describes the OS and driver interaction for burst reads. Burst read can happen outside of the voice activation scenario as long as the driver supports the packet based streaming WaveRT model, including the [**IMiniportWaveRTInputStream::GetReadPacket**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportwavertinputstream-getreadpacket) function.

Two burst example read scenarios are discussed. In one scenario, if the miniport supports a pin having pin category [**KSNODETYPE\_AUDIO\_KEYWORDDETECTOR**](./ksnodetype-audio-keyworddetector.md) then the driver will begin capturing and internally buffering data when a keyword is detected. In another scenario, the driver can optionally internally buffer data outside of the WaveRT buffer if the OS is not reading data quickly enough by calling [**IMiniportWaveRTInputStream::GetReadPacket**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportwavertinputstream-getreadpacket).

To burst data that has been captured prior to transition to KSSTATE\_RUN, the driver must retain accurate sample timestamp information along with the buffered capture data. The timestamps identify the sampling instant of the captured samples.

1. After the stream transitions to KSSTATE\_RUN, the driver immediately sets the buffer notification event because it already has data available.
2. On this event, the OS calls GetReadPacket() to get information about the available data.

    a. The driver returns the packet number of the valid captured data (0 for the first packet after the transition from KSSTATE\_STOP to KSSTATE\_RUN), from which the OS can derive the packet position within the WaveRT buffer as well as the packet position relative to start of stream.

    b. The driver also returns the performance counter value that corresponds to the sampling instant of the first sample in the packet. Note that this performance counter value might be relatively old, depending on how much capture data has been buffered within the hardware or driver (outside of the WaveRT buffer).

    c. If there is more unread buffered data available the driver either:
       i. Immediately transfers that data into the available space of WaveRT buffer (i.e. space not used by the packet returned from GetReadPacket), returns true for MoreData, and sets the buffer notification event before returning from this routine. Or,
       ii. Programs hardware to burst the next packet into the available space of the WaveRT buffer, returns false for MoreData, and later sets the buffer event when the transfer completes.
3. The OS reads data from the WaveRT buffer using the information returned by GetReadPacket().
4. The OS waits for the next buffer notification event. The wait might terminate immediately if the driver set the buffer notification in step (2c).
5. If the driver did not immediately set the event in step (2c), the driver sets the event after it transfers more captured data into the WaveRT buffer and makes it available for the OS to read
6. Go to (2).

For [**KSNODETYPE\_AUDIO\_KEYWORDDETECTOR**](./ksnodetype-audio-keyworddetector.md) keyword detector pins, drivers should allocate enough internal burst buffering for at least 5000ms of audio data. If the OS fails to create a stream on the pin before the buffer overflows then the driver may end the internal buffering activity and free associated resources.

## Wake on Voice

Wake-on-Voice (WoV) enables the user to activate and query a speech recognition engine from a low power state to a full power state with screen on by saying a certain keyword, such as "Hey Contoso."

This feature allows for the device to be always listening for the user's voice while the device is idle and the screen is off. This is due to listening mode which uses much less power compared to normal microphone recording. WoV allows for chained speech phrase like "Hey Contoso, when's my next appointment" to invoke a response from a voice assistant in a hands-free manner.

The audio stack is responsible for communicating the wake data (speaker ID, keyword trigger, context information on confidence level) as well as notifying interested clients that the keyword has been detected.

### Validation on Modern Standby Systems

WoV from a system idle state can be validated on [Modern Standby](/windows-hardware/design/device-experiences/modern-standby) systems using the [Modern Standby Wake on Voice Basic Test on AC-power Source](/windows-hardware/test/hlk/testref/69df7cf2-6024-4eee-92ee-1506480614ee) and the [Modern Standby Wake on Voice Basic Test on DC-power Source](/windows-hardware/test/hlk/testref/614ffb93-eced-45ab-bf7b-e09291a97fd2) in the [HLK](/windows-hardware/test/hlk/). These tests check that the system has a hardware keyword spotter (HW-KWS), is able to enter the Deepest Runtime Idle Platform State (DRIPS) and is able to wake from Modern Standby on voice command with system resume latency of less than or equal to one second.
