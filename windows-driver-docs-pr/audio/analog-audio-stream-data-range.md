---
Description: Analog Audio Stream Data Range
MS-HAID: 'audio.analog\_audio\_stream\_data\_range'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Analog Audio Stream Data Range
---

# Analog Audio Stream Data Range


## <span id="analog_audio_stream_data_range"></span><span id="ANALOG_AUDIO_STREAM_DATA_RANGE"></span>


This example uses a [**KSDATARANGE**](stream.ksdatarange) structure to describe the data range for an analog audio stream.

```
  DataRange.FormatSize  = sizeof(KSDATARANGE);
  DataRange.Flags       = 0;
  DataRange.SampleSize  = 0;
  DataRange.Reserved    = 0;
  DataRange.MajorFormat = STATICGUIDOF(KSDATAFORMAT_TYPE_AUDIO);
  DataRange.SubFormat   = STATICGUIDOF(KSDATAFORMAT_SUBTYPE_ANALOG);
  DataRange.Specifier   = STATICGUIDOF(KSDATAFORMAT_SPECIFIER_NONE);
```

Typically, a miniport driver uses this type of data range to describe the analog signal passing through a [*bridge pin*](wdkgloss.b#wdkgloss-bridge-pin), which represents a hardwired connection on an audio adapter card. For more information about bridge pins, see [Audio Filter Graphs](audio-filter-graphs.md). Also, see the code example in [Exposing Filter Topology](exposing-filter-topology.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Analog%20Audio%20Stream%20Data%20Range%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")


