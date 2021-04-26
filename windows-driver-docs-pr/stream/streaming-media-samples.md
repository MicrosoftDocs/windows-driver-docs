---
title: Streaming Media Samples
description: Streaming media samples
keywords:
- streaming media samples WDK
- samples WDK streaming media
ms.date: 06/19/2020
ms.localizationpriority: medium
---

# Streaming media samples

You can browse and download individual Windows 10 driver samples on the [Microsoft Samples portal](/samples/browse/?products=windows-wdk). You can also clone, fork, or download the [Windows-driver-samples](https://github.com/Microsoft/Windows-driver-samples) repo on GitHub.

Earlier versions of Windows driver samples are archived here:

- [Windows 8.1 driver samples](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/master/Official%20Windows%20Driver%20Kit%20Sample/Windows%20Driver%20Kit%20(WDK)%208.1%20Samples)

- [Windows 8 driver samples](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/master/Official%20Windows%20Driver%20Kit%20Sample/Windows%20Driver%20Kit%20(WDK)%208.0%20Samples)

For Windows 7, samples were included with [Windows Driver Kit (WDK) 7 download](https://www.microsoft.com/download/details.aspx?id=11800).

| Sample name | Build environment | Target operating system | PnP driver | In-box driver | Sample description |
|--|--|--|--|--|--|
| AVStream Filter-Centric Simulated Capture Driver (Avssamp) | Windows 8.1<br><br>Windows 8<br><br>Windows 7 | Windows 8.1<br><br>Windows 8<br><br>Windows 7 | No | No | Provides a filter-centric AVStream capture driver with functional audio. The driver performs captures at 320 x 240 resolution in RGB24 or YUV422 format while playing a user-provided pulse code modulation (PCM) wave audio file in a loop. The sample demonstrates how to write a filter-centric AVStream minidriver. |
| AVStream Simulated Hardware Sample Driver (Avshws) |Windows 8.1<br><br>Windows 8<br><br>Windows 7 | Windows 8.1<br><br>Windows 8<br><br>Windows 7| No | No | Provides a pin-centric AVStream capture driver for a simulated piece of hardware. The driver performs captures at 320 x 240 in either an RGB24 or YUV422 format through direct DMA into capture buffers.<br><br>The purpose of the sample is to demonstrate how to write a pin-centric AVStream minidriver. The sample also shows how to implement DMA by using the related functionality that AVStream provides.<br><br>This sample features enhanced parameter validation and overflow detection. |
| SonyDCam 1394 Webcam Driver | Windows 7 | Windows 7 | No | Yes | A Microsoft Windows Driver Model (WDM) Stream class video capture driver that supports 1394-based digital cameras that conform to the Digital Camera Specification from the 1394 Trade Association. |
| USBIntel Webcam Driver | Windows 7 | Windows 7 | No | Yes | A Microsoft Windows Driver Model (WDM) stream class video capture driver. |
| SW Tuner | Windows 7 | Windows 7 | No | No | Demonstrates several digital network types. |
