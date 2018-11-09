---
title: Data-Intersection Handlers
description: Data-Intersection Handlers
ms.assetid: 7206afdb-8a34-4b5a-8cea-87119f426161
keywords:
- WDM audio drivers WDK , data-intersection handlers
- audio drivers WDK , data-intersection handlers
- data-intersection handlers WDK audio
- handlers WDK audio
- virtual audio devices WDK
- audio filters WDK audio , data-intersection handlers
- filters WDK audio , data-intersection handlers
- formats WDK audio , data-intersection handlers
- pins WDK audio , data-intersection handlers
- graphs WDK audio
- range intersections WDK audio
- data ranges WDK audio , intersections
- audio data formats WDK
- audio data ranges WDK
- port drivers WDK audio , data-intersection handlers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Data-Intersection Handlers


## <span id="data_intersection_handlers"></span><span id="DATA_INTERSECTION_HANDLERS"></span>


This section discusses data-intersection handlers in Microsoft Windows Driver Model (WDM) audio drivers. For a broader discussion of data-intersection handling for KS filters in general, see [DataRange Intersections in AVStream](https://msdn.microsoft.com/library/windows/hardware/ff558680).

In older versions of Windows such as Windows XP, the [SysAudio system driver](kernel-mode-wdm-audio-components.md#sysaudio_system_driver) constructs a [virtual audio device](virtual-audio-devices.md) by connecting together pairs of audio-filter pins to form an [audio filter graph](audio-filter-graphs.md). Before a source pin on one filter can be connected to a sink pin of another, SysAudio must negotiate a common format that the two pins can use to exchange data. The details of this negotiation are largely delegated to the data-intersection handlers that are implemented in the individual filters.

Similarly, in Windows Vista and later, the audio engine must negotiate a common stream format with the data-intersection handler in the wave filter that represents the audio rendering device.

An adapter driver creates a WaveRT filter for an audio device by binding one of its miniport drivers to the corresponding port driver from Portcls.sys. The port driver contains a default data-intersection handler, but the default handler always gives the miniport driver's proprietary data-intersection handler the first opportunity to determine a common format. If the proprietary handler declines this opportunity, however, the port driver's default handler determines the format.

The port driver's default data-intersection handler is designed to deal with the most common hardware features. For simple audio devices, the default handler provides a convenient alternative to implementing a proprietary handler in the adapter driver. However, adapters with more advanced features might need proprietary handlers in order to expose the full capabilities of the hardware.

The remainder of this section describes some of the limitations of the port driver's default data-intersection handler and presents the techniques that are needed to design a proprietary data-intersection handler for an adapter driver. The following topics are discussed:

[Data Intersection](data-intersection.md)

[Default Data-Intersection Handlers](default-data-intersection-handlers.md)

[Proprietary Data-Intersection Handlers](proprietary-data-intersection-handlers.md)

[Hardware Constraints on Sample Frequency](hardware-constraints-on-sample-frequency.md)

[Output Buffer Size](output-buffer-size.md)

[Data Ranges with Discrete Values](data-ranges-with-discrete-values.md)

[Wild Cards](wild-cards.md)

[Data-Range Properties](data-range-properties.md)



 

 




