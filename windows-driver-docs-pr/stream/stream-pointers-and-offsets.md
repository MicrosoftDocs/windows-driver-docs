---
title: Stream Pointers and Offsets
description: Stream Pointers and Offsets
keywords:
- stream pointers WDK AVStream , offsets
- offsets WDK AVStream
- stream positions WDK AVStream
- input positions WDK AVStream
- output positions WDK AVStream
- AVStream pointers WDK
- AVStream offsets WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Stream Pointers and Offsets





A [**KSSTREAM\_POINTER**](/windows-hardware/drivers/ddi/ks/ns-ks-_ksstream_pointer) structure contains two [**KSSTREAM\_POINTER\_OFFSET**](/windows-hardware/drivers/ddi/ks/ns-ks-_ksstream_pointer_offset) structures that index input and output positions within a frame. A minidriver can either manipulate these offsets or access the data at frame resolution.

To advance a stream pointer within a frame, the minidriver calls [**KsStreamPointerAdvanceOffsets**](/windows-hardware/drivers/ddi/ks/nf-ks-ksstreampointeradvanceoffsets) and [**KsStreamPointerAdvanceOffsetsAndUnlock**](/windows-hardware/drivers/ddi/ks/nf-ks-ksstreampointeradvanceoffsetsandunlock).

Minidrivers that access stream data with virtual addresses can use these offsets to specify a stream position at byte resolution. Minidrivers that use scatter/gather physical mappings can specify stream position at the granularity of a [**KSMAPPING**](/windows-hardware/drivers/ddi/ks/ns-ks-_ksmapping) structure.

 

