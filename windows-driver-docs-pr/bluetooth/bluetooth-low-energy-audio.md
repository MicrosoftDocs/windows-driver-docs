---
title: Bluetooth Low Energy (LE) Audio
description: This article provides an overview of Bluetooth LE Audio introduced in Windows 11 version 22H2 (KB5026446).
ms.date: 07/11/2023
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
| TMAP | The [Telephony and Media Audio Profile](https://www.bluetooth.com/specifications/tmap-1-0/) specifies interoperable configurations of the lower-level audio services and profiles. |
| ASCS | The [Audio Stream Control Service](https://www.bluetooth.com/specifications/specs/audio-stream-control-service/) defines a standard way for Bluetooth LE Audio devices to configure and establish unicast audio streams. |
| PACS | The [Published Audio Capabilities Service](https://www.bluetooth.com/specifications/specs/published-audio-capabilities-service-1-0-1/) defines a standard way for Bluetooth LE Audio devices to report its supported audio codec capabilities. |
| CIS | The Connected Isochronous Streams transport is used to send and receive unicast audio data between Bluetooth LE devices. |
| BIS | The Broadcast Isochronous Stream transport is used for connectionless audio data transfers. |
| ACX | Short for audio class extensions, which is the driver model required by all audio drivers to support for Bluetooth LE Audio on Windows. |
| Streaming circuits | One or more **ACXCIRCUIT** objects created by the Vendor Specific Audio Driver Stack for its streaming path. |
| Profile circuit | An **ACXCIRCUIT** object created by the Bluetooth LE Audio profile implementation on Windows. This **ACXCIRCUIT** serves as the head circuit as defined in the ACX specification and isn't a streaming circuit. |

This document assumes familiarity with the previously defined terms and the following HCI commands defined in the [Bluetooth Core 5.3 specification](https://www.bluetooth.org/DocMan/handlers/DownloadDoc.ashx?doc_id=521059):

- HCI_Read_Local_Supported_Codecs (v2)
- HCI_Read_Local_Supported_Codec_Capabilities
- HCI_LE_Set_CIG_Parameters
- HCI_LE_Create_CIS
- HCI_Configure_Data_Path
- HCI_LE_Setup_ISO_Data_Path
- HCI_LE_Remove_ISO_Data_Path
- HCI_LE_Remove_CIG

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

This vendor specific component is responsible for sending and receiving Bluetooth LE Audio data to and from a Bluetooth controller via a vendor defined audio interface. It shall consist of at a minimum an ACX streaming driver to manage the incoming and outgoing audio data. More ACX drivers may be included if they're necessary parts of the multi circuit ACX audio endpoint. This component is also referred to as the IHV ACX Streaming Driver in this document.

#### Windows Bluetooth LE Audio profile

This component contains the implementation of the Basic Audio Profile (BAP), Volume Control Profile, and Microphone Control Profile. It's responsible for creating the head **[ACXCIRCUIT](/windows-hardware/drivers/audio/acx-summary-of-objects#acx-circuit)** for each Bluetooth LE Audio device or set of devices paired to Windows, reporting audio formats reported by the remote device and Bluetooth controller, and manages the state of isochronous channels and groups.

#### Windows Bluetooth core stack

This component provides an interface to allow the Windows Bluetooth LE Audio Profile to query supported codec capabilities from the local Bluetooth controller and manage the state of isochronous channels and groups.

#### LC3 codec

This subcomponent is responsible for translating between compressed LC3 audio and PCM audio. It shall support both encoding and decoding capabilities and may be implemented either in software as part of the vendor specific audio driver (VSAP) stack, or in hardware as part of the audio DSP or Bluetooth Controller. The diagram mentions LC3 by name since it's the standard codec supported by the Bluetooth SIG. However, future codecs and vendor specific codecs supported by Windows may also be incorporated into the architecture in a similar manner.

### Architecture Variants

The Bluetooth LE Audio VSAP architecture supports different variants for streaming.

1. Sideband Bluetooth LE Audio streaming without audio offload
1. Sideband Bluetooth LE Audio streaming with audio offload
1. Vendor specific inband Bluetooth LE Audio streaming

In the following diagrams, the shaded components are provided by the IHV and the nonshaded components are provided by the OS.

#### Sideband Bluetooth LE Audio architecture without audio offload

A sideband architecture uses a vendor specific audio interface to allow the audio driver stack to send and receive audio data to the Bluetooth controller. This data path is separate from the HCI data path used for other Bluetooth data, such as signaling messages between the unicast client and remote unicast server. The following diagram models a sideband architecture where the LC3 codec is hosted in the Bluetooth controller. It's also valid to have the LC3 codec hosted as part of the Vendor Specific Audio Driver Stack for software encoding and decoding. In that case, the audio being sent to the Bluetooth controller would be formatted as LC3 audio frames instead of PCM audio.

The following diagram shows a sideband Bluetooth LE Audio architecture with an LC3 codec in the Bluetooth controller.

:::image type="content" source="images/bluetooth-le-audio-architecture-with-lc3-codec-in-bluetooth-controller.png" alt-text="Diagram of sideband Bluetooth LE Audio architecture with LC3 codec in the Bluetooth controller.":::

The following diagram shows a sideband Bluetooth LE Audio architecture with an LC3 codec in the audio driver stack.

:::image type="content" source="images/bluetooth-le-audio-architecture-with-lc3-codec-in-audio-driver-stack.png" alt-text="Diagram of sideband Bluetooth LE Audio architecture with LC3 codec in the audio driver stack.":::

#### Sideband Bluetooth LE Audio architecture with audio offload

A sideband architecture with audio offload includes an audio DSP hardware component to provide a Bluetooth LE Audio streaming solution with power saving benefits. The following diagrams demonstrate a possible architecture with the LC3 codec in the Bluetooth controller and the codec in the audio DSP.

The following diagram shows a sideband Bluetooth LE Audio with audio offload architecture with an LC3 codec in the Bluetooth controller.

:::image type="content" source="images/bluetooth-le-audio-with-audio-offload-architecture-with-lc3-codec-in-bluetooth-controller.png" alt-text="Diagram of sideband Bluetooth LE Audio with audio offload architecture with LC3 codec in the Bluetooth controller.":::

The following diagram shows a sideband Bluetooth LE Audio with audio offload architecture with an LC3 codec in the audio DSP.

:::image type="content" source="images/bluetooth-le-audio-with-audio-offload-architecture-with-lc3-codec-in-audio-dsp.png" alt-text="Diagram of sideband Bluetooth LE Audio with audio offload architecture with LC3 codec in the audio DSP.":::

#### Vendor specific inband Bluetooth LE Audio architecture

The VSAP inband architecture enables a custom pipeline to send and receive Bluetooth LE Audio data from the vendor specific audio driver stack to the Bluetooth controller's HCI. This architecture includes a new component, the "IHV ISO Merging Component." This component is responsible for managing the flow control for the ISO data. It also shall share HCI command flow control with the Windows Bluetooth Core Stack if it needs to send any HCI commands.

The following diagram shows a vendor specific inband Bluetooth LE Audio architecture.

:::image type="content" source="images/bluetooth-le-audio-vendor-specific-inband-architecture.png" alt-text="Diagram of a vendor specific inband Bluetooth LE Audio architecture.":::

## Detailed design

### Audio format requirements

#### Audio frame durations

The Bluetooth LE Audio profiles allow implementations to support audio streaming with audio frame durations of either 7.5 milliseconds or 10 milliseconds. Windows requires the codecs provided by IHVs to support both frame durations to ensure interoperability with Bluetooth LE Audio accessory devices and quality coexistence with other Bluetooth LE devices connected to the system.

#### Signal processing mode definitions

Bluetooth LE Audio supports a wide range of streaming formats to support different user scenarios. The BAP and TMAP specifications define mandatory supported formats for certification. Windows applies [audio signal processing modes](../audio/audio-signal-processing-modes.md) to correlate the format to use with the scenario being performed by the system. Audio drivers that support Bluetooth LE Audio shall indicate support for the signal processing modes and formats in the following table. Furthermore, Bluetooth LE Audio doesn't support the raw signal processing mode, so audio drivers shall not advertise any supported formats for this mode.

##### Render stream audio signal processing modes

Bluetooth LE Audio requires render audio formats to be declared for the following signal processing modes:

- Default (AUDIO_SIGNALPROCESSINGMODE_DEFAULT)
  - This mode is used for unidirectional render scenarios, such as music playback, notifications, and video game audio.
- Communications (AUDIO_SIGNALPROCESSINGMODE_COMMUNICATIONS)
  - This mode is used for bidirectional scenarios, such as voice calls.

The following tables are lists of formats for each use case and signal processing mode. Audio formats are ordered from most preferred to least preferred.

###### System sounds, music playback, and video game audio when connected to a stereo device or coordinated set of devices

Signal processing mode: **Default**

| Sampling Frequency | Channel Count | Bit Depth | Frame Duration | Audio Data Rate | BAP Codec Configuration ID (Table 3.11 of the BAP Specification) |
|---|---|---|---|---|---|
| 48 kHz | 2 | 16 | 7.5 ms | 96 kbps | 48_3 |
| 48 kHz | 2 | 16 | 7.5 ms | 80 kbps | 48_1 |
| 48 kHz | 2 | 16 | 10 ms | 96 kbps | 48_4 |
| 48 kHz | 2 | 16 | 10 ms | 80 kbps | 48_2 |
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

##### Capture stream audio signal processing modes

Bluetooth LE Audio requires capture audio formats to be declared for the Default (AUDIO_SIGNALPROCESSINGMODE_DEFAULT) signal processing mode. The list of supported capture formats is in the following table.

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

#### Defined stream configurations and topologies

##### Render-only configurations

###### Basic audio profile configuration 1

The following audio configuration is defined in table 4.1 of the [Bluetooth BAP specification](https://www.bluetooth.com/specifications/specs/basic-audio-profile-1-0-1/)

:::image type="content" source="images/bap-configuration-1.png" alt-text="Diagram of basic audio profile configuration 1.":::

The PC is connected to a single audio device that supports mono streams. The single device may be a standalone device or a single connected member of a coordinated set.

| Use Case Examples | Windows Audio Settings | Bluetooth Controller Settings |
|---|---|---|
| Media playback | **Render**:<br>Signal Processing Mode: Default<br>Channel Count: 1<br>**Capture**: None | CIS Count: 1<br>CIG Count: 1<br>BAP QoS Settings: High reliability |
| Voice call with no microphone on audio device | **Render**:<br>Signal Processing Mode: Communications<br>Channel Count: 1<br>**Capture**: None | CIS Count: 1<br>CIG Count: 1<br>BAP QoS Settings: Low latency |
| Video game playback | **Render**:<br>Signal Processing Mode: Default<br>Channel Count: 1<br>**Capture**: None | CIS Count: 1<br>CIG Count: 1<br>BAP QoS Settings: Low latency |

###### Basic audio profile configuration 4

The following audio configuration is defined in table 4.1 of the [Bluetooth BAP specification](https://www.bluetooth.com/specifications/specs/basic-audio-profile-1-0-1/)

:::image type="content" source="images/bap-configuration-4.png" alt-text="Diagram of basic audio profile configuration 4.":::

The PC is connected to a single audio device that supports stereo streams. The audio device is capable of processing two audio channels on a single CIS.

| Use Case Examples | Windows Audio Settings | Bluetooth Controller Settings |
|---|---|---|
| Media playback | **Render**: Signal Processing Mode: Default<br>Channel Count: 2<br>**Capture**: None | CIS Count: 1<br>CIG Count: 1<br>BAP QoS Settings: High reliability Audio Channel Allocation: Front left and front right |
| Video game playback | Signal Processing Mode: Default<br>Channel Count: 2<br>**Capture**: None | CIS Count: 1<br>CIG Count: 1<br>BAP QoS Settings: Low latency<br>Audio Channel Allocation: Front left and front right |

###### Basic audio profile configuration 6(i)

The following audio configuration is defined in table 4.1 of the [Bluetooth BAP specification](https://www.bluetooth.com/specifications/specs/basic-audio-profile-1-0-1/)

:::image type="content" source="images/bap-configuration-6-i.png" alt-text="Diagram of basic audio profile configuration 6 I.":::

The PC is connected to a single audio device that supports stereo streams. The audio device is only capable of processing one audio channel on each of the two CISs

| Use Case Examples | Windows Audio Settings | Bluetooth Controller Settings |
|---|---|---|
| Media playback | Signal Processing Mode: Default<br>Channel Count: 2<br>**Capture**: None | CIS Count: 2<br>CIG Count: 1<br>BAP QoS Settings: High reliability |
| Voice call with no microphone on audio device | Signal Processing Mode: Communications<br>Channel Count: 1<br>**Capture**: None | CIS Count: 2<br>CIG Count: 1<br>BAP QoS Settings: Low latency<br>Audio Channel Allocation: Either front left or front right |
| Video game playback | Signal Processing Mode: Default<br>Channel Count: 2<br>**Capture**: None | CIS Count: 2<br>CIG Count: 1<br>BAP QoS Settings: Low latency<br>Audio Channel Allocation: Front left and front right |

###### Basic audio profile configuration 6(ii)

The following audio configuration is defined in table 4.1 of the [Bluetooth BAP specification](https://www.bluetooth.com/specifications/specs/basic-audio-profile-1-0-1/)

:::image type="content" source="images/bap-configuration-6-ii.png" alt-text="Diagram of basic audio profile configuration 6 II.":::

The PC is connected to a coordinated set of audio devices. The set is capable of processing two channels of audio with each member processing a single channel.

| Use Case Examples | Windows Audio Settings | Bluetooth Controller Settings |
|---|---|---|
| Media playback | Signal Processing Mode: Default<br>Channel Count: 2<br>**Capture**: None | CIS Count: 2<br>CIG Count: 1<br>BAP QoS Settings: High reliability |
| Voice call with no microphone on either device | Signal Processing Mode: Communications<br>Channel Count: 1<br>**Capture**: None | CIS Count: 2<br>CIG Count: 1<br>BAP QoS Settings: Low latency |
| Video game playback | Signal Processing Mode: Default<br>Channel Count: 2<br>**Capture**: None | CIS Count: 2<br>CIG Count: 1<br>BAP QoS Settings: Low latency |

##### Bidirectional configurations

Bidirectional configurations are used when the Bluetooth LE Audio profile detects that an application intends to create both a capture and render stream to a remote device or set of devices. Since applications control capture and render streams separately, IHV audio drivers and Bluetooth controllers shall allow audio to flow over a single direction of a bidirectional CIS after it's provisioned using the HCI commands Configure Data Path and LE Setup ISO Data Path.

###### Basic audio profile configuration 3

The following audio configuration is defined in table 4.1 of the [Bluetooth BAP specification](https://www.bluetooth.com/specifications/specs/basic-audio-profile-1-0-1/)

:::image type="content" source="images/bap-configuration-3.png" alt-text="Diagram of basic audio profile configuration 3.":::

The PC is connected to a single audio device with a bidirectional mono stream established on a single CIS.

| Use Case | Windows Audio Settings | Bluetooth Controller Settings |
|---|---|---|
| Voice call | **Render:**<br>Signal Processing Mode: Communications<br>Channel Count: 1<br>**Capture:**<br>Signal Processing Mode: Default<br>Channel Count: 1 | CIS Count: 1<br>CIG Count: 1<br>BAP QoS Settings: Low Latency |
| Video game playback with voice chat | **Render:**<br>Signal Processing Mode: Communications<br>Channel Count: 1<br>**Capture:**<br>Signal Processing Mode: Default<br>Channel Count: 1 | CIS Count: 1<br>CIG Count: 1<br>BAP QoS Settings: Low Latency |

###### Basic audio profile configuration 8(i)

The following audio configuration is defined in table 4.1 of the [Bluetooth BAP specification](https://www.bluetooth.com/specifications/specs/basic-audio-profile-1-0-1/)

:::image type="content" source="images/bap-configuration-8-i.png" alt-text="Diagram of basic audio profile configuration 8 I.":::

The PC is connected to a single audio device that supports stereo render streams and mono capture streams. The device is capable of processing one channel of audio on a single CIS for a given direction.

| Use Case | Windows Audio Settings | Bluetooth Controller Settings |
|---|---|---|
| Voice call | **Render:**<br>Signal Processing Mode: Communications<br>Channel Count: 1<br>**Capture:**<br>Signal Processing Mode: Default<br>Channel Count: 1 | CIS Count: 2<br>CIG Count: 1<br>BAP QoS Settings: Low Latency |
| Video game playback with voice chat | **Render:**<br>Signal Processing Mode: Communications<br>Channel Count: 2<br>**Capture:**<br>Signal Processing Mode: Default<br>Channel Count: 1 | CIS Count: 2<br>CIG Count: 1<br>BAP QoS Settings: Low Latency |

###### Basic audio profile configuration 8(ii)

The following audio configuration is defined in table 4.1 of the [Bluetooth BAP specification](https://www.bluetooth.com/specifications/specs/basic-audio-profile-1-0-1/)

:::image type="content" source="images/bap-configuration-8-ii.png" alt-text="Diagram of basic audio profile configuration 8 II.":::

The PC is connected to a coordinated set of audio devices. Each set member is receiving one channel of render audio. A single set member has an established capture stream. The set member with the capture stream is the first set member that connects to the PC that also supports capture streams.

| Use Case | Windows Audio Settings | Bluetooth Controller Settings |
|---|---|---|
| Voice call | **Render:**<br>Signal Processing Mode: Communications<br>Channel Count: 1<br>**Capture:**<br>Signal Processing Mode: Default<br>Channel Count: 1 | CIS Count: 2<br>CIG Count: 1<br>BAP QoS Settings: Low Latency |
| Video game playback with voice chat | **Render:**<br>Signal Processing Mode: Communications<br>Channel Count: 2<br>**Capture:**<br>Signal Processing Mode: Default<br>Channel Count: 1 | CIS Count: 2<br>CIG Count: 1<br>BAP QoS Settings: Low Latency |

##### Capture-only configurations

###### Basic audio profile configuration 2

The following audio configuration is defined in table 4.1 of the [Bluetooth BAP specification](https://www.bluetooth.com/specifications/specs/basic-audio-profile-1-0-1/)

:::image type="content" source="images/bap-configuration-2.png" alt-text="Diagram of basic audio profile configuration 2.":::

The PC is connected to a single audio device that supports mono capture streams.

| Use Case | Windows Audio Settings | Bluetooth Controller Settings |
|---|---|---|
| Voice call with no speaker on device | Render: None<br>Capture:<br>Signal Processing Mode: Default<br>Channel Count: 1 | CIS Count: 1<br>CIG Count: 1<br>BAP QoS Settings: Low Latency |

###### Basic audio profile configuration 9(i)

The following audio configuration is defined in table 4.1 of the [Bluetooth BAP specification](https://www.bluetooth.com/specifications/specs/basic-audio-profile-1-0-1/)

:::image type="content" source="images/bap-configuration-9-i.png" alt-text="Diagram of basic audio profile configuration 9 I.":::

The PC is connected to a single audio device that supports sending stereo audio data. The device is capable of encoding one channel of audio on a single CIS.

| Use Case | Windows Audio Settings | Bluetooth Controller Settings |
|---|---|---|
| Multi channel microphone capture | Render: None<br>Capture:<br>Signal Processing Mode: Default<br>Channel Count: 1<br> | CIS Count: 2<br>CIG Count: 1<br>BAP QoS Settings: Low Latency |

###### Basic audio profile configuration 9(ii)

The PC is connected to a single audio device that supports mono capture streams.

The following audio configuration is defined in table 4.1 of the [Bluetooth BAP specification](https://www.bluetooth.com/specifications/specs/basic-audio-profile-1-0-1/)

:::image type="content" source="images/bap-configuration-9-ii.png" alt-text="Diagram of basic audio profile configuration 9 II.":::

The PC is connected to a set of audio devices. Each set member sends one channel of audio to the PC.

| Use Case | Windows Audio Settings | Bluetooth Controller Settings |
|---|---|---|
| Multi channel microphone capture | Render: None<br>Capture:<br>Signal Processing Mode: Default<br>Channel Count: 1 | CIS Count: 2<br>CIG Count: 1<br>BAP QoS Settings: Low Latency |

If the remote device or device set supports bidirectional audio, then the configurations for a capture only stream are the same as bidirectional configurations. This allows transitions from capture only scenarios to bidirectional scenarios without needing to re-create the streams.

### Data structures

#### Microsoft defined Bluetooth LE Audio interface properties

##### Stream creation properties

The following properties are shared between the vendor specific audio driver stack and the Bluetooth LE Audio Profile via the [ACXOBJECTBAG](/windows-hardware/drivers/audio/acx-summary-of-objects#acx-object-bag) [DDIs](/windows-hardware/drivers/ddi/acxmisc/) to inform decisions on stream endpoint creation and configuration, as shown in the [Stream Creation](#stream-creation) scenario.

###### BluetoothLEAudio_CodecCapabilities

This property is set by the audio driver to indicate support for audio streaming capabilities that are supported in the audio driver or audio DSP. The property value is set using the DDI **[AcxObjectBagAddBlob](/windows-hardware/drivers/ddi/acxmisc/nf-acxmisc-acxobjectbagaddblob)** and the format of the value is the same as a PAC record as defined in the [PACS specification](https://www.bluetooth.com/specifications/specs/published-audio-capabilities-service-1-0-1/).

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

This property is set by the audio driver to indicate the data path ID used as the parameter for the commands HCI_LE_Setup_ISO_Data_Path and HCI_Configure_Data_Path. The property value is set using the **[AcxObjectBagAddUI8](/windows-hardware/drivers/ddi/acxmisc/nf-acxmisc-acxobjectbagaddui8)** DDI.

The Bluetooth LE Audio profile reads and uses this property is as a parameter in HCI_Configure_Data_Path and HCI_LE_Setup_ISO_Data_Path commands. This ID is applied for all isochronous streams created for the **ACXSTREAM** associated with the object bag.

| Field | Octet |
|---|---|
| Data path ID | 0 |

If the property isn't set by the audio driver, then the OS uses the value 1 as the parameter for the HCI commands.

###### Bluetooth_DatapathConfiguration

This property is set by the audio driver to provide vendor specific configurations to the Bluetooth controller via the HCI_Configure_Data_Path command. It shall not be larger than 255 bytes, which is the largest payload that a Bluetooth controller accepts for an HCI command. The property value is set using the **[AcxObjectBagAddBlob](/windows-hardware/drivers/ddi/acxmisc/nf-acxmisc-acxobjectbagaddblob)** DDI. This configuration is applied for everything data path ID set by the audio driver.

###### BluetoothLEAudio_CodecConfiguration

This property shall be set by the Bluetooth LE Audio profile using the DDI **[AcxObjectBagAddBlob](/windows-hardware/drivers/ddi/acxmisc/nf-acxmisc-acxobjectbagaddblob)** after the codec configuration is configured with an audio device. The structure of the value is:

| Field | Octet |
|---|---|
| Configuration Count | 0 |
| Coding Format[i] | 3 |
| Company ID[i] | 1-2 |
| Vendor Specific Codec ID[i] | 3-4 |
| Codec Specific Configuration Length[i] | 5 |
| Codec Specific Configuration[i] | 6... n |

Field values are defined in table 4.3 of the [Bluetooth Audio Stream Control Service Specification](https://www.bluetooth.org/DocMan/handlers/DownloadDoc.ashx?doc_id=522995).

The vendor specific audio driver stack should read this property if the LC3 codec is in the ACX streaming driver or audio DSP.

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

### Sequences

#### Audio driver initialization

When the IHV ACX Streaming driver loads and determines that it supports Bluetooth LE Audio streaming, it shall show support for the technology by creating an **ACXFACTORYCIRCUIT** object and registering for Bluetooth template bindings with ACX using the IDs defined in [Audio Endpoint Template Binding IDs](#audio-endpoint-template-binding-ids).

:::image type="content" source="images/btle-audio-driver-init-seq.png" alt-text="Diagram of the Bluetooth LE Audio driver initialization sequence.":::

#### Endpoint creation

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

:::image type="content" source="images/btle-audio-endpoint-creation.png" alt-text="Diagram of the Bluetooth LE Audio endpoint creation.":::

#### Stream creation

1. When an application requests to create an audio stream, ACX invokes the registered **EvtCircuitCreateStream** callbacks for each circuit, beginning with the IHV ACX streaming driver.
1. When its **EvtCircuitCreateStream** callback is invoked, the IHV ACX streaming driver:
   1. Sets or updates the Bluetooth_DatapathId and Bluetooth_DataPathConfiguration properties on the [ACXOBJECTBAG](/windows-hardware/drivers/audio/acx-summary-of-objects#acx-object-bag) attached to the [ACXSTREAMBRIDGE](/windows-hardware/drivers/audio/acx-summary-of-objects#acx-stream-bridge).
   1. Creates an [ACXSTREAM](/windows-hardware/drivers/audio/acx-summary-of-objects#acx-stream) with callbacks set for stream state transitions and RT stream processing
   1. Creates an audio-engine element on the stream if the audio pipeline supports offload streaming.
   1. Adds the **ACXSTREAM** to its stream bridge. This invokes the Bluetooth LE Audio profile's **EvtCircuitCreateStream** callback.
1. When its **[EvtAcxCircuitCreateStream](/windows-hardware/drivers/ddi/acxcircuit/nc-acxcircuit-evt_acx_circuit_create_stream)** callback is invoked, the Bluetooth LE Audio profile:
   1. Saves the properties locally from the **ACXOBJECTBAG** set by the IHV ACX streaming driver for future stream transition callbacks.
   1. If the audio endpoint is for unicast streaming the Bluetooth LE Audio profile:
      1. Performs the Config Codec Operation as defined in the BAP specification. The parameters for the operation are derived from the **ACXDATAFORMAT** specified in the **EvtAcxCircuitCreateStream** callback and either the other stream parameters in the **ACXOBJECTBAG** or the codec capabilities supported by the Bluetooth Controller.
      1. Sets the *BluetoothLEAudio_CodecConfiguration* property on the **ACXOBJECTBAG** with the value used to configure the remote audio devices.
1. If the IHV ACX streaming driver needs to update its data path ID or data path configuration based on the object bag values set by the profile, then it may invoke the KSPROPERTY set operations to update the value stored by the profile circuit.
    1. Creates an **ACXSTREAM** with callbacks set for stream state transitions.

:::image type="content" source="images/btle-audio-stream-creation.png" alt-text="Diagram of the Bluetooth LE Audio stream creation.":::

#### Stream state transitions

ACX decides the circuit order of stream state transitions based on the audio flow and whether the state is transitioning to a more active or less active state.

- For Render streams going from a less-active state to a more-active state, the profile circuit receives the event first, followed by the streaming circuit.
- For Render streams going from a more-active state to a less-active state, the streaming circuit receives the event first, followed by the profile circuit.  
- For Capture streams going from a less-active state to a more-active state, the streaming circuit receives the event first, followed by the profile circuit.  
- For Capture streams going from a more-active state to a less-active state, the profile circuit with receive the event first, followed by the streaming circuit.

#### Prepare stream

When its **[EvtAcxStreamPrepareHardware](/windows-hardware/drivers/ddi/acxstreams/nc-acxstreams-evt_acx_stream_prepare_hardware)** callback is invoked, the Bluetooth LE Audio profile:

1. Allocates resources for a unicast stream by:
   1. Configuring a CIG with the HCI_LE_Set_CIG_Parameters command.
   1. Sending the ASCS config QoS operation to synchronize settings with the remote device.

:::image type="content" source="images/btle-audio-stream-preparation-profile-circuit.png" alt-text="Diagram of the Bluetooth LE Audio stream preparation of a profile circuit.":::

When its **EvtAcxStreamPrepareHardware** callback is invoked, the IHV ACX streaming driver allocates the necessary streaming resources and initializes the audio pipeline to be in the acquired state.

:::image type="content" source="images/btle-audio-stream-preparation-streaming-circuit.png" alt-text="Diagram of the Bluetooth LE Audio stream preparation of a streaming circuit":::

#### Start stream

When its **[EvtAcxStreamRun](/windows-hardware/drivers/ddi/acxstreams/nc-acxstreams-evt_acx_stream_run)** callback is invoked, the Bluetooth LE Audio profile:

1. Applies any data path configuration settings set by the ACX streaming driver in the stream creation procedure using the HCI_Configure_Data_Path command.
1. Begins the stream start procedure by:
   1. Performing the BAP unicast stream Enable procedure for a unicast stream:
      1. Sending the Enable operation to the remote endpoints.
      1. Creating CISes if they aren't already created using the HCI_LE_Create_CIS command.
1. If the data path isn't already configured, the Bluetooth LE Audio profile:
   1. Establishes the ISO data paths using the HCI_LE_Setup_ISO_Data_Path command
      1. If the IHV ACX streaming driver sets the *BluetoothLEAudio_CodecCapabilities* property, the value of the Codec_ID field in HCI_LE_Setup_ISO_Data_Path shall be set to transparent (0x3) as defined in the Bluetooth Assigned Numbers. Otherwise, the value shall be the same as the Codec ID used in the config codec operation in the stream creation procedure.
1. If the audio stream is a unicast capture stream, the Bluetooth LE Audio profile performs the BAP receiver start ready operation.

:::image type="content" source="images/btle-audio-stream-start-profile-circuit.png" alt-text="Diagram of the Bluetooth LE Audio stream starting of a profile circuit.":::

When its **EvtAcxStreamRun** callback is invoked, the IHV ACX streaming driver starts processing incoming audio data from either the Windows audio system (render) or the Bluetooth controller (capture).

:::image type="content" source="images/btle-audio-stream-start-streaming-circuit.png" alt-text="Diagram of the Bluetooth LE Audio stream starting of a streaming circuit.":::

#### Pause stream

When its **[EvtAcxStreamPause](/windows-hardware/drivers/ddi/acxstreams/nc-acxstreams-evt_acx_stream_pause)** callback is invoked, the Bluetooth LE Audio profile:

1. Performs the BAP unicast stream disable procedure.
1. Removes the ISO data path using the HCI_LE_Remove_ISO_Data_Path command.
1. Performs the ASCS receiver stop ready procedure if the audio stream is a unicast capture stream.

:::image type="content" source="images/btle-audio-stream-pause-profile-circuit.png" alt-text="Diagram of the Bluetooth LE Audio stream pausing of a profile circuit.":::

When its **EvtAcxStreamPause** callback is invoked, the IHV ACX streaming driver pauses its audio processing pipeline.

:::image type="content" source="images/btle-audio-stream-pause-streaming-circuit.png" alt-text="Diagram of the Bluetooth LE Audio stream pausing of a streaming circuit.":::

#### Release stream

When its **[EvtAcxStreamReleaseHardware](/windows-hardware/drivers/ddi/acxstreams/nc-acxstreams-evt_acx_stream_release_hardware)** callback is invoked, the Bluetooth LE Audio Profile performs the BAP unicast stream release procedure by:

1. Sending the ASCS Release operation to the remote Bluetooth LE Audio device
1. Disconnecting the CIS if it isn't used by another active stream.
1. Removing the CIG if all CISes are disconnected.

:::image type="content" source="images/btle-audio-stream-release-profile-circuit.png" alt-text="Diagram of the Bluetooth LE Audio stream releasing of a profile circuit.":::

When its **EvtAcxStreamReleaseHardware** callback is invoked, the IHV ACX streaming driver releases its audio pipeline resources.

:::image type="content" source="images/btle-audio-stream-release-streaming-circuit.png" alt-text="Diagram of the Bluetooth LE Audio stream releasing of a streaming circuit.":::

#### Endpoint disconnection

The Windows Bluetooth LE Audio profile updates an endpoint's connection state if the remote unicast device doesn't have an LE-ACL connection to the PC or is reporting through its PACS available audio contexts that it isn't available for streaming. When the endpoint is disconnected, the Windows audio service invalidates any active streams to the endpoint. This results in the stream pause and release sequences to occur.

#### Endpoint removal

A Bluetooth LE Audio endpoint is removed from the system when either the profile circuit or streaming circuit is destroyed. The profile circuit may be removed when the remote unicast device's pairing is removed from Windows or the Bluetooth radio is disabled.

1. When the Windows Bluetooth LE Audio profile removes its circuit, ACX disables its endpoint interfaces to signal to the Windows audio service that the endpoint should be removed.
1. When the interfaces are disabled, the Windows audio service invalidates any active streams to the Bluetooth LE Audio endpoint, this operation results in the stream pause and release callbacks to be invoked on the streaming circuit.
1. To complete endpoint removal, ACX invalidates the IHV ACX streaming driver's circuit, which results in the WDF invoking the circuit's cleanup callback.
1. When its cleanup callback is invoked, the IHV ACX streaming driver releases its circuit.

:::image type="content" source="images/btle-audio-endpoint-removal.png" alt-text="Diagram of the Bluetooth LE Audio endpoint removal.":::

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

### Bluetooth LE and classic audio coexistence

Windows shall ensure that only classic audio or LE audio is active for a paired Bluetooth audio device that supports both technologies. If LE audio is active, then the sideband DDIs for A2DP and HFP for the remote device are disabled and the profile circuit is created for the LE audio endpoint. If classic audio is active, the sideband DDIs for A2DP and HFP for the remote device are enabled and the profile circuit isn't created for the LE audio endpoint.

### Power management

Bluetooth LE Audio doesn't have any power management requirements or flows outside of what is already defined by [WDF](../wdf/pnp-and-power-management-callback-sequences.md).

## Related topics

- [ACX audio class extensions](../audio/acx-audio-class-extensions-overview.md)
- [Bluetooth Basic Audio Profile specification](https://www.bluetooth.com/specifications/specs/basic-audio-profile-1-0-1/)
- [Bluetooth Core Specification](https://www.bluetooth.org/DocMan/handlers/DownloadDoc.ashx?doc_id=521059)
- [Bluetooth Published Audio Capabilities Service Specification](https://www.bluetooth.com/specifications/specs/published-audio-capabilities-service/)
- [Bluetooth Audio Stream Control Service Specification](https://www.bluetooth.com/specifications/specs/audio-stream-control-service/)
- [Bluetooth Assigned Numbers](https://www.bluetooth.com/specifications/assigned-numbers/)
