---
title: Determining the Cause of a Video Stream Stall
description: Determining the Cause of a Video Stream Stall
ms.assetid: 959c2295-1ec3-48b0-aed9-93a81378372f
keywords: ["kernel streaming debugging, video stream stall, cause"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

2.  Determine whether samples are flowing downstream. If you can reproduce the bug in [GraphEdit](http://go.microsoft.com/fwlink/p/?linkid=9230), place an intermediate filter in the graph to display samples.

3.  Determine if the processing routine is being called. This can be done by attaching a kernel-mode debugger and setting a breakpoint in this routine.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Determining%20the%20Cause%20of%20a%20Video%20Stream%20Stall%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




