---
title: Data Range Intersections in AVStream
description: Data Range Intersections in AVStream
keywords:
- data intersections WDK AVStream
- intersections WDK AVStream
- data formats WDK AVStream
- data ranges WDK AVStream
- ranges WDK AVStream
- formats WDK AVStream
- pin data ranges WDK
ms.date: 04/20/2017
---

# Data Range Intersections in AVStream





A data format is a single set of parameters describing some aspect of a connection. For example, an audio data format might specify a certain format of audio at X samples per second and Y bits per sample.

A data range specifies a sequence of valid parameters. For instance, an audio data range could specify a certain format of audio at A-B samples per second and C-D bits per sample.

The minidriver provides a list of data ranges that it supports for a specific pin in the **DataRanges** member of the corresponding [**KSPIN\_DESCRIPTOR**](/windows-hardware/drivers/ddi/ks/ns-ks-kspin_descriptor) structure.

In AVStream, minidrivers can supply their own data-range intersection handlers by providing a pointer to a minidriver-provided callback routine in the **IntersectHandler** member of a [**KSPIN\_DESCRIPTOR\_EX**](/windows-hardware/drivers/ddi/ks/ns-ks-_kspin_descriptor_ex). To let AVStream intersect the ranges, set this member to **NULL**. See [*AVStrMiniIntersectHandlerEx*](/windows-hardware/drivers/ddi/ks/nc-ks-pfnksintersecthandlerex) to learn how to define the callback routine.

If a minidriver provides an intersect handler, when an intersection needs to be made, the minidriver receives two data ranges that match in major type, subformat, and specifier. In addition, the required attributes of the data ranges match.

If the ranges intersect and sufficient buffer space is provided in the **Data** parameter of the *AVStrMiniIntersectHandlerEx* callback routine, the intersection routine chooses a format in the intersection and returns it to the caller in the buffer pointed to by **Data**.

If the two data ranges do not intersect, the handler returns STATUS\_NO\_MATCH.

If the minidriver has specified an [*AVStrMiniPinSetDataFormat*](/windows-hardware/drivers/ddi/ks/nc-ks-pfnkspinsetdataformat) dispatch, then AVStream calls this dispatch to inform the minidriver that AVStream is setting a specific format on the pin. Provide a pointer to your *AVStrMiniPinSetDataFormat* callback routine in the **SetDataFormat** member of the [**KSPIN\_DISPATCH**](/windows-hardware/drivers/ddi/ks/ns-ks-_kspin_dispatch) structure. (Minidrivers that are clients of [stream class](/windows-hardware/drivers/ddi/_stream/index) receive [**SRB\_SET\_DATA\_FORMAT**](./srb-set-data-format.md) instead of *AVStrMiniPinSetDataFormat*.)

The minidriver can refuse a proposed format by returning STATUS\_NO\_MATCH from *AVStrMiniPinSetDataFormat*.

In addition to the initial call to [*AVStrMiniPinSetDataFormat*](/windows-hardware/drivers/ddi/ks/nc-ks-pfnkspinsetdataformat) before the pin is created, your minidriver could receive a second *AVStrMiniPinSetDataFormat* call just before the pin transitions to RUN state. If your AVStream or stream class client is a video capture minidriver and you receive such a notification, *this dispatch contains the actual surface parameters*. If possible, the minidriver should not fail this second format change. Do not assume that a second dispatch call will occur.

The minidriver should capture data in whatever format was contained in the last successful *AVStrMiniPinSetDataFormat* dispatch.

 

