---
title: Selecting Source Files
description: Selecting Source Files
ms.assetid: 259a7092-1197-4521-853a-6064aaa0c037
keywords: ["INF files WDK joysticks , source files"]
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Selecting Source Files





The "SourceDisksFiles" section of the INF file specifies which files to copy. This includes all necessary drivers, as well as any other files, such as documentation and setup applications. As this may be the first joystick driver to be installed on a user's system, the system joystick drivers Vjoyd.vxd and Msjstrick.drv should be copied, in addition to the specific drivers for this device. The source of these two drivers should be established by reference to Layout.inf (causing the user to be prompted for the Windows 95/98/Me installation disc) and not distributed on the OEM disc. The drivers should be copied to the user's system directory, which is destination code 11.

 

 




