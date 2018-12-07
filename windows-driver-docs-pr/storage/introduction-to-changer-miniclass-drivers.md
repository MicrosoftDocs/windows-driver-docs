---
title: Introduction to Changer Miniclass Drivers
description: Introduction to Changer Miniclass Drivers
ms.assetid: ce0f78a3-69ae-4ca7-b2e1-f4892e35a230
keywords:
- changer drivers WDK storage , miniclass drivers
- storage changer drivers WDK , miniclass drivers
- miniclass drivers WDK changer
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Introduction to Changer Miniclass Drivers


## <span id="ddk_introduction_to_changer_miniclass_drivers_kg"></span><span id="DDK_INTRODUCTION_TO_CHANGER_MINICLASS_DRIVERS_KG"></span>


To support a new changer, a driver writer implements a changer miniclass driver that links to the system-supplied changer class driver. A new changer miniclass driver must be written only to support a changer for which the system does not already provide a driver.

Before starting to implement a new miniclass driver, you should ensure that:

-   The device is a true changer and not a serial access stacker. A changer permits media to be mounted in its drives in random order, rather than a fixed sequence, as in a stacker.

-   The device's drives are not write-once optical drives such as WORM, CD-R, or DVD-R.

-   The device's drives are all the same type, not a mix of types such as CD-ROM and CD-R.

Microsoft operating systems do not support write-once optical drives or changers with more than one type of drive.

 

 




