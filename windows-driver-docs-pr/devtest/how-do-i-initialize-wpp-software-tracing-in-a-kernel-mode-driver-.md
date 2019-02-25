---
title: How do I initialize WPP software tracing in a kernel-mode driver
description: How do I initialize WPP software tracing in a kernel-mode driver
ms.assetid: 739428e8-14ff-4435-80e6-35b5c3366c79
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How do I initialize WPP software tracing in a kernel-mode driver?


You can initialize WPP tracing in a kernel-mode driver by calling the [WPP\_INIT\_TRACING](https://msdn.microsoft.com/library/windows/hardware/ff556191) macro to initialize WPP software tracing.

To avoid errors, you should call the [WPP\_INIT\_TRACING](https://msdn.microsoft.com/library/windows/hardware/ff556191) macro in the [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff552644) function of the driver.

 

 





