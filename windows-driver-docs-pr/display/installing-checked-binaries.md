---
title: Installing Checked Binaries
description: Installing Checked Binaries
ms.assetid: a289206a-e793-48a6-875c-f0204edfaaf3
keywords:
- checked binaries WDK display
- binaries WDK display
- free binaries WDK display
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

     

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Installing%20Checked%20Binaries%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




