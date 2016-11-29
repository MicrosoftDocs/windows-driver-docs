---
title: Operating System Model
description: Operating System Model
ms.assetid: a7200472-24e1-4ecf-86c7-a1b72c5661fc
keywords: ["Static Driver Verifier WDK , operating system model", "StaticDV WDK , operating system model", "SDV WDK , operating system model", "operating system model WDK Static Driver Verifier", "harness WDK Static Driver Verifier"]
---

# Operating System Model


An SDV *operating system model* or *harness* consists of partial and abstracted segments of Windows code that act as the operating system during a verification. SDV includes a default operating system model and several specialized models that are used to verify particular [rules](static-driver-verifier-rule.md). SDV assembles the operating system model for a verification during the **Check** step of the [verification process](verification-process.md).

There is also a harness that executes parts of your driver in the same manner as the Windows Operating System by calling into entry points in the driver.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Operating%20System%20Model%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




