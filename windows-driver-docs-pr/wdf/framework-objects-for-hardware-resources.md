---
title: Framework Objects for Hardware Resources
description: Framework Objects for Hardware Resources
keywords:
- hardware resources WDK KMDF , framework objects
- framework objects WDK KMDF , hardware resources
- framework resource-requirements-list objects WDK KMDF
- framework resource-range-list objects WDK KMDF
- framework resource-list objects WDK KMDF
- resource-list objects WDK KMDF
- resource-range-list objects WDK KMDF
- resource-requirements-list objects WDK KMDF
- hardware resources WDK KMDF , specifying
ms.date: 04/20/2017
---

# Framework Objects for Hardware Resources


The framework defines the following three objects, which the framework and drivers use to specify a device's hardware resources:

<a href="" id="framework-resource-requirements-list-objects"></a>*Framework resource-requirements-list objects*  
Each framework resource-requirements-list object represents a [resource requirements list](../kernel/hardware-resources.md). Handles to these objects have a type of WDFIORESREQLIST. The object defines [framework resource-requirements-list object methods](/windows-hardware/drivers/ddi/wdfresource/). A resource requirements list consists of a set of logical configurations.

<a href="" id="framework-resource-range-list-objects"></a>*Framework resource-range-list objects*  
Each framework resource-range-list object represents a [logical configuration](../kernel/hardware-resources.md#ddk-logical-configurations-kg) (that is, a set of ranges of resources that the device is capable of using) in a resource requirements list. Handles to these objects have a type of WDFIORESLIST. The object defines [framework resource-range-list object methods](/windows-hardware/drivers/ddi/wdfresource/).

<a href="" id="framework-resource-list-objects"></a>*Framework resource-list objects*  
Each framework resource-list object represents a logical configuration (that is, a set of specific resources) in a [resource list](../kernel/hardware-resources.md). Handles to these objects have a type of WDFCMRESLIST. The object defines [framework resource-list object methods](/windows-hardware/drivers/ddi/wdfresource/).

 

