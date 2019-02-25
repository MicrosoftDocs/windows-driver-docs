---
title: WDDM 1.2 driver enforcement
description: Validation by the Microsoft DirectX graphics kernel subsystem (Dxgkrnl) is enforced starting with Windows 8 to determine whether the mandatory Windows Display Driver Model (WDDM) 1.2 features are supported by the WDDM 1.2 driver.
ms.assetid: DF0C6F50-CC68-4002-9ED3-F42EA24D24B1
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WDDM 1.2 driver enforcement


Validation by the Microsoft DirectX graphics kernel subsystem (Dxgkrnl) is enforced starting with Windows 8 to determine whether the mandatory Windows Display Driver Model (WDDM) 1.2 features are supported by the WDDM 1.2 driver.

WDDM 1.2 has both mandatory and optional features. The driver must set all the mandatory feature caps to claim itself as a WDDM 1.2 driver, while the driver can implement any combination (or none) of the optional features. A non-WDDM 1.2 driver must report none of the WDDM 1.2 features.

## <span id="User_experience_when_a_driver_fails_the_Dxgkrnl_validation"></span><span id="user_experience_when_a_driver_fails_the_dxgkrnl_validation"></span><span id="USER_EXPERIENCE_WHEN_A_DRIVER_FAILS_THE_DXGKRNL_VALIDATION"></span>User experience when a driver fails the Dxgkrnl validation


If a driver has wrongly claimed itself as WDDM 1.2 or has implemented only some of the mandatory features, then it will fail to create an adapter, and the system will fall back to the Microsoft Basic Display Driver (MSBDD).

 

 





