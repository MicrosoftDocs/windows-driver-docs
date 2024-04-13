---
title: Supporting Multiple PDEVs
description: Supporting Multiple PDEVs
keywords:
- display drivers WDK Windows 2000 , desktop management
- desktop management WDK Windows 2000 display
- multiple PDEVs WDK Windows 2000 display
- PDEV WDK Windows 2000 display
ms.date: 04/20/2017
---

# Supporting Multiple PDEVs

This section shows how an application can create a new PDEV while the current PDEV is still loaded. Control Panel's Display program requires that a display driver support the enabling of additional PDEVs, because it is possible for an application to create a new PDEV with a new desktop. Specifically, the end user can click the Display icon to run a test on changes to such elements as the size, number of colors, and refresh rate of the screen. The Display program creates a new desktop dynamically to test the display's mode changes.

GDI performs the following steps when the user clicks on the Display icon to request a mode change. These steps assume that no active Direct3D, WNDOBJ, or DRIVEROBJ objects are owned by the current driver instance.

1. Temporarily disable the current PDEV. Call [**DrvAssertMode**](/windows/win32/api/winddi/nf-winddi-drvassertmode) (old PDEV instance). Call is made using **FALSE** if miniport driver is to assume control, and with **TRUE** if PDEV should be used.

2. Call [**DrvEnableDriver**](/windows/win32/api/winddi/nf-winddi-drvenabledriver) to load new driver (if required by new PDEV instance).

3. Create new PDEV
   * Call [**DrvEnablePDEV**](/windows/win32/api/winddi/nf-winddi-drvenablepdev) (new PDEV instance).
   * Call [**DrvCompletePDEV**](/windows/win32/api/winddi/nf-winddi-drvcompletepdev) (new PDEV instance).
   * Call [**DrvEnableSurface**](/windows/win32/api/winddi/nf-winddi-drvenablesurface) (new PDEV instance).

4. Get DirectDraw information (if DirectDraw is hooked by driver). Second call to [**DrvGetDirectDrawInfo**](/windows/win32/api/winddi/nf-winddi-drvgetdirectdrawinfo) is made only if the first call succeeds.
   * Call *DrvGetDirectDrawInfo* (new PDEV instance).
   * Call *DrvGetDirectDrawInfo* (new PDEV instance).

5. Enable DirectDraw (if hooked by driver and previous call to *DrvGetDirectDrawInfo* succeeded): Call [**DrvEnableDirectDraw**](/windows/win32/api/winddi/nf-winddi-drvenabledirectdraw) (new PDEV instance).

6. Copy old PDEV state to new PDEV instance (if both instances use same driver, and DirectDraw is hooked by driver): Call [**DrvResetPDEV**](/windows/win32/api/winddi/nf-winddi-drvresetpdev).

7. Notify each driver instance of its new HDEV association. The first call to [**DrvCompletePDEV**](/windows/win32/api/winddi/nf-winddi-drvcompletepdev) notifies the new driver instance; the second call notifies the old driver instance.

   * Call *DrvCompletePDEV* (new PDEV instance).
   * Call *DrvCompletePDEV* (old PDEV instance).

   The driver should use the new HDEV value in any callbacks to GDI that require an HDEV.

8. Disable DirectDraw (if hooked by the driver and DirectDraw is active): Call [**DrvDisableDirectDraw**](/windows/win32/api/winddi/nf-winddi-drvdisabledirectdraw) (old PDEV instance).

9. Disable surface: Call [**DrvDisableSurface**](/windows/win32/api/winddi/nf-winddi-drvdisablesurface) (old PDEV instance).

10. Disable PDEV: Call [**DrvDisablePDEV**](/windows/win32/api/winddi/nf-winddi-drvdisablepdev) (old PDEV instance).

