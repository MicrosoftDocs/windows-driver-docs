---
title: Framework Base Object
description: Framework Base Object
ms.assetid: 9d400192-faf0-4d8f-849b-6b955105e21a
keywords:
- UMDF objects WDK , base objects
- framework objects WDK UMDF , base objects
- base objects WDK UMDF
- IWDFObject
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Framework Base Object


[!include[UMDF 1 Deprecation](../umdf-1-deprecation.md)]

The framework base object is exposed to drivers by the [IWDFObject](https://msdn.microsoft.com/library/windows/hardware/ff560200) interface. It provides basic functionality that is common across all framework object types. All framework objects are derived from this root object.

When drivers create framework base objects through a call to the [**IWDFDriver::CreateWdfObject**](https://msdn.microsoft.com/library/windows/hardware/ff558906) method, they can initially register their [IObjectCleanup](https://msdn.microsoft.com/library/windows/hardware/ff556754) interfaces so that the framework notifies the driver when the objects are about to be destroyed. Later, drivers can use the [**IWDFObject::AssignContext**](https://msdn.microsoft.com/library/windows/hardware/ff560208) method to change how they receive notifications on the framework base object instance.

 

 





