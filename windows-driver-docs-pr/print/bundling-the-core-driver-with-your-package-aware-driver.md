---
title: Bundling the Core Driver with Your Package-Aware Driver
author: windows-driver-content
description: Bundling the Core Driver with Your Package-Aware Driver
ms.assetid: 72e29f79-4e71-4aa8-929f-eefdebfe4835
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Bundling the Core Driver with Your Package-Aware Driver


After you [expand](getting-the-updated-core-driver-package.md) the contents of the Microsoft standalone update (MSU) file containing the core driver package, the next step is to bundle the core driver with your package-aware driver.

Change to the directory that contains the files for your package-aware driver and create a subdirectory for the core driver package. These packages are architecture-specific, and if you ship a multi-architecture driver you must include the proper core driver package for each architecture, and assign appropriate names to the subdirectories that contain these core driver packages. Copy the contents of the updated core driver package subdirectory containing the MSU file into the new subdirectory. No other changes are needed. Do not tamper with or change the core driver package, which is digitally signed. The signature will remain valid unless you alter the package contents.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Bundling%20the%20Core%20Driver%20with%20Your%20Package-Aware%20Driver%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


