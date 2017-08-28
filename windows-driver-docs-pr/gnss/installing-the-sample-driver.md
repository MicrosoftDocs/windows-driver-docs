---
title: Installing the geolocation driver sample
author: windows-driver-content
description: Because the geolocation driver sample simulates hardware, there is no Plug-n-Play functionality to automate the installation. Instead, must use a Windows utility, devcon.exe, to install the sample.
ms.assetid: A08EA9B0-E1D6-47AE-BD89-C43D7D817DAF
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Installing the geolocation driver sample

> [!IMPORTANT] 
> This documentation and the geolocation driver sample for Windows 8.1 has been deprecated.

Because the geolocation driver sample simulates hardware, there is no Plug-n-Play functionality to automate the installation. Instead, must use a Windows utility, devcon.exe, to install the sample.

The following steps outline the installation process.

1.  Make sure that your driver builds without errors.

2.  2. Enable test signing by running the command “bcdedit /set testsigning on” from an elevated command prompt. (You’ll need to reboot your machine after you enable test signing.)
3.  Copy the DLL and INF files for your driver to a separate folder.

4.  Locate the two co-installer DLL files (either checked or free) from the redist/wdf/*processor\_type* folder where you installed the WDK. Copy these files to the folder that you created in step 3. For example, if you installed the WDK on your drive C, you might copy WUDFUpdate\_01009.dll from C:\\WinDDK\\*build\#*\\redist\\wdf\\x86.

5.  Run Devcon.exe. You can find this program in the tools\\devcon folder where you installed the WDK. For example, for a sensor named WDKExample, you type:

    **devcon.exe install WDKExample.inf "Sensors\\WDKExample"**

    **Note**  Do not use Devcon.exe to install released drivers. This recommendation is for testing only.

     

## Related topics
[The Sensors Geolocation Driver Sample](sensors-geolocation-driver-sample.md)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20Installing%20the%20geolocation%20driver%20sample%20%20RELEASE:%20%281/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


