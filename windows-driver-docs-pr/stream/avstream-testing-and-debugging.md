---
title: AVStream Testing and Debugging
author: windows-driver-content
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
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

For more information about DirectShow, see the DirectShow documentation on [MSDN](http://go.microsoft.com/fwlink/p/?linkid=68207).

The *AMCap2.exe* tool appears in the Windows Server 2008 WDK and earlier versions of the WDK. The tool has been removed from the Windows 7 WDK for both x86-based and x64-based platforms.

All the functionality of AMCap2 is still available in the existing GraphEdt tool, which is included in the Windows 7 WDK.

### **MCStream**

*MCStream.exe* (MultiChannel Streaming Tool) is a development tool that allows the user to generate and render multiple channel wave tones. MCStream is an older tool that uses KS directly, instead of DirectShow or Media Foundation.

**Warning**  MCStream does not work with all audio renderers.

 

MCStream includes two binary components: *MCStream.exe* (the application) and *MCStream.txt* (the help documentation).

MCStream binaries are provided for x86-based and x64-based architectures. MCStream runs on Microsoft Windows 2000, XP, Windows 2003 Server, and Vista.

The *MCstream.exe* tool is not included in the Windows 7 WDK for both x86-based and x64-based platforms.

This tool uses legacy technology that is no longer recommended for driver development in Windows 7 and later operating systems.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20AVStream%20Testing%20and%20Debugging%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


