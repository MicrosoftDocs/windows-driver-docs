---
title: MIDI Stream Data Format
description: MIDI Stream Data Format
ms.assetid: c179cf74-7493-4c27-97bd-5eb4d0dffbe6
keywords:
- MIDI stream data formats WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# MIDI Stream Data Format


## <span id="midi_stream_data_format"></span><span id="MIDI_STREAM_DATA_FORMAT"></span>


This example uses a [**KSDATAFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff561656) structure to describe the data format of a MIDI stream.

```cpp
  DataFormat.FormatSize  = sizeof(KSDATAFORMAT);
  DataFormat.Flags       = 0;
  DataFormat.SampleSize  = 0;
 DataFormat.Reserved    = 0;
  DataFormat.MajorFormat = STATICGUIDOF(KSDATAFORMAT_TYPE_MUSIC);
  DataFormat.SubFormat   = STATICGUIDOF(KSDATAFORMAT_SUBTYPE_MIDI);
  DataFormat.Specifier   = STATICGUIDOF(KSDATAFORMAT_SPECIFIER_NONE);
```

 

 




