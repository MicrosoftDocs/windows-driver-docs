---
title: Advantages of Writing UMDF Drivers
description: This topic describes the advantages of writing a User-Mode Driver Framework (UMDF) driver instead of a kernel-mode driver.
ms.assetid: 28db2121-a5d4-4375-8081-52709416efb0
keywords:
- User-Mode Driver Framework WDK , advantages
- UMDF WDK , advantages
- user-mode drivers WDK UMDF , advantages
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Advantages of Writing UMDF Drivers


This topic describes the advantages of writing a User-Mode Driver Framework (UMDF) driver instead of a kernel-mode driver.

When you write a UMDF driver, you benefit from the following:

-   UMDF drivers contribute to greater operating system stability because they have access only to the address space of the process in which they run.
-   Because UMDF drivers run under the **LocalService** account, they have limited access to a user's data or to system files.
-   User-mode drivers operate in a much simpler environment than kernel-mode drivers. For example, kernel-mode drivers must take into account IRQL, page faults, and thread context. In user mode, however, these issues do not exist. User-mode drivers always run in a different thread from the requesting process and can always take page faults.

-   UMDF version 2 offers feature parity with KMDF in most areas. For a full comparison, see [Comparing UMDF 2 Functionality to KMDF](comparing-umdf-2-0-functionality-to-kmdf.md).
-   UMDF version 2 facilitates converting between KMDF and UMDF. See [How to convert a KMDF driver to a UMDF 2 driver (and vice-versa)](how-to-generate-a-umdf-driver-from-a-kmdf-driver.md).
-   You can debug UMDF drivers by using either a user-mode debugger or, starting with UMDF version 2, a kernel-mode debugger.

-   You can use the Wdfkd.dll debugger extension commands with KMDF and starting with UMDF version 2. For more info, see [Debugger Extensions](debugger-extensions-for-kmdf-drivers.md).

A fundamental goal of the overall WDF model is to provide intelligent defaults, so that you can focus on your device hardware and avoid writing code to perform tasks that are common to most drivers.

To achieve this goal, the framework is designed to work with drivers on an "opt-in" basis. When you write a UMDF driver, you provide callback routines for only the events that affect your device. For example, some devices require intervention immediately after they are turned on and just before they are turned off. The driver for such a device can implement callback functions that the framework calls at those times.

The driver includes code to handle only those events for which its device requires device-specific support. All other events can be handled by framework defaults.

In addition, a driver can configure its I/O request queues so that the framework stops dispatching requests while the device is in a low-power state and resumes dispatching after the device has returned to the operational state. Similarly, if an I/O request arrives while the device is in a low-power state, the framework can automatically turn on the device.

 

 





