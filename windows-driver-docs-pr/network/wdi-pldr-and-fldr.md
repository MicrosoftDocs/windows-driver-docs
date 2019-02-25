---
title: WDI PLDR Recovery
description: This section describes recovery of PLDR for WDI drivers
ms.assetid: 53C96AB8-721C-4EB9-80E4-9F841B76D4D2
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# PLDR


## Recovery of PLDR


After the surprise-remove, the drivers (both UE and LE) must release all resources so that the device object can be removed and re-enumerated (by the bus). If this does not happen, the device is not re-enumerated, and therefore not recovered.

 

 





