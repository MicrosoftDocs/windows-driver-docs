---
title: PCM Stream Data Range
description: PCM Stream Data Range
ms.assetid: e8a9b681-3bd2-46ed-970f-5217dbfb2e4e
keywords:
- PCM stream data ranges WDK
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# PCM Stream Data Range


## <span id="pcm_stream_data_range"></span><span id="PCM_STREAM_DATA_RANGE"></span>


This example uses a [**KSDATARANGE\_AUDIO**](https://msdn.microsoft.com/library/windows/hardware/ff537096) structure to describe the data range for a PCM stream.

```
  DataRange.FormatSize  = sizeof(KSDATARANGE_AUDIO);
  DataRange.Flags       = 0;
  DataRange.SampleSize  = 0;
  DataRange.Reserved    = 0;
  DataRange.MajorFormat = STATICGUIDOF(KSDATAFORMAT_TYPE_AUDIO);
  DataRange.SubFormat   = STATICGUIDOF(KSDATAFORMAT_SUBTYPE_PCM);
  DataRange.Specifier   = STATICGUIDOF(KSDATAFORMAT_SPECIFIER_WAVEFORMATEX);
  MaximumChannels        = 2;
  MinimumBitsPerSample   = 2;
  MaximumBitsPerSample   = 16;
  MinimumSampleFrequency = 5000;
  MaximumSampleFrequency = 48000;
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20PCM%20Stream%20Data%20Range%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