In this example, GDI temporarily disables the current PDEV when the user clicks Apply, and then creates a second PDEV that matches the display mode selections in the dialog box. After the user views a bitmap on the display screen under the test mode, the second PDEV is destroyed and the Display program restores the original PDEV for the desktop. Note that without the ability to revert back to the original display settings, the system would become unusable if the settings were incompatible with the hardware and driver.

If the current instance of the driver owns a Direct3D, WNDOBJ, or DRIVEROBJ object, the driver's view of the previous mode change sequence changes as follows (note that in Windows 2000 and later, DirectDraw is always enabled as soon as the driver is initialized):

* Destruction of the owning driver instance will be deferred. Specifically, the second call to [**DrvCompletePDEV**](/windows/win32/api/winddi/nf-winddi-drvcompletepdev) in step 7, step 8, and step 9 will not occur at the time of the mode change. As a result, the old driver instance is disabled due to the call to [**DrvAssertMode**](/windows/win32/api/winddi/nf-winddi-drvassertmode)(**FALSE**) in step 1, and is retained until either the system does a mode change back to the original mode, or until all the objects that reference the instance are destroyed.

* If the system reverts back to the original mode before the referencing objects are destroyed, the original driver instance will be resurrected. That is, steps 2 through 5 do not occur, and the original driver instance is reenabled by a call to *DrvAssertMode*(**TRUE**) (see step 1).

* If the system does not revert back to the original mode before all the referencing objects are destroyed, then the driver instance will be destroyed when the final referencing object is destroyed. That is, the second call to *DrvCompletePDEV* in step 7, step 8, and step 9 will occur at the time the final referencing object is destroyed (for example, when all the owning processes are terminated).

An implication of this is that Direct3D or OpenGL drivers can be called to destroy an inactive driver instance at any time. These drivers can be called even if another instance of the driver is currently active, or if the driver is in full-screen MS-DOS mode, or if another driver owns the hardware entirely (such as the VGA driver). Consequently, the [**DrvDisableDirectDraw**](/windows/win32/api/winddi/nf-winddi-drvdisabledirectdraw), [**DrvDisableSurface**](/windows/win32/api/winddi/nf-winddi-drvdisablesurface), and [**DrvDisablePDEV**](/windows/win32/api/winddi/nf-winddi-drvdisablepdev) routines (see steps 8-10) of a driver cannot assume that the device is in graphics mode and that they own exclusive access. As a general rule, drivers should not manipulate their video hardware in their *DrvDisableXxx* routines unless they know that their instance is currently active (by remembering the state from the last [**DrvAssertMode**](/windows/win32/api/winddi/nf-winddi-drvassertmode) call).

A PDEV is private to a driver and contains all the information and data that represents the associated physical device. To create multiple PDEVs, the graphics driver must meet both of the following requirements:

1. The driver must not use global variables instead of dereferencing members of a PDEV structure. If global variables are used, they might contain or point to random data when a new PDEV is created, or an old one restored. All state information must be saved in the PDEV. The PDEV is always passed to any graphics operation and is therefore used to get or set global data.
2. The [**DrvDisableSurface**](/windows/win32/api/winddi/nf-winddi-drvdisablesurface), [**DrvDisablePDEV**](/windows/win32/api/winddi/nf-winddi-drvdisablepdev), and [**DrvDisableDriver**](/windows/win32/api/winddi/nf-winddi-drvdisabledriver) routines must be implemented in the graphics driver so that an application can create and destroy additional PDEVs, and in some cases load more than one driver.

> [!NOTE]
> If the driver's version number is 1.0, GDI will not call the driver to create a second PDEV. The version number of the driver is returned in [**DRVENABLEDATA**](/windows/win32/api/winddi/ns-winddi-drvenabledata).
>
> Occasionally, the Display program's test bitmap will be displayed using a different driver than the currently-loaded driver. For example, if a system is running in 16-color mode with the VGA driver and testing a 64K-color mode with the VGA64K display driver, the VGA64K driver will be loaded dynamically and unloaded when the test is complete.
