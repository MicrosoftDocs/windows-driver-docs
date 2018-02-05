---
title: Previous WDK versions and other downloads
description: Install versions of the Windows Driver Kit (WDK), the Windows Debugger (WinDBG), and more.
ms.assetid: e07d9f05-f8d0-46e5-82e6-c23baa614bb1
keywords:
- Windows Driver Kit
- previous versions
- WDK
ms.author: windowsdriverdev
ms.date: 02/02/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Other WDK downloads

Use the [latest public versions of the Windows Driver Kit (WDK) and tools](download-the-wdk.md) to develop drivers. This topic contains information about earlier versions of the WDK and additional downloads for support purposes.

## WDK for Windows 10, version 1703 

### ![download icon](/images/download-install.png) Install Visual Studio 2015

> [!IMPORTANT]
> WDK for Windows 10, version 1703, is not compatible with Visual Studio 2017. Use Visual Studio 2015 for driver development with this version of the WDK. 

These editions of Visual Studio 2015 support driver development. 

* [Download Visual Studio Express for Desktop](https://go.microsoft.com/fwlink/p/?LinkId=691984)
* [Download Visual Studio Community 2015](https://go.microsoft.com/fwlink/p/?LinkId=534599)
* [Download Visual Studio Professional 2015](https://go.microsoft.com/fwlink/p/?LinkId=619628)
* [Download Visual Studio Enterprise 2015](https://go.microsoft.com/fwlink/p/?LinkId=619629)

### ![download icon](/images/download-install.png) Install Windows SDK for Windows 10, version 1703 

* [Download the Windows SDK for Windows 10, version 1703](https://go.microsoft.com/fwlink/p/?LinkID=845298)

### ![download icon](/images/download-install.png) Install WDK for Windows 10, version 1703 

* [Download the WDK for Windows 10, version 1703](https://go.microsoft.com/fwlink/p/?LinkID=845980)

> [!IMPORTANT]
> If you install the WDK, you will not be able to develop Modern Applications. 

> [!IMPORTANT]
> If you have installed WDK for Windows 10, version 1607, some WDK files get removed when installing the WDK for Windows 10, version 1703, on top of the WDK for Windows 10, version 1607. To restore these files: 
> 1. On the Start menu, enter **Apps & features** in the search box, and select **Apps & features** from the results. 
> 2. Find **Windows Driver Kit - Windows 10.0.15063.0** in the list of **Apps & Features**, and then select the program. 
> 3. Select **Modify**, select **Repair**, and then follow the directions on the screen. 
> 4. The files will be restored. 

## ![download icon](/images/download-install.png) EWDK for Windows 10, version 1703 

You can also install the EWDK to build drivers and basic Win32 test applications in a command-line build environment. This environment doesn't include all the features available in Visual Studio, such as the integrated development environment (IDE), so you'll need to use a code editor of your choice. 

* [Learn more about the EWDK](https://go.microsoft.com/fwlink/p/?LinkId=846040)
* [Download EWDK for Windows 10, version 1703](https://developer.microsoft.com/windows/hardware/license-terms-enterprise-wdk-1703)


## ![download icon](/images/download-install.png) WDK for Windows 10, version 1607

1. Run Windows Update. 
2. Install the version of Visual Studio that best suits your development needs. 

    * [Download Visual Studio Express for Desktop](https://go.microsoft.com/fwlink/p/?LinkId=691984)
    * [Download Visual Studio Community 2015](https://go.microsoft.com/fwlink/p/?LinkId=534599)
    * [Download Visual Studio Professional 2015](https://go.microsoft.com/fwlink/p/?LinkId=619628)
    * [Download Visual Studio Enterprise 2015](https://go.microsoft.com/fwlink/p/?LinkId=619629)

3. During installation, select the **Typical for Windows 10 Developers** option. 
4. Follow the prompts to complete the installation. 
5. [Install the WDK for Windows 10, version 1607](https://go.microsoft.com/fwlink/p/?LinkId=526733) 
**OR**
[Install the EWDK 1607](https://developer.microsoft.com/windows/hardware/license-terms-enterprise-wdk)

## ![download icon](/images/download-install.png) WDK 8.1 Update (for Windows 8.1, 8, and 7 drivers)

WDK 8.1 Update has tools to build, test, debug, and deploy drivers for Windows 8.1 Update, Windows 8.1, Windows 8, and Windows 7. When you have the WDK, we recommend that you install the WDK 8.1 Update Test Pack. It has the tests for device fundamentals, graphics, imaging, mobile broadband (CDMA, GSM, WLAN), sensors, and other utilities. 

> [!IMPORTANT]
> Before installing WDK 8.1 Update, you need to install Visual Studio 2013. 

1. [Download Visual Studio 2013](https://go.microsoft.com/fwlink/p/?LinkId=620683)
2. [Download WDK 8.1 Update](https://go.microsoft.com/fwlink/p/?LinkId=393659) (English only) 
3. [Download the WDK 8.1 Update Test Pack](https://go.microsoft.com/fwlink/p/?LinkID=393660) (English only) 
4. [Get driver samples for Windows 8.1](https://code.msdn.microsoft.com/windowshardware/Windows-Driver-Kit-WDK-81-cf35e953) 

## ![download icon](/images/download-install.png) WinDbg for Windows 8.1
Debugging Tools for Windows (WinDbg) are included in the WDK 8.1 Update, but you can also install them as a standalone component from the Windows 8.1 SDK. In the installation wizard, select Debugging Tools for Windows, and clear all other components. 

* [Get (WinDbg) as part of Windows 8.1 SDK](https://www.microsoft.com/click/services/Redirect2.ashx?CR_EAC=300135395) (English only)

## ![download icon](/images/download-install.png) Remote Debugging client for Windows 8.1
With the Windows Remote Debugging client, you can work remotely with developers from Microsoft, over the internet, to debug kernel-mode failures using the kernel debugger. 
* [Learn more and prepare for remote debugging.](https://msdn.microsoft.com/library/windows/hardware/br230785)
* [Download the Remote Debugging client](http://go.microsoft.com/fwlink/p/?LinkId=316921) (English only)  

## ![download icon](/images/download-install.png) WDK 8
WDK 8 enables you to migrate earlier drivers to WDK 8.1 Update and Visual Studio 2013. Microsoft does not support WDK 8 and will make no further updates to this kit. You should use the latest versions of the WDK and Visual Studio to build drivers for Windows. 

> [!IMPORTANT]
> You must install [Visual Studio Professional 2012](https://go.microsoft.com/fwlink/p/?LinkID=255976) or [Visual Studio Ultimate](https://go.microsoft.com/fwlink/p/?LinkID=255982) before you install WDK 8. 

1. [Download WDK 8 (English only)](https://go.microsoft.com/fwlink/p/?LinkID=324284)
2. [Download the WDK 8 redistributable components](https://go.microsoft.com/fwlink/p/?LinkID=253170) (English only) 
3. [Get driver samples for Windows 8](https://code.msdn.microsoft.com/windowshardware/Windows-Driver-Kit-WDK-80-e3161626) 

## ![download icon](/images/download-install.png) WDK 7.1.0 (for Windows XP drivers)
Developing a driver for Windows XP or Windows Server 2003? WDK 7.1.0 has the tools, code samples, docs, compilers, headers, and libraries that you can use to create drivers for these operating systems. 

* [Download WDK 7.1.0](https://www.microsoft.com/download/confirmation.aspx?id=11800) (English only) 

## ![download icon](/images/download-install.png) Standalone debugging tools for debugging Windows XP and Windows Vista
If you're debugging Windows XP, Windows Server 2003, Windows Vista, or Windows Server 2008 (or using one of these operating systems to run Debugging Tools for Windows), you need to use the Windows 7 release of the debugging tools. It's included in the SDK for Windows 7 and .NET Framework 4.0. To install the Debugging Tools for Windows as a standalone component, in the SDK installation wizard, select Debugging Tools for Windows, and clear all other components. 

> [!IMPORTANT]
> Newer versions of the Visual C++ 2010 Redistributable can cause issues when you install the SDK for Windows 7. For more information, see [support for the Windows SDK](https://support.microsoft.com/kb/2717426). 

* [Get the standalone debugging tools for Windows XP as part of Windows 7 SDK](https://www.microsoft.com/download/confirmation.aspx?id=8279) 

## Related downloads
* [Download the Windows Assessment and Deployment Kit (Windows ADK)](https://developer.microsoft.com/windows/hardware/windows-assessment-deployment-kit)
* [Download the Windows HLK, HCK, or Logo Kit](https://developer.microsoft.com/windows/hardware/windows-hardware-lab-kit) 
* [Download the debugging Tools for Windows (WinDbg)](https://developer.microsoft.com/windows/hardware/download-windbg) 
* [Download Windows Symbol Packages](https://developer.microsoft.com/windows/hardware/download-symbols) 
* [Download the WDK Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewWDK) 