---
title: Creating a 'Hello World' WIA Minidriver
author: windows-driver-content
description: Creating a 'Hello World' WIA Minidriver
MS-HAID:
- 'WIA\_db\_hello\_4ec19070-996b-4c7b-82c9-45857d104ca3.xml'
- 'image.creating\_a\_\_\_hello\_world\_\_\_wia\_minidriver'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 074da2ff-bc60-48a9-b2ff-83f070bd5351
---

# Creating a 'Hello World' WIA Minidriver


## <a href="" id="ddk-creating-a-hello-world-wia-minidriver-si"></a>


This WIA minidriver is a simple DLL that exports two functions and implements three COM interfaces. The following code example can be compiled into a working WIA minidriver. The item tree that this WIA minidriver creates has only a root item and cannot transfer data, but it shows the basics needed to get a WIA driver loaded and running.

The following files are used to create the "Hello World" WIA Minidriver:

*hellowld.def* − the ['Hello World' Definition File](--hello-world---definition-file.md).

*hellowld.inf* − the ['Hello World' Installation File](--hello-world---installation-file.md).

*hellowld.cpp* − the ['Hello World' Implementation File](--hello-world---implementation-file.md).

For information about how to add a custom UI to a minidriver, see, [Creating a "Hello World" WIA Minidriver UI Extension](creating-a--hello-world--wia-minidriver-ui-extension.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Creating%20a%20'Hello%20World'%20WIA%20Minidriver%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


