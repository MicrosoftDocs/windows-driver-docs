---
title: PCM High Bitdepth Stream Data Format
description: PCM High Bitdepth Stream Data Format
ms.assetid: 0ad63f01-4fcf-4eca-b8d6-b0b65f384455
keywords:
- PCM high-bitdepth stream data formats WDK
- high-bitdepth stream data formats WDK
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# PCM High Bitdepth Stream Data Format


## <span id="pcm_high_bitdepth_stream_data_format"></span><span id="PCM_HIGH_BITDEPTH_STREAM_DATA_FORMAT"></span>


This example uses an extended version of a [**KSDATAFORMAT\_WAVEFORMATEX**](https://msdn.microsoft.com/library/windows/hardware/ff537095) structure to describe the data format of a PCM high-bitdepth stream. This is similar to the PCM multichannel example, with the exception of the values for `Format.wBitsPerSample` and `Format.wValidBitsPerSample` that appear below.

```
  DataFormat.FormatSize  = sizeof(KSDATAFORMAT) + sizeof(WAVEFORMATEXTENSIBLE);
 DataFormat.Flags       = 0;
  DataFormat.SampleSize  = 0;
  DataFormat.Reserved    = 0;
  DataFormat.MajorFormat = STATICGUIDOF(KSDATAFORMAT_TYPE_AUDIO);
  DataFormat.SubFormat   = STATICGUIDOF(KSDATAFORMAT_SUBTYPE_PCM);
 DataFormat.Specifier   = STATICGUIDOF(KSDATAFORMAT_SPECIFIER_WAVEFORMATEX);
  Format.wFormatTag      = WAVE_FORMAT_EXTENSIBLE;
  Format.nChannels       = 4;
  Format.nSamplesPerSec  = 44100;
  Format.nAvgBytesPerSec = 529200;
  Format.nBlockAlign     = 8;
  Format.wBitsPerSample  = 24;
  Format.cbSize          = sizeof(WAVEFORMATEXTENSIBLE) - sizeof(WAVEFORMATEX);
  Format.wValidBitsPerSample = 20;
  Format.dwChannelMask   = KSAUDIO_SPEAKER_SURROUND;
  Format.SubFormat       = KSDATAFORMAT_SUBTYPE_PCM;
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20PCM%20High%20Bitdepth%20Stream%20Data%20Format%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


