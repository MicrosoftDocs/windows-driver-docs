---
title: How do I initialize WPP software tracing in a user-mode application
description: How do I initialize WPP software tracing in a user-mode application
ms.date: 04/20/2017
---

# How do I initialize WPP software tracing in a user-mode application?


You can initialize WPP tracing in a user-mode application by calling the [WPP\_INIT\_TRACING](/previous-versions/windows/hardware/previsioning-framework/ff556191(v=vs.85)) macro to initialize WPP software tracing.

To avoid errors, you should call the [WPP\_INIT\_TRACING](/previous-versions/windows/hardware/previsioning-framework/ff556191(v=vs.85)) macro at a point in your source code where no tracing attempts have been previously made.

 

