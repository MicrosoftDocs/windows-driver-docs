---
title: Connecting and Configuring Displays
description: Connecting and Configuring Displays
ms.assetid: 8c16f99e-c7fd-46e2-b102-f5f0a297fbec
keywords:
- displays WDK Windows 7 display
- displays WDK Windows Server 2008 R2 display
- displays WDK Windows 7 display , connecting
- displays WDK Windows Server 2008 R2 display , connecting
- displays WDK Windows 7 display , configuring
- displays WDK Windows Server 2008 R2 display , configuring
- connecting displays WDK Windows 7 display
- connecting displays WDK Windows Server 2008 R2 display
- configuring displays WDK Windows 7 display
- configuring displays WDK Windows Server 2008 R2 display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Connecting and Configuring Displays


This section applies only to Windows 7 and later, and Windows Server 2008 R2 and later versions of the Microsoft Windows operating system.

The new Connecting and Configuring Displays (CCD) Win32 APIs that are described in [CCD DDIs](ccd-ddis.md) provide more control over the desktop display setup. They can also be used to make your app [display correctly on a portrait device](displaying-app-on-portrait-device.md). For example, in versions of Windows prior to Windows 7, it was impossible to set clone mode by using the **ChangeDisplaySettingsEx** function. The new CCD APIs move away from using Windows Graphics Device Interface (GDI) concepts like view name and toward [Windows Display Driver Model (WDDM)](windows-vista-display-driver-model-design-guide.md) concepts like adapter, source, and target identifiers.

The display control panel, new hot keys, and the Hot Plug Detection (HPD) manager can use the CCD APIs. OEMs can use the CCD APIs for their value-add applets instead of using private driver escapes.

The CCD APIs provide the following functionality:

-   Enumerate the display paths that are possible from the currently connected displays.

-   Set the topology (for example, clone and extend), layout information, resolution, orientation, and aspect ratio for all the connected displays in one function call. By performing multiple settings for all connected displays in one function call, the number of screen flashes is reduced.

-   Add or update settings to the persistence database.

-   Apply settings that are persisted in the database.

-   Use best mode logic to apply optimum display settings.

-   Use best topology logic to apply the optimum topology for the connected displays.

-   Start or stop forced output.

-   Allow OEM hot keys to use the new operating system persistence database.

The CCD APIs cannot handle the following tasks. In addition, the CCD APIs are not backward compatible with the [Windows 2000 display driver model](windows-2000-display-driver-model-design-guide.md).

-   Replace the API sets and private driver escapes that hardware vendors previously provided to control desktop display setup.

-   Pass private data down to the kernel-mode display miniport driver.

-   Provide a new set of monitor-control APIs.

-   Query the monitor capabilities, which include EDID, DDCCI, and so on.

-   Provide a context identifier to uniquely identify the settings that the CCD APIs retrieve from the persistence database.

-   Although the CCD APIs allows a caller to get and set the displays, they do not provide any functionality to enumerate the possible source modes in a given path. APIs that existed prior to Windows 7 already provide this functionality.

The following sections describe the CCD APIs in more detail:

[CCD Concepts](ccd-concepts.md)

[CCD APIs](ccd-apis.md)

**Note**   In addition to using the CCD APIs to set up the desktop display, hardware vendors must modify their Windows 7 [Windows Display Driver Model (WDDM)](windows-vista-display-driver-model-design-guide.md) display miniport drivers to support CCD. For more information about supporting CCD in display miniport drivers, see [CCD DDIs](ccd-ddis.md).

 

 

 





