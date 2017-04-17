---
title: Strong Authentication
author: windows-driver-content
description: Strong Authentication
ms.assetid: 75670d86-fb4d-4aa6-87fd-0320cb7c2a34
---

# Strong Authentication


To add support for strong authentication utilizing smart cards you should develop a strategy that includes support for:

Smart card reader driver support (for more information about USB based devices, see [Approved Class Specification Documents](http://go.microsoft.com/fwlink/p/?linkid=516989))

Smart card device driver support

Smart card resource management and associated APIs

Windows natively provides these elements, which simplifies the addition of Smart card support. For devices being built on other platforms you have several choices:

If available, utilize the development platform native support for smart cards.

Develop solution-specific support for smart cards in-house.

Utilize open source implementations that aid integration of smart cards into your solution.

Work with a third-party that provides a commercial cross-platform smart card platform that can be integrated with your solution.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Strong%20Authentication%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


