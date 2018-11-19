---
title: Organization of DPC Queues
description: Organization of DPC Queues
ms.assetid: df176a6d-d7a7-4d8b-ab1b-fd7f5b89fcbe
keywords: ["DPC queues WDK kernel", "queues WDK DPC"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Organization of DPC Queues


The system provides one DPC queue for each processor. Drivers can control which queue the system assigns a DPC to, the location of the DPC within the queue, and when the queue is processed.

DPCs that are assigned to a particular processor's queue are run on that processor. By default, when the driver calls [**KeInsertQueueDpc**](https://msdn.microsoft.com/library/windows/hardware/ff552185) or [**IoRequestDpc**](https://msdn.microsoft.com/library/windows/hardware/ff549657), the DPC is queued on the currently active processor. Drivers can specify the processor queue by calling [**KeSetTargetProcessorDpc**](https://msdn.microsoft.com/library/windows/hardware/ff553278) before calling **KeInsertQueueDpc** or **IoRequestDpc**.

On Windows Vista and later versions of Windows, the system also has one threaded DPC queue for each processor. Drivers can use **KeSetTargetProcessorDpc** to specify the processor queue for threaded DPCs.

The [**KeSetImportanceDpc**](https://msdn.microsoft.com/library/windows/hardware/ff553259) routine controls where a DPC is placed within the queue. Typically, the DPC is placed at the end of the queue; but if the driver first calls **KeSetImportanceDpc** with the *Importance* parameter equal to **HighImportance**, the DPC is placed at the beginning of the queue.

For ordinary (non-threaded) DPCs, **KeSetImportanceDpc** also determines whether **KeInsertQueueDpc** or **IoRequestDpc** will immediately begin processing the DPC queue. The following list describes the rules for processing the queue:

-   Processing of the DPC queue begins immediately if the DPC is assigned to the current processor and *Importance* is not equal to **LowImportance**, or if *Importance* is equal to **LowImportance** and the DPC queue depth of the current processor exceeds a system-defined limit or the DPC request rate has fallen below a system-defined minimum. Otherwise, processing of the DPC is deferred until the appropriate queue depth and rate requirements are met.

-   Processing of the DPC queue begins immediately on the target processor if the DPC is assigned to a processor that is different than the current processor and *Importance* equals **MediumHighImportance** or **HighImportance**, or if the DPC queue depth of the target processor exceeds a system-defined limit. Otherwise, processing of the DPC is deferred until the appropriate queue depth and rate requirements are met.

 

 




