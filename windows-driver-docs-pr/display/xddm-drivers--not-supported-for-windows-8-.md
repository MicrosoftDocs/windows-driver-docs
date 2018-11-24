---
title: XDDM drivers not supported for Windows 8
description: XDDM drivers are not supported for Windows 8 and will not install or run on Windows 8.
ms.assetid: 2D527787-55AF-4D44-BBA2-8052FB594902
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# XDDM drivers not supported for Windows 8


XDDM drivers are not supported for Windows 8 and will not install or run on Windows 8.

If the graphics hardware is not supported by a Windows 8 in-box graphics driver, Windows 8 will run the MSBDD until a Windows 8 compatible driver is installed from Windows Update or an OEM/IHV site.

**Note**  
The vendor can develop a Windows 8-compatible display-only driver for the hardware if it is a server product.

 

T*able 1 Driver Upgrade Experience in Windows 8* summarizes graphics driver migration behavior during a Windows 8 upgrade and clean installations. In this table, *ITB* = in-box, and *OTB* = out-of-the-box; this is an OEM or IHV retail driver package or Windows Update package.

**Table 1 Driver Upgrade Experience in Windows 8**

| Driver used in Windows 7                                       | Scenario | Windows 8 in-box coverage | Resulting initial driver in Windows 8 |
|----------------------------------------------------------------|----------|---------------------------|---------------------------------------|
| Win7 OTB Driver / Win7 ITB Driver / No Driver / XDDM Driver    | Upgrade  | ITB Driver Support        | Win8 ITB Driver                       |
| Win7 OTB Driver                                                | Upgrade  | No ITB Driver Support     | Win7 OTB Driver                       |
| Win7 ITB Driver / No Driver / Blocked OTB Driver / XDDM Driver | Upgrade  | No ITB Driver Support     | Win8 MSBDD                            |
| N/A                                                            | Clean    | ITB Driver Support        | Win8 ITB Driver                       |
| N/A                                                            | Clean    | No ITB Driver Support     | Win8 MSBDD                            |

 

In cases where the Windows 7 graphics driver itself is not migrated, any IHV or OEM value-add components from the Windows 7 graphics driver package, such as control panels and OpenGL support libraries, can persist after a Windows 8 upgrade installation. This happens because the Windows 8 installer cannot know that these value-add components are associated with the Windows 7 retail or OEM driver package. These value-add components might not function properly in the absence of the rest of their driver package.

IHVs should harden these value-add components to simply exit in such cases. In the rare cases where the value-add causes problems, the specific value-add components can be blocked from migrating by the Microsoft compatibility team. In some cases, an IHV's Windows 8 in-box driver removes the value-add component on upgrade. This is up to the IHV.

Some retail and OEM Windows 7 graphics drivers are intentionally structured to prevent their installation on Windows 8. Windows 8 might try to migrate such a driver according to the rules above, but it would fail to install on Windows 8, resulting in the use of the MSBDD.

An IHV can create a unified driver package that is a WDDM 1.2 driver on Windows 8, but that appears like a WDDM 1.1 or 1.0 driver on previous Windows releases.

 

 





