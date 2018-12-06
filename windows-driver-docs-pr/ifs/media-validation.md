---
title: Media Validation
description: Media Validation
ms.assetid: 609ac09b-88be-49a6-8b87-9fd453c21446
keywords:
- security WDK file systems , semantic model checks
- semantic model checks WDK file systems , media validation
- media validation WDK file systems
- disk of death attacks WDK file systems
- validating media WDK file systems
- removable media validation WDK file systems
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Media Validation


## <span id="ddk_media_validation_if"></span><span id="DDK_MEDIA_VALIDATION_IF"></span>


A major concern when developing a file system that supports removable media (FASTFAT, for example) is guarding against the "disk of death" attack. When implementing a file system, the driver must guard against maliciously malformed structures since anyone can insert a removable disk (CD-ROM, DVD-ROM, or USB flash memory disk, for example) into the system.

 

 




