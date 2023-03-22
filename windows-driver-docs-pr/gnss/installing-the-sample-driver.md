---
title: Installing the geolocation driver sample
description: Because the geolocation driver sample simulates hardware, there is no Plug-n-Play functionality to automate the installation. Instead, must use a Windows utility, devcon.exe, to install the sample.
ms.date: 03/21/2023
---

# Installing the geolocation driver sample

> [!IMPORTANT]
> This documentation and the geolocation driver sample for Windows 8.1 has been deprecated.

Because the geolocation driver sample simulates hardware, there is no Plug-n-Play functionality to automate the installation. Instead, must use a Windows utility, devcon.exe, to install the sample.

The following steps outline the installation process.

1. Make sure that your driver builds without errors.

1. Enable test signing by running the command "bcdedit /set testsigning on" from an elevated command prompt. (You'll need to reboot your machine after you enable test signing.)

1. Copy the DLL and INF files for your driver to a separate folder.

1. Locate the two co-installer DLL files (either checked or free) from the redist/wdf/*processor\_type* folder where you installed the WDK. Copy these files to the folder that you created in step 3. For example, if you installed the WDK on your drive C, you might copy WUDFUpdate\_01009.dll from C:\\WinDDK\\*build\#*\\redist\\wdf\\x86.

1. Run Devcon.exe. You can find this program in the tools\\devcon folder where you installed the WDK. For example, for a sensor named WDKExample, run the following command:

    `devcon.exe install WDKExample.inf "Sensors\WDKExample"`

    Do not use Devcon.exe to install released drivers. This recommendation is for testing only.

## Related topics

[The Sensors Geolocation Driver Sample](sensors-geolocation-driver-sample.md)  
