---
title: Determining Why an Application Request Does Not Complete
description: This topic describes how you can use the Wudfext.dll debugger extensions in conjunction with a User-Mode Driver Framework (UMDF) version 1 or 2 driver to determine why an application request does not complete.
keywords:
- UMDF WDK , application request not completing
- debugging scenarios WDK UMDF , application request not completing
- UMDF WDK , debugging scenarios, application request not completing
ms.date: 04/20/2017
---

# Determining Why an Application Request Does Not Complete


This topic describes how you can use the Wudfext.dll debugger extensions in conjunction with a User-Mode Driver Framework (UMDF) version 1 or 2 driver to determine why an application request does not complete.

For UMDF version 1, you'll use extension commands implemented in wudfext.dll. Starting in UMDF version 2, you'll use extension commands implemented in wdfkd.dll.

You can perform the following steps to determine why an application request does not complete:

1.  Use [**!wudfext.umirps**](../debuggercmds/-wudfext-umirps.md) (UMDF 1) or [**!wdfkd.wdfumirps**](../debuggercmds/-wdfkd-wdfumirps.md) (UMDF 2) to display all the outstanding user-mode I/O request packets (IRPs) in the host process. The information for each user-mode IRP includes the original kernel-mode IRP for which the user-mode IRP was created.

    Determine the user-mode IRP that corresponds to the kernel-mode IRP that the application originated.

2.  Use [**!wudfext.umirp**](../debuggercmds/-wudfext-umirp.md) (UMDF 1) or [**!wdfkd.wdfumirp**](../debuggercmds/-wdfkd-wdfumirp.md) (UMDF 2) to obtain information about a particular user-mode IRP.

    The information for the user-mode IRP includes the stack locations. If you know the stack locations, you can determine where the IRP is being processed. Stack location 0 represents the stack below UMDF (that is, the kernel-mode stack or some other sub-system, such as Microsoft Win32 or Winsock).

3.  If the IRP is at your driver's layer (that is, the layer in which your driver processes the IRP), perform the following steps:
    1.  View the I/O queues that are set up at your driver's layer. You can use [**!wudfext.wudfdevicequeues**](../debuggercmds/-wudfext-wudfdevicequeues.md) (UMDF 1) or [**!wdfkd.wdfdevicequeues**](../debuggercmds/-wdfkd-wdfdevicequeues.md) (UMDF 2) to view all the I/O queues that are set up at your driver's layer. You can also use [**!wudfext.wudfqueue**](../debuggercmds/-wudfext-wudfqueue.md) (UMDF 1) or [**!wdfkd.wdfqueue**](../debuggercmds/-wdfkd-wdfqueue.md) (UMDF 2) to obtain information about a particular queue.

    2.  If there are multiple requests outstanding, you can use [**!wudfext.wudfrequest**](../debuggercmds/-wudfext-wudfrequest.md) (UMDF 1) or [**!wdfkd.wdfrequest**](../debuggercmds/-wdfkd-wdfrequest.md) (UMDF 2) to obtain information about a request, which includes the underlying user-mode IRP. From the user-mode IRP information, you can determine the request that you are interested in.
    3.  Verify whether the request is owned by a queue or by the driver. This information is displayed as part of the output from [**!wudfext.wudfqueue**](../debuggercmds/-wudfext-wudfqueue.md) or [**!wdfkd.wdfqueue**](../debuggercmds/-wdfkd-wdfqueue.md). Perform one of the following verifications depending on whether the queue or the driver owns the request:
        -   If the request is owned by the queue, check the state of the queue to determine why the queue did not deliver the request to the driver.
        -   If the request is owned by the driver, check the threads in the host process to determine if a thread became stuck or deadlocked while processing the request.

4.  If the IRP is at another UMDF driver layer, you can repeat the preceding steps for that layer. Remember that you can use [**!wudfext.umdevstack**](../debuggercmds/-wudfext-umdevstack.md) (UMDF 1) or [**!wdfkd.wdfumdevstack**](../debuggercmds/-wdfkd-wdfumdevstack.md) (UMDF 2) to view information about all stack layers.

5.  If the IRP is beyond the UMDF stack (for example, if stack location 0 is where the IRP is currently being processed), determine why the corresponding kernel-mode IRP did not complete.

 

