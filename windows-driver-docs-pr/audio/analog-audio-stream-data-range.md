---
title: Analog Audio Stream Data Range
description: Analog Audio Stream Data Range
ms.assetid: e4503ace-1e96-401e-b410-18ee6b07a37b
keywords:
- analog audio WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Analog Audio Stream Data Range


## <span id="analog_audio_stream_data_range"></span><span id="ANALOG_AUDIO_STREAM_DATA_RANGE"></span>


This example uses a [**KSDATARANGE**](https://msdn.microsoft.com/library/windows/hardware/ff561658) structure to describe the data range for an analog audio stream.

```cpp
  DataRange.FormatSize  = sizeof(KSDATARANGE);
  DataRange.Flags       = 0;
  DataRange.SampleSize  = 0;
  DataRange.Reserved    = 0;
  DataRange.MajorFormat = STATICGUIDOF(KSDATAFORMAT_TYPE_AUDIO);
  DataRange.SubFormat   = STATICGUIDOF(KSDATAFORMAT_SUBTYPE_ANALOG);
  DataRange.Specifier   = STATICGUIDOF(KSDATAFORMAT_SPECIFIER_NONE);
```

Typically, a miniport driver uses this type of data range to describe the analog signal passing through a [*bridge pin*](https://msdn.microsoft.com/library/windows/hardware/ff556272#wdkgloss_bridge_pin), which represents a hardwired connection on an audio adapter card. For more information about bridge pins, see [Audio Filter Graphs](audio-filter-graphs.md). Also, see the code example in [Exposing Filter Topology](exposing-filter-topology.md).

 

 




