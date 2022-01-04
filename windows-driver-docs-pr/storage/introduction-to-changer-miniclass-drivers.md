---
title: About Changer Miniclass Drivers
description: About Changer Miniclass Drivers
keywords:
- changer drivers WDK storage , miniclass drivers
- storage changer drivers WDK , miniclass drivers
- miniclass drivers WDK changer
ms.date: 12/15/2019
---

# About Changer Miniclass Drivers

To support a new changer, a driver writer implements a changer miniclass driver that links to the system-supplied changer class driver. A new changer miniclass driver must be written only to support a changer for which the system does not already provide a driver.

Before starting to implement a new miniclass driver, you should ensure that:

- The device is a true changer and not a serial access stacker. A changer permits media to be mounted in its drives in random order, rather than a fixed sequence, as in a stacker.

- The device's drives are not write-once optical drives such as WORM, CD-R, or DVD-R.

- The device's drives are all the same type, not a mix of types such as CD-ROM and CD-R.

Microsoft operating systems do not support write-once optical drives or changers with more than one type of drive.
