---
title: Quality Management
description: Quality Management
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

Pins that report quality management problems support the [**KSPROPERTY\_STREAM\_QUALITY**](./ksproperty-stream-quality.md) property. This is an optional write-only property that the pin can set to the handle and context parameter of a QM complaint sink. To do this, the pin provides a structure of type [**KSQUALITY\_MANAGER**](/windows-hardware/drivers/ddi/ks/ns-ks-ksquality_manager) that contains this information. The pin connection in turn uses this information to notify the quality manager of problems using [**KSQUALITY**](/windows-hardware/drivers/ddi/ks/ns-ks-ksquality) structures with the given context parameter.

To allow user-mode clients to submit quality management complaints, a minidriver supports properties in [KSPROPSETID\_Quality](./kspropsetid-quality.md).

If the pin allows degradation strategies, the minidriver supports the [**KSPROPERTY\_STREAM\_DEGRADATION**](./ksproperty-stream-degradation.md) property.

For more information, see [**KSDEGRADE**](/previous-versions/ff561671(v=vs.85)) and [**KSDEGRADE\_STANDARD**](/windows-hardware/drivers/ddi/ks/ne-ks-ksdegrade_standard).

 

