---
title: AVStream Samples
description: AVStream samples
ms.assetid: 18ddd9f1-d8bb-49a7-91bf-a8aeaa9565ad
keywords:
- AVStream WDK , samples
- sample minidrivers WDK AVStream
ms.date: 06/16/2020
ms.localizationpriority: medium
---

# AVStream samples

Source code for sample AVStream minidrivers are provided in the Windows Driver Kit (WDK) samples on GitHub:

| Sample | Description |
|--|--|
| [AVStream Filter-Centric Simulated Capture Driver (Avssamp)](/samples/microsoft/windows-driver-samples/avstream-filter-centric-simulated-capture-sample-driver-avssamp/) | A pin-centric capture driver for a simulated piece of hardware that shows how to implement DMA through AVStream. |
| [AVStream Simulated Hardware Sample Driver (AVSHwS)](/samples/microsoft/windows-driver-samples/avstream-simulated-hardware-sample-driver-avshws/) | A filter-centric capture driver that does not perform direct memory access (DMA). |

These samples demonstrate many of the concepts that are described in this documentation, and the samples can be tailored to a driver developer's needs.