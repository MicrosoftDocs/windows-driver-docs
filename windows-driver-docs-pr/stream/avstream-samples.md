---
title: AVStream Samples
description: AVStream samples
keywords:
- AVStream WDK , samples
- sample minidrivers WDK AVStream
ms.date: 06/07/2021
ms.localizationpriority: medium
---

# AVStream samples

Source code for sample AVStream minidrivers are provided in the Windows Driver Kit (WDK) samples on GitHub:

| Sample | Description |
|--|--|
| [AVStream Filter-Centric Simulated Capture Driver (Avssamp)](/samples/microsoft/windows-driver-samples/avstream-filter-centric-simulated-capture-sample-driver-avssamp/) | The AVStream filter-centric simulated capture sample driver (Avssamp) provides a filter-centric AVStream capture driver with functional audio. This streaming media driver performs video captures at 320 x 240 pixel resolution in RGB24 or YUV422 format while playing a user-provided Pulse Code Modulation (PCM) wave audio file in a loop. The sample demonstrates how to write a filter-centric AVStream minidriver. |
| [AVStream Simulated Hardware Sample Driver (Avshws)](/samples/microsoft/windows-driver-samples/avstream-simulated-hardware-sample-driver-avshws/) | The AVStream simulated hardware sample driver (Avshws) provides a pin-centric AVStream capture driver for a simulated piece of hardware. This streaming media driver performs video captures at 320 x 240 pixels in either RGB24 or YUV422 format using direct memory access (DMA) into capture buffers. The purpose of the sample is to demonstrate how to write a pin-centric AVStream minidriver. The sample also shows how to implement DMA by using the related functionality provided by the AVStream class driver. This sample features enhanced parameter validation and overflow detection. |

These samples demonstrate many of the concepts that are described in this documentation, and the samples can be tailored to a driver developer's needs.
