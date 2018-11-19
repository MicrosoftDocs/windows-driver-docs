---
title: Overview of Partial Print Providers
description: Overview of Partial Print Providers
ms.assetid: 622f99e3-d4a5-42f0-ab71-4d256e0ea02c
keywords:
- print providers WDK , partial print providers
- network print providers WDK , partial print providers
- partial print providers WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Overview of Partial Print Providers





A partial provider DLL typically implements customized versions of only the provider functions that manage print queues and print jobs. The partial provider executes only on the print client system and depends on the local print provider for driver management operations and for generating printer data. Multiple partial providers can exist on a client system.

In [Functions Defined by Print Providers](functions-defined-by-print-providers.md), certain functions are identified as "required". Partial print providers must provide all required functions. Partial print providers generally do not implement any of the optional functions. Required functions belong to the following function groups:

[Initialization Function](functions-defined-by-print-providers.md#ddk-initialization-function-gg)

[Print Queue Management Functions](functions-defined-by-print-providers.md#ddk-print-queue-management-functions-gg)

[Print Job Creation Functions](functions-defined-by-print-providers.md#ddk-print-job-creation-functions-gg)

[Print Job Scheduling Functions](functions-defined-by-print-providers.md#ddk-print-job-scheduling-functions-gg)

[Port Management Functions](functions-defined-by-print-providers.md#ddk-port-management-functions-gg)

For partial print providers, printer ports should be considered to be equivalent to print queues. For any function that receives a PRINTER\_INFO\_2 structure (described in the Microsoft Windows SDK documentation), the structure's **pPort** member should be set to the print queue name. Thus if the print queue name is \\\\Server\\Printer1, the port name should also be \\\\Server\\Printer1. The partial print provider's implementation of EnumPorts (described in the Windows SDK documentation) must return a port name of \\\\Server\\Printer1.

As described in [Introduction to Print Providers](introduction-to-print-providers.md), an application's call to **OpenPrinter** causes the spooler's router to call each print provider until one of them recognizes the specified print queue and returns a handle.

It is important to remember that a partial print provider does not replace the local provider. Once a user connection to a printer has been created, each call to a provider function is routed through the local provider, which either handles the call itself or reroutes it to a partial provider. All calls to provider functions that are identified as "required" are rerouted from the local provider to the appropriate partial provider.

Partial providers do not generate print jobs; they depend on the local provider and its [*print processors*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-print-processor) to create [RAW data](raw-data-type.md) that can be sent to a printer. When a print processor calls the local provider's **StartDocPrinter** function (see [Printing a Print Job](printing-a-print-job.md)), and the print queue is supported by a partial provider, the local provider calls the partial provider's **StartDocPrinter** function, supplying the RAW data (as a file). The partial provider's **StartDocPrinter**, **WritePrinter**, and **EndDocPrinter** functions should send the RAW data over the network to the remote print queue.

 

 




