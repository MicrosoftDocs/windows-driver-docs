---
title: PNPCPU Limitations
description: PNPCPU Limitations
ms.assetid: e25a54e7-cf6f-4723-9bf3-3b68cce8ec7e
keywords:
- PNPCPU WDK , limitations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# PNPCPU Limitations


**Note**   Running this tool on a machine that is license restricted is unsupported. If the system is using fewer CPUs than are physically present in the system due to license restrictions for the installed edition, you cannot use the Pnpcpu tool.

 

-   After you have executed the **-add** command once, you must restart your computer. You cannot perform a hot remove of processors that you added using the **-add** command.

-   The discrepancy between the Task Manager and Device Manager views of the system results from the difference between the number of processors being used by Windows (Task Manager view) and the number that can be managed by the processor driver and that were enumerated by ACPI (Device Manager view) or the test's processor enumerator driver.

-   When the custom bus enumerator driver is loaded, the default processor driver will not be loaded, hence the error code 28 on each processor that is shown in Device Manager.

-   After performing the hot-add operation, there will be two entries in Device Manager for each processor, one with error code 28 and the other not. When you select **View** &gt; **Devices by Connection** in Device Manager, you will see one instance of each processor under **Microsoft ACPI-Compliant System**, and a second instance for each under **Processor Bus Enumerator**, which will be the actual running instance.

 

 





