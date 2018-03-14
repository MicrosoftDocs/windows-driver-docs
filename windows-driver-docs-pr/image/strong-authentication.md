---
title: Strong Authentication
author: windows-driver-content
description: Strong Authentication
ms.assetid: 75670d86-fb4d-4aa6-87fd-0320cb7c2a34
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 




