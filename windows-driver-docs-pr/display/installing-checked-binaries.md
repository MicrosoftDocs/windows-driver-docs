---
title: Installing Checked Binaries
description: Installing Checked Binaries
ms.assetid: a289206a-e793-48a6-875c-f0204edfaaf3
keywords:
- checked binaries WDK display
- binaries WDK display
- free binaries WDK display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installing Checked Binaries


When developing a new driver for the Windows Display Driver Model (WDDM), you should use checked binaries of WDDM components. The checked-binary versions of these components have extensive validation and debugging aids that are not available with the free binaries. However, free binaries should be used for performance tuning because checked binaries are slower.

Hardware vendors who want to run checked binaries for WDDM can use one of the following approaches:

-   Install the checked-binary version of Windows Vista or later. For example, install the checked-binary version of Windows 7 if you are developing a driver for Windows 7 rather than Windows Vista.

    This is the most straightforward approach. However, running all checked-binary versions of operating system components can lead to poor overall performance. Therefore, this is not always an appropriate choice.

-   Install checked-binary versions of the WDDM components over a free-binary version of Windows Vista or later.

    This is the recommended way to run binaries for WDDM.

    Replace the WDDM binaries in the free-binary Windows Vista or later with their checked-binary versions by restarting using an alternate installation of Windows Vista or later.

    **Note**   The *Win32k.sys*, *Gdi32.dll*, *Winsrv.dll*, and *User32.dll*WDDM binaries are exceptions to this rule. These binaries should always match the type of operating system build being installed. Therefore, on a free-binary version of the operating system, these binaries should also be free binary; on a checked-binary version of the operating system build, these binaries should be checked binary. Otherwise, hardware vendors can mix and match free-binary and checked-binary versions of all other WDDM binaries.

     

 

 





