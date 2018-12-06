---
title: Sdv-map.h
description: Sdv-map.h
ms.assetid: c230fb86-fe65-416b-bd3e-a0ab7270576d
keywords:
- output files WDK Static Driver Verifier
- Sdv-map.h WDK Static Driver Verifier
- header files WDK Static Driver Verifier
- driver entry points WDK Static Driver Verifier
- entry points WDK Static Driver Verifier
- Sdv-map.h WDK Static Driver Verifier , about Sdv-map.h
- scanning DriverEntry routine WDK Static Driver Verifier
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Sdv-map.h


Sdv-map.h is a header file that lists the driver entry points that SDV detected in the driver.

SDV creates an Sdv-map.h file in the driver's sources directory when you use a **staticdv /scan** command to scan the driver's source code. SDV uses the function role type declarations to identify the entry points. If you do not use a **staticdv /scan** command, SDV creates an Sdv-map.h file when you use a **staticdv /check** command to run an SDV analysis.

If this file is inaccurate or incomplete, you can correct it, approve it, and then rescan and rerun the verification.

This section includes:

[Understanding Sdv-map.h](understanding-the-sdv-map-h-file.md)

[Sdv-map.h Format](format-of-the-sdv-map-h-file.md)

[Approving Sdv-map.h](approving-the-sdv-map-h-file.md)

[Duplicate Entry Points for a Function Role Type](duplicate-entry-points-for-a-function-role-type.md)

 

 





