---
title: Default Data-Intersection Handlers
description: Default Data-Intersection Handlers
ms.assetid: 5c70a6e4-702f-4fd0-bb3e-2cde2955b2ad
keywords:
- data-intersection handlers WDK audio , default
- default data-intersection handlers
- minimal data-intersection handlers WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Default Data-Intersection Handlers


## <span id="default_data_intersection_handlers"></span><span id="DEFAULT_DATA_INTERSECTION_HANDLERS"></span>


An adapter's proprietary data-intersection handler (the miniport driver object's [**IMiniport::DataRangeIntersection**](https://msdn.microsoft.com/library/windows/hardware/ff536764) method) can decline to perform the data-intersection check by returning the STATUS\_NOT\_IMPLEMENTED status code. In this case, the port driver's default data-intersection handler performs the check on behalf of the adapter.

You can implement a minimal data-intersection handler for your adapter driver as a **DataRangeIntersection** method that declines all data-intersection requests by returning STATUS\_NOT\_IMPLEMENTED.

The current implementation of the port driver's default handler is limited in the types of data ranges that it can handle:

-   Only PCM data formats

-   Only mono and stereo audio streams

An adapter driver that supports non-PCM or multichannel formats should implement a proprietary data-intersection handler instead of relying on the port driver to handle data intersections for these formats.

In addition, the default handler supports only audio formats that can be specified by a [**KSDATAFORMAT\_DSOUND**](https://msdn.microsoft.com/library/windows/hardware/ff537094) or [**KSDATAFORMAT\_WAVEFORMATEX**](https://msdn.microsoft.com/library/windows/hardware/ff537095) structure. It does not support any format containing a [**WAVEFORMATEXTENSIBLE**](https://msdn.microsoft.com/library/windows/hardware/ff538802) structure, which is needed, for example, to specify the channel mask for a format with more than two channels.

When choosing a common format from the intersection between two data ranges, the port driver's default handler always selects the highest value in each parameter's region of intersection:

-   If the intersection spans more than one valid sample frequency (11, 22, and 44 kHz, for example), the default handler picks the highest frequency.

-   If the intersection spans more than one valid bits-per-sample value (8, 16, and 32 bits, for example), the default handler picks the largest value.

-   If the intersection spans both mono and stereo formats, the default handler picks stereo.

If the default handler selects a format that is unsatisfactory, the adapter driver has the option of rejecting the format by failing the **NewStream** call (for example, see [**IMiniportWavePci::NewStream**](https://msdn.microsoft.com/library/windows/hardware/ff536735)) when SysAudio attempts to create a sink pin with the format. If the call fails, SysAudio will not continue looking for data intersections. Instead, it will attempt to create a connection by iterating through a list of the PCM formats that are supported by system filters such as KMixer until it finds one that the adapter's sink pin can support as well. The list is ordered with higher quality formats first. As before, the adapter rejects unsatisfactory formats in the list by failing the **NewStream** calls for those formats.

 

 




