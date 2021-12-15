---
title: '[String] section changes for localized strings'
description: This INF requirement ensures that pseudo-localized builds work. The requirement is to delineate localizable versus non-localizable strings within the strings section
ms.date: 04/20/2017
---

# \[String\] section changes for localized strings


This INF requirement ensures that pseudo-localized builds work. The requirement is to delineate localizable versus non-localizable strings within the strings section.

The following example has no preface of what is localized or not; this should not be used:

``` syntax
[Strings]

REG_MULTI_SZ   = 0x00010000
REG_DWORD      = 0x00010001

MSFT = "Microsoft"
IHV  = "Contoso, Ltd"
```

The following example should be used instead; note the new lines:

``` syntax
[Strings]

;Localizable
MSFT = "Microsoft"
IHV  = "Contoso, Ltd"


;Non-Localizable
REG_MULTI_SZ   = 0x00010000
REG_DWORD      = 0x00010001
```

 

 





