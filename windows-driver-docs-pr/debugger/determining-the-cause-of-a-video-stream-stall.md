---
title: Determining the Cause of a Video Stream Stall
description: Determining the Cause of a Video Stream Stall
ms.assetid: 959c2295-1ec3-48b0-aed9-93a81378372f
keywords: ["kernel streaming debugging, video stream stall, cause"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Determining the Cause of a Video Stream Stall


There are two basic causes for a video stream stall:

-   **A hang.** Either a user-mode thread or a kernel-mode thread is not being released by the driver.

-   **A stall.** This is the result of a problem with a component in the streaming path. Some possibilities include:
    -   The capture driver is not completing packets. In this case, either a driver component or the hardware might be the source of the stall.
    -   The capture driver has no packets to complete. In this case, the buffers might be stalled in a codec or other downstream component.

If you can reproduce the problem, attach a debugger at this point to determine which is the actual cause.

**To determine if the problem is a hang**

1.  Attach a user-mode debugger to the application and look for blocked user-mode threads.

2.  Determine whether the application is responsive. Can the graph be paused? Can the graph be stopped? Does streaming restart if the graph is stopped and restarted?

3.  If the application is non-responsive, attempt to end the task by using Task Manager. If this fails, there is a kernel-mode hang.

**To determine if the problem is a stall**

1.  Determine where the samples are in the graph. This can be done locally or in a kernel-mode debugging session.

2.  Determine whether samples are flowing downstream. If you can reproduce the bug in [GraphEdit](https://go.microsoft.com/fwlink/p/?linkid=9230), place an intermediate filter in the graph to display samples.

3.  Determine if the processing routine is being called. This can be done by attaching a kernel-mode debugger and setting a breakpoint in this routine.

 

 





