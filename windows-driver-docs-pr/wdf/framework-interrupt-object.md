---
title: Framework Interrupt Object
description: Framework Interrupt Object
ms.assetid: FA2B8C11-69D2-4A9E-8F57-C7295DA4EE44
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Framework Interrupt Object


[!include[UMDF 1 Deprecation](../includes/umdf-1-deprecation.md)]

The framework interrupt object is exposed to drivers by the [**IWDFInterrupt**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfinterrupt) interface. It represents a hardware interrupt. Interrupt objects are children of [UMDF device objects](framework-device-object.md). A driver can call the [**IWDFDevice3::CreateInterrupt**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdevice3-createinterrupt) method to create an interrupt object.

When drivers create interrupts, they can provide interfaces for callback functions that the framework calls to notify the driver when events related to the interfaces occur. For more information, see [UMDF Interrupt Object Event Callback Functions](https://docs.microsoft.com/windows-hardware/drivers/ddi/wudfddi/).

For more information about interrupt objects, see [Handling Interrupts](handling-interrupts.md).

 

 





