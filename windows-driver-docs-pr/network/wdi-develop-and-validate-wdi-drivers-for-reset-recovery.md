---
title: Develop and validate WDI drivers for Reset Recovery
description: The UE has a built-in hook for stressing reset and recovery by simulating firmware hangs.
ms.assetid: 5C669F22-2C82-4072-8010-1DDC918C064F
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Develop and validate WDI drivers for Reset Recovery


The UE has a built-in hook for stressing reset and recovery by simulating firmware hangs. It exercises the UE and LE but not the actual firmware, which likely remains functional in the simulation. The code is in M1 UE. It is ideal if the IHV has mechanisms to inject firmware hangs. This exercises Reset Recovery on modules below the LE, specifically Bus, ACPI, and UEFI. There have been hard-to-debug issues in these lower layers regarding to Reset Recovery where the lower layer failed to actually reset the firmware.

 

 





