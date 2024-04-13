---
title: MIDI Stream Data Range
description: MIDI Stream Data Range
keywords:
- MIDI stream data ranges WDK audio
ms.date: 04/20/2017
---

# MIDI Stream Data Range


## <span id="midi_stream_data_range"></span><span id="MIDI_STREAM_DATA_RANGE"></span>


This example uses a [**KSDATARANGE\_MUSIC**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksdatarange_music) structure to describe the data range for a MIDI stream.

```cpp
  DataRange.FormatSize  = sizeof(KSDATARANGE_MUSIC);
 DataRange.Flags       = 0;
  DataRange.SampleSize  = 0;
  DataRange.Reserved    = 0;
 DataRange.MajorFormat = STATICGUIDOF(KSDATAFORMAT_TYPE_MUSIC);
  DataRange.SubFormat   = STATICGUIDOF(KSDATAFORMAT_SUBTYPE_MIDI);
  DataRange.Specifier   = STATICGUIDOF(KSDATAFORMAT_SPECIFIER_NONE);
  Technology            = STATICGUIDOF(KSMUSIC_TECHNOLOGY_PORT);
  Channels              = 0;
  Notes                 = 0;
  ChannelMask           = 0xFFFF;
```

 

