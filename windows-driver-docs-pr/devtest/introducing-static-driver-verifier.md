---
title: Introducing Static Driver Verifier
description: Introducing Static Driver Verifier
ms.assetid: fa6e8b0f-0d0f-4293-87ec-e67decd6acb7
keywords: ["Static Driver Verifier WDK , about Static Driver Verifier", "StaticDV WDK , about Static Driver Verifier", "SDV WDK , about Static Driver Verifier"]
---

# Introducing Static Driver Verifier


Static Driver Verifier (SDV) is a static verification tool that runs at compile time. It explores paths in the driver code by symbolically executing the source code, making the fewest possible assumptions about the state of the operating system and the initial state of the driver. As a result, SDV can exercise code in paths that are missed in traditional testing.

SDV includes a set of rules that define proper interaction between a driver and the operating system kernel. During verification, SDV examines every applicable branch of the driver code and the library code that it uses, and tries to prove that the driver violates the rules. If SDV fails to prove a violation, it reports that the driver complies with the rules and passes the verification.

This section includes:

[Understanding Static Driver Verifier](understanding-static-driver-verifier.md)

[Static Driver Verifier Concepts](static-driver-verifier-concepts.md)

[Supported Drivers](supported-drivers.md)

[Static Driver Verifier Limitations](static-driver-verifier-limitations.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Introducing%20Static%20Driver%20Verifier%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




