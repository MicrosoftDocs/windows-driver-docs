---
title: No Entry Points Found
description: No Entry Points Found
ms.assetid: bb355c8a-66a9-4cb5-aea5-906111710a91
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# No Entry Points Found


SDV reports this error when it cannot find or cannot interpret the driver entry points or interpret the callback function role type annotations. As a result, it cannot proceed past the scan step. For information, see [Scanning the Driver](scanning-the-driver.md) or [Using Function Role Type Declarations](using-function-role-type-declarations.md).

**Important**   You must add function role type annotations to your driver's callback function declarations. See [Using Function Role Type Declarations](using-function-role-type-declarations.md) and then repeat the scan step, so that SDV creates the Sdv-map.h file in your driver's sources directory. For more information, see [Scanning the Driver](scanning-the-driver.md).

 

 

 





