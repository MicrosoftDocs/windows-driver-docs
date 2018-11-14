---
title: Dynamic Format Change
description: Dynamic Format Change
ms.assetid: 41e6ec8c-3a96-4103-a991-3b9ba6acad6c
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Dynamic Format Change


Dynamic format change is a feature in Windows 7 and later versions of the Windows operating system that allows the format used to stream audio data between an audio application and an audio adapter to be changed dynamically. Dynamic format change accommodates the behavior of audio streaming in high definition multimedia interface (HDMI) devices. This topic provides an overview of dynamic format change and describes how it works.

The following list shows the scenarios in which dynamic format change is used.

-   **HDMI devices present new capabilities.** When an HDMI device streams audio or video data or both, the total HDMI bandwidth used for the audio and video transfer is fixed and the video signal is given preference in capacity allocation. This means that if you have an HDMI display device connected to a computer and you change the display resolution, this affects the size of the bandwidth that remains for audio data transfer to the computer.

    Assume, for example, that your HDMI device is initially configured with the data format set to 192 KHz, 16-bit stereo with a particular display mode. When you change to a different display mode, the remaining bandwidth for streaming audio data might not be enough for the 192 KHz format. So the device driver notifies the audio service for the connected computer about the change in display mode, and this causes the audio driver and the audio service to renegotiate the audio data format. If the currently selected 192 KHz format cannot be streamed within the remaining bandwidth, a new format is selected. For more information about the format negotiation process, see [Format Negotiation](format-negotiation.md).

    In another HDMI-related dynamic format change scenario, an audio device is unplugged and a new, HDMI-capable device is plugged in. The device driver for the HDMI device generates a format change event and the audio service renegotiates the audio data format with the device driver.

-   **Some stand-alone audio devices provide hardware controls that a user can use to change the audio data format.** In this scenario, the user manipulates a control knob on a surround sound amplifier, for example, to select an audio data format. If there is a computer connected to the stand-alone audio device, this newly selected data format causes the audio driver on the connected computer to renegotiate the data format and, possibly, change it.

-   **Third-party UI for the Sound applet in the Control Panel provides options for enabling or disabling system effects.** When you develop your own system effects audio processing objects (sAPOs), you can also provide a custom UI for the **Sound** applet in the Control Panel. This custom UI can include modifications to the **Enhanced** or the **Advanced** tabs of the **Sound** applet or both. In this scenario, a user selects a check box in the **Enhanced** tab to enable or disable a global system effects (GFX) feature that requires the audio data format to be changed. The selection made by the user causes the HDMI driver to generate a format change event. The audio service receives the notification about this event and renegotiates with the audio driver to select a new format for the audio data.

To provide support for HDMI and IEC61937-compliant compressed audio formats such as Dolby Digital and digital theater sound (DTS), Windows 7 and later Windows operating systems provide a new set of subtype GUIDs for use by the kernel streaming (KS) properties and structures. The International Electrotechnical Commission (IEC) standard, IEC 61937, applies to digital audio interfaces that transfer non-linear [PCM](pcm-stream-data-format.md) encoded bit streams. For more information about the subtype GUIDs, see the KSDATAFORMAT\_SUBTYPE\_IEC61937\_Xxx GUIDs in Ksmedia.h.

**Note**  
When the audio endpoint builder receives the dynamic format change notification, and the proposed data format is not supported by the device driver, the endpoint builder will then recalculate a new default device data format.

And in the case where a redesigned audio driver now supports a new format, it can force the endpoint builder to select the new format as the default format for the device. To force a changeover to the new format as the default for the device, the audio driver must fail the format support query that it receives regarding the old format. The failed format support query triggers a format change notification, and the endpoint builder then calculates a new default format for the device.

 

 

 




