---
title: Introduction to User Interface Plug-Ins
author: windows-driver-content
description: Introduction to User Interface Plug-Ins
MS-HAID:
- 'custdrvr\_20bf5ee6-44ea-4bfd-9b36-578f5066c924.xml'
- 'print.introduction\_to\_user\_interface\_plug\_ins'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 7f01bd14-bcc5-4c26-a9b8-a12aa1ffe242
keywords: ["user interface plug-ins WDK print , about user interface plug-ins", "UI plug-ins WDK print , about user interface plug-ins"]
---

# Introduction to User Interface Plug-Ins


## <a href="" id="ddk-introduction-to-user-interface-plug-ins-gg"></a>


When you add support for a new printer device to either the [Microsoft Universal printer driver](microsoft-universal-printer-driver.md) (Unidrv) or the [Microsoft PostScript printer driver](microsoft-postscript-printer-driver.md) (Pscript), you can customize the driver's user interface by modifying the printer property sheet or the document property sheet for your printer.

You accomplish this customization by providing a user-mode DLL. This DLL is referred to as a *user interface plug-in*, or just *UI plug-in*.

A UI plug-in can modify the printer property sheet by adding, removing, or replacing options within the property sheet's **Device Settings** page. It can also add a new page. Likewise, the plug-in can modify the document property sheet by adding, removing, or replacing options within the property sheet's **Layout**, **Paper/Quality**, and **Advanced** pages, or it can add a new page.

If you are using Unidrv from Windows Vista, you can implement the [**IPrintOemUI2::HideStandardUI**](https://msdn.microsoft.com/library/windows/hardware/ff554142) method in the plug-in to hide all of the printer configuration property pages that the standard driver provides. You can use this method if you want to provide a completely custom printer configuration user interface for your printer.

**Important**   Windows Help (WinHlp32.exe) is an application that enables users to view .hlp files. Starting with Windows Vista, the Windows Help application is not included as a part of the Windows operating system. Software developers who develop applications that rely on .hlp files,should transition their files to an alternative Help format, such as .chm, .hxs, .html, or .xml files. For more information, see the [Windows Help program (WinHlp32.exe) is no longer included with Windows](http://go.microsoft.com/fwlink/p/?linkid=80917) KB article.

 

The [printer interface DLL](printer-interface-dll.md) calls UI plug-ins for Unidrv or Pscript, with a set of COM interfaces. Printer interface DLLs are implemented by using CPSUI, and a UI plug-in interacts indirectly with CPSUI through the driver's printer interface DLL. Therefore, you should read the [CPSUI](common-property-sheet-user-interface.md) section before you develop a UI plug-in.

In addition to modifying the printer driver's user interface, a UI plug-in can perform other operations, such as processing certain printer events and reporting supported capabilities. For more information, see [Customizing Other Printer Interface Operations](customizing-other-printer-interface-operations.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Introduction%20to%20User%20Interface%20Plug-Ins%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


