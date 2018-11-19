---
title: Creating a 'Hello World' WIA Minidriver
description: Creating a 'Hello World' WIA Minidriver
ms.assetid: 074da2ff-bc60-48a9-b2ff-83f070bd5351
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating a 'Hello World' WIA Minidriver





This WIA minidriver is a simple DLL that exports two functions and implements three COM interfaces. The following code example can be compiled into a working WIA minidriver. The item tree that this WIA minidriver creates has only a root item and cannot transfer data, but it shows the basics needed to get a WIA driver loaded and running.

The following files are used to create the "Hello World" WIA Minidriver:

*hellowld.def* − the ['Hello World' Definition File](--hello-world---definition-file.md).

*hellowld.inf* − the ['Hello World' Installation File](--hello-world---installation-file.md).

*hellowld.cpp* − the ['Hello World' Implementation File](--hello-world---implementation-file.md).

For information about how to add a custom UI to a minidriver, see, [Creating a "Hello World" WIA Minidriver UI Extension](creating-a--hello-world--wia-minidriver-ui-extension.md).

 

 




