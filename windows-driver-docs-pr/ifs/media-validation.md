---
title: Media Validation
description: Media Validation
ms.assetid: 609ac09b-88be-49a6-8b87-9fd453c21446
keywords: ["security WDK file systems , semantic model checks", "semantic model checks WDK file systems , media validation", "media validation WDK file systems", "disk of death attacks WDK file systems", "validating media WDK file systems", "removable media validation WDK file systems"]
---

# Media Validation


## <span id="ddk_media_validation_if"></span><span id="DDK_MEDIA_VALIDATION_IF"></span>


A major concern when developing a file system that supports removable media (FASTFAT, for example) is guarding against the "disk of death" attack. When implementing a file system, the driver must guard against maliciously malformed structures since anyone can insert a removable disk (CD-ROM, DVD-ROM, or USB flash memory disk, for example) into the system.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Media%20Validation%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




