---
title: Removing a Device in a Filter Driver
author: windows-driver-content
description: Removing a Device in a Filter Driver
ms.assetid: f1166240-446d-4f37-871b-baf687e25735
keywords: ["filter drivers WDK PnP"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# Removing a Device in a Filter Driver





When removing a device, a filter driver must undo any operations it performed to add and start the device. A filter driver follows essentially the same procedure as a function driver when removing a device.

 

 




