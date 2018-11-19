---
title: COM Interface Design Skills
description: COM Interface Design Skills
ms.assetid: 3a3adbc2-af6f-4495-8993-fd25d56ffad6
keywords:
- Windows Device Testing Framework WDK , action interfaces
- WDTF WDK , action interfaces
- action interfaces WDK WDTF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# COM Interface Design Skills


When you create a new action interface, you should design your object model with the following features in mind:

1.  **Intuitive**. Express manual testing in words.

2.  **Easy to learn and use.** Make it easy enough to use so that manual testers can write the top-level scenario scripts. These testers have valuable insight into how to break applications, so let them solidify that knowledge into an automated [scenario script](creating-wdtf-scenarios.md).

3.  **Object-oriented**. Make your interface object-oriented, to increase productivity. Fortunately, the [WDTF scenario model](extending-the-framework.md) makes it hard to break this rule.

4.  **Robust**. Action interfaces are meant for reusability, so try to prepare for more than just the simple use cases.

5.  **Diagnosable**. Make sure you include diagnosability in your design. Try to think about how people can debug problems when they use your interface. It helps to instrument your code with [WPP Software Tracing](https://msdn.microsoft.com/library/windows/hardware/ff556204).

 

 




