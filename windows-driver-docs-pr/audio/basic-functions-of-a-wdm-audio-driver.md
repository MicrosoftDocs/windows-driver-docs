---
title: Basic Functions of a WDM Audio Driver
description: Basic Functions of a WDM Audio Driver
keywords:
- WDM audio drivers WDK , about WDM audio drivers
- audio drivers WDK , about audio drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Basic Functions of a WDM Audio Driver


## <span id="basic_functions_of_a_wdm_audio_driver"></span><span id="BASIC_FUNCTIONS_OF_A_WDM_AUDIO_DRIVER"></span>


A Microsoft Windows Driver Model (WDM) audio driver provides the following functionality:

-   The driver exposes all the types of input and output streams, and the number of instances of each stream type that it can support. The driver provides this information in the form of a set of pin factories and the number of pins that each factory can instantiate. For example, a simple audio device might input a single PCM audio stream and output a single PCM audio stream. The filter for this device contains two pin factories--one for the input stream an one for the output stream--and each pin factory supports only a single pin instance. If the adapter card contains only one of these devices, the adapter driver provides a filter factory containing only a single instance of a filter with these capabilities.

-   The driver supports one or more property sets. For example, all audio drivers should support [KSPROPSETID\_Audio](./kspropsetid-audio.md), but some audio drivers might support additional property sets as well. Clients of the driver use property requests both to discover a filter's capabilities and to change the filter's configurable settings.

-   The driver optionally supports a hardware clock. This clock should be readable and writable so that streams can synchronize with other streams on the same or different hardware. For additional information, see [KSPROPSETID\_Clock](../stream/kspropsetid-clock.md).

-   The driver optionally supports other media interfaces, such as [**KSINTERFACE\_STANDARD\_STREAMING**](../stream/ksinterface-standard-streaming.md), [**KSINTERFACE\_MEDIA\_WAVE\_QUEUED**](../stream/ksinterface-media-wave-queued.md), or [**KSINTERFACE\_STANDARD\_LOOPED\_STREAMING**](../stream/ksinterface-standard-looped-streaming.md).

 

