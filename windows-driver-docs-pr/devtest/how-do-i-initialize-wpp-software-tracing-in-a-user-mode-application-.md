---
title: How do I initialize WPP software tracing in a user-mode application
description: How do I initialize WPP software tracing in a user-mode application
ms.assetid: 1f1ab873-a1c3-4915-af31-ab74c1898fcb
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How do I initialize WPP software tracing in a user-mode application?


You can initialize WPP tracing in a user-mode application by calling the [WPP\_INIT\_TRACING](https://msdn.microsoft.com/library/windows/hardware/ff556191) macro to initialize WPP software tracing.

To avoid errors, you should call the [WPP\_INIT\_TRACING](https://msdn.microsoft.com/library/windows/hardware/ff556191) macro at a point in your source code where no tracing attempts have been previously made.

 

 





