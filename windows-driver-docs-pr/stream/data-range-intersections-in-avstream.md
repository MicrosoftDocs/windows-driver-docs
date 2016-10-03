---
title: Data Range Intersections in AVStream
author: windows-driver-content
description: Data Range Intersections in AVStream
MS-HAID:
- 'avsover\_6dc5ac10-3b2e-46b8-9c2f-6db654b9e903.xml'
- 'stream.data\_range\_intersections\_in\_avstream'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 44281574-8258-47a3-857d-fd44bb949f17
keywords: ["data intersections WDK AVStream", "intersections WDK AVStream", "data formats WDK AVStream", "data ranges WDK AVStream", "ranges WDK AVStream", "formats WDK AVStream", "pin data ranges WDK"]
---

# Data Range Intersections in AVStream


## <a href="" id="ddk-data-range-intersections-in-avstream-ksg"></a>


A data format is a single set of parameters describing some aspect of a connection. For example, an audio data format might specify a certain format of audio at X samples per second and Y bits per sample.

A data range specifies a sequence of valid parameters. For instance, an audio data range could specify a certain format of audio at A-B samples per second and C-D bits per sample.

The minidriver provides a list of data ranges that it supports for a specific pin in the **DataRanges** member of the corresponding [**KSPIN\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff563533) structure.

In AVStream, minidrivers can supply their own data-range intersection handlers by providing a pointer to a minidriver-provided callback routine in the **IntersectHandler** member of a [**KSPIN\_DESCRIPTOR\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff563534). To let AVStream intersect the ranges, set this member to **NULL**. See [*AVStrMiniIntersectHandlerEx*](https://msdn.microsoft.com/library/windows/hardware/ff556326) to learn how to define the callback routine.

If a minidriver provides an intersect handler, when an intersection needs to be made, the minidriver receives two data ranges that match in major type, subformat, and specifier. In addition, the required attributes of the data ranges match.

If the ranges intersect and sufficient buffer space is provided in the **Data** parameter of the *AVStrMiniIntersectHandlerEx* callback routine, the intersection routine chooses a format in the intersection and returns it to the caller in the buffer pointed to by **Data**.

If the two data ranges do not intersect, the handler returns STATUS\_NO\_MATCH.

If the minidriver has specified an [*AVStrMiniPinSetDataFormat*](https://msdn.microsoft.com/library/windows/hardware/ff556355) dispatch, then AVStream calls this dispatch to inform the minidriver that AVStream is setting a specific format on the pin. Provide a pointer to your *AVStrMiniPinSetDataFormat* callback routine in the **SetDataFormat** member of the [**KSPIN\_DISPATCH**](https://msdn.microsoft.com/library/windows/hardware/ff563535) structure. (Minidrivers that are clients of [stream class](https://msdn.microsoft.com/library/windows/hardware/ff568275) receive [**SRB\_SET\_DATA\_FORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff568201) instead of *AVStrMiniPinSetDataFormat*.)

The minidriver can refuse a proposed format by returning STATUS\_NO\_MATCH from *AVStrMiniPinSetDataFormat*.

In addition to the initial call to [*AVStrMiniPinSetDataFormat*](https://msdn.microsoft.com/library/windows/hardware/ff556355) before the pin is created, your minidriver could receive a second *AVStrMiniPinSetDataFormat* call just before the pin transitions to RUN state. If your AVStream or stream class client is a video capture minidriver and you receive such a notification, *this dispatch contains the actual surface parameters*. If possible, the minidriver should not fail this second format change. Do not assume that a second dispatch call will occur.

The minidriver should capture data in whatever format was contained in the last successful *AVStrMiniPinSetDataFormat* dispatch.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Data%20Range%20Intersections%20in%20AVStream%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


