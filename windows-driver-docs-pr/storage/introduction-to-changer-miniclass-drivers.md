---
title: Introduction to Changer Miniclass Drivers
description: Introduction to Changer Miniclass Drivers
ms.assetid: ce0f78a3-69ae-4ca7-b2e1-f4892e35a230
keywords: ["changer drivers WDK storage , miniclass drivers", "storage changer drivers WDK , miniclass drivers", "miniclass drivers WDK changer"]
---

# Introduction to Changer Miniclass Drivers


## <span id="ddk_introduction_to_changer_miniclass_drivers_kg"></span><span id="DDK_INTRODUCTION_TO_CHANGER_MINICLASS_DRIVERS_KG"></span>


To support a new changer, a driver writer implements a changer miniclass driver that links to the system-supplied changer class driver. A new changer miniclass driver must be written only to support a changer for which the system does not already provide a driver.

Before starting to implement a new miniclass driver, you should ensure that:

-   The device is a true changer and not a serial access stacker. A changer permits media to be mounted in its drives in random order, rather than a fixed sequence, as in a stacker.

-   The device's drives are not write-once optical drives such as WORM, CD-R, or DVD-R.

-   The device's drives are all the same type, not a mix of types such as CD-ROM and CD-R.

Microsoft operating systems do not support write-once optical drives or changers with more than one type of drive.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Introduction%20to%20Changer%20Miniclass%20Drivers%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




