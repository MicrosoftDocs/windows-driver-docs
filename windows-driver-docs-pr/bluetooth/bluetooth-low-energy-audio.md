---
title: Bluetooth Low Energy (LE) audio
description: This article provides an overview of Bluetooth LE audio introduced in Windows 11.
ms.date: 01/18/2023
---

# Bluetooth Low Energy (LE) audio

This article provides an overview of Bluetooth LE audio introduced in Windows 11.

## Introduction

Bluetooth LE audio enables streaming unicast or broadcast audio to Bluetooth LE devices over an isochronous transport. As of version 5.3 of the Bluetooth core specification, there is no standard defined host controller interface (HCI) for host platforms to send and receive isochronous data to and from the Bluetooth controller. This document defines the Windows Bluetooth vendor specific audio path (VSAP) to allow platforms to use vendor-specific solutions to enable Bluetooth LE audio streaming. The VSAP software interface leverages Windows audio class extensions (ACX) and additional interface properties defined in this document.

### Terminology and prerequisites

In addition to the terms defined in this table, this document also references terms defined by Windows audio class extensions.

| Term | Definition |
|---|---|
| LE audio | Short for Bluetooth LE audio |
| Classic audio | Bluetooth audio streaming that uses the hands-free profile (HFP) and advanced audio distribution profile (A2DP) |
| Audio Device | A single remote Bluetooth LE audio device or set of Bluetooth LE audio devices that together compose a single audio endpoint from the perspective of Windows. |
| BAP | Acronym for the [Basic Audio Profile](https://www.bluetooth.org/DocMan/handlers/DownloadDoc.ashx?doc_id=522996) defined by the Bluetooth SIG. |
| ASCS | The [Audio Stream Control Service](https://www.bluetooth.com/specifications/specs/audio-stream-control-service/) defines a standard way for Bluetooth LE audio devices to configure and establish unicast audio streams. |
| PACS | The [Published Audio Capabilities Service](https://www.bluetooth.com/specifications/specs/published-audio-capabilities-service/) defines a standard way for Bluetooth LE audio devices to report its supported audio codec capabilities. |
| CIS | The Connected Isochronous Streams transport is used to send and receive unicast audio data between Bluetooth LE devices. |
| BIS | The Broadcast Isochronous Stream transport is used for connectionless audio data transfers. |
| ACX | Short for audio class extensions, which is the driver model required by all audio drivers to support for Bluetooth LE audio on Windows. |
| Streaming circuits | One or more ACXCIRCUIT objects created by the Vendor Specific Audio Driver Stack for its streaming path. |
| Profile circuit | An ACXCIRCUIT object created by the Bluetooth LE audio profile implementation on Windows. This ACXCIRCUIT serves as the head circuit as defined in the ACX specification and is not a streaming circuit. |

This document assumes familiarity with the terms defined above and the following HCI commands defined in the [Bluetooth Core 5.3 specification](https://www.bluetooth.org/DocMan/handlers/DownloadDoc.ashx?doc_id=521059):

- HCI_Read_Local_Supported_Codecs (v2)
- HCI_Read_Local_Supported_Codec_Capabilities
- HCI_LE_Set_CIG_Parameters
- HCI_LE_Create_CIS
- HCI_Configure_Data_Path
- HCI_LE_Setup_ISO_Data_Path
- HCI_LE_Remove_ISO_Data_Path
- HCI_LE_Remove_CIG

Bluetooth LE audio VSAP requires the audio drivers to use the ACX framework. Adopting ACX for Bluetooth LE audio provides several advantages, such as:

- Supports the preferred audio driver model for Windows going forward.
- Leverages ACX's native support for multi stack audio solutions without requiring a dedicated DDI between drivers.
- Does not require IHV audio drivers to relay requests from the audio system to the Bluetooth stack. Instead, ACX can send requests directly to the Bluetooth stack via the profile circuit.

## Architecture

### Definitions

The following components are involved in the different VSAP architecture variants.

#### Windows ACX framework

This component enables support for a multi-stack audio endpoint. For Bluetooth LE audio, the software components that compose an audio endpoint are the vendor specific audio driver stack and the Windows Bluetooth LE audio profile.

#### Vendor specific audio driver stack

This vendor specific component is responsible for sending and receiving Bluetooth LE audio data to and from a Bluetooth controller via a vendor defined audio interface. It shall consist of at a minimum an ACX streaming driver to manage the incoming and outgoing audio data. Additional ACX drivers may be included if they are necessary parts of the multi circuit ACX audio endpoint. This component is also referred to as the IHV ACX Streaming Driver in this document. 

#### Windows Bluetooth LE audio profile

This component contains the implementation of the Basic Audio Profile, Volume Control Profile, and Microphone Control Profile. It is responsible for creating the head ACXCIRCUIT for each Bluetooth LE Audio device or set of devices paired to Windows, reporting audio formats reported by the remote device and Bluetooth controller, and manages the state of isochronous channels and groups.

#### Windows Bluetooth core stack

This component provides an interface to allow the Windows Bluetooth LE Audio Profile to do query supported codec capabilities from the local Bluetooth controller and manage the state of isochronous channels and groups.

#### LC3 codec

This sub-component is responsible for translating between compressed LC3 audio and PCM audio. It shall support both encoding and decoding capabilities and may be implemented either in software as part of the Vendor Specific Audio Driver stack, or in hardware as part of the audio DSP or Bluetooth Controller. The diagram mentions LC3 by name since it is the standard codec supported by the Bluetooth SIG. However, future codecs and vendor specific codecs supported by Windows may also be incorporated into the architecture in a similar manner.

### Architecture Variants

The Bluetooth LE Audio VSAP architecture supports different variants for streaming.

1. Sideband Bluetooth LE audio streaming without audio offload
1. Sideband Bluetooth LE audio streaming with audio offload
1. Vendor specific inband Bluetooth LE audio streaming

In the following diagrams, the shaded components are provided by the IHV and the non-shaded components are provided by the OS.

#### Sideband Bluetooth LE audio architecture without audio offload

A sideband architecture uses a vendor specific audio interface to allow the audio driver stack to send and receive audio data to the Bluetooth controller. This data path is separate from the HCI data path used for other Bluetooth data, such as signaling messages between the unicast client and remote unicast server. The following diagram models a sideband architecture where the LC3 codec is hosted in the Bluetooth controller. It is also valid to have the LC3 codec hosted as part of the Vendor Specific Audio Driver Stack for software encoding and decoding. In that case, the audio being sent to the Bluetooth controller would be formatted as LC3 audio frames instead of PCM audio.

The following diagram shows a sideband Bluetooth LE audio architecture with an LC3 codec in the Bluetooth controller.

:::image type="content" source="images/bluetooth-le-audio-architecture-with-lc3-codec-in-bluetooth-controller.png" alt-text="Diagram of sideband Bluetooth LE audio architecture with LC3 codec in the Bluetooth controller.":::

The following diagram shows a sideband Bluetooth LE audio architecture with an LC3 codec in the audio driver stack.

:::image type="content" source="images/bluetooth-le-audio-architecture-with-lc3-codec-in-audio-driver-stack.png" alt-text="Diagram of sideband Bluetooth LE audio architecture with LC3 codec in the audio driver stack.":::

#### Sideband Bluetooth LE audio architecture with audio offload

A sideband architecture with audio offload includes an audio DSP hardware component to provide a Bluetooth LE audio streaming solution with power saving benefits. The following diagrams demonstrate a possible architecture with the LC3 codec in the Bluetooth controller and the codec in the audio DSP.

The following diagram shows a sideband Bluetooth LE audio with audio offload architecture with an LC3 codec in the Bluetooth controller.

:::image type="content" source="images/bluetooth-le-audio-with-audio-offload-architecture-with-lc3-codec-in-bluetooth-controller.png" alt-text="Diagram of sideband Bluetooth LE audio with audio offload architecture with LC3 codec in the Bluetooth controller.":::

The following diagram shows a sideband Bluetooth LE audio with audio offload architecture with an LC3 codec in the audio DSP.

:::image type="content" source="images/bluetooth-le-audio-with-audio-offload-architecture-with-lc3-codec-in-audio-dsp.png" alt-text="Diagram of sideband Bluetooth LE audio with audio offload architecture with LC3 codec in the audio DSP.":::

#### Vendor specific inband Bluetooth LE audio architecture

The VSAP inband architecture enables a custom pipeline to send and receive Bluetooth LE audio data from the vendor specific audio driver stack to the Bluetooth controller's HCI. This architecture includes a new component, the "IHV ISO Merging Component." This component is responsible for managing the flow control for the ISO data. It also shall share HCI command flow control with the Windows Bluetooth Core Stack if it needs to send any HCI commands.

The following diagram shows a vendor specific inband Bluetooth LE audio architecture.

:::image type="content" source="images/bluetooth-le-audio-vendor-specific-inband-architecture.png" alt-text="Diagram of a vendor specific inband Bluetooth LE audio architecture.":::

## Detailed design

### Audio format requirements

#### Audio frame durations

The Bluetooth LE audio profiles allow implementations to support audio streaming with audio frame durations of either 7.5 or 10 milliseconds. Windows requires the codecs provided by IHVs to support both frame durations for the formats previously defined to ensure interoperability with Bluetooth LE audio accessory devices and quality coexistence with other Bluetooth LE devices connected to the system.

#### Signal processing mode definitions

Bluetooth LE audio supports a wide range of streaming formats to support different user scenarios. The BAP and TMAP specifications define mandatory supported formats for certification. Windows leverages [audio signal processing modes](../audio/audio-signal-processing-modes.md) to correlate the format to use with the scenario being performed by the system. Audio drivers that support Bluetooth LE audio shall indicate support for the signal processing modes and formats in the following table. Furthermore, Bluetooth LE audio does not support the raw signal processing mode, so audio drivers shall not advertise any supported formats for this mode.

##### Render stream audio signal processing modes

Bluetooth LE Audio requires render audio formats to be declared for the following signal processing modes:

- Default (AUDIO_SIGNALPROCESSINGMODE_DEFAULT)
  - This mode is used for unidirectional render scenarios, such as music playback, notifications, and video game audio.
- Communications (AUDIO_SIGNALPROCESSINGMODE_COMMUNICATIONS)
  - This mode is used for bidirectional scenarios, such as voice calls.

The complete list of formats for each signal processing mode is below.

<table>
  <tr>
    <td width=126 rowspan=2 valign=top style='width:94.25pt;border:solid black 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
    <b>Signal Processing Mode</b>
    </td>
    <td width=146 rowspan=2 valign=top style='width:109.8pt;border:solid black 1.0pt;
  border-left:none;padding:0in 5.4pt 0in 5.4pt'>
      <b>Use Cases</b>
    </td>
    <td width=447 colspan=6 valign=top style='width:335.45pt;border:solid black 1.0pt;
  border-left:none;padding:0in 5.4pt 0in 5.4pt'>
      <b>Audio formats ordered from most preferred to
  least preferred</b>
    </td>
  </tr>
  <tr>
  <td width=80 valign=top style='width:59.95pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <b><i>Sampling Frequency</i></b>
  </td>
  <td width=66 valign=top style='width:49.4pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;padding:0in 5.4pt 0in 5.4pt'>
  <b><i>Channel Count</i></b>
  </td>
  <td width=52 valign=top style='width:39.2pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;padding:0in 5.4pt 0in 5.4pt'>
  <b><i>Bit Depth</i></b>
  </td>
  <td width=71 valign=top style='width:52.9pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;padding:0in 5.4pt 0in 5.4pt'>
  <b><i>Frame Duration</i></b>
  </td>
  <td width=63 valign=top style='width:47.4pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;padding:0in 5.4pt 0in 5.4pt'>
  <p><b><i>Audio Data Rate</i></b></p>
  </td>
  <td width=115 valign=top style='width:86.6pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p><b><i>BAP Codec Configuration ID (Table 3.11 of the BAP
  Specification)</i></b></p>
  </td>
 </tr>
 <tr>
  <td width=126 rowspan=6 valign=top style='width:94.25pt;border:solid black 1.0pt;
  border-top:none;padding:0in 5.4pt 0in 5.4pt'>
  <p>Default</p>
  </td>
  <td width=146 rowspan=6 valign=top style='width:109.8pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p>Voice recorder, VOIP calls, or video game audio
  with voice chat.</p>
  </td>
  <td width=80 valign=top style='width:59.95pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p>32 kHz</p>
  </td>
  <td width=66 valign=top style='width:49.4pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;padding:0in 5.4pt 0in 5.4pt'>
  <p>1</p>
  </td>
  <td width=52 valign=top style='width:39.2pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;padding:0in 5.4pt 0in 5.4pt'>
  <p>16</p>
  </td>
  <td width=71 valign=top style='width:52.9pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;padding:0in 5.4pt 0in 5.4pt'>
  <p>7.5ms</p>
  </td>
  <td width=63 valign=top style='width:47.4pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;padding:0in 5.4pt 0in 5.4pt'>
  <p>64 kbps</p>
  </td>
  <td width=115 valign=top style='width:86.6pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p>32_1</p>
  </td>
 </tr>
 <tr>
  <td width=80 valign=top style='width:59.95pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p>32 kHz</p>
  </td>
  <td width=66 valign=top style='width:49.4pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;padding:0in 5.4pt 0in 5.4pt'>
  <p>1</p>
  </td>
  <td width=52 valign=top style='width:39.2pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;padding:0in 5.4pt 0in 5.4pt'>
  <p>16</p>
  </td>
  <td width=71 valign=top style='width:52.9pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;padding:0in 5.4pt 0in 5.4pt'>
  <p>10ms</p>
  </td>
  <td width=63 valign=top style='width:47.4pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;padding:0in 5.4pt 0in 5.4pt'>
  <p>64 kbps</p>
  </td>
  <td width=115 valign=top style='width:86.6pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p>32_2</p>
  </td>
 </tr>
 <tr>
  <td width=80 valign=top style='width:59.95pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p>24 kHz</p>
  </td>
  <td width=66 valign=top style='width:49.4pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;padding:0in 5.4pt 0in 5.4pt'>
  <p>1</p>
  </td>
  <td width=52 valign=top style='width:39.2pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;padding:0in 5.4pt 0in 5.4pt'>
  <p>16</p>
  </td>
  <td width=71 valign=top style='width:52.9pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;padding:0in 5.4pt 0in 5.4pt'>
  <p>7.5ms</p>
  </td>
  <td width=63 valign=top style='width:47.4pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;padding:0in 5.4pt 0in 5.4pt'>
  <p>48 kbps</p>
  </td>
  <td width=115 valign=top style='width:86.6pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p>24_1</p>
  </td>
 </tr>
 <tr>
  <td width=80 valign=top style='width:59.95pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p>24 kHz</p>
  </td>
  <td width=66 valign=top style='width:49.4pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;padding:0in 5.4pt 0in 5.4pt'>
  <p>1</p>
  </td>
  <td width=52 valign=top style='width:39.2pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;padding:0in 5.4pt 0in 5.4pt'>
  <p>16</p>
  </td>
  <td width=71 valign=top style='width:52.9pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;padding:0in 5.4pt 0in 5.4pt'>
  <p>10ms</p>
  </td>
  <td width=63 valign=top style='width:47.4pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;padding:0in 5.4pt 0in 5.4pt'>
  <p>48 kbps</p>
  </td>
  <td width=115 valign=top style='width:86.6pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p>24_2</p>
  </td>
 </tr>
 <tr>
  <td width=80 valign=top style='width:59.95pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p>16 kHz</p>
  </td>
  <td width=66 valign=top style='width:49.4pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;padding:0in 5.4pt 0in 5.4pt'>
  <p>1</p>
  </td>
  <td width=52 valign=top style='width:39.2pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;padding:0in 5.4pt 0in 5.4pt'>
  <p>16</p>
  </td>
  <td width=71 valign=top style='width:52.9pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;padding:0in 5.4pt 0in 5.4pt'>
  <p>7.5ms</p>
  </td>
  <td width=63 valign=top style='width:47.4pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;padding:0in 5.4pt 0in 5.4pt'>
  <p>32 kbps</p>
  </td>
  <td width=115 valign=top style='width:86.6pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p>16_1</p>
  </td>
 </tr>
 <tr>
  <td width=80 valign=top style='width:59.95pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p>16 kHz</p>
  </td>
  <td width=66 valign=top style='width:49.4pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;padding:0in 5.4pt 0in 5.4pt'>
  <p>1</p>
  </td>
  <td width=52 valign=top style='width:39.2pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;padding:0in 5.4pt 0in 5.4pt'>
  <p>16</p>
  </td>
  <td width=71 valign=top style='width:52.9pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;padding:0in 5.4pt 0in 5.4pt'>
  <p>10ms</p>
  </td>
  <td width=63 valign=top style='width:47.4pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;padding:0in 5.4pt 0in 5.4pt'>
  <p>32 kbps</p>
  </td>
  <td width=115 valign=top style='width:86.6pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p>16_2</p>
  </td>
 </tr>
</table>
