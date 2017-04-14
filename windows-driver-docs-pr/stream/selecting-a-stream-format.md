---
title: Selecting a Stream Format
author: windows-driver-content
description: Selecting a Stream Format
ms.assetid: 876eca52-4d5e-45bd-90df-ff4b6405078d
keywords: ["video capture WDK AVStream , stream formats", "capturing video WDK AVStream , stream formats", "stream formats WDK video capture", "formats WDK video capture", "performing data intersections WDK video capture", "data intersections WDK video capture", "intersections WDK video capture"]
---

# Selecting a Stream Format


Video capture devices can capture video in a number of different formats. The [**KSDATARANGE**](https://msdn.microsoft.com/library/windows/hardware/ff561658) structure is used to convey information about the width, height, granularity, cropping, and frame rates for a particular color space. The structures [**KS\_DATARANGE\_VIDEO**](https://msdn.microsoft.com/library/windows/hardware/ff567628) and [**KS\_DATARANGE\_VIDEO2**](https://msdn.microsoft.com/library/windows/hardware/ff567629) are extensions of the KSDATARANGE structure and should be used for describing video capture formats. Use KS\_DATARANGE\_VIDEO to describe video frames only. Use KS\_DATARANGE\_VIDEO2 to describe video fields and video frames, with or without bob or weave settings.

The process of selecting a stream format is called *performing a data intersection*. The Stream class interface sends an [**SRB\_GET\_DATA\_INTERSECTION**](https://msdn.microsoft.com/library/windows/hardware/ff568168) request to a Stream class minidriver to perform a data intersection. The minidriver is responsible for determining the validity of the data range requested and then selecting a particular stream format from the supplied data range, typically using [**KS\_DATAFORMAT\_VIDEOINFOHEADER**](https://msdn.microsoft.com/library/windows/hardware/ff567331) or [**KS\_DATAFORMAT\_VIDEOINFOHEADER2**](https://msdn.microsoft.com/library/windows/hardware/ff567335) structures.

Finally, the minidriver must set certain members of the resulting format as shown below:

```
.
.
.
// Calculate biSizeImage for this request, and put the result in both
// the biSizeImage field of the bmiHeader AND in the SampleSize field
// of the DataFormat.
//
// Note that for compressed sizes, this calculation will probably not
// be just width * height * bitdepth
 
DataFormatVideoInfoHeaderOut->VideoInfoHeader.bmiHeader.biSizeImage =
DataFormatVideoInfoHeaderOut->DataFormat.SampleSize = 
KS_DIBSIZE(DataFormatVideoInfoHeaderOut->VideoInfoHeader.bmiHeader);
.
.
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Selecting%20a%20Stream%20Format%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


