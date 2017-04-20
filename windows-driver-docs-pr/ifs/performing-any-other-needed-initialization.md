---
title: Performing Any Other Needed Initialization
author: windows-driver-content
description: Performing Any Other Needed Initialization
ms.assetid: 781f241f-fb12-460e-b093-ffa916aae495
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Performing Any Other Needed Initialization


## <span id="ddk_performing_any_other_needed_initialization_if"></span><span id="DDK_PERFORMING_ANY_OTHER_NEEDED_INITIALIZATION_IF"></span>


After registering IRP and fast I/O dispatch routines, your file system filter driver's **DriverEntry** routine can initialize additional global driver variables and data structures as needed.

 

 


--------------------


