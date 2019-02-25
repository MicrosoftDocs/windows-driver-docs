---
title: Gcdef.dll, the Default Analog Device Property Sheet
description: Gcdef.dll, the Default Analog Device Property Sheet
ms.assetid: a8226abb-11c1-4425-93d8-b74e1960ba10
keywords: ["Gcdef.dll", "default analog device property sheet", "property sheets WDK DirectInput , Gcdef.dll", "game controllers WDK DirectInput , Gcdef.dll", "control panels WDK DirectInput , Gcdef.dll"]
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Gcdef.dll, the Default Analog Device Property Sheet





Hardware vendors who do not create their own control panel use the services of the default analog device property sheet supplied by Gcdef.dll. Any controller that does not have a **ConfigCLSID** key in the registry under its **HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Control\\MediaProperties\\PrivateProperties\\Joystick\\OEM\\**<em>CONTROLLER\_NAME</em> entry uses this default property sheet. This property sheet contains the following two pages:

-   **Test:** This page demonstrates that the device is responding properly. It returns a graphical representation of the registry settings that are associated with the device attributes and allows the user to view them.

-   **Settings:** This page allows the user to write specific information about the device to the system. Services are provided for calibration and for a rudder or pedals.

 

 




