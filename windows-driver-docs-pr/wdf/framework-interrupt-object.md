---
title: Framework Interrupt Object
description: Framework Interrupt Object
ms.date: 04/20/2017
---

# Framework Interrupt Object


[!include[UMDF 1 Deprecation](../includes/umdf-1-deprecation.md)]

The framework interrupt object is exposed to drivers by the [**IWDFInterrupt**](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfinterrupt) interface. It represents a hardware interrupt. Interrupt objects are children of [UMDF device objects](framework-device-object.md). A driver can call the [**IWDFDevice3::CreateInterrupt**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdevice3-createinterrupt) method to create an interrupt object.

When drivers create interrupts, they can provide interfaces for callback functions that the framework calls to notify the driver when events related to the interfaces occur. For more information, see [UMDF Interrupt Object Event Callback Functions](/windows-hardware/drivers/ddi/wudfddi/).

For more information about interrupt objects, see [Handling Interrupts](handling-interrupts.md).

 

