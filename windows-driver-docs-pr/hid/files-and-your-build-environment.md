---
title: Files and Your Build Environment
description: Files and Your Build Environment
ms.assetid: 0c85a599-65bb-45e5-a2f8-eefd47e82025
keywords: ["property sheets WDK DirectInput , files", "game controllers WDK DirectInput , files", "control panels WDK DirectInput , files", "property sheets WDK DirectInput , build environments", "game controllers WDK DirectInput , build environments", "control panels WDK DirectInput , build environments", "build environments WDK DirectInput", "files WDK DirectInput"]
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Files and Your Build Environment





At a minimum, you will need the Direct X Direct Development Kit (DDK) header file Dicpl.h. This file provides you with the necessary interface, structures, class definitions, and errors. It is recommended that you use DirectInput's **IDirectInputJoyConfig8** interface for all registry access to assure that your property sheet also works on Windows NT 4.0 and later. If you plan to use DirectInput in your property page, you must also used the associated DirectX SDK files. All structures in the DirectInput control panel are packed on 8-byte boundaries. Verify that your property sheet packs structures on 8-byte boundaries.

**Note**   When testing your control panel, make sure to test it on a system whose primary display is set to a resolution of 640 x 480 pixels. Make sure that all the controls are still visible at this reduced resolution.

 

 

 




