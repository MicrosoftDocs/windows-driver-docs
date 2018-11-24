---
title: Glitch Reporting for Offloaded Audio
description: This topic explains the mechanism that an audio driver must use when it has to report glitching errors in connection with hardware-offloaded audio streams.
ms.assetid: 9FF2A5D6-9382-4EE6-AA21-DCF47210F73B
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Glitch Reporting for Offloaded Audio


This topic explains the mechanism that an audio driver must use when it has to report glitching errors in connection with hardware-offloaded audio streams.

When an audio driver detects glitching errors, it must raise an Event Tracing for Windows (ETW) event to report the errors. This event should include the reason for the glitch, along with information about the DMA buffer in use for the audio streams.

The following enum shows the events that have been defined for the audio driver to use for glitch error reporting.

```ManagedCPlusPlus
typedef enum 
{
    eMINIPORT_IHV_DEFINED = 0, 
    eMINIPORT_BUFFER_COMPLETE,
    eMINIPORT_PIN_STATE,
    eMINIPORT_GET_STREAM_POS,
    eMINIPORT_SET_WAVERT_BUFFER_WRITE_POS,
    eMINIPORT_GET_PRESENTATION_POS,
    eMINIPORT_PROGRAM_DMA,
    eMINIPORT_GLITCH_REPORT
} EPcMiniportEngineEvent;
```

For more information about this enum, see [**EPcMiniportEngineEvent**](https://msdn.microsoft.com/library/windows/hardware/dn302036).

And for more information about how to develop a driver that can handle hardware-offloaded audio streams, see [Driver Implementation Details](driver-implementation-details.md).

 

 




