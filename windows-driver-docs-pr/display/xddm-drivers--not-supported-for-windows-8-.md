---
title: XDDM drivers not supported for Windows 8
description: XDDM drivers are not supported for Windows 8 and will not install or run on Windows 8.
ms.assetid: 2D527787-55AF-4D44-BBA2-8052FB594902
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

IHVs should harden these value-add components to simply exit in such cases. In the rare cases where the value-add causes problems, the specific value-add components can be blocked from migrating by the Microsoft compatibility team. In some cases, an IHVâ€™s Windows 8 in-box driver removes the value-add component on upgrade. This is up to the IHV.

Some retail and OEM Windows 7 graphics drivers are intentionally structured to prevent their installation on Windows 8. Windows 8 might try to migrate such a driver according to the rules above, but it would fail to install on Windows 8, resulting in the use of the MSBDD.

An IHV can create a unified driver package that is a WDDM 1.2 driver on Windows 8, but that appears like a WDDM 1.1 or 1.0 driver on previous Windows releases.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20XDDM%20drivers%20%20not%20supported%20for%20Windows%208%20%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




