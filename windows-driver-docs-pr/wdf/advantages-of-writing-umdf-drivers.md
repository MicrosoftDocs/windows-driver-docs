---
title: Advantages of Writing UMDF Drivers
description: This topic describes the advantages of writing a User Mode Driver Framework (UMDF) driver instead of a kernel mode driver.
ms.assetid: 28db2121-a5d4-4375-8081-52709416efb0
keywords: ["User Mode Driver Framework WDK advantages", "UMDF WDK advantages", "user mode drivers WDK UMDF advantages"]
---

# Advantages of Writing UMDF Drivers


This topic describes the advantages of writing a User-Mode Driver Framework (UMDF) driver instead of a kernel-mode driver.

When you write a UMDF driver, you benefit from the following:

-   UMDF drivers contribute to greater operating system stability because they have access only to the address space of the process in which they run.
-   Because UMDF drivers run under the **LocalService** account, they have limited access to a user's data or to system files.
-   User-mode drivers operate in a much simpler environment than kernel-mode drivers. For example, kernel-mode drivers must take into account IRQL, page faults, and thread context. In user mode, however, these issues do not exist. User-mode drivers always run in a different thread from the requesting process and can always take page faults.

-   UMDF version 2 offers feature parity with KMDF in most areas. For a full comparison, see [Comparing UMDF 2.0 Functionality to KMDF](comparing-umdf-2-0-functionality-to-kmdf.md).
-   UMDF version 2 facilitates converting between KMDF and UMDF. See [How to convert a KMDF driver to a UMDF 2.0 driver (and vice-versa)](how-to-generate-a-umdf-driver-from-a-kmdf-driver.md).
-   You can debug UMDF drivers by using either a user-mode debugger or, starting with UMDF version 2, a kernel-mode debugger.

-   You can use the Wdfkd.dll debugger extension commands with KMDF and starting with UMDF version 2. For more info, see [Debugger Extensions](debugger-extensions-for-kmdf-drivers.md).

A fundamental goal of the overall WDF model is to provide intelligent defaults, so that you can focus on your device hardware and avoid writing code to perform tasks that are common to most drivers.

To achieve this goal, the framework is designed to work with drivers on an "opt-in" basis. When you write a UMDF driver, you provide callback routines for only the events that affect your device. For example, some devices require intervention immediately after they are turned on and just before they are turned off. The driver for such a device can implement callback functions that the framework calls at those times.

The driver includes code to handle only those events for which its device requires device-specific support. All other events can be handled by framework defaults.

In addition, a driver can configure its I/O request queues so that the framework stops dispatching requests while the device is in a low-power state and resumes dispatching after the device has returned to the operational state. Similarly, if an I/O request arrives while the device is in a low-power state, the framework can automatically turn on the device.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Advantages%20of%20Writing%20UMDF%20Drivers%20%20RELEASE:%20%283/16/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




