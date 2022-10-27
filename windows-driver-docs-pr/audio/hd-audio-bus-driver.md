---
title: HD audio bus driver
description: HD audio bus driver
keywords:
- HD audio, Universal Audio Architecture
- High Definition Audio (HD audio), Universal Audio Architecture
- UAA WDK
- Universal Audio Architecture WDK
- bus drivers WDK audio
- HD audio, bus driver
- High Definition Audio (HD audio), bus driver
ms.date: 10/27/2022
---

# HD audio bus driver

The HD audio bus driver is the only software component that directly accesses the hardware registers of the HD audio bus interface controller. The bus driver exposes the HD audio DDI that its children--instances of the function drivers that control the audio and modem codecs--can use to program the HD audio controller hardware. In addition, the bus driver manages the HD audio link hardware resources, which include the DMA engines and bus bandwidth. Function drivers allocate and free these resources through the HD audio DDI.

The HD audio bus driver:

- Queries the codecs on the bus and creates children to manage the codecs.

- Handles interrupt service routines (ISRs) for unsolicited responses and propagates the unsolicited responses to its children.

- Passes commands from its children to the codecs and retrieves responses from the codecs.

- Sets up the DMA engines that transfer data to or from the cyclic buffers.

- Manages bus bandwidth resources on the HD audio link.

- Provides access to the wall clock register and link position registers.

- Provides synchronized starting and stopping of groups of streams.

The HD audio bus driver does not provide:

- An interface for programming a DSP or additional registers that are not defined in the Intel High Definition Audio Specification.

- Prioritized bandwidth management.

During device enumeration, the HD audio bus driver detects the codecs that are attached to the HD audio controller's HD audio link. For each codec, the bus driver loads one function driver (if available) for each function group that it finds within the codec. For information about function groups, see the Intel High Definition Audio Specification at the [Intel HD audio](https://www.intel.com/content/www/us/en/standards/high-definition-audio-specification.html) website.
