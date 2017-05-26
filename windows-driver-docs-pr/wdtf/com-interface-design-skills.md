---
title: COM Interface Design Skills
author: windows-driver-content
description: COM Interface Design Skills
ms.assetid: 3a3adbc2-af6f-4495-8993-fd25d56ffad6
keywords:
- Windows Device Testing Framework WDK , action interfaces
- WDTF WDK , action interfaces
- action interfaces WDK WDTF
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# COM Interface Design Skills


When you create a new action interface, you should design your object model with the following features in mind:

1.  **Intuitive**. Express manual testing in words.

2.  **Easy to learn and use.** Make it easy enough to use so that manual testers can write the top-level scenario scripts. These testers have valuable insight into how to break applications, so let them solidify that knowledge into an automated [scenario script](creating-wdtf-scenarios.md).

3.  **Object-oriented**. Make your interface object-oriented, to increase productivity. Fortunately, the [WDTF scenario model](extending-the-framework.md) makes it hard to break this rule.

4.  **Robust**. Action interfaces are meant for reusability, so try to prepare for more than just the simple use cases.

5.  **Diagnosable**. Make sure you include diagnosability in your design. Try to think about how people can debug problems when they use your interface. It helps to instrument your code with [WPP Software Tracing](https://msdn.microsoft.com/library/windows/hardware/ff556204).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdtf\dtf%5D:%20COM%20Interface%20Design%20Skills%20%20RELEASE:%20%289/13/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


