---
title: DirectSound Stream Data Range
description: DirectSound Stream Data Range
ms.assetid: cc31eb2d-7421-4748-b14c-f4d3d15f9884
keywords:
- DirectSound WDK audio , stream data ranges
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DirectSound Stream Data Range


## <span id="directsound_stream_data_range"></span><span id="DIRECTSOUND_STREAM_DATA_RANGE"></span>


This example uses a [**KSDATARANGE\_AUDIO**](https://msdn.microsoft.com/library/windows/hardware/ff537096) structure to describe the data range for a DirectSound stream.

```cpp
  DataRange.FormatSize  = sizeof(KSDATARANGE_AUDIO);
  DataRange.Flags       = 0;
  DataRange.SampleSize  = 0;
  DataRange.Reserved    = 0;
  DataRange.MajorFormat = STATICGUIDOF(KSDATAFORMAT_TYPE_AUDIO);
  DataRange.SubFormat   = STATICGUIDOF(KSDATAFORMAT_SUBTYPE_PCM);
  DataRange.Specifier   = STATICGUIDOF(KSDATAFORMAT_SPECIFIER_DSOUND);
  MaximumChannels        = 4;   // max number of channels, or -1 for unlimited
  MinimumBitsPerSample   = 2;
  MaximumBitsPerSample   = 16;  // 16, 24, 32, etc.
  MinimumSampleFrequency = 5000;
  MaximumSampleFrequency = 48000;
```

The member values in this example are similar to those of the [PCM multichannel stream data range](pcm-multichannel-stream-data-range.md) example, with the exception of the **MaximumBitsPerSample** value. This value is set to the sample container size and should be a multiple of eight. For example, if the device supports 20 bits of valid audio data in 24-bit containers, the value for **MaximumBitsPerSample** should be set to 24.

 

 




