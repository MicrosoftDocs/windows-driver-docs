---
title: How do I initialize WPP software tracing in a kernel-mode driver
description: How do I initialize WPP software tracing in a kernel-mode driver
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How do I initialize WPP software tracing in a kernel-mode driver?


You can initialize WPP tracing in a kernel-mode driver by calling the [WPP\_INIT\_TRACING](/previous-versions/windows/hardware/previsioning-framework/ff556191(v=vs.85)) macro to initialize WPP software tracing.

To avoid errors, you should call the [WPP\_INIT\_TRACING](/previous-versions/windows/hardware/previsioning-framework/ff556191(v=vs.85)) macro in the [**DriverEntry**](../storage/driverentry-of-ide-controller-minidriver.md) function of the driver.

 

