---
title: DirectMusic Stream Data Format
description: DirectMusic Stream Data Format
ms.assetid: f3aae6c0-6b9d-43fa-9ef1-d6702017f55d
keywords:
- DirectMusic WDK audio , stream data formats
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DirectMusic Stream Data Format


## <span id="directmusic_stream_data_format"></span><span id="DIRECTMUSIC_STREAM_DATA_FORMAT"></span>


This example uses a [**KSDATAFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff561656) structure to describe the data format of a DirectMusic stream.

```cpp
  DataFormat.FormatSize  = sizeof(KSDATAFORMAT);
  DataFormat.Flags       = 0;
  DataFormat.SampleSize  = 0;
 DataFormat.Reserved    = 0;
  DataFormat.MajorFormat = STATICGUIDOF(KSDATAFORMAT_TYPE_MUSIC);
  DataFormat.SubFormat   = STATICGUIDOF(KSDATAFORMAT_SUBTYPE_DIRECTMUSIC);
  DataFormat.Specifier   = STATICGUIDOF(KSDATAFORMAT_SPECIFIER_NONE);
```

 

 




