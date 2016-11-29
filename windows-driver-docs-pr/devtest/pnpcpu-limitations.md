---
title: PNPCPU Limitations
description: PNPCPU Limitations
ms.assetid: e25a54e7-cf6f-4723-9bf3-3b68cce8ec7e
keywords: ["PNPCPU WDK , limitations"]
---

# PNPCPU Limitations


**Note**   Running this tool on a machine that is license restricted is unsupported. If the system is using fewer CPUs than are physically present in the system due to license restrictions for the installed edition, you cannot use the Pnpcpu tool.

 

-   After you have executed the **-add** command once, you must restart your computer. You cannot perform a hot remove of processors that you added using the **-add** command.

-   The discrepancy between the Task Manager and Device Manager views of the system results from the difference between the number of processors being used by Windows (Task Manager view) and the number that can be managed by the processor driver and that were enumerated by ACPI (Device Manager view) or the test's processor enumerator driver.

-   When the custom bus enumerator driver is loaded, the default processor driver will not be loaded, hence the error code 28 on each processor that is shown in Device Manager.

-   After performing the hot-add operation, there will be two entries in Device Manager for each processor, one with error code 28 and the other not. When you select **View** &gt; **Devices by Connection** in Device Manager, you will see one instance of each processor under **Microsoft ACPI-Compliant System**, and a second instance for each under **Processor Bus Enumerator**, which will be the actual running instance.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20PNPCPU%20Limitations%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




