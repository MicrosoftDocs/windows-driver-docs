---
title: Bundling the Core Driver with Your Package-Aware Driver
description: Bundling the Core Driver with Your Package-Aware Driver
ms.assetid: 72e29f79-4e71-4aa8-929f-eefdebfe4835
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Bundling the Core Driver with Your Package-Aware Driver


After you [expand](getting-the-updated-core-driver-package.md) the contents of the Microsoft standalone update (MSU) file containing the core driver package, the next step is to bundle the core driver with your package-aware driver.

Change to the directory that contains the files for your package-aware driver and create a subdirectory for the core driver package. These packages are architecture-specific, and if you ship a multi-architecture driver you must include the proper core driver package for each architecture, and assign appropriate names to the subdirectories that contain these core driver packages. Copy the contents of the updated core driver package subdirectory containing the MSU file into the new subdirectory. No other changes are needed. Do not tamper with or change the core driver package, which is digitally signed. The signature will remain valid unless you alter the package contents.

 

 




