---
title: Quality Management
description: Quality Management
ms.assetid: 359e6e12-903f-4037-8f35-b090ce41f770
keywords:
- quality management WDK kernel streaming
- KSPROPERTY_STREAM_QUALITY
- KSQUALITY_MANAGER
- notifications WDK kernel streaming
- complaints WDK kernel streaming
- kernel streaming WDK , quality management
- KS WDK , quality management
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Quality Management





The kernel streaming architecture provides optional support for quality management. This mechanism adjusts flow control to match resource constraints and determines degradation needs in a filter graph. Quality management notifications are sent through a kernel-mode proxy.

Pins that report quality management problems support the [**KSPROPERTY\_STREAM\_QUALITY**](https://msdn.microsoft.com/library/windows/hardware/ff565750) property. This is an optional write-only property that the pin can set to the handle and context parameter of a QM complaint sink. To do this, the pin provides a structure of type [**KSQUALITY\_MANAGER**](https://msdn.microsoft.com/library/windows/hardware/ff566730) that contains this information. The pin connection in turn uses this information to notify the quality manager of problems using [**KSQUALITY**](https://msdn.microsoft.com/library/windows/hardware/ff566728) structures with the given context parameter.

To allow user-mode clients to submit quality management complaints, a minidriver supports properties in [KSPROPSETID\_Quality](https://msdn.microsoft.com/library/windows/hardware/ff566587).

If the pin allows degradation strategies, the minidriver supports the [**KSPROPERTY\_STREAM\_DEGRADATION**](https://msdn.microsoft.com/library/windows/hardware/ff565690) property.

For more information, see [**KSDEGRADE**](https://msdn.microsoft.com/library/windows/hardware/ff561671) and [**KSDEGRADE\_STANDARD**](https://msdn.microsoft.com/library/windows/hardware/ff561673).

 

 




