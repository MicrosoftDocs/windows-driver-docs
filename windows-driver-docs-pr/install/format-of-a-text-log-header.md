---
title: Format of a Text Log Header
description: Format of a Text Log Header
ms.assetid: d4a50905-215f-4156-b5cf-f160c757bb90
keywords:
- headers WDK SetupAPI logging
- formats WDK SetupAPI logging
- text logs WDK SetupAPI , headers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Format of a Text Log Header


A *text log header* consists of the first few log entries in a SetupAPI text log. The text log header contains information about the operating system and system architecture. The following is an example of a text log header:

```cpp
[Device Install Log]
     OS Version = 6.0.5033
     Service Pack = 0.0
     Suite = 0x0100
     ProductType = 1
     Architecture = x86

[BeginLog]
```

The information in a text log header is a subset of the information that is returned by a call to [GetVersionEx](http://go.microsoft.com/fwlink/p/?linkid=179601) in an [OVSERVERSIONINFOEX](http://go.microsoft.com/fwlink/p/?linkid=179602) structure. For more information, see the Microsoft Windows SDK.

 

 





