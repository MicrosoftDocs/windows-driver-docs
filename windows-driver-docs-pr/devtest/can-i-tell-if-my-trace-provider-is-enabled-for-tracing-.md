---
title: Can I tell if my trace provider is enabled for tracing
description: Can I tell if my trace provider is enabled for tracing
ms.assetid: 8cc4e364-a0bc-4ef3-af3c-c08f3183b548
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Can I tell if my trace provider is enabled for tracing?


Yes, you can use the WPP\_LEVEL\_ENABLED macro to tell whether your [trace provider](trace-provider.md), such as a kernel-mode driver or user-mode application, is enabled for tracing and which flags are enabled. This is especially useful if your trace provider does extra work to prepare for software tracing.

For example, you can use a condition of the form:

```
If (WPP_LEVEL_ENABLED(flag) {
            // Tracing is enabled
            Prepare to trace
            DoTraceMessage(flag...);
}
```

 

 





