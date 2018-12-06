---
title: PCM Stream Data Format
description: PCM Stream Data Format
ms.assetid: 86599e55-e771-4d6e-ad59-6dc905c53cd8
keywords:
- PCM stream data formats WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# PCM Stream Data Format


## <span id="pcm_stream_data_format"></span><span id="PCM_STREAM_DATA_FORMAT"></span>


This example uses a [**KSDATAFORMAT\_WAVEFORMATEX**](https://msdn.microsoft.com/library/windows/hardware/ff537095) structure to describe the data format of a PCM stream.

```cpp
  DataFormat.FormatSize  = sizeof(KSDATAFORMAT_WAVEFORMATEX);
  DataFormat.Flags       = 0;
  DataFormat.SampleSize  = 0;
  DataFormat.Reserved    = 0;
  DataFormat.MajorFormat = STATICGUIDOF(KSDATAFORMAT_TYPE_AUDIO);
  DataFormat.SubFormat   = STATICGUIDOF(KSDATAFORMAT_SUBTYPE_PCM);
 DataFormat.Specifier   = STATICGUIDOF(KSDATAFORMAT_SPECIFIER_WAVEFORMATEX);
  Format.wFormatTag      = WAVE_FORMAT_PCM;
  Format.nChannels       = 2;
  Format.nSamplesPerSec  = 44100;
  Format.nAvgBytesPerSec = 176400;
  Format.nBlockAlign     = 4;
  Format.wBitsPerSample  = 16;
  Format.cbSize          = 0;
```

 

 




