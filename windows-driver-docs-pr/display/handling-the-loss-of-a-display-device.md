---
title: Handling the Loss of a Display Device
description: Handling the Loss of a Display Device
ms.assetid: 7af8d7e6-733d-4976-a516-7b41fa74dd5d
keywords:
- OPM WDK display , loss of device
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling the Loss of a Display Device


The following scenarios initiate a call to the display miniport driver's [**DxgkDdiOPMDestroyProtectedOutput**](https://msdn.microsoft.com/library/windows/hardware/ff559708) function while content protection on a graphics adapter's output connector might be enabled:

-   Changing the display mode

-   Attaching or detaching a monitor from the Windows desktop

-   Entering a full-screen Command Prompt window

-   Starting any DirectDraw or Direct3D exclusive-mode application

-   Performing Fast User Switching

-   Locking the workstation or pressing CTRL+ALT+DELETE

-   Attaching to the workstation by using Remote Desktop Connection

-   Entering a power-saving mode--for example, suspend or hibernate

-   Terminating the application unexpectedly--for example, through a page fault

 

 





