---
title: Understanding Static Driver Verifier
description: Understanding Static Driver Verifier
ms.assetid: 519e3314-2fea-4acd-8c0d-954a57e257ba
keywords:
- Static Driver Verifier WDK , about Static Driver Verifier
- StaticDV WDK , about Static Driver Verifier
- SDV WDK , about Static Driver Verifier
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Understanding Static Driver Verifier


To write a robust driver that complies with the Windows Driver Model (WDM) or the Kernel Mode Driver Framework (KMDF), NDIS, or Storport, you must have expertise and understand how the driver interacts with the I/O manager. Testing these drivers is equally tricky.

Developing solid drivers can be challenging for the following reasons:

-   Drivers are asynchronous, even on single-processor machines.

-   Drivers are massively reentrant.

-   Drivers use many obscure rules.

-   Driver models are evolutionary and age over time.

Testing device drivers is limited by the following reasons:

-   *Observation*. You cannot observe an error in the interaction between the driver and the operating system. Drivers can violate implicit usage rules, resulting in a crash or improper behavior, but it is difficult to detect the root cause of an error when developing and testing drivers.

-   *Control*. Drivers that work correctly under normal circumstances can have subtle errors that occur only in exceptional situations, such as when a driver below it in the stack fails an IRP. Such situations are hard to exercise, so traditional testing does not adequately detect the error paths through the driver code.

SDV enhances both the observation and control that you have when you test drivers. By defining rules for the proper use of WDM, KMDF, NDIS, and Storport functions and monitoring the driver's compliance with those rules, SDV improves your ability to observe errors. For example, the WDM rule [LowerDriverReturn](https://msdn.microsoft.com/library/windows/hardware/ff548273) specifies that, under certain circumstances, a driver's dispatch routine should always return the value that was returned by the lower driver in the stack.

SDV also increases control by providing:

-   A hostile model of the driver's environment, where several worst-case scenarios (such as operating system calls continually failing) can happen.

-   Powerful static analysis (called *model checking*) that systematically explores all possible execution paths in the driver.

SDV is an essential unit-testing tool for device drivers. It places a driver in a hostile environment and systematically tests code paths through the driver by looking for violations of driver model usage rules.

 

 





