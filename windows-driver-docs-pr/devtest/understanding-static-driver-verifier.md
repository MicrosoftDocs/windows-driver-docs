---
title: Understanding Static Driver Verifier
description: Understanding Static Driver Verifier
ms.assetid: 519e3314-2fea-4acd-8c0d-954a57e257ba
keywords: ["Static Driver Verifier WDK , about Static Driver Verifier", "StaticDV WDK , about Static Driver Verifier", "SDV WDK , about Static Driver Verifier"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Understanding%20Static%20Driver%20Verifier%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




