---
title: Framework I/O Target Object
description: Framework I/O Target Object
keywords:
- UMDF objects WDK , I/O target objects
- framework objects WDK UMDF , I/O target objects
- I/O target objects WDK UMDF
- IWDFIoTarget
- targets WDK UMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Framework I/O Target Object


[!include[UMDF 1 Deprecation](../includes/umdf-1-deprecation.md)]

The framework I/O target object is exposed to drivers by the [IWDFIoTarget](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfiotarget) interface. It retrieves information about an I/O target, which typically represents a lower driver in the stack but can also represent another UMDF driver or the kernel-mode portion of the stack. The I/O target object provides UMDF drivers a way to send requests to another device.

UMDF drivers can also use the [IWDFIoTargetStateManagement](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfiotargetstatemanagement) interface to manage and monitor the state of an I/O target object.

 

