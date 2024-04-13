---
title: Default Data-Intersection Handlers
description: Default Data-Intersection Handlers
keywords:
- data-intersection handlers WDK audio , default
- default data-intersection handlers
- minimal data-intersection handlers WDK audio
ms.date: 04/20/2017
---

# Default Data-Intersection Handlers


## <span id="default_data_intersection_handlers"></span><span id="DEFAULT_DATA_INTERSECTION_HANDLERS"></span>


An adapter's proprietary data-intersection handler (the miniport driver object's [**IMiniport::DataRangeIntersection**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiport-datarangeintersection) method) can decline to perform the data-intersection check by returning the STATUS\_NOT\_IMPLEMENTED status code. In this case, the port driver's default data-intersection handler performs the check on behalf of the adapter.

You can implement a minimal data-intersection handler for your adapter driver as a **DataRangeIntersection** method that declines all data-intersection requests by returning STATUS\_NOT\_IMPLEMENTED.

The current implementation of the port driver's default handler is limited in the types of data ranges that it can handle:

-   Only PCM data formats

-   Only mono and stereo audio streams

An adapter driver that supports non-PCM or multichannel formats should implement a proprietary data-intersection handler instead of relying on the port driver to handle data intersections for these formats.

In addition, the default handler supports only audio formats that can be specified by a [**KSDATAFORMAT\_DSOUND**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksdataformat_dsound) or [**KSDATAFORMAT\_WAVEFORMATEX**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksdataformat_waveformatex) structure. It does not support any format containing a [**WAVEFORMATEXTENSIBLE**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-waveformatextensible) structure, which is needed, for example, to specify the channel mask for a format with more than two channels.

When choosing a common format from the intersection between two data ranges, the port driver's default handler always selects the highest value in each parameter's region of intersection:

-   If the intersection spans more than one valid sample frequency (11, 22, and 44 kHz, for example), the default handler picks the highest frequency.

-   If the intersection spans more than one valid bits-per-sample value (8, 16, and 32 bits, for example), the default handler picks the largest value.

-   If the intersection spans both mono and stereo formats, the default handler picks stereo.

If the default handler selects a format that is unsatisfactory, the adapter driver has the option of rejecting the format by failing the **NewStream** call (for example, see [**IMiniportWavePci::NewStream**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportwavepci-newstream)) when SysAudio attempts to create a sink pin with the format. If the call fails, SysAudio will not continue looking for data intersections. Instead, it will attempt to create a connection by iterating through a list of the PCM formats that are supported by system filters such as KMixer until it finds one that the adapter's sink pin can support as well. The list is ordered with higher quality formats first. As before, the adapter rejects unsatisfactory formats in the list by failing the **NewStream** calls for those formats.

 

