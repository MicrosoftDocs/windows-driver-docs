---
title: AVStream Testing and Debugging
description: AVStream Testing and Debugging
ms.assetid: 7a3eeeb5-1ff4-4110-9168-c716cd7776b8
keywords:
- testing AVStream WDK streaming media
- AVStream WDK , testing
- debugging WDK AVStream
- AVStream WDK , debugging
- AMCap2
- GraphEdt
- KsStudio utility
- MCStream
- UVCView
- Active Movie Capture WDK AVStream
- AVStream WDK , tools
- Kernel Streaming Development Studio WDK AVStream
- MultiChannel Streaming Tool WDK AVStream
- USB Video Class descriptor viewer WDK AVStream
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# AVStream Testing and Debugging


Beginning with the Windows 7 WDK, three tools are provided in the *WDKPath\\tools\\avstream* folder hierarchy. This topic explains the purpose and basic usage of each tool. In some cases, additional documentation is included in the folder hierarchy.

### **GraphEdt**

*GraphEdt.exe* is a development tool for visually building functional multimedia filter graphs using the DirectShow application programming interface.

GraphEdt includes three binary components: *GraphEdt.exe* (the application), *GraphEdt.chm* (the help documentation), and *Proppage.dll* (a helper filter). *Proppage.dll* exposes additional property settings for filters when registered with the operating system using the command "regsvr32 proppage.dll". The regsvr32 command must be run at elevated privilege level.

GraphEdt binaries are provided for x86-based and x64-based architectures. GraphEdt runs on Microsoft Windows 2000, XP, Windows 2003 Server, Windows Vista, and Windows 7.

### **KsStudio**

*KsStudio.exe* (Kernel Streaming Development Studio) is a development tool used to examine multimedia driver properties, pins, and supported media.

The Windows 7 WDK includes KsStudio binaries for the x86-based and x64-based architectures. Additionally, there is a version for Windows XP and Windows 2003 Server in the XP folder (for both x86 and x64). For Windows 7, the binaries are *KsStudio.exe* (the application), *KsStudio.chm* (the help documentation), and *KsMon.sys* (a helper device driver). For XP and Windows 2003 Server, there is also S*ndAnlyz.dll* (a helper file).

KsStudio is a kernel development tool, and therefore should be used carefully. *KsStudio.exe* must write a summary log to the starting directory, which must have write access for the user. KsStudio attempts to load its helper driver *KsMon.sys*. This loading is optional and will only succeed if *KsMon.sys* is in the starting directory and the command is run at elevated privilege level. Typically, KsStudio will present a dialog box titled "KS Studio Filter Options," which allows the user to specify parameters, the most important of which are the Classes to enumerate. Use the **Classes** button on that dialog box to select none, any, or all classes.

This is a complex, yet elegant, and very handy development tool for multimedia device authors. For more information, refer to the *KsStudio.chm* help file.

### <a href="" id="uvcview"></a>**USBView**

*USBView.exe* (USB Video Class descriptor viewer) is a development tool that allows the user to examine the descriptors on any attached USB device. USBView ships in the Windows Driver Kit (WDK) as a sample in the USB section. USBView adds descriptive descriptor information for multimedia USB Audio and Video Class devices.

**Note**  In the Windows 7 WDK, this tool is titled UVCView.

 

USBView includes one binary component: *USBView.exe*. In the WDK, this executable is located in the *tools\\avstream* folder hierarchy. For documentation, see the USBView sample in *WDKPath\\src\\usb\\usbview*.

USBView binaries are provided for x86-based and x64-based architectures. USBView runs on Microsoft Windows 2000, XP, Windows 2003 Server, Windows Vista, and Windows 7.

The following tools are provided in earlier versions of Windows and are not recommended for use on Windows 7 and later:

### **AMCap2**

*AMCap2.exe* (Active Movie Capture) is an application for enumerating and using audio and video capture devices with the Microsoft DirectShow application programming interface.

AMCap2 includes one binary component: *AMCap2.exe*.

AMCap2 binaries are provided for x86-based and x64-based architectures. AMCap2 runs on Microsoft Windows 2000, XP, Windows 2003 Server, and Vista.

When AMCap2 initializes, it enumerates available audio and video capture devices on its device menu. You can select none or one audio and/or video device. On the Settings menu, you can select specific device attributes.

For more information about DirectShow, the [DirectShow documentation](http://go.microsoft.com/fwlink/p/?linkid=68207).

The *AMCap2.exe* tool appears in the Windows Server 2008 WDK and earlier versions of the WDK. The tool has been removed from the Windows 7 WDK for both x86-based and x64-based platforms.

All the functionality of AMCap2 is still available in the existing GraphEdt tool, which is included in the Windows 7 WDK.

### **MCStream**

*MCStream.exe* (MultiChannel Streaming Tool) is a development tool that allows the user to generate and render multiple channel wave tones. MCStream is an older tool that uses KS directly, instead of DirectShow or Media Foundation.

**Warning**  MCStream does not work with all audio renderers.

 

MCStream includes two binary components: *MCStream.exe* (the application) and *MCStream.txt* (the help documentation).

MCStream binaries are provided for x86-based and x64-based architectures. MCStream runs on Microsoft Windows 2000, XP, Windows 2003 Server, and Vista.

The *MCstream.exe* tool is not included in the Windows 7 WDK for both x86-based and x64-based platforms.

This tool uses legacy technology that is no longer recommended for driver development in Windows 7 and later operating systems.

 

 




