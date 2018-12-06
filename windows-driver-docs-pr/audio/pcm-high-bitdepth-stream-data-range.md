---
title: PCM High Bitdepth Stream Data Range
description: PCM High Bitdepth Stream Data Range
ms.assetid: 4f3d48ff-e01d-4c80-b493-253afdba6fd7
keywords:
- PCM high-bitdepth stream data ranges WDK
- high-bitdepth stream data ranges WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# PCM High Bitdepth Stream Data Range


## <span id="pcm_high_bitdepth_stream_data_range"></span><span id="PCM_HIGH_BITDEPTH_STREAM_DATA_RANGE"></span>


This example uses a [**KSDATARANGE\_AUDIO**](https://msdn.microsoft.com/library/windows/hardware/ff537096) structure to describe the data range for a PCM high-bitdepth stream.

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
  MaximumBitsPerSample   = 24;  // 24, 32, etc.
  MinimumSampleFrequency = 5000;
  MaximumSampleFrequency = 48000;
```

The member values in this example are similar to those in the [PCM Multichannel Stream Data Range](pcm-multichannel-stream-data-range.md) example, with the exception of the `MaximumBitsPerSample` value, which is greater than 16. This value is set to the maximum number of valid bits supported. For example, if the device supports 20 bits of valid audio data in 24-bit containers, the value for `MaximumBitsPerSample` should be set to 20.

 

 




