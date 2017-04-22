---
title: DirectMusic Stream Data Format
description: DirectMusic Stream Data Format
ms.assetid: f3aae6c0-6b9d-43fa-9ef1-d6702017f55d
keywords:
- DirectMusic WDK audio , stream data formats
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# DirectMusic Stream Data Format


## <span id="directmusic_stream_data_format"></span><span id="DIRECTMUSIC_STREAM_DATA_FORMAT"></span>


This example uses a [**KSDATAFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff561656) structure to describe the data format of a DirectMusic stream.

```
  DataFormat.FormatSize  = sizeof(KSDATAFORMAT);
  DataFormat.Flags       = 0;
  DataFormat.SampleSize  = 0;
 DataFormat.Reserved    = 0;
  DataFormat.MajorFormat = STATICGUIDOF(KSDATAFORMAT_TYPE_MUSIC);
  DataFormat.SubFormat   = STATICGUIDOF(KSDATAFORMAT_SUBTYPE_DIRECTMUSIC);
  DataFormat.Specifier   = STATICGUIDOF(KSDATAFORMAT_SPECIFIER_NONE);
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20DirectMusic%20Stream%20Data%20Format%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


