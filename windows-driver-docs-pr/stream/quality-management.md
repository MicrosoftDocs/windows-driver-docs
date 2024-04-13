---
title: Quality Management
description: Describes the quality management mechanism that adjusts flow control to match resource constraints and determines degradation needs in a filter graph.
keywords:
- quality management WDK kernel streaming
- KSPROPERTY_STREAM_QUALITY
- KSQUALITY_MANAGER
- notifications WDK kernel streaming
- complaints WDK kernel streaming
- kernel streaming WDK , quality management
- KS WDK , quality management
ms.date: 07/13/2021
---

# Quality Management

The kernel streaming architecture provides optional support for quality management. This mechanism adjusts flow control to match resource constraints and determines degradation needs in a filter graph. Quality management notifications are sent through a kernel-mode proxy.

Pins that report quality management problems support the [**KSPROPERTY_STREAM_QUALITY**](ksproperty-stream-quality.md) property. This is an optional write-only property that the pin can set to the handle and context parameter of a quality management complaint sink. To do this, the pin provides a structure of type [**KSQUALITY_MANAGER**](/windows-hardware/drivers/ddi/ks/ns-ks-ksquality_manager) that contains this information. The pin connection in turn uses this information to notify the quality manager of problems using [**KSQUALITY**](/windows-hardware/drivers/ddi/ks/ns-ks-ksquality) structures with the given context parameter.

To allow user-mode clients to submit quality management complaints, a minidriver supports properties in [KSPROPSETID_Quality](./kspropsetid-quality.md).

If the pin allows degradation strategies, the minidriver supports the [**KSPROPERTY_STREAM_DEGRADATION**](ksproperty-stream-degradation.md) property.

For more information, see [**KSDEGRADE**](ksdegrade-structure.md) and [**KSDEGRADE_STANDARD**](/windows-hardware/drivers/ddi/ks/ne-ks-ksdegrade_standard).
