---
title: Format of a Text Log Header
description: Format of a Text Log Header
ms.assetid: d4a50905-215f-4156-b5cf-f160c757bb90
keywords: ["headers WDK SetupAPI logging", "formats WDK SetupAPI logging", "text logs WDK SetupAPI , headers"]
---

# Format of a Text Log Header


A *text log header* consists of the first few log entries in a SetupAPI text log. The text log header contains information about the operating system and system architecture. The following is an example of a text log header:

```
[Device Install Log]
     OS Version = 6.0.5033
     Service Pack = 0.0
     Suite = 0x0100
     ProductType = 1
     Architecture = x86

[BeginLog]
```

The information in a text log header is a subset of the information that is returned by a call to [GetVersionEx](http://go.microsoft.com/fwlink/p/?linkid=179601) in an [OVSERVERSIONINFOEX](http://go.microsoft.com/fwlink/p/?linkid=179602) structure. For more information, see the Microsoft Windows SDK.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Format%20of%20a%20Text%20Log%20Header%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




