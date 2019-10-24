---
title: Selecting a Stream Format
description: Selecting a Stream Format
ms.assetid: 876eca52-4d5e-45bd-90df-ff4b6405078d
keywords:
- video capture WDK AVStream , stream formats
- capturing video WDK AVStream , stream formats
- stream formats WDK video capture
- formats WDK video capture
- performing data intersections WDK video capture
- data intersections WDK video capture
- intersections WDK video capture
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Selecting a Stream Format


Video capture devices can capture video in a number of different formats. The [**KSDATARANGE**](https://docs.microsoft.com/previous-versions/ff561658(v=vs.85)) structure is used to convey information about the width, height, granularity, cropping, and frame rates for a particular color space. The structures [**KS\_DATARANGE\_VIDEO**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagks_datarange_video) and [**KS\_DATARANGE\_VIDEO2**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagks_datarange_video2) are extensions of the KSDATARANGE structure and should be used for describing video capture formats. Use KS\_DATARANGE\_VIDEO to describe video frames only. Use KS\_DATARANGE\_VIDEO2 to describe video fields and video frames, with or without bob or weave settings.

The process of selecting a stream format is called *performing a data intersection*. The Stream class interface sends an [**SRB\_GET\_DATA\_INTERSECTION**](https://docs.microsoft.com/windows-hardware/drivers/stream/srb-get-data-intersection) request to a Stream class minidriver to perform a data intersection. The minidriver is responsible for determining the validity of the data range requested and then selecting a particular stream format from the supplied data range, typically using [**KS\_DATAFORMAT\_VIDEOINFOHEADER**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagks_dataformat_videoinfoheader) or [**KS\_DATAFORMAT\_VIDEOINFOHEADER2**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagks_dataformat_videoinfoheader2) structures.

Finally, the minidriver must set certain members of the resulting format as shown below:

```cpp
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

 

 




