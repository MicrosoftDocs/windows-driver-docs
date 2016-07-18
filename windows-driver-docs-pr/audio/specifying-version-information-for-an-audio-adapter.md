---
title: Specifying Version Information for an Audio Adapter
description: Specifying Version Information for an Audio Adapter
ms.assetid: 2d1fb5e7-84fe-451f-b53f-bf6017ae94ad
keywords: ["audio adapters WDK , version information", "adapter drivers WDK audio , version information", "Port Class audio adapters WDK , version information", "versions WDK audio"]
---

# Specifying Version Information for an Audio Adapter


## <span id="specifying_version_information_for_an_audio_adapter"></span><span id="SPECIFYING_VERSION_INFORMATION_FOR_AN_AUDIO_ADAPTER"></span>


A vendor should specify the following entries in the **Version** section of an INF file for a port-class audio adapter:

```
  Signature="$CHICAGO$"
  Class=MEDIA
  ClassGUID={4d36e96c-e325-11ce-bfc1-08002be10318}
```

For a description of additional version requirements and options for all device classes, see [**INF Version Section**](https://msdn.microsoft.com/library/windows/hardware/ff547502).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Specifying%20Version%20Information%20for%20an%20Audio%20Adapter%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




