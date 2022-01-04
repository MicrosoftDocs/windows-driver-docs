---
title: Filter context best practices
description: Best Practices
keywords:
- contexts WDK file system minifilter , best practices
ms.date: 01/20/2021
---

# Filter context best practices

If your minifilter driver creates only one minifilter driver instance per volume, you should use instance contexts rather than volume contexts for better performance.

You can also improve performance by storing a pointer to the minifilter driver instance context inside its stream or stream handle contexts.
