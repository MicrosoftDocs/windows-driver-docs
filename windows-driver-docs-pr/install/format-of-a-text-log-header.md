---
title: Format of a Text Log Header
description: Format of a Text Log Header
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

The information in a text log header is a subset of the information that is returned by a call to [GetVersionEx](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getversionexa) in an [OVSERVERSIONINFOEX](/windows/win32/api/winnt/ns-winnt-osversioninfoexa) structure. For more information, see the Microsoft Windows SDK.

 

