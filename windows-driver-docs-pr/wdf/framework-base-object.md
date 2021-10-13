---
title: Framework Base Object
description: Framework Base Object
keywords:
- UMDF objects WDK , base objects
- framework objects WDK UMDF , base objects
- base objects WDK UMDF
- IWDFObject
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Framework Base Object


[!include[UMDF 1 Deprecation](../includes/umdf-1-deprecation.md)]

The framework base object is exposed to drivers by the [IWDFObject](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfobject) interface. It provides basic functionality that is common across all framework object types. All framework objects are derived from this root object.

When drivers create framework base objects through a call to the [**IWDFDriver::CreateWdfObject**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdriver-createwdfobject) method, they can initially register their [IObjectCleanup](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iobjectcleanup) interfaces so that the framework notifies the driver when the objects are about to be destroyed. Later, drivers can use the [**IWDFObject::AssignContext**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfobject-assigncontext) method to change how they receive notifications on the framework base object instance.

 

