---
title: Framework Objects for Hardware Resources
description: Framework Objects for Hardware Resources
ms.assetid: 64eb628f-ce3d-494b-9fc1-7179a722c5f2
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
ms.localizationpriority: medium
---

# Framework Objects for Hardware Resources


The framework defines the following three objects, which the framework and drivers use to specify a device's hardware resources:

<a href="" id="framework-resource-requirements-list-objects"></a>*Framework resource-requirements-list objects*  
Each framework resource-requirements-list object represents a [resource requirements list](https://msdn.microsoft.com/library/windows/hardware/ff547012). Handles to these objects have a type of WDFIORESREQLIST. The object defines [framework resource-requirements-list object methods](https://msdn.microsoft.com/library/windows/hardware/dn265665). A resource requirements list consists of a set of logical configurations.

<a href="" id="framework-resource-range-list-objects"></a>*Framework resource-range-list objects*  
Each framework resource-range-list object represents a [logical configuration](https://msdn.microsoft.com/library/windows/hardware/ff547012#ddk-logical-configurations-kg) (that is, a set of ranges of resources that the device is capable of using) in a resource requirements list. Handles to these objects have a type of WDFIORESLIST. The object defines [framework resource-range-list object methods](https://msdn.microsoft.com/library/windows/hardware/dn265665).

<a href="" id="framework-resource-list-objects"></a>*Framework resource-list objects*  
Each framework resource-list object represents a logical configuration (that is, a set of specific resources) in a [resource list](https://msdn.microsoft.com/library/windows/hardware/ff547012). Handles to these objects have a type of WDFCMRESLIST. The object defines [framework resource-list object methods](https://msdn.microsoft.com/library/windows/hardware/dn265665).

 

 





