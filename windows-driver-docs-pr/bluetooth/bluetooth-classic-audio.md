---
title: Bluetooth Classic Audio
description: This article describes the Bluetooth Classic audio functionality in Windows.
ms.date: 11/14/2024
---

# Bluetooth Classic audio

This article describes the Bluetooth Classic audio functionality in Windows. For information about Bluetooth LE audio, see [Bluetooth Low Energy (LE) Audio](./bluetooth-low-energy-audio.md).

Bluetooth Classic audio supports stereo audio playback over the Advanced Audio Distribution Profile (A2DP) and mono playback and capture over the Hands-Free Profile (HFP). Windows supports various audio codecs and sampling rates depending on the version of Windows, the capabilities of the headset, and the current usage of the playback or capture capabilities of the audio device.

## Terminology and prerequisites

In addition to the terms defined in this table, this article also references terms defined by Windows audio class extensions.

| Term | Definition |
|------|------------|
| LE audio | Bluetooth Low Energy Audio, an audio streaming technology that runs over the Bluetooth Low Energy radio |
| Classic audio | Bluetooth audio streaming that uses the hands-free profile (HFP) and advanced audio distribution profile (A2DP) |
| Audio device | A remote Bluetooth audio device that composes an input (microphone) or output (playback) endpoint from the perspective of Windows. |
| AAC | Advanced Audio Coding, an audio compression codec |
| aptX&trade; | Brand name for a family of audio compression codecs from Qualcomm |
| SBC | Sub Band Coding, an audio compression codec |
| mSBC | Modified SBC, an audio compression codec used for wideband speech |
| Narrowband speech | Operation of HFP at an 8 kilohertz (8kHz) sampling rate using the SBC codec |
| Wideband speech | Operation of HFP at a higher 16 kilohertz (16kHz) sampling rate using the mSBC codec |

## Advanced Audio Distribution Profile

A2DP supports high quality stereo audio playback and is used for general audio playback. For example, media, video, and so on. A2DP requires audio devices and Bluetooth hosts to support the SBC codec. Many audio devices support more codecs for higher quality audio.

Windows supports the following audio codecs for A2DP, beginning with the listed OS version. Windows starts from the top of the list, and chooses the first codec supported by both the host and the audio device for A2DP playback:

| Codec | Windows 10 | Windows 11 |
|-------|------------|------------|
| aptX&trade; Adaptive (lossless) | Not supported | Windows 11, version 24H2* |
| AAC | Not Supported | Windows 11, version 21H2 |
| aptX&trade; Classic | Windows 10, version 1507 | Windows 11, version 21H2 |
| SBC | Windows 10, version 1507 | Windows 11, version 21H2 |

\* *aptX Adaptive is only supported on select Windows devices with compatible Qualcomm Bluetooth radios.*

A2DP only supports audio output from the host to the audio device. When audio capture (for example, voice capture using the microphone in the audio devices) is used, it's necessary to use HFP instead.

## Hands-Free Profile

HFP supports concurrent monaural capture (microphone) and monaural playback, and is used for access to the Bluetooth audio device's microphone. Windows supports two modes for HFP, narrowband (8kHz) and wideband (16kHz), beginning with the listed OS version. Windows starts from the top of the list, and chooses the first mode supported by the host and audio device for HFP operation:

| Mode | Windows 10 | Windows 11 |
|------|------------|------------|
| Wideband (16kHz) | Windows 10, version 1703** | Windows 11, version 21H2** (compatibility improved in Windows 11, version 22H2) |
| Narrowband (8kHz) | Windows 10, version 1507 | Windows 11, version 21H2 |

\*\* *Some wideband capable audio devices aren't compatible with the Bluetooth radio in select Windows devices, causing these devices to revert to narrowband mode.*

## Selection of A2DP and HFP endpoints

### Windows 10

In Windows 10, up to three audio endpoints are created when a Bluetooth Classic audio device is paired to the PC, depending on if the audio device supports A2DP and/or HFP:

| Bluetooth Profile | Audio Output Endpoint Name | Audio Input Endpoint Name |
|-------------------|----------------------------|---------------------------|
| A2DP | {Device Name} Stereo | None |
| HFP | {Device Name} Hands-Free | {Device Name} Hands-Free |

When audio is streamed to the hands-free output, or an application opens the hands-free microphone input, regardless of if content is also being streamed to the Stereo output, the device switches into HFP mode, and any audio streaming to the stereo output is discarded.

Applications that need to capture audio from the audio device's microphone (such as VoIP applications) should be configured to use the hands-free endpoints.

### Windows 11

In Windows 11, the endpoints are unified between A2DP and HFP. If an audio device supports HFP, a single output and single input endpoint are created for the device. If an audio device only supports A2DP, only an output endpoint is created for the device.

Windows selects HFP instead of A2DP when any of the following scenarios are true:

- An application opens the input (microphone) endpoint.
- An application creates an output (playback) stream with the category set to *[Communications](../audio/audio-signal-processing-modes.md#windows-audio-stream-categories)*.

In all other cases, audio output (playback) to the device uses A2DP.

Windows automatically resamples audio as needed for the currently selected profile. For example, if the microphone is used during a VoIP call, which puts the headset into HFP mode at 8kHz or 16kHz, and another application plays audio to the same device at 48kHz, the sound is resampled to match the HFP endpoint.

Profile selection changes occur automatically based on microphone usage state. For example, if media is playing and the device is in A2DP mode, and then the microphone is opened, the device switches to HFP mode. If media continues playing once the microphone is closed, the device switches back to A2DP momentarily.
