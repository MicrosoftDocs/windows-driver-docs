---
title: Storage Requirements for ControllerControl Routines
description: Storage Requirements for ControllerControl Routines
ms.assetid: 1ee69144-5f52-4d61-ad30-02e8fbe1f91e
keywords: ["controller objects WDK kernel , writing ControllerControl routines", "ControllerControl routines, writing", "ControllerControl routines, storage", "storage WDK controller objects"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Storage Requirements for ControllerControl Routines





If it has a *ControllerControl* routine, a non-WDM driver must provide resident storage for a *ControllerObject* pointer returned by [**IoCreateController**](https://msdn.microsoft.com/library/windows/hardware/ff548395).

A driver can provide the necessary storage in a device extension or in nonpaged pool allocated by the driver. Usually, drivers that use controller objects store the *ControllerObject* pointer in the device extension of each device object that represents a physical or logical device controlled by the hardware represented by the controller object.

The driver writer determines the size and internal structure of the *ControllerObject*-&gt;**ControllerExtension**.

A controller object, which cannot be given a name, cannot be the target of an I/O request. The hardware it represents usually controls a set of homogeneous devices that are the actual targets of I/O requests.

 

 




