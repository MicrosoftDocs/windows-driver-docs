---
title: Data-Range Properties
description: Data-Range Properties
ms.assetid: 84bdd151-a034-445e-9f6d-19940e32b2c1
keywords:
- data-intersection handlers WDK audio , data-range properties
- data ranges WDK audio , properties
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Data-Range Properties


## <span id="data_range_properties"></span><span id="DATA_RANGE_PROPERTIES"></span>


Data ranges are used not only for data intersection, but can be accessed as device properties as well (see [Pin Data-Range and Intersection Properties](pin-data-range-and-intersection-properties.md)). For this reason, an adapter driver whose data-intersection handler takes care of all format negotiations on its pins should still include a complete set of data ranges. The data ranges should reflect as closely as possible the data-format preferences that are embodied in the adapter's data-intersection handler.

A pin's data ranges can be accessed through the following properties:

[**KSPROPERTY\_PIN\_DATARANGES**](https://msdn.microsoft.com/library/windows/hardware/ff565199)

[**KSPROPERTY\_PIN\_CONSTRAINEDDATARANGES**](https://msdn.microsoft.com/library/windows/hardware/ff565195)

These two properties designate the pin's static data ranges and constrained data ranges, respectively.

Constrained data ranges provide more accurate information about the current capabilities of a device because they are dynamically updated to account for any on-board resources that have already been allocated for other purposes. By comparison, static data ranges might inaccurately report hardware capabilities that depend on resources that are no longer available.

In the current PortCls implementation, the default data-intersection handlers in the port drivers use only an adapter's static data ranges.

 

 




