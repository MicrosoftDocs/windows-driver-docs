---
title: Glitch Reporting for Offloaded Audio
description: This topic explains the mechanism that an audio driver must use when it has to report glitching errors in connection with hardware-offloaded audio streams.
ms.assetid: 9FF2A5D6-9382-4EE6-AA21-DCF47210F73B
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Glitch%20Reporting%20for%20Offloaded%20Audio%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


