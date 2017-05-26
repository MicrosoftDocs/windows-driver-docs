---
title: WDDM 1.2 driver enforcement
description: Validation by the Microsoft DirectX graphics kernel subsystem (Dxgkrnl) is enforced starting with Windows 8 to determine whether the mandatory Windows Display Driver Model (WDDM) 1.2 features are supported by the WDDM 1.2 driver.
ms.assetid: DF0C6F50-CC68-4002-9ED3-F42EA24D24B1
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WDDM 1.2 driver enforcement


Validation by the Microsoft DirectX graphics kernel subsystem (Dxgkrnl) is enforced starting with Windows 8 to determine whether the mandatory Windows Display Driver Model (WDDM) 1.2 features are supported by the WDDM 1.2 driver.

WDDM 1.2 has both mandatory and optional features. The driver must set all the mandatory feature caps to claim itself as a WDDM 1.2 driver, while the driver can implement any combination (or none) of the optional features. A non-WDDM 1.2 driver must report none of the WDDM 1.2 features.

## <span id="User_experience_when_a_driver_fails_the_Dxgkrnl_validation"></span><span id="user_experience_when_a_driver_fails_the_dxgkrnl_validation"></span><span id="USER_EXPERIENCE_WHEN_A_DRIVER_FAILS_THE_DXGKRNL_VALIDATION"></span>User experience when a driver fails the Dxgkrnl validation


If a driver has wrongly claimed itself as WDDM 1.2 or has implemented only some of the mandatory features, then it will fail to create an adapter, and the system will fall back to the Microsoft Basic Display Driver (MSBDD).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20WDDM%201.2%20driver%20enforcement%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




