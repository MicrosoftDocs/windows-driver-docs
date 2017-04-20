---
title: Framework Interrupt Object
author: windows-driver-content
description: Framework Interrupt Object
ms.assetid: FA2B8C11-69D2-4A9E-8F57-C7295DA4EE44
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Framework Interrupt Object


\[This topic applies to UMDF 1.*x*.\]

The framework interrupt object is exposed to drivers by the [**IWDFInterrupt**](https://msdn.microsoft.com/library/windows/hardware/hh451283) interface. It represents a hardware interrupt. Interrupt objects are children of [UMDF device objects](framework-device-object.md). A driver can call the [**IWDFDevice3::CreateInterrupt**](https://msdn.microsoft.com/library/windows/hardware/hh451208) method to create an interrupt object.

When drivers create interrupts, they can provide interfaces for callback functions that the framework calls to notify the driver when events related to the interfaces occur. For more information, see [UMDF Interrupt Object Event Callback Functions](https://msdn.microsoft.com/library/windows/hardware/hh463979).

For more information about interrupt objects, see [Handling Interrupts](handling-interrupts.md).

 

 





