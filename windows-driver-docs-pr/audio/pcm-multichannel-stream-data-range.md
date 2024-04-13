---
title: PCM Multichannel Stream Data Range
description: PCM Multichannel Stream Data Range
keywords:
- PCM multichannel stream data ranges WDK
ms.date: 04/20/2017
---

# PCM Multichannel Stream Data Range


## <span id="pcm_multichannel_stream_data_range"></span><span id="PCM_MULTICHANNEL_STREAM_DATA_RANGE"></span>


This example uses a [**KSDATARANGE\_AUDIO**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksdatarange_audio) structure to describe the data range for a PCM multichannel stream.

```cpp
  DataRange.FormatSize  = sizeof(KSDATARANGE_AUDIO);
  DataRange.Flags       = 0;
  DataRange.SampleSize  = 0;
  DataRange.Reserved    = 0;
  DataRange.MajorFormat = STATICGUIDOF(KSDATAFORMAT_TYPE_AUDIO);
  DataRange.SubFormat   = STATICGUIDOF(KSDATAFORMAT_SUBTYPE_PCM);
 DataRange.Specifier   = STATICGUIDOF(KSDATAFORMAT_SPECIFIER_WAVEFORMATEX);
  MaximumChannels        = 4;   // max number of channels, or -1 for unlimited
  MinimumBitsPerSample   = 2;
  MaximumBitsPerSample   = 16;
  MinimumSampleFrequency = 5000;
  MaximumSampleFrequency = 48000;
```

 

