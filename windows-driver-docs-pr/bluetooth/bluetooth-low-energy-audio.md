---
title: Bluetooth Low Energy (LE) Audio
description: This article provides an overview of Bluetooth LE Audio introduced in Windows 11 version 22H2 (KB5026446).
ms.date: 05/05/2025
ms.topic: overview
---

# Bluetooth Low Energy (LE) Audio

This article provides an overview of Bluetooth LE Audio introduced in Windows 11 version 22H2 (KB5026446).

## Introduction

Bluetooth LE Audio enables streaming unicast or broadcast audio to Bluetooth LE devices over an isochronous transport. As of version 5.3 of the Bluetooth core specification, there's no standard defined host controller interface (HCI) for host platforms to send and receive isochronous data to and from the Bluetooth controller. This document defines the Windows Bluetooth vendor specific audio path (VSAP) to allow platforms to use vendor-specific solutions to enable Bluetooth LE Audio streaming. The VSAP software interface uses Windows [audio class extensions](../audio/acx-audio-class-extensions-overview.md) (ACX) and more interface properties defined in this document.

### Terminology and prerequisites

In addition to the terms defined in this table, this document also references terms defined by Windows audio class extensions.

| Term | Definition |
|---|---|
| LE audio | Short for Bluetooth LE Audio |
| Classic audio | Bluetooth audio streaming that uses the hands-free profile (HFP) and advanced audio distribution profile (A2DP) |
| Audio Device | A single remote Bluetooth LE Audio device or set of Bluetooth LE Audio devices that together compose a single audio endpoint from the perspective of Windows. |
| BAP | The [Basic Audio Profile](https://www.bluetooth.com/specifications/specs/basic-audio-profile-1-0-1/) defines how devices can distribute and consume audio using Bluetooth Low Energy (LE) communications. |
| TMAP | The [Telephony and Media Audio Profile](https://www.bluetooth.com/specifications/specs/tmap-1-0/) specifies interoperable configurations of the lower-level audio services and profiles. |
| ASCS | The [Audio Stream Control Service](https://www.bluetooth.com/specifications/specs/audio-stream-control-service/) defines a standard way for Bluetooth LE Audio devices to configure and establish unicast audio streams. |
| PACS | The [Published Audio Capabilities Service](https://www.bluetooth.com/specifications/specs/published-audio-capabilities-service-1-0-1/) defines a standard way for Bluetooth LE Audio devices to report its supported audio codec capabilities. |
| CIS | The Connected Isochronous Streams transport is used to send and receive unicast audio data between Bluetooth LE devices. |
| BIS | The Broadcast Isochronous Stream transport is used for connectionless audio data transfers. |
| ACX | Short for audio class extensions, which is the driver model required by all audio drivers to support Bluetooth LE Audio on Windows. |
| Streaming circuits | One or more **ACXCIRCUIT** objects created by the Vendor Specific Audio Driver Stack for its streaming path. |
| Profile circuit | An **ACXCIRCUIT** object created by the Bluetooth LE audio profile implementation on Windows. This **ACXCIRCUIT** isn't a streaming circuit. |

This article assumes familiarity with the previously defined terms and the following HCI commands defined in the [Bluetooth Core specification](https://www.bluetooth.com/specifications/specs/core54-html/):

- Local Controller Commands
  - HCI_Read_Local_Supported_Codecs (v2)
  - HCI_Read_Local_Supported_Codec_Capabilities
  - HCI_LE_Setup_ISO_Data_Path
  - HCI_LE_Remove_ISO_Data_Path
  - HCI_Configure_Data_Path
- Unicast Streaming Commands
  - HCI_LE_Set_CIG_Parameters
  - HCI_LE_Create_CIS
  - HCI_LE_Remove_CIG
- Broadcast Streaming Commands
  - HCI_LE_Create_BIG
  - HCI_LE_Terminate_BIG
  - HCI_LE_BIG_Create_Sync
  - HCI_LE_BIG_Terminate_Sync
  - HCI_LE_Set_Periodic_Advertising_Parameters
  - HCI_LE_Set_Periodic_Advertising_Data
  - HCI_LE_Set_Periodic_Advertising_Enable
  - HCI_LE_Periodic_Advertising_Create_Sync
  - HCI_LE_Periodic_Advertising_Create_Sync_Cancel
  - HCI_LE_Periodic_Advertising_Terminate_Sync
  - HCI_LE_Set_Periodic_Advertising_Receive_Enable
  - HCI_LE_Periodic_Advertising_Report
  - HCI_LE_BIGInfo_Advertising_Report
  - HCI_LE_Read_Periodic_Advertiser_List_Size
  - HCI_LE_Add_Device_To_Periodic_Advertiser_List
  - HCI_LE_Remove_Device_From_Periodic_Advertiser_List
  - HCI_LE_Clear_Periodic_Advertiser_List
  - HCI_LE_Periodic_Advertising_Set_Info_Transfer
  - HCI_LE_Periodic_Advertising_Sync_Transfer
  - HCI_LE_Set_Default_Periodic_Advertising_Sync_Transfer_Parameters
  - HCI_LE_Set_Periodic_Advertising_Sync_Transfer_Parameters

Bluetooth LE Audio VSAP requires the audio drivers to use the ACX framework. Adopting ACX for Bluetooth LE Audio provides several advantages, such as:

- Supports the preferred audio driver model for Windows going forward.
- Uses ACX's native support for multi stack audio solutions without requiring a dedicated DDI between drivers.
- Doesn't require IHV audio drivers to relay requests from the audio system to the Bluetooth stack. Instead, ACX can send requests directly to the Bluetooth stack via the profile circuit.

## Architecture

### Definitions

The following components are involved in the different VSAP architecture variants.

#### Windows ACX framework

This component enables support for a multi-stack audio endpoint. For Bluetooth LE Audio, the software components that compose an audio endpoint are the vendor specific audio driver stack and the Windows Bluetooth LE Audio profile.

#### Vendor specific audio driver stack

This vendor specific component is responsible for sending and receiving Bluetooth LE Audio data to and from a Bluetooth controller via a vendor defined audio interface. It shall consist of at a minimum an ACX streaming driver to manage the incoming and outgoing audio data. More ACX drivers might be included if they're necessary parts of the multi circuit ACX audio endpoint. This component is also referred to as the IHV ACX Streaming Driver in this document.

#### Windows Bluetooth LE Audio profile

This component contains the implementation of the Basic Audio Profile (BAP), Volume Control Profile, and Microphone Control Profile. It's responsible for creating the control **[ACXCIRCUIT](/windows-hardware/drivers/audio/acx-summary-of-objects#acx-circuit)** for each Bluetooth LE Audio device or set of devices paired to Windows. It also reports audio formats from the remote device and Bluetooth controller, and manages the state of isochronous channels and groups.

#### Windows Bluetooth core stack

This component provides an interface to allow the Windows Bluetooth LE Audio Profile to query supported codec capabilities from the local Bluetooth controller and manage the state of isochronous channels and groups.

#### LC3 codec

This subcomponent translates between compressed LC3 audio and PCM audio. It must support both encoding and decoding capabilities. The LC3 codec can be implemented in software as part of the vendor specific audio driver (VSAP) stack. Alternatively, it can be implemented in hardware as part of the audio DSP or Bluetooth Controller. The diagram mentions LC3 by name since it's the standard codec supported by the Bluetooth SIG. Future codecs and vendor specific codecs supported by Windows might also be incorporated into the architecture in a similar manner.

### Architecture Variants

The Bluetooth LE Audio VSAP architecture supports different variants for streaming.

1. Sideband Bluetooth LE Audio streaming without audio offload
1. Sideband Bluetooth LE Audio streaming with audio offload
1. Vendor specific inband Bluetooth LE Audio streaming

In the following diagrams, the shaded components are provided by the IHV and the nonshaded components are provided by the OS.

#### Sideband Bluetooth LE Audio architecture without audio offload

A sideband architecture uses a vendor specific audio interface to allow the audio driver stack to send and receive audio data to the Bluetooth controller. This data path is separate from the HCI data path used for other Bluetooth data, such as signaling messages between the unicast client and remote unicast server. The following diagram models a sideband architecture where the LC3 codec is hosted in the Bluetooth controller. It's also valid to have the LC3 codec hosted as part of the Vendor Specific Audio Driver Stack for software encoding and decoding. In that case, the audio being sent to the Bluetooth controller would be formatted as LC3 audio frames instead of PCM audio.

The following diagram shows a sideband Bluetooth LE Audio architecture with an LC3 codec in the Bluetooth controller.

:::image type="content" source="images/bluetooth-le-audio-architecture-with-lc3-codec-in-bluetooth-controller.png" alt-text="Diagram of sideband Bluetooth LE Audio architecture with LC3 codec located in the Bluetooth controller.":::

The following diagram shows a sideband Bluetooth LE Audio architecture with an LC3 codec in the audio driver stack.

:::image type="content" source="images/bluetooth-le-audio-architecture-with-lc3-codec-in-audio-driver-stack.png" alt-text="Diagram of sideband Bluetooth LE Audio architecture with LC3 codec located in the audio driver stack.":::

#### Sideband Bluetooth LE Audio architecture with audio offload

A sideband architecture with audio offload includes an audio DSP hardware component to provide a Bluetooth LE Audio streaming solution with power saving benefits. The following diagrams demonstrate a possible architecture with the LC3 codec in the Bluetooth controller and the codec in the audio DSP.

The following diagram shows a sideband Bluetooth LE Audio with audio offload architecture with an LC3 codec in the Bluetooth controller.

:::image type="content" source="images/bluetooth-le-audio-with-audio-offload-architecture-with-lc3-codec-in-bluetooth-controller.png" alt-text="Diagram of sideband Bluetooth LE Audio with audio offload architecture, featuring LC3 codec in the Bluetooth controller.":::

The following diagram shows a sideband Bluetooth LE Audio with audio offload architecture with an LC3 codec in the audio DSP.

:::image type="content" source="images/bluetooth-le-audio-with-audio-offload-architecture-with-lc3-codec-in-audio-dsp.png" alt-text="Diagram of sideband Bluetooth LE Audio with audio offload architecture, featuring LC3 codec in the audio DSP.":::

#### Vendor specific inband Bluetooth LE Audio architecture

The VSAP inband architecture enables a custom pipeline to send and receive Bluetooth LE Audio data from the vendor specific audio driver stack to the Bluetooth controller's HCI. This architecture includes a new component, the "IHV ISO Merging Component." This component is responsible for managing the flow control for the ISO data. It also shall share HCI command flow control with the Windows Bluetooth Core Stack if it needs to send any HCI commands.

The following diagram shows a vendor specific inband Bluetooth LE Audio architecture.

:::image type="content" source="images/bluetooth-le-audio-vendor-specific-inband-architecture.png" alt-text="Diagram of vendor-specific inband Bluetooth LE Audio architecture.":::

## Detailed design

### Audio format requirements

#### KSAUDIO_PACKETSIZE_CONSTRAINTS2

IHV ACX audio drivers are required to support the KSAUDIO_PACKETSIZE_CONSTRAINTS2 property. Supporting this property reduces the time between adding a Bluetooth LE audio device to windows and the audio device becoming available to applications for streaming.

#### Audio frame durations

Bluetooth LE Audio profiles allow implementations to support audio streaming with frame durations of either 7.5 milliseconds or 10 milliseconds. Windows requires codecs provided by IHVs to support both frame durations. This requirement ensures interoperability with Bluetooth LE Audio accessory devices and quality coexistence with other Bluetooth LE devices connected to the system.

#### Signal processing mode definitions

Bluetooth LE Audio supports a wide range of streaming formats to support different user scenarios. The BAP and TMAP specifications define mandatory supported formats for certification. Windows applies [audio signal processing modes](../audio/audio-signal-processing-modes.md) to correlate the format to use with the scenario the system is performing. Audio drivers that support Bluetooth LE Audio shall indicate support for the signal processing modes and formats in the following table. Furthermore, Bluetooth LE Audio doesn't support the raw signal processing mode, so audio drivers shall not advertise any supported formats for this mode.

##### Unicast render stream audio formats and signal processing modes

Bluetooth LE Audio requires unicast render audio formats to be declared for the following signal processing modes:

- Default (AUDIO_SIGNALPROCESSINGMODE_DEFAULT)
  - This mode is used for unidirectional render scenarios, such as music playback, notifications, and video game audio.
- Communications (AUDIO_SIGNALPROCESSINGMODE_COMMUNICATIONS)
  - This mode is used for bidirectional scenarios, such as voice calls.

The following tables are lists of symmetric formats for each use case and signal processing mode. Asymmetric format support is defined in [Stereo render with mono capture](#stereo-render-with-mono-capture).

Audio formats are ordered from most preferred to least preferred.

###### System sounds, music playback, and video game audio when connected to a stereo device or coordinated set of devices

Signal processing mode: **Default**

| Sampling Frequency | Channel Count | Bit Depth | Frame Duration | Audio Data Rate | BAP Codec Configuration ID (Table 3.11 of the BAP Specification) |
|---|---|---|---|---|---|
| 48 kHz | 2 | 16 | 7.5 ms | 96 kbps | 48_3 |
| 48 kHz | 2 | 16 | 7.5 ms | 80 kbps | 48_1 |
| 48 kHz | 2 | 16 | 10 ms | 96 kbps | 48_4 |
| 48 kHz | 2 | 16 | 10 ms | 80 kbps | 48_2 |
| 32 kHz | 2 | 16 | 7.5 ms | 64 kbps | 32_1 |
| 32 kHz | 2 | 16 | 10 ms | 64 kbps | 32_2 |
| 24 kHz | 2 | 16 | 7.5 ms | 48 kbps | 24_1 |
| 24 kHz | 2 | 16 | 10 ms | 48 kbps | 24_2 |

###### System sounds, music playback, and video game audio when connected to a single member of a coordinated set (single earbud or hearing aid)

Signal processing mode: **Default**

| Sampling Frequency | Channel Count | Bit Depth | Frame Duration | Audio Data Rate | BAP Codec Configuration ID (Table 3.11 of the BAP Specification) |
|---|---|---|---|---|---|
| 48 kHz | 1 | 16 | 7.5 ms | 96 kbps | 48_3 |
| 48 kHz | 1 | 16 | 7.5 ms | 80 kbps | 48_1 |
| 48 kHz | 1 | 16 | 10 ms | 96 kbps | 48_4 |
| 48 kHz | 1 | 16 | 10 ms | 80 kbps | 48_2 |
| 32 kHz | 1 | 16 | 7.5 ms | 64 kbps | 32_1 |
| 32 kHz | 1 | 16 | 10ms | 64 kbps | 32_2 |
| 24 kHz | 1 | 16 | 7.5 ms | 48 kbps | 24_1 |
| 24 kHz | 1 | 16 | 10 ms | 48 kbps | 24_2 |
| 16 kHz | 1 | 16 | 7.5 ms | 32 kbps | 16_1 |
| 16 kHz | 1 | 16 | 10 ms | 32 kbps | 16_2 |

###### Render voice recorder, VOIP calls, or video game audio with voice chat

Signal processing mode: **Communications**

| Sampling Frequency | Channel Count | Bit Depth | Frame Duration | Audio Data Rate | BAP Codec Configuration ID (Table 3.11 of the BAP Specification) |
|---|---|---|---|---|---|
| 32 kHz | 1 | 16 | 7.5 ms | 64 kbps | 32_1 |
| 32 kHz | 1 | 16 | 10 ms | 64 kbps | 32_2 |
| 24 kHz | 1 | 16 | 7.5 ms | 48 kbps | 24_1 |
| 24 kHz | 1 | 16 | 10 ms | 48 kbps | 24_2 |
| 16 kHz | 1 | 16 | 7.5 ms | 32 kbps | 16_1 |
| 16 kHz | 1 | 16 | 10 ms | 32 kbps | 16_2 |

##### Unicast capture stream audio formats and signal processing modes

Bluetooth LE Audio requires unicast capture audio formats to be declared for the Default (AUDIO_SIGNALPROCESSINGMODE_DEFAULT) signal processing mode. The list of supported capture formats is in the following table.

Audio formats are ordered from most preferred to least preferred.

###### Capture voice recorder, VOIP calls, or video game audio with voice chat

Signal processing mode: **Default**

| Sampling Frequency | Channel Count | Bit Depth | Frame Duration | Audio Data Rate | BAP Codec Configuration ID (Table 3.11 of the BAP Specification) |
|---|---|---|---|---|---|
| 32 kHz | 1 | 16 | 7.5 ms | 64 kbps | 32_1 |
| 32 kHz | 1 | 16 | 10 ms | 64 kbps | 32_2 |
| 24 kHz | 1 | 16 | 7.5 ms | 48 kbps | 24_1 |
| 24 kHz | 1 | 16 | 10 ms | 48 kbps | 24_2 |
| 16 kHz | 1 | 16 | 7.5 ms | 32 kbps | 16_1 |
| 16 kHz | 1 | 16 | 10 ms | 32 kbps | 16_2 |

##### Broadcast Audio Signal Processing Modes

Windows Bluetooth LE audio requires broadcast source (render) audio formats to be declared for the Default (AUDIO_SIGNALPROCESSINGMODE_DEFAULT) signal processing mode.

Windows Bluetooth LE Audio requires broadcast sink (capture) audio formats to be declared for the Default(AUDIO_SIGNALPROCESSINGMODE_DEFAULT) signal processing mode.

The following complete list of required supported formats is identical for both roles.

###### Stereo broadcast stream for system sounds, music playback, and video game audio

Signal processing mode: **Default**

| Sampling Frequency | Channel Count | Bit Depth | Frame Duration | Audio Data Rate | BAP Codec Configuration ID (Table 3.11 of the BAP Specification) |
|---|---|---|---|---|---|
| 48 kHz | 2 | 16 | 7.5 ms | 96 kbps | 48_3 |
| 48 kHz | 2 | 16 | 7.5ms | 80 kbps | 48_1 |
| 48 kHz | 2 | 16 | 10 ms | 96 kbps | 48_4 |
| 48 kHz | 2 | 16 | 10ms | 80 kbps | 48_2 |
| 24 kHz | 2 | 16 | 7.5ms | 48 kbps | 24_1 |
| 24 kHz | 2 | 16 | 10ms | 48 kbps | 24_2 |

###### Mono broadcast stream for system sounds, music playback, and video game audio

Signal processing mode: **Default**

| Sampling Frequency | Channel Count | Bit Depth | Frame Duration | Audio Data Rate | BAP Codec Configuration ID (Table 3.11 of the BAP Specification) |
|---|---|---|---|---|---|
| 48 kHz | 1 | 16 | 7.5ms | 96 kbps | 48_3 |
| 48 kHz | 1 | 16 | 7.5ms | 80 kbps | 48_1 |
| 48 kHz | 1 | 16 | 10ms | 96 kbps | 48_4 |
| 48 kHz | 1 | 16 | 10ms | 80 kbps | 48_2 |
| 24 kHz | 1 | 16 | 7.5ms | 48 kbps | 24_1 |
| 24 kHz | 1 | 16 | 10ms | 48 kbps | 24_2 |
| 16 kHz | 1 | 16 | 7.5ms | 32 kbps | 16_1 |
| 16 kHz | 1 | 16 | 10ms | 32 kbps | 16_2 |

#### Defined stream configurations and topologies

##### Unicast render-only configurations

###### Basic audio profile configuration 1

The following audio configuration is defined in table 4.1 of the [Bluetooth BAP specification](https://www.bluetooth.com/specifications/specs/basic-audio-profile-1-0-1/)

:::image type="content" source="images/bap-configuration-1.png" alt-text="Diagram illustrating basic audio profile configuration 1.":::

The PC is connected to a single audio device that supports mono streams. The single device might be a standalone device or a single connected member of a coordinated set.

| Use Case Examples | Windows Audio Settings | Bluetooth Controller Settings |
|---|---|---|
| Media playback | **Render**:<br>Signal Processing Mode: Default<br>Channel Count: 1<br>**Capture**: None | CIS Count: 1<br>CIG Count: 1<br>BAP QoS Settings: High reliability |
| Voice call with no microphone on audio device | **Render**:<br>Signal Processing Mode: Communications<br>Channel Count: 1<br>**Capture**: None | CIS Count: 1<br>CIG Count: 1<br>BAP QoS Settings: Low latency |
| Video game playback | **Render**:<br>Signal Processing Mode: Default<br>Channel Count: 1<br>**Capture**: None | CIS Count: 1<br>CIG Count: 1<br>BAP QoS Settings: Low latency |

###### Basic audio profile configuration 4

The following audio configuration is defined in table 4.1 of the [Bluetooth BAP specification](https://www.bluetooth.com/specifications/specs/basic-audio-profile-1-0-1/)

:::image type="content" source="images/bap-configuration-4.png" alt-text="Diagram illustrating basic audio profile configuration 4.":::

The PC is connected to a single audio device that supports stereo streams. The audio device is capable of processing two audio channels on a single CIS.

| Use Case Examples | Windows Audio Settings | Bluetooth Controller Settings |
|---|---|---|
| Media playback | **Render**: Signal Processing Mode: Default<br>Channel Count: 2<br>**Capture**: None | CIS Count: 1<br>CIG Count: 1<br>BAP QoS Settings: High reliability Audio Channel Allocation: Front left and front right |
| Video game playback | Signal Processing Mode: Default<br>Channel Count: 2<br>**Capture**: None | CIS Count: 1<br>CIG Count: 1<br>BAP QoS Settings: Low latency<br>Audio Channel Allocation: Front left and front right |

###### Basic audio profile configuration 6(i)

The following audio configuration is defined in table 4.1 of the [Bluetooth BAP specification](https://www.bluetooth.com/specifications/specs/basic-audio-profile-1-0-1/)

:::image type="content" source="images/bap-configuration-6-i.png" alt-text="Diagram illustrating basic audio profile configuration 6 I.":::

The PC is connected to a single audio device that supports stereo streams. The audio device is only capable of processing one audio channel on each of the two CISs

| Use Case Examples | Windows Audio Settings | Bluetooth Controller Settings |
|---|---|---|
| Media playback | Signal Processing Mode: Default<br>Channel Count: 2<br>**Capture**: None | CIS Count: 2<br>CIG Count: 1<br>BAP QoS Settings: High reliability |
| Voice call with no microphone on audio device | Signal Processing Mode: Communications<br>Channel Count: 1<br>**Capture**: None | CIS Count: 2<br>CIG Count: 1<br>BAP QoS Settings: Low latency<br>Audio Channel Allocation: Either front left or front right |
| Video game playback | Signal Processing Mode: Default<br>Channel Count: 2<br>**Capture**: None | CIS Count: 2<br>CIG Count: 1<br>BAP QoS Settings: Low latency<br>Audio Channel Allocation: Front left and front right |

###### Basic audio profile configuration 6(ii)

The following audio configuration is defined in table 4.1 of the [Bluetooth BAP specification](https://www.bluetooth.com/specifications/specs/basic-audio-profile-1-0-1/)

:::image type="content" source="images/bap-configuration-6-ii.png" alt-text="Diagram illustrating basic audio profile configuration 6 II.":::

The PC is connected to a coordinated set of audio devices. The set is capable of processing two channels of audio with each member processing a single channel.

| Use Case Examples | Windows Audio Settings | Bluetooth Controller Settings |
|---|---|---|
| Media playback | Signal Processing Mode: Default<br>Channel Count: 2<br>**Capture**: None | CIS Count: 2<br>CIG Count: 1<br>BAP QoS Settings: High reliability |
| Voice call with no microphone on either device | Signal Processing Mode: Communications<br>Channel Count: 1<br>**Capture**: None | CIS Count: 2<br>CIG Count: 1<br>BAP QoS Settings: Low latency |
| Video game playback | Signal Processing Mode: Default<br>Channel Count: 2<br>**Capture**: None | CIS Count: 2<br>CIG Count: 1<br>BAP QoS Settings: Low latency |

##### Unicast bidirectional configurations

Bidirectional configurations are used when the Bluetooth LE Audio profile detects that an application intends to create both a capture and render stream to a remote device or set of devices. Applications control capture and render streams separately. Therefore, IHV audio drivers and Bluetooth controllers shall allow audio to flow over a single direction of a bidirectional CIS after provisioning. This provisioning uses the HCI commands Configure Data Path and LE Setup ISO Data Path.

###### Basic audio profile configuration 3

The following audio configuration is defined in table 4.1 of the [Bluetooth BAP specification](https://www.bluetooth.com/specifications/specs/basic-audio-profile-1-0-1/)

:::image type="content" source="images/bap-configuration-3.png" alt-text="Diagram illustrating basic audio profile configuration 3.":::

The PC is connected to a single audio device with a bidirectional mono stream established on a single CIS.

| Use Case | Windows Audio Settings | Bluetooth Controller Settings |
|---|---|---|
| Voice call | **Render:**<br>Signal Processing Mode: Communications<br>Channel Count: 1<br>**Capture:**<br>Signal Processing Mode: Default<br>Channel Count: 1 | CIS Count: 1<br>CIG Count: 1<br>BAP QoS Settings: Low Latency |
| Video game playback with voice chat | **Render:**<br>Signal Processing Mode: Communications<br>Channel Count: 1<br>**Capture:**<br>Signal Processing Mode: Default<br>Channel Count: 1 | CIS Count: 2<br>CIG Count: 1<br>BAP QoS Settings: Low Latency |

###### Basic audio profile configuration 8(i)

The following audio configuration is defined in table 4.1 of the [Bluetooth BAP specification](https://www.bluetooth.com/specifications/specs/basic-audio-profile-1-0-1/)

:::image type="content" source="images/bap-configuration-8-i.png" alt-text="Diagram illustrating basic audio profile configuration 8 I.":::

The PC is connected to a single audio device that supports stereo render streams and mono capture streams. The device is capable of processing one channel of audio on a single CIS for a given direction.

| Use Case | Windows Audio Settings | Bluetooth Controller Settings |
|---|---|---|
| Voice call | **Render:**<br>Signal Processing Mode: Communications<br>Channel Count: 1 or 2<br>**Capture:**<br>Signal Processing Mode: Default<br>Channel Count: 1 | CIS Count: 2<br>CIG Count: 1<br>BAP QoS Settings: Low Latency |
| Video game playback with voice chat | **Render:**<br>Signal Processing Mode: Communications<br>Channel Count: 2<br>**Capture:**<br>Signal Processing Mode: Default<br>Channel Count: 1 | CIS Count: 2<br>CIG Count: 1<br>BAP QoS Settings: Low Latency |

###### Basic audio profile configuration 8(ii)

The following audio configuration is defined in table 4.1 of the [Bluetooth BAP specification](https://www.bluetooth.com/specifications/specs/basic-audio-profile-1-0-1/)

:::image type="content" source="images/bap-configuration-8-ii.png" alt-text="Diagram illustrating basic audio profile configuration 8 II.":::

The PC is connected to a coordinated set of audio devices. Each set member is receiving one channel of render audio. A single set member has an established capture stream. The set member with the capture stream is the first set member that connects to the PC that also supports capture streams.

| Use Case | Windows Audio Settings | Bluetooth Controller Settings |
|---|---|---|
| Voice call | **Render:**<br>Signal Processing Mode: Communications<br>Channel Count: 1 or 2<br>**Capture:**<br>Signal Processing Mode: Default<br>Channel Count: 1 | CIS Count: 2<br>CIG Count: 1<br>BAP QoS Settings: Low Latency |
| Video game playback with voice chat | **Render:**<br>Signal Processing Mode: Communications<br>Channel Count: 2<br>**Capture:**<br>Signal Processing Mode: Default<br>Channel Count: 1 | CIS Count: 2<br>CIG Count: 1<br>BAP QoS Settings: Low Latency |

##### Unicast capture-only configurations

###### Basic audio profile configuration 2

The following audio configuration is defined in table 4.1 of the [Bluetooth BAP specification](https://www.bluetooth.com/specifications/specs/basic-audio-profile-1-0-1/)

:::image type="content" source="images/bap-configuration-2.png" alt-text="Diagram illustrating basic audio profile configuration 2.":::

The PC is connected to a single audio device that supports mono capture streams.

| Use Case | Windows Audio Settings | Bluetooth Controller Settings |
|---|---|---|
| Voice call with no speaker on device | **Render:** None<br>**Capture:**<br>Signal Processing Mode: Default<br>Channel Count: 1 | CIS Count: 1<br>CIG Count: 1<br>BAP QoS Settings: Low Latency |

###### Basic audio profile configuration 9(i)

The following audio configuration is defined in table 4.1 of the [Bluetooth BAP specification](https://www.bluetooth.com/specifications/specs/basic-audio-profile-1-0-1/)

:::image type="content" source="images/bap-configuration-9-i.png" alt-text="Diagram illustrating basic audio profile configuration 9 I.":::

The PC is connected to a single audio device that supports sending stereo audio data. The device is capable of encoding one channel of audio on a single CIS.

| Use Case | Windows Audio Settings | Bluetooth Controller Settings |
|---|---|---|
| Multi channel microphone capture | **Render:** None<br>**Capture:**<br>Signal Processing Mode: Default<br>Channel Count: 1<br> | CIS Count: 2<br>CIG Count: 1<br>BAP QoS Settings: Low Latency |

###### Basic audio profile configuration 9(ii)

The PC is connected to a single audio device that supports mono capture streams.

The following audio configuration is defined in table 4.1 of the [Bluetooth BAP specification](https://www.bluetooth.com/specifications/specs/basic-audio-profile-1-0-1/)

:::image type="content" source="images/bap-configuration-9-ii.png" alt-text="Diagram showing basic audio profile configuration 9(ii) with PC connected to a single audio device.":::

The PC is connected to a set of audio devices. Each set member sends one channel of audio to the PC.

| Use Case | Windows Audio Settings | Bluetooth Controller Settings |
|---|---|---|
| Multi channel microphone capture | **Render:** None<br>**Capture:**<br>Signal Processing Mode: Default<br>Channel Count: 1 | CIS Count: 2<br>CIG Count: 1<br>BAP QoS Settings: Low Latency |

If the remote device or device set supports bidirectional audio, then the configuration for a capture only stream is the same as for bidirectional. This configuration allows transitions from capture only scenarios to bidirectional scenarios without needing to re-create the streams.

##### Broadcast source configurations

###### Basic audio profile configuration 12

The following audio configuration is defined in table 4.2 of the [Bluetooth BAP specification](https://www.bluetooth.com/specifications/specs/basic-audio-profile-1-0-1/)

:::image type="content" source="images/bluetooth-audio-profile-configuration-12.png" alt-text="Diagram showing basic audio profile configuration 12 with PC connected to a single audio device in mono.":::

The PC is broadcasting one channel of mono audio.

| Use Case | Windows Audio Settings | Bluetooth Controller Settings |
|---|---|---|
| System sounds, music playback | **Render:**<br>Signal Processing Mode: Default<br>Channel Count: 1<br> | BIS Count: 1<br>BIG Count: 1<br>BAP QoS Settings: High Reliability |
| Video game audio | **Render:**<br>Signal Processing Mode: Default<br>Channel Count: 1<br> | BIS Count: 1<br>BIG Count: 1<br>BAP QoS Settings: Low Latency |

###### Basic audio profile configuration 13

The following audio configuration is defined in table 4.2 of the [Bluetooth BAP specification](https://www.bluetooth.com/specifications/specs/basic-audio-profile-1-0-1/)

:::image type="content" source="images/bluetooth-audio-profile-configuration-13.png" alt-text="Diagram showing basic audio profile configuration 13 with PC connected to a single audio device in stereo.":::

The PC is broadcasting stereo audio with each channel transmitting on its own BIS.

| Use Case | Windows Audio Settings | Bluetooth Controller Settings |
|---|---|---|
| System sounds, music playback | **Render:**<br>Signal Processing Mode: Default<br>Channel Count: 2<br> | BIS Count: 1<br>BIG Count: 1<br>BAP QoS Settings: High Reliability |
| Video game audio | **Render:**<br>Signal Processing Mode: Default<br>Channel Count: 1<br> | BIS Count: 1<br>BIG Count: 1<br>BAP QoS Settings: Low Latency |

### Data structures

#### Microsoft defined Bluetooth LE Audio interface properties

##### Stream creation properties

The following properties are shared between the vendor specific audio driver stack and the Bluetooth LE Audio Profile via the [ACXOBJECTBAG](/windows-hardware/drivers/audio/acx-summary-of-objects#acx-object-bag) [DDIs](/windows-hardware/drivers/ddi/acxmisc/). These properties inform decisions on stream endpoint creation and configuration, as shown in the [Stream Creation](#stream-creation) scenario.

###### BluetoothLEAudio_CodecCapabilities

The audio driver sets this property to indicate support for audio streaming capabilities that are supported in the audio driver or audio DSP. The property value is set using the DDI **[AcxObjectBagAddBlob](/windows-hardware/drivers/ddi/acxmisc/nf-acxmisc-acxobjectbagaddblob)** and the format of the value is the same as a PAC record as defined in the [PACS specification](https://www.bluetooth.com/specifications/specs/published-audio-capabilities-service-1-0-1/).

The Windows Bluetooth LE Audio profile reads the property to determine the possible codec configurations and stream composition to use.

| Field | Octet |
|---|---|
| Capability Count | 0 |
| Codec ID[i] | 1-6 |
| Codec Specific Capabilities Length[i] | 7 |
| Codec Specific Capabilities | 8... n |
| Metadata Length (m) | n + 1 |
| Metadata | n+2... m |

Field values are defined in tables 3.2 and 3.4 of the PACS specification.

###### Bluetooth_DatapathID

 The audio driver sets this property to indicate the data path ID used as the parameter for the commands HCI_LE_Setup_ISO_Data_Path and HCI_Configure_Data_Path. The property value is set using the **[AcxObjectBagAddUI8](/windows-hardware/drivers/ddi/acxmisc/nf-acxmisc-acxobjectbagaddui8)** DDI.

The Bluetooth LE Audio profile reads and uses this property is as a parameter in HCI_Configure_Data_Path and HCI_LE_Setup_ISO_Data_Path commands. This ID is applied for all isochronous streams created for the **ACXSTREAM** associated with the object bag. To assign a different data path ID for each stream connection, use *[KSPROPERTY_BtLeAudio_DATAPATH_ID](#ksproperty_btleaudio_datapath_id)* in your audio drivers.

| Field | Octet |
|---|---|
| Data path ID | 0 |

If the audio driver doesn't set this property, then the OS uses the value 1 as the parameter for the HCI commands.

###### Bluetooth_DatapathConfiguration

The audio driver sets this property to provide vendor specific configurations to the Bluetooth controller via the HCI_Configure_Data_Path command. It must not be larger than 255 bytes, which is the largest payload that a Bluetooth controller accepts for an HCI command. The property value is set using the **[AcxObjectBagAddBlob](/windows-hardware/drivers/ddi/acxmisc/nf-acxmisc-acxobjectbagaddblob)** DDI. This configuration applies to all data path IDs set by the audio driver. To assign a different data path configuration for each datapath ID, use *[KSPROPERTY_BtLeAudio_DATAPATH_CONFIG](#ksproperty_btleaudio_datapath_config)* in your audio drivers.

###### Bluetooth_RequiresHciTransportInD0ForStreaming

The audio driver sets this property to indicate that the Bluetooth controller shall not transition to a low power state while an audio stream is active. The property value is set using the **[AcxObjectBagAddUI8](/windows-hardware/drivers/ddi/acxmisc/nf-acxmisc-acxobjectbagaddui8)** DDI.

| Field | Octet |
|---|---|
| ActiveTransportRequired (shall be set to 1) | 0 |

###### BluetoothLEAudio_CodecConfiguration

This property shall be set by the Bluetooth LE Audio profile using the DDI **[AcxObjectBagAddBlob](/windows-hardware/drivers/ddi/acxmisc/nf-acxmisc-acxobjectbagaddblob)** after the codec configuration is configured with an audio device. The structure of the value is:

| Field | Octet |
|---|---|
| Configuration Count | 0 |
| Stream Connection Handle[i] | 1-2 |
| Coding Format[i] | 3 |
| Company ID[i] | 4-5 |
| Vendor Specific Codec ID[i] | 6-7 |
| Codec Specific Configuration Length[i] | 8 |
| Codec Specific Configuration[i] | 9... n |

Field values are derived from table 4.3 of the [Bluetooth Audio Stream Control Service Specification](https://www.bluetooth.com/specifications/specs/audio-stream-control-service/).

The vendor specific audio driver stack should read this property if the LC3 codec is in the ACX streaming driver or audio DSP.

###### BluetoothLEAudio_StreamConnectionHandles

This property shall be set by the Bluetooth LE audio profile to inform the audio driver of the list of BIS or CIS handles created for a BIG or CIG. The order of the handles matches the order returned by the Bluetooth controller to the HCI command LE_Set_CIG_Parameters or the HCI event LE_Create_BIG_Complete. The structure of the value is:

| Field | Size | Octet |
|---|---|---|
| Connection Handle Count | 1 | 0 |
| Connection Handle[i] | 2 | 1-n |

###### Bluetooth LE Audio KS Properties

KS Properties allows the IHV ACX audio driver to set or update audio stream settings after the stream is created. This scenario is useful for audio drivers to set configuration settings based on properties set by the Bluetooth profile circuit in the create stream procedure.

Definitions

```cpp
#define STATIC_KSPROPSETID_BtLeAudio\
    0x1159b79, 0xea6, 0x4923, 0x80, 0xf5, 0x32, 0x58, 0xd1, 0xfd, 0x91, 0x56
DEFINE_GUIDSTRUCT("01159B79-0EA6-4923-80F5-3258D1FD9156", KSPROPSETID_BtLeAudio);
#define KSPROPSETID_BtLeAudio DEFINE_GUIDNAMED(KSPROPSETID_BtLeAudio)

typedef enum {
    KSPROPERTY_BtLeAudio_DATAPATH_ID,
    KSPROPERTY_BtLeAudio_DATAPATH_CONFIG,
} ksproperty_btleaudio;
```

###### KSPROPERTY_BtLeAudio_DATAPATH_ID

This KSProperty allows IHV ACX audio drivers to set or update the value set by Bluetooth_DatapathID after the create stream callback is invoked. This property also allows IHV audio drivers to assign a different data path ID for each codec configuration entry in BluetoothLEAudio_CodecConfiguration. The value of this property shall either be set to a single byte value to represent the data path ID used for all codec configurations, or n bytes where n is equal to the Configuration Count value set in the BluetoothLEAudio_CodecConfiguration property. If the value contains multiple data path IDs, then the order of the IDs shall be used for the codec configuration as ordered in the property BluetoothLEAudio_CodecConfiguration.

###### KSPROPERTY_BtLeAudio_DATAPATH_CONFIG

This KSProperty allows IHV ACX audio drivers to set or update the data path configuration as defined in Bluetooth_DatapathConfiguration. The KSProperty shall be sent by the audio driver to the Bluetooth profile before the start audio stream callback is invoked. This property may be used to set a single configuration for all data paths in a single direction or to set a specific data path configuration for each codec configuration entry set in BluetoothLEAudio_CodecConfiguration. If the value contains multiple data path configurations, then the order of the configurations shall be used for the codec configuration entry as ordered in the property BluetoothLEAudio_CodecConfiguration. The number of codec configurations shall be equal to the number of data path IDs set by either KSPROPERTY_BtLeAudio_DATAPATH_ID or Bluetooth_DatapathID.

| Field | Size | Value
|---|---|---|
| Configuration Count | 1 byte | 1 or Codec Configuration Count set in BluetoothLEAudio_CodecConfiguration |
| Configuration Size[i] | 1 byte | Shall not exceed 255 |
| Configuration[i] | Configuration Size[i] | &nbsp; |

### Interfaces

#### Audio endpoint template binding IDs

Used by the audio driver's ACX circuit factory to know when an ACX circuit for a paired Bluetooth device is created.

The following component IDs are used to create Bluetooth LE Audio circuits:

```cpp
// {5C52FDB5-722A-4AB7-A342-70163B7E9B5C}
DEFINE_GUID(GUID_BLUETOOTH_LEAUDIO_RENDER_COMPONENT_ID,
0x5c52fdb5, 0x722a, 0x4ab7, 0xa3, 0x42, 0x70, 0x16, 0x3b, 0x7e, 0x9b, 0x5c);

// {1DFF2EE3-AE89-441C-BDE3-24F885C55DF8}
DEFINE_GUID(GUID_BLUETOOTH_LEAUDIO_CAPTURE_COMPONENT_ID,
0x1dff2ee3, 0xae89, 0x441c, 0xbd, 0xe3, 0x24, 0xf8, 0x85, 0xc5, 0x5d, 0xf8);
```

#### Bluetooth LE Audio support interface

Used by the audio driver stack to indicate that it's available for streaming Bluetooth LE Audio. Windows Bluetooth Audio service-level watch for this interface and wait until it's published before enabling Bluetooth LE Audio support.

The following interface IDs are used to publish the Bluetooth LE Audio support interface:

```cpp
// {BA02FA1B-0FD0-4A0F-A748-4FAE2E2D2F67}
DEFINE_GUID(GUID_BLUETOOTH_LEAUDIO_SUPPORT_INTERFACE,
0xba02fa1b, 0x0fd0, 0x4a0f, 0xa7, 0x48, 0x4f, 0xae, 0x2e, 0x2d, 0x2f, 0x67);
```

### Common sequences

The following sequences are executed for both unicast and broadcast LE audio scenarios.

#### Audio driver initialization

When the IHV ACX Streaming driver loads and determines that it supports Bluetooth LE Audio streaming, it shall show support for the technology by creating an **ACXFACTORYCIRCUIT** object and registering for Bluetooth template bindings with ACX using the IDs defined in [Audio Endpoint Template Binding IDs](#audio-endpoint-template-binding-ids).

:::image type="content" source="images/btle-audio-driver-init-seq.png" alt-text="Flowchart illustrating the Bluetooth LE Audio driver initialization sequence.":::

#### Unicast Audio Sequences

##### Endpoint creation

1. When an LE Audio device is paired with the system, the Bluetooth LE Audio Profile:
   1. Reads the published audio capabilities of the remote device.
   1. Discovers the controller supported capabilities by sending the commands HCI_Read_Local_Support_Codecs [v2] and HCI_Read_Local_Supported_Codec_Capabilities.
   1. Creates an [ACXCIRCUIT](/windows-hardware/drivers/audio/acx-summary-of-objects#acx-circuit) with the supported formats set based on the codec capabilities supported by the Bluetooth controller and remote audio device. If the controller doesn't support any codecs because codec support is in the audio DSP or audio driver, then the supported formats are set to the formats supported by the remote audio device.
1. After the **ACXCIRCUIT** is created, ACX requests the IHV ACX streaming driver's ACX circuit factory to create an **ACXCIRCUIT** for stream processing.
1. When a request to create a circuit is received, the IHV ACX streaming driver:
   1. Creates **ACXCIRCUIT**, [ACXPIN](/windows-hardware/drivers/audio/acx-summary-of-objects#acx-pin), [ACXOBJECTBAG](/windows-hardware/drivers/audio/acx-summary-of-objects#acx-object-bag), and [ACXSTREAMBRIDGE](/windows-hardware/drivers/audio/acx-summary-of-objects#acx-stream-bridge) objects.
   1. If the LC3 or vendor specific codec is hosted in the audio driver or DSP, then the IHV ACX streaming driver sets the *BluetoothLEAudio_CodecCapabilities* property on the **ACXOBJECTBAG**.
   1. The IHV ACX streaming driver may set *Bluetooth_DatapathID* or *Bluetooth_DatapathConfiguration* on the **ACXOBJECTBAG** if it's known at this time.
1. After both circuits are created, ACX invokes the **[EvtAcxPinConnected](/windows-hardware/drivers/ddi/acxpin/nc-acxpin-evt_acx_pin_connected)** callback on the IHV ACX driver's bridge pin.
1. When it's **EvtAcxPinConnected** callback is invoked, the IHV ACX streaming driver:
   1. Retrieves the bridge pin of the profile circuit with **[AcxTarget...](/windows-hardware/drivers/ddi/acxtargets/)** APIs to retrieve the formats supported by the profile circuit.
   1. Iterates through the list of **ACXDATAFORMAT**s set by the profile circuit. If the Bluetooth audio codec is hosted in the audio driver or audio DSP, then the IHV audio driver updates its **ACXDATAFORMAT**s with the formats that are supported by the codec and profile circuit. Otherwise, all formats are copied to the IHV ACX streaming driver's host pin.
   1. Sets the updated format list on the bridge pin if an audio-engine is created for offload streaming.
1. After the formats are updated, ACX enables both interfaces, and an audio endpoint is created.

    :::image type="content" source="images/btle-audio-endpoint-creation.png" alt-text="Flowchart depicting the Bluetooth LE Audio endpoint creation process.":::

##### Stream creation

1. When an application requests to create an audio stream, ACX invokes the registered **EvtCircuitCreateStream** callbacks for each circuit, beginning with the IHV ACX streaming driver.
1. When its **EvtCircuitCreateStream** callback is invoked, the IHV ACX streaming driver:
   1. Sets or updates the Bluetooth_DatapathId and Bluetooth_DataPathConfiguration properties on the [ACXOBJECTBAG](/windows-hardware/drivers/audio/acx-summary-of-objects#acx-object-bag) attached to the [ACXSTREAMBRIDGE](/windows-hardware/drivers/audio/acx-summary-of-objects#acx-stream-bridge).
   1. Creates an [ACXSTREAM](/windows-hardware/drivers/audio/acx-summary-of-objects#acx-stream) with callbacks set for stream state transitions and RT stream processing
   1. Creates an audio-engine element on the stream if the audio pipeline supports offload streaming.
   1. Adds the **ACXSTREAM** to its stream bridge. This invokes the Bluetooth LE Audio profile's **EvtCircuitCreateStream** callback.
1. When its **[EvtAcxCircuitCreateStream](/windows-hardware/drivers/ddi/acxcircuit/nc-acxcircuit-evt_acx_circuit_create_stream)** callback is invoked, the Bluetooth LE Audio profile:
   1. Saves the properties locally from the **ACXOBJECTBAG** set by the IHV ACX streaming driver for future stream transition callbacks.
   1. Performs the Config Codec Operation as defined in the BAP specification. The parameters for the operation are derived from the **ACXDATAFORMAT** specified in the **EvtAcxCircuitCreateStream** callback and either the other stream parameters in the **ACXOBJECTBAG** or the codec capabilities supported by the Bluetooth Controller.
   1. Allocates stream resources by sending the HCI LE Set CIG Parameters command.
   1. Sets the BluetoothLEAudio_StreamConnectionHandles property with the list of CIS connection handles returned by the Bluetooth controller.
   1. Sets the *BluetoothLEAudio_CodecConfiguration* property on the **ACXOBJECTBAG** with the value used to configure the remote audio devices.
1. If the IHV ACX streaming driver needs to update its data path ID or data path configuration based on the object bag values set by the profile, then it can invoke the KSPROPERTY set operations to update the value stored by the profile circuit.
    1. Creates an **ACXSTREAM** with callbacks set for stream state transitions.

      :::image type="content" source="images/btle-audio-stream-creation.png" alt-text="Flowchart showing the Bluetooth LE Audio stream creation process.":::

#### Stream state transitions

ACX decides the circuit order of stream state transitions based on the audio flow and whether the state is transitioning to a more active or less active state.

- For Render streams going from a less-active state to a more-active state, the profile circuit receives the event first, followed by the streaming circuit.
- For Render streams going from a more-active state to a less-active state, the streaming circuit receives the event first, followed by the profile circuit. 
- For Capture streams going from a less-active state to a more-active state, the streaming circuit receives the event first, followed by the profile circuit. 
- For Capture streams going from a more-active state to a less-active state, the profile circuit with receive the event first, followed by the streaming circuit.

#### Prepare stream

When its **[EvtAcxStreamPrepareHardware](/windows-hardware/drivers/ddi/acxstreams/nc-acxstreams-evt_acx_stream_prepare_hardware)** callback is invoked, the Bluetooth LE Audio profile sends the ASCS config QoS operation to synchronize settings with the remote device if needed. It's possible that the ASCS config QoS operation was already complete when the callback was invoked for the other direction of a bidirectional stream.

:::image type="content" source="images/btle-audio-stream-preparation-profile-circuit.png" alt-text="Flowchart illustrating the Bluetooth LE Audio stream preparation for a profile circuit.":::

When its **EvtAcxStreamPrepareHardware** callback is invoked, the IHV ACX streaming driver allocates the necessary streaming resources and initializes the audio pipeline to be in the acquired state.

:::image type="content" source="images/btle-audio-stream-preparation-streaming-circuit.png" alt-text="Flowchart depicting the Bluetooth LE Audio stream preparation for a streaming circuit.":::

#### Start stream

When its **[EvtAcxStreamRun](/windows-hardware/drivers/ddi/acxstreams/nc-acxstreams-evt_acx_stream_run)** callback is invoked, the Bluetooth LE Audio profile:

1. Applies any configuration arguments from the ACX streaming driver, as described below, using the HCI_Configure_Data_Path command if they have changed. The Windows Bluetooth Core Stack caches the Vendor_Specific_Config buffer for each Data_Path_Direction and Data_Path_ID pair. The HCI_Configure_Data_Path command is sent only when the Vendor_Specific_Config changes for a Data_Path_Direction and Data_Path_ID pair.
    1. Data_Path_Direction is the AudioDirection of the streaming circuit callback issuing the EvtAcxStreamRun callback.
    1. The Data_Path_ID is populated with the most recently assigned value from either of the following sources:
        1. Bluetooth_DatapathID on the ACXOBJECTBAG attached to the ACXSTREAMBRIDGE passed to the Windows Bluetooth LE Audio Profile during the EvtCircuitCreateStream callback.
        1. Data from KSPROPERTY_BtLeAudio_DATAPATH_ID.
    1. The Vendor_Specific_Config data is populated with the most recently assigned value from either of the following sources:
        1. Bluetooth_DatapathConfiguration on the ACXOBJECTBAG attached to the ACXSTREAMBRIDGE passed to the Windows Bluetooth LE Audio Profile circuit during the EvtCircuitCreateStream callback.
        1. Data from KSPROPERTY_BtLeAudio_DATAPATH_CONFIG.
1. Sends the ASCS Enable operation to the remote devices.
1. Creates CISes if they aren't already created using the HCI_LE_Create_CIS command.
1. If the data path isn't already configured, the Bluetooth LE audio profile:
    1. Establishes the ISO data paths using the HCI_LE_Setup_ISO_Data_Path command
        1. If the IHV ACX streaming driver sets the property BluetoothLEAudio_CodecCapabilities, then the value of the Codec_ID field in HCI_LE_Setup_ISO_Data_Path shall be set to transparent (0x3) as defined in the Bluetooth Assigned Numbers. Otherwise, the value shall be the same as the Codec ID used in the config codec operation in the stream creation procedure.
1. If the audio stream is a capture stream, the Bluetooth LE audio profile performs the BAP receiver start ready operation.

:::image type="content" source="images/btle-audio-stream-start-profile-circuit.png" alt-text="Flowchart showing the Bluetooth LE Audio stream starting process for a profile circuit.":::

When its **EvtAcxStreamRun** callback is invoked, the IHV ACX streaming driver starts processing incoming audio data from either the Windows audio system (render) or the Bluetooth controller (capture).

:::image type="content" source="images/btle-audio-stream-start-streaming-circuit.png" alt-text="Flowchart illustrating the Bluetooth LE Audio stream starting process for a streaming circuit.":::

#### Pause stream

When its **[EvtAcxStreamPause](/windows-hardware/drivers/ddi/acxstreams/nc-acxstreams-evt_acx_stream_pause)** callback is invoked, the Bluetooth LE Audio profile:

1. Performs the BAP unicast stream disable procedure.
1. Removes the ISO data path using the HCI_LE_Remove_ISO_Data_Path command.
1. Performs the ASCS receiver stop ready procedure if the audio stream is a unicast capture stream.
1. Disconnect CISes if there are no other streams in use for that CIS.

:::image type="content" source="images/btle-audio-stream-pause-profile-circuit.png" alt-text="Flowchart depicting the Bluetooth LE Audio stream pausing process for a profile circuit.":::

When its **EvtAcxStreamPause** callback is invoked, the IHV ACX streaming driver pauses its audio processing pipeline.

:::image type="content" source="images/btle-audio-stream-pause-streaming-circuit.png" alt-text="Flowchart showing the Bluetooth LE Audio stream pausing process for a streaming circuit.":::

#### Release stream

When its **[EvtAcxStreamReleaseHardware](/windows-hardware/drivers/ddi/acxstreams/nc-acxstreams-evt_acx_stream_release_hardware)** callback is invoked, the Bluetooth LE Audio Profile:

1. Sends the ASCS Release operation to the remote Bluetooth LE Audio device
1. Removes the CIG if all CISes are disconnected.

:::image type="content" source="images/btle-audio-stream-release-profile-circuit.png" alt-text="Flowchart illustrating the Bluetooth LE Audio stream releasing process for a profile circuit.":::

When its **EvtAcxStreamReleaseHardware** callback is invoked, the IHV ACX streaming driver releases its audio pipeline resources.

:::image type="content" source="images/btle-audio-stream-release-streaming-circuit.png" alt-text="Flowchart depicting the Bluetooth LE Audio stream releasing process for a streaming circuit.":::

#### Endpoint disconnection

The Windows Bluetooth LE Audio profile updates an endpoint's connection state if the remote unicast device doesn't have an LE-ACL connection to the PC or is reporting through its PACS available audio contexts that it isn't available for streaming. When the endpoint is disconnected, the Windows audio service invalidates any active streams to the endpoint. This results in the stream pause and release sequences to occur.

### Volume and mute

The IHV ACX streaming circuit should only include volume and mute elements if the streaming driver requires an audio-engine. When using an audio-engine, the configuration flags must be set as such:

```cpp
ACX_AUDIOENGINE_CONFIG audioEngineCfg;
ACX_AUDIOENGINE_CONFIG_INIT(&audioEngineCfg);
…

audioEngineCfg.Flags |= AcxAudioEngineConfigVolumeSecondary; // Use this control only if endpoint doesn't have one.

audioEngineCfg.MuteElement = muteElement;

audioEngineCfg.Flags |= AcxAudioEngineConfigMuteSecondary; // Use this control only if endpoint doesn't have one.

audioEngineCfg.PeakMeterElement = peakmeterElement;

audioEngineCfg.Flags |= AcxAudioEngineConfigPeakMeterSecondary; // Use this control only if endpoint doesn't have one.
```

This is required to allow Bluetooth LE Audio endpoints to use the Bluetooth SIG defined volume and microphone control profiles for volume and mute changes for unicast audio endpoints.

If the remote Bluetooth LE Audio device doesn't support the volume or microphone control services, or the endpoint is created for broadcast audio, then the volume and mute elements in the audio-engine shall serve as a fallback to handle the change requests from the audio system. The Windows audio system handles changes to volume and mute. If there's no audio-engine and either remote device doesn't support the volume, or microphone services or the audio endpoint is for broadcast audio.

#### Endpoint removal

A Bluetooth LE audio endpoint is removed from the system when either the profile circuit or streaming circuit is destroyed. The profile circuit can be removed when the remote unicast device's pairing is removed from Windows or the Bluetooth radio is disabled.

1. When the Windows Bluetooth LE audio profile removes its circuit, ACX disables its endpoint interfaces to signal to the Windows audio service that the endpoint should be removed.
1. When the interfaces are disabled, the Windows audio service invalidates any active streams to the Bluetooth LE audio endpoint, this operation results in the stream pause and release callbacks to be invoked on the streaming circuit.
1. To complete endpoint removal, ACX invalidates the IHV ACX streaming driver's circuit, which results in the WDF invoking the circuit's cleanup callback.
1. When its cleanup callback is invoked, the IHV ACX streaming driver releases its circuit.

:::image type="content" source="images/btle-audio-endpoint-removal.png" alt-text="Flowchart showing the Bluetooth LE Audio endpoint removal process.":::

### Bluetooth LE and classic audio coexistence

Windows shall ensure that only classic audio or LE audio is active for a paired Bluetooth audio device that supports both technologies. If LE audio is active, then the sideband DDIs for A2DP and HFP for the remote device are disabled and the profile circuit is created for the LE audio endpoint. If classic audio is active, the sideband DDIs for A2DP and HFP for the remote device are enabled and the profile circuit isn't created for the LE audio endpoint.

### Power management

Bluetooth LE Audio doesn't have any power management requirements or flows outside of what is already defined by [WDF](../wdf/pnp-and-power-management-callback-sequences.md).

### Stereo render with mono capture

Today's Bluetooth audio experience is convenient but has limitations, especially when compared to wired audio experiences. One key limitation, with user-facing consequences, is the drop to mono audio whenever the microphone is active. This blocks experiences like Spatial Audio in Teams and other VoIP apps from working, and it heavily degrades gaming experiences involving voice chat.

Bluetooth LE Audio can close the gap with improved audio fidelity and reduced latency for these scenarios by adding support for stereo playback while the microphone is in use.

#### Render/capture format pairs

An IHV solution advertises its support for stereo render with mono capture by providing a list of render/capture format pairs, each of which consists of a stereo render format and a mono capture format that can be used simultaneously for bidirectional streaming. A stereo render (or mono capture) format is defined as a pair of a Sampling_Frequency (for example, 16/24/32/48 kHz) and an Audio_Channel_Count (for example, 1/2 ch) associated with a specific audio codec, which isn't limited to LC3.

For example, suppose an IHV solution supports both 16kHz stereo render with 16kHz mono capture, and 48kHz stereo render with either 24kHz or 32kHz mono capture. The corresponding render/capture format pairs look like this:

| Entry | Render format | Capture format |
|---|---|---|
| 1 | Render(16 kHz, 2 ch) | Capture(16 kHz, 1 ch) |
| 2 | Render(48 kHz, 2 ch) | Capture(24 kHz, 1 ch) |
| 3 | Render(48 kHz, 2 ch) | Capture(32 kHz, 1 ch) |

*<sup>Table 3: Sample render/capture format pairs</sup>*

Since a coordinated set member might join or disjoin at any time, an IHV solution must support mono render with mono capture at the same respective sampling frequencies for each entry in the format pairs. This means that, given the example in Table 3, all format pairs below must also be implicitly supported even though they aren't explicitly declared:

| Entry | Render format | Capture format |
|---|---|---|
| 1 | Render(16 kHz, 1 ch) | Capture(16 kHz, 1 ch) |
| 2 | Render(48 kHz, 1 ch) | Capture(24 kHz, 1 ch) |
| 3 | Render(48 kHz, 1 ch) | Capture(32 kHz, 1 ch) |

*<sup>Table 4: Implicit render/capture format pairs for Table 3</sup>*

The main difference between Table 3 and Table 4 is that the Audio_Channel_Count for each render format in the latter is set to one (for "mono render"); everything else stays the same.

#### Mandatory Render/Capture Format Pairs

Table 5 defines the list of audio formats all IHV solutions shall support:

| Entry | (Render_format, Capture_format) |
|---|---|
| 1 | { Render(48 kHz, 2 ch), Capture(32 kHz,1 ch) } |
| 2 | { Render(32 kHz, 2 ch), Capture(32 kHz,1 ch) } |
| 3 | { Render(24 kHz, 2 ch), Capture(24 kHz,1 ch) } |
| 4 | { Render(16 kHz, 2 ch), Capture(16 kHz,1 ch) } |

*<sup>Table 5 Mandatory render/capture format pairs</sup>*

#### Capabilities Advertisement

Depending on whether the Bluetooth controller supports the audio codec involved (default to LC3), an IHV solution advertises the list of render/capture format pairs it supports in different ways. Specifically:

- If the codec is in the Bluetooth controller, both the controller and the IHV ACX streaming driver shall advertise the lists of format pairs independently. If the two lists disagree with each other, Windows shall intersect and keep the common parts.

- If the codec isn't in the Bluetooth controller (for example, it is in the audio DSP), only the IHV ACX streaming driver is required to advertise the list of format pairs.
Bluetooth controller

Since the Codec_Capability[i] in the response for an HCI_Read_Local_Supported_Codec_Capabilities doesn't support metadata, the Bluetooth controller is required to support a family of Microsoft-specific codec IDs (see Table 7) such that Windows can query for more codec capabilities, for example, the list of render/capture format pairs, that can't be easily conveyed through the existing HCI interface.

| Parameter | Size (Octets) | Description |
|---|---|---|
| Codec_ID | 5 | **Octet 0:** 0xFF (Vendor Specific)<br><hr>**Octet 1 to 2:** 0x0006 (Microsoft)<br><hr>**Octet 3 to 4:** Vendor-defined codec ID <br><br>If the most significant bit of octet 4 is set to zero (0), octet 3 contains a SIG-approved coding format (ranging from 0x00 to 0x07 as of May 31, 2024), except for 0xFF.<br><br>If the most significant bit of octet 4 is set to one (1), octet 3 contains a coding format that is yet to be defined and is reserved by Windows for future use. |

*<sup>Table 7 Microsoft-specific codec ID</sup>*

The scopes of these Microsoft-specific codec IDs are limited to:

- HCI_Read_Local_Supported_Codecs [v2]
- HCI_Read_Local_Supported_Codec_Capabilities

By contract, Windows shall not use any of these Microsoft-specific codec IDs for other types of HCI commands.

##### HCI_Read_Local_Supported_Codecs [v2]

The controller shall advertise its support for the Microsoft-specific codec ID via Vendor_Specific_Codec_ID and Vendor_Specific_Codec_Transport:

| Field | Description |
|---|---|
| Vendor_Specific_Codec_ID[k] | **Octets 0 to 1:** Company ID (0x0006)<br>For more information, see **Octet 1 to 2** in Table 7.<br><hr>**Octets 2 to 3:** Vendor-defined codec ID (for example, 0x0006 for LC3)<br>For more information, see **Octet 3 to 4** in Table 7. |
| Vendor_Specific_Codec_Transport[k] | LE_CIS (0x02) must be supported. |

*<sup>Table 8 HCI_Read_Local_Supported_Codec [v2] response value</sup>*

##### HCI_Read_Local_Supported_Codec_Capabilities

To query for all Windows-specific codec capabilities, including the list of render/capture format pairs, Windows calls HCI_Read_Local_Supported_Codec_Capabilities with the following arguments:

| Parameter | Size (Octets) | Description |
|---|---|---|
| Codec_ID (Microsoft-specific codec ID) | 5 | **Octet 0:** 0xFF (Vendor Specific)<br><hr>**Octet 1 to 2:** Company ID (0x0006)<br>For more information, see **Octet 1 to 2** in Table 8.<br><hr>**Octet 3 to 4:** Vendor-defined codec ID (for example, 0x0006 for LC3)<br>For more information, see **Octet 3 to 4** in Table 8. |
| Logical_Transport_Type | 1 | 0x2 (LE CIS) |
| Direction | 1 | 0x00 (Input, for example, Host to Controller) |

*<sup>Table 9 HCI_Read_Local_Supported_Codec_Capabilities command arguments</sup>*

Upon receiving such a command, the controller shall return all Windows-specific capabilities for the codec specified by the Vendor-defined codec ID. For example, if the Vendor-defined codec ID is set to 0x0006, the controller shall return all LC3-related capabilities required by Windows.

The response for the command maintains the same top-level structure as that defined by Bluetooth Core Specification:

| Parameter | Size (Octets) | Description |
|---|---|---|
| Status | 1 | 0x00 (Success); 0x01 to 0xFF (Error code) |
| Num_Codec_Capabilities | 1 | Total number of capabilities returned. |
| Codec_Capability_Length[i] | 1 | Length of the Codec_Capability[i] field. |
| Codec_Capability [i] | Varies | Codec_Capability_Length[i] octets of codec-specific capability data. |

*<sup>Table 10 HCI_Read_Local_Supported_Codec_Capabilities response structure</sup>*

However, the payload of *Codec_Capability[i]* is different from that defined by the SIG and is tailored for Windows.

Currently, the only codec capability defined by Windows is Bidirectional_Multichannel_Streaming, which is described below.

###### Bidirectional_Multichannel_Streaming

By advertising Bidirectional_Multichannel_Streaming, the controller affirms that it supports concurrent *m*-channel render with *n*-channel capture where *m* ≥ 1, *n* ≥ 1, and *m* + *n* > 2. (Stereo render with mono capture is effectively a Bidirectional_Multichannel_Streaming with m = 2 and n = 1.)

This table describes the format for Bidirectional_Multichannel_Streaming:

| Parameter | Size (Octets) | Bits| Description |
|---|---|---|---|
| Type  1 | 0x00 | (Bidirectional_Multichannel_Streaming) |
| Channel_Counts | 1 | **Bit 0 to 4:** (m – 1), where m is the number of render channels | (For stereo render with mono capture, this should have the value, 2 – 1 = 1.) |
| Channel_Counts | 1 | **Bit 5 to 7:** (n – 1), where n is the number of capture channels | (For stereo render with mono capture, this should have the value, 1 – 1 = 0.) |
| Render_Sampling_Frequencies | 1 | **Bit 0:** 16 kHz<br>**Bit 1:** 24 kHz<br>**Bit 2:** 32 kHz<br>**Bit 3:** 48 kHz<br>**Bit 4:** RFU<br>**Bit 5:** RFU<br>**Bit 6:** RFU<br>**Bit 7:** RFU | All sampling frequencies in this list have the same channel count as that specified by bit 0-4 of Channel_Count.<br><br>All RFU bits are reserved and must be set to zero. |
| Capture_Sampling_Frequencies_-List[i], where 0 ≤ i ≤ 7 | i + 1 | **Bit 0:** 16 kHz<br>**Bit 1:** 24 kHz<br>**Bit 2:** 32 kHz<br>**Bit 3:** 48 kHz<br>**Bit 4:** RFU<br>**Bit 5:** RFU<br>**Bit 6:** RFU<br>**Bit 7:** RFU | All sampling frequencies in this list have the same channel count as that specified by bit 5-7 of Channel_Count. <br><br>Each Capture_Sampling_Frequencies_List instance is one octet in size and there can be up to eight such instances (if all bits in Render_Sampling_Frequencies are set to one).<br><br>All RFU bits are reserved and must be set to zero. |

*<sup>Table 11 Bidirectional_Multichannel_Streaming Format (Max length: 11 bytes)</sup>*

**Channel_Counts**

The choice of bit counts for render/capture is arbitrary – five bits are allocated for render (to cover all SIG-defined audio locations), and three bits for capture (to minimize HCI payload size).

For example, the *Channel_Counts* for Table 3 is 0b0000'0001 because the number of render/capture channels, for example, *m* and *n*, are 2 and 1 respectively:

| &nbsp; | Capture | Render |
|---|---|---|
| **Bit** | 7 6 5 | 4 3 2 1 0 |
| **Value** | 0  0  **0** | 0 0 0 0 **1** |

*<sup>Table 12 Channel_Counts for Table 3</sup>*

By design, all capabilities with the same pair of Microsoft-specific codec ID and *Channel_Counts* must be grouped together and represented by a single Bidirectional_Multichannel_Streaming record.

**Render_Sampling_Frequencies**

The *Render_Sampling_Frequencies* field specifies all render frequencies that can be used in the context of the associated Bidirectional_Multichannel_Streaming structure.

For example, the *Render_Sampling_Frequencies* for Table 3 is 0b0000'1001, which means that both 16kHz and 48kHz can be used as the sampling frequency for two-channel render:

| kHz | RFU | RFU | RFU | RFU | 48 | 32 | 24 | 16 |
|---|---|---|---|---|---|---|---|---|
| **Bit** | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| **Value** | 0 | 0 | 0 | 0 | **1** | 0 | 0 | **1** |

*<sup>Table 13 Render_Sampling_Frequencies for Table 3</sup>*

**Capture_Sampling_Frequencies_List[i]**

For each "one" bit in *Render_Sampling_Frequencies*, starting from the least significant to the most significant one, the controller shall provide a unique bit mask (*Capture_Sampling_Frequencies_List[i]*) specifying all capture frequencies that are compatible with the frequency represented by that render bit. The controller shall not provide a *Capture_Sampling_Frequencies* bit mask for any "zero" bit in *Render_Sampling_Frequencies*.

For example, the capture bit masks for Table 3 look like this:

```cpp
// The order matters!
{
    // Capture_Sampling_Frequencies_List[0] for 16kHz dual-channel rendering.
    0b0000'0001, // 16 kHz single-channel capture

    // Do not create a dummy Capture_Sampling_Frequencies_List entry, for example, 0b0000'0000,
    // for 24kHz dual-channel rendering, which is not supported at all.

    // Do not create a dummy Capture_Sampling_Frequencies_List entry, for example, 0b0000'0000,
    // for 32kHz dual-channel rendering, which is not supported at all.

    // Capture_Sampling_Frequencies_List[1] for 48kHz dual-channel rendering.
    0b0000'0110 // Either 24 or 32 kHz single-channel capture
}
```

Specifically:

| Render_-Sampling_-Frequencies | *i* | Capture_-Sampling_-Frequencies[*i*] | Description |
|---|---|---|---|
| 0b0000'100**1**<br>&nbsp;&nbsp;&nbsp;⇤ order ↤ | 0 | 0b0000'000**1** | The first least significant "one" bit (bit 0) in *Render_Sampling_Frequencies* corresponds to 16 kHz.<br><br>Enable bit 0 of *Capture_Sampling_Frequencies_List[0]* to indicate that 16 kHz capture can be paired with that render frequency. |
| 0b0000'**1**001<br>&nbsp;&nbsp;&nbsp;⇤ order ↤ | 1 | 0b0000'0**11**0 | The second least significant "one" bit (bit 3) in *Render_Sampling_Frequencies* corresponds to 48 kHz.<br><br>Enable bit 1 and 2 of *Capture_Sampling_Frequencies_List[1]* to indicate that 24 kHz and 32 kHz capture can be paired with that render frequency. |

*<sup>Table 14 Example for building a Capture_Sampling_Frequencies_List[i] for a Render_Sampling_Frequencies</sup>*

#### IHV ACX Streaming Driver

To support stereo render with mono capture, an IHV ACX streaming driver sets the device property, BluetoothLEAudioBidirectionalMultichannelStreamingCapabilities, which represents the render/capture format pairs described in 3.11.2, to an instance of the device interface class, GUID_BLUETOOTH_LEAUDIO_SUPPORT_INTERFACE.

The property should be made available immediately after the device interface class instance is created and the value of the property remains constant throughout the lifetime of the device interface class instance.

The property key of BluetoothLEAudioBidirectionalMultichannelStreamingCapabilities is defined as:

```cpp
DEFINE_DEVPROPKEY(DEVPKEY_BluetoothLEAudioBidirectionalMultichannelStreamingCapabilities,
    0xd27ba3a4, 0x1bfe, 0x4374, 0x88, 0x7d, 0xe8, 0xb3, 0xa6, 0xac, 0xe, 0xe9, 2); // DEVPROP_TYPE_BINARY (BTH_LE_AUDIO_BIDIRECTIONAL_MULTICHANNEL_STREAMING_CAPABILITY[])
```

The property value type associated with the key, DEVPKEY_BluetoothLEAudioBidirectionalMultichannelStreamingCapabilities, is defined as:

```cpp
typedef struct _BTH_LE_AUDIO_BIDIRECTIONAL_MULTICHANNEL_STREAMING_CAPABILITY
{
    BTH_LE_AUDIO_CODEC_ID CodecId;
    BOOL IsCodecPresent;
    BTH_LE_AUDIO_BIDIRECTIONAL_MULTICHANNEL_STREAMING_CHANNEL_COUNT RenderChannelCount;
    BTH_LE_AUDIO_BIDIRECTIONAL_MULTICHANNEL_STREAMING_CHANNEL_COUNT CaptureChannelCount;
    BTH_LE_AUDIO_BIDIRECTIONAL_MULTICHANNEL_STREAMING_SAMPLING_FREQUENCY RenderSamplingFrequencies;
    BTH_LE_AUDIO_BIDIRECTIONAL_MULTICHANNEL_STREAMING_SAMPLING_FREQUENCY CaptureSamplingFrequenciesList[
        BTH_LE_AUDIO_BIDIRECTIONAL_MULTICHANNEL_STREAMING_SAMPLING_FREQUENCY_BIT_LENGTH
    ];
} BTH_LE_AUDIO_BIDIRECTIONAL_MULTICHANNEL_STREAMING_CAPABILITY;

Where:

typedef struct _BTH_LE_AUDIO_CODEC_ID
{
    UINT8 CodingFormat;
    UINT16 CompanyId;
    UINT16 VendorCodecId;
} BTH_LE_AUDIO_CODEC_ID;

typedef UINT8 BTH_LE_AUDIO_BIDIRECTIONAL_MULTICHANNEL_STREAMING_CHANNEL_COUNT;

typedef enum _BTH_LE_AUDIO_BIDIRECTIONAL_MULTICHANNEL_STREAMING_SAMPLING_FREQUENCY :
    UINT8 // Bit flags
{
    // 16 kHz
    BTH_LE_AUDIO_BIDIRECTIONAL_MULTICHANNEL_STREAMING_SAMPLING_FREQUENCY_16000HZ = 0x1,

    // 24 kHz
    BTH_LE_AUDIO_BIDIRECTIONAL_MULTICHANNEL_STREAMING_SAMPLING_FREQUENCY_24000HZ = 0x2,

    // 32 kHz
    BTH_LE_AUDIO_BIDIRECTIONAL_MULTICHANNEL_STREAMING_SAMPLING_FREQUENCY_32000HZ = 0x4,

    // 48 kHz
    BTH_LE_AUDIO_BIDIRECTIONAL_MULTICHANNEL_STREAMING_SAMPLING_FREQUENCY_48000HZ = 0x8,

    // A dummy value for indicating a sampling frequency is "not applicable" in the
    // respective context.
    BTH_LE_AUDIO_BIDIRECTIONAL_MULTICHANNEL_STREAMING_SAMPLING_FREQUENCY_NONE = 0,

    // All valid sampling frequencies combined.
    BTH_LE_AUDIO_BIDIRECTIONAL_MULTICHANNEL_STREAMING_SAMPLING_FREQUENCY_ALL =
        BTH_LE_AUDIO_BIDIRECTIONAL_MULTICHANNEL_STREAMING_SAMPLING_FREQUENCY_16000HZ |
        BTH_LE_AUDIO_BIDIRECTIONAL_MULTICHANNEL_STREAMING_SAMPLING_FREQUENCY_24000HZ |
        BTH_LE_AUDIO_BIDIRECTIONAL_MULTICHANNEL_STREAMING_SAMPLING_FREQUENCY_32000HZ |
        BTH_LE_AUDIO_BIDIRECTIONAL_MULTICHANNEL_STREAMING_SAMPLING_FREQUENCY_48000HZ,
} BTH_LE_AUDIO_BIDIRECTIONAL_MULTICHANNEL_STREAMING_SAMPLING_FREQUENCY;

DEFINE_ENUM_FLAG_OPERATORS(BTH_LE_AUDIO_BIDIRECTIONAL_MULTICHANNEL_STREAMING_SAMPLING_FREQUENCY);

#define BTH_LE_AUDIO_BIDIRECTIONAL_MULTICHANNEL_STREAMING_SAMPLING_FREQUENCY_BIT_LENGTH \
    (sizeof(BTH_LE_AUDIO_BIDIRECTIONAL_MULTICHANNEL_STREAMING_SAMPLING_FREQUENCY) * 8)
```

The **BTH_LE_AUDIO_BIDIRECTIONAL_MULTICHANNEL_STREAMING_CAPABILITY** structure follows similar rules as described in [Bidirectional_Multichannel_Streaming](#bidirectional_multichannel_streaming), except that:

- The ACX streaming driver is required to set an extra flag, IsCodecPresent, to indicate whether the codec of interest is conceptually part of the ACX streaming driver. For example, if the codec is in the audio DSP, IsCodecPresent should be set to TRUE. If the codec is in the Bluetooth controller, the flag should be set to FALSE.

- For m-channel render with n-channel capture, the values for RenderChannelCount and CaptureChannelCount are m and n, respectively. In other words, RenderChannelCount and CaptureChannelCount indicate the real number of render and capture channels.

- Given an index, i, there's a one-to-one mapping between the i-th least significant bit of RenderSamplingFrequencies and the i-th entry of CaptureSamplingFrequenciesList. If the i-th bit of RenderSamplingFrequencies is zero, set CaptureSamplingFrequenciesList[i] to zero.

The following sample code shows how to create the GUID_BLUETOOTH_LEAUDIO_SUPPORT_INTERFACE device interface, and sets the BluetoothLEAudioBidirectionalMultichannelStreamingCapabilities device interface property:

```cpp
PAGED_CODE_SEG
NTSTATUS
AdvertiseBluetoothLEAudioSupport(
    WDFDEVICE Device
    )
{
    // Create a device interface with the class,
    // GUID_BLUETOOTH_LEAUDIO_SUPPORT_INTERFACE, for the specified WDF device.
    DECLARE_CONST_UNICODE_STRING(
        bluetoothLEAudioSupportInterface, L"BluetoothLEAudioSupport");
    RETURN_NTSTATUS_IF_FAILED(WdfDeviceCreateDeviceInterface(
        Device,
        &GUID_BLUETOOTH_LEAUDIO_SUPPORT_INTERFACE,
        (PUNICODE_STRING)&bluetoothLEAudioSupportInterface));

#pragma region associate BluetoothLEAudioBidirectionalMultichannelStreamingCapabilities with GUID_BLUETOOTH_LEAUDIO_SUPPORT_INTERFACE.
    // Advertise bidirectional multichannel streaming support by setting the device
    // interface property, 
    // BluetoothLEAudioBidirectionalMultichannelStreamingCapabilities,
    // to the newly created device interface.

    // See Table 7 "Microsoft-specific codec ID" in Microsoft Bluetooth LE Audio
    // IHV Specification for reference.
    constexpr BTH_LE_AUDIO_CODEC_ID microsoftLC3CodecId
    {
        0xff, // Vendor-specific
        0x6,  // Microsoft
        0x6,  // LC3
    };

    constexpr BTH_LE_AUDIO_CODEC_ID microsoftCVSDCodecId
    {
        0xff, // Vendor-specific
        0x6,  // Microsoft
        0x2,  // CVSD
    };

    // For readability purpose only
    constexpr auto SamplingFrequency_None = BTH_LE_AUDIO_BIDIRECTIONAL_MULTICHANNEL_STREAMING_SAMPLING_FREQUENCY_NONE;
    constexpr auto SamplingFrequency_16000Hz = BTH_LE_AUDIO_BIDIRECTIONAL_MULTICHANNEL_STREAMING_SAMPLING_FREQUENCY_16000HZ;
    constexpr auto SamplingFrequency_24000Hz = BTH_LE_AUDIO_BIDIRECTIONAL_MULTICHANNEL_STREAMING_SAMPLING_FREQUENCY_24000HZ;
    constexpr auto SamplingFrequency_32000Hz = BTH_LE_AUDIO_BIDIRECTIONAL_MULTICHANNEL_STREAMING_SAMPLING_FREQUENCY_32000HZ;
    constexpr auto SamplingFrequency_48000Hz = BTH_LE_AUDIO_BIDIRECTIONAL_MULTICHANNEL_STREAMING_SAMPLING_FREQUENCY_48000HZ;
    constexpr auto SamplingFrequency_All = BTH_LE_AUDIO_BIDIRECTIONAL_MULTICHANNEL_STREAMING_SAMPLING_FREQUENCY_ALL;

    // Bidirectional multichannel streaming capabilities
    BTH_LE_AUDIO_BIDIRECTIONAL_MULTICHANNEL_STREAMING_CAPABILITY capabilities[]
    {
        // List of formats supported for 2-channel render with 1-channel capture using
        // the LC3 codec:
        //
        //      Render           Capture
        //   (Freq, #Chan)    (Freq, #Chan)
        //   =============    =============
        //    (16kHz, 2) <---> (16kHz, 1)
        //    ----------       ----------
        //    (24kHz, 2) <---> (16kHz, 1)
        //    (24kHz, 2) <---> (24kHz, 1)
        //    ----------       ----------
        //    (32kHz, 2) <---> (16kHz, 1)
        //    (32kHz, 2) <---> (24kHz, 1)
        //    (32kHz, 2) <---> (32kHz, 1)
        //    ----------       ----------
        //    (48kHz, 2) <---> (16kHz, 1)
        //    (48kHz, 2) <---> (24kHz, 1)
        //    (48kHz, 2) <---> (32kHz, 1)
        //    (48kHz, 2) <---> (48kHz, 1)
        //
        {
            // CodecId
            microsoftLC3CodecId,
            // IsCodecPresent,
            FALSE, // The LC3 codec is in the Bluetooth Controller.
            // RenderChannelCount
            2,
            // CaptureChannelCount
            1,
            // RenderSamplingFrequencies
            SamplingFrequency_All,
            // CaptureSamplingFrequencies: List of 1-channel capture sampling
            // frequencies compatible with 16kHz, 2-channel render
            SamplingFrequency_16000Hz,
            // CaptureSamplingFrequencies: List of 1-channel capture sampling
            // frequencies compatible with 24kHz, 2-channel render
            SamplingFrequency_16000Hz | SamplingFrequency_24000Hz,
            // CaptureSamplingFrequencies: List of 1-channel capture sampling
            // frequencies compatible with 32kHz, 2-channel render
            SamplingFrequency_16000Hz |
                SamplingFrequency_24000Hz |
                SamplingFrequency_32000Hz,
            // CaptureSamplingFrequencies: List of 1-channel capture sampling
            // frequencies compatible with 48kHz, 2-channel render
            SamplingFrequency_All,
            // CaptureSamplingFrequencies: RFU
            SamplingFrequency_None,
            // CaptureSamplingFrequencies: RFU
            SamplingFrequency_None,
            // CaptureSamplingFrequencies: RFU
            SamplingFrequency_None,
            // CaptureSamplingFrequencies: RFU
            SamplingFrequency_None,
        },
        // List of formats supported for 4-channel render with 2-channel capture using
        // the CVSD codec:
        //
        //      Render           Capture
        //   (Freq, #Chan)    (Freq, #Chan)
        //   =============    =============
        //    (16kHz, 4) <---> (16kHz, 2)
        //    ----------       ----------
        //    (32kHz, 4) <---> (16kHz, 2)
        //    (32kHz, 4) <---> (32kHz, 2)
        //
        {
            // CodecId
            microsoftCVSDCodecId,
            // IsCodecPresent,
            TRUE, // The CVSD codec is in the audio DSP.
            // RenderChannelCount
            4,
            // CaptureChannelCount
            2,
            // RenderSamplingFrequencies
            SamplingFrequency_16000Hz | SamplingFrequency_32000Hz,
            // CaptureSamplingFrequencies: List of 2-channel capture sampling
            // frequencies compatible with 16kHz, 4-channel render
            SamplingFrequency_16000Hz,
            // CaptureSamplingFrequencies: List of 2-channel capture sampling
            // frequencies compatible with 24kHz, 4-channel render
            SamplingFrequency_None, // N/A
            // CaptureSamplingFrequencies: List of 2-channel capture sampling
            // frequencies compatible with 32kHz, 4-channel render
            SamplingFrequency_16000Hz | SamplingFrequency_32000Hz,
            // CaptureSamplingFrequencies: List of 2-channel capture sampling
            // frequencies compatible with 48kHz, 4-channel render
            SamplingFrequency_None, // N/A
            // CaptureSamplingFrequencies: RFU
            SamplingFrequency_None,
            // CaptureSamplingFrequencies: RFU
            SamplingFrequency_None,
            // CaptureSamplingFrequencies: RFU
            SamplingFrequency_None,
            // CaptureSamplingFrequencies: RFU
            SamplingFrequency_None,
        }
    };

    // Call IoSetDeviceInterfacePropertyData to associate the capabilities associated
    // with the DEVPKEY.
    WDFSTRING wdfSymbolicLinkName;
    RETURN_NTSTATUS_IF_FAILED(WdfStringCreate(
        nullptr, WDF_NO_OBJECT_ATTRIBUTES, &wdfSymbolicLinkName));
    auto deleteWdfStringOnExt = scope_exit([wdfSymbolicLinkName]() -> void
    {
        WdfObjectDelete(wdfSymbolicLinkName);
    });

    RETURN_NTSTATUS_IF_FAILED(WdfDeviceRetrieveDeviceInterfaceString(
        Device,
        &GUID_BLUETOOTH_LEAUDIO_SUPPORT_INTERFACE,
        &bluetoothLEAudioSupportInterface,
        wdfSymbolicLinkName));
    
    UNICODE_STRING symbolicLinkName;
    WdfStringGetUnicodeString(wdfSymbolicLinkName, &symbolicLinkName);

    RETURN_NTSTATUS_IF_FAILED(IoSetDeviceInterfacePropertyData(
        &symbolicLinkName,
        &DEVPKEY_BluetoothLEAudioBidirectionalMultichannelStreamingCapabilities,
        LOCALE_NEUTRAL,
        PLUGPLAY_PROPERTY_PERSISTENT,
        DEVPROP_TYPE_BINARY,
        sizeof(capabilities), capabilities));
#pragma endregion

    return STATUS_SUCCESS;
}
```

## Related articles

- [ACX audio class extensions](../audio/acx-audio-class-extensions-overview.md)
- [Bluetooth Basic Audio Profile specification](https://www.bluetooth.com/specifications/specs/basic-audio-profile-1-0-1/)
- [Bluetooth Core 5.3 specification](https://www.bluetooth.com/specifications/specs/core-specification-5-3/)
- [Bluetooth Published Audio Capabilities Service Specification](https://www.bluetooth.com/specifications/specs/published-audio-capabilities-service/)
- [Bluetooth Audio Stream Control Service Specification](https://www.bluetooth.com/specifications/specs/audio-stream-control-service/)
- [Bluetooth Assigned Numbers](https://www.bluetooth.com/specifications/assigned-numbers/)
- [Bluetooth HFP bypass guidelines for audio drivers](../audio/bluetooth-bypass-guidelines-for-audio-drivers.md)
- [Bluetooth HFP bypass audio streaming](../audio/bluetooth-hfp-bypass-audio-streaming.md)
