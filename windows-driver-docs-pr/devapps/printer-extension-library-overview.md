---
title: Printer extension library overview for Windows Store device apps
description: This topic introduces the printer extension library, a library that helps device manufacturers write Windows Store device apps for their printer.
ms.assetid: A47B17CE-BF5A-4C02-807C-890F315A13E0
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Printer extension library overview for Windows Store device apps


This topic introduces the printer extension library, a library that helps device manufacturers write Windows Store device apps for their printer. The printer extension library is included with the [Print settings and print notifications](http://go.microsoft.com/fwlink/p/?LinkID=242862) sample, and also the [Job management and printer maintenance](http://go.microsoft.com/fwlink/p/?LinkID=299829) sample.

## <span id="Overview"></span><span id="overview"></span><span id="OVERVIEW"></span>Overview


A high level design goal for the [v4 printer driver](http://go.microsoft.com/fwlink/p/?LinkId=314231) architecture was to provide built-in support for the Windows Store app user interface. To provide access to the printer, the v4 print driver exposes COM-based [Printer Extension Interfaces](http://go.microsoft.com/fwlink/p/?LinkID=299887).

To access those interfaces from your Windows Store device app, you can use the printer extension library that is included with the Windows Store device app printer samples. The printer extension library wraps the COM implementation of the COM interface `PrinterExtensionLib`. This enables code sharing between printer extensions and your Windows Store device app.

![printer extension library overview](images/373030-printer-app-architecture.png)

## <span id="PrinterExtensionLibrary"></span><span id="printerextensionlibrary"></span><span id="PRINTEREXTENSIONLIBRARY"></span>PrinterExtensionLibrary


Within the PrinterExtensionLibrary project that is included with the printer samples, there are two C# files. These files wrap the contents of PrinterExtensionLib. But additional classes could be added at this layer in order to enable code sharing between printer extensions and Windows Store device apps .

-   **PrinterExtensionTypes.cs** specifies a number of helpful enumerations, constants and interfaces that wrap the COM PrinterExtensionLib APIs.

-   **PrinterExtensionAdapters.cs** specifies all of the constructable classes used to wrap the COM PrinterExtensionLib APIs.

You can augment this project with any necessary C# files that describe common model layer code necessary to build your printer extension and/or Windows Store device app. However, we don't recommend updating the existing classes, as this will make it more difficult to incorporate any bug fixes that made available through updates to the samples.

## <span id="DeviceAppForPrintersLibrary"></span><span id="deviceappforprinterslibrary"></span><span id="DEVICEAPPFORPRINTERSLIBRARY"></span>DeviceAppForPrintersLibrary


An additional project named DeviceAppForPrintersLibrary, provides helper classes and methods for C# apps that you can use to access printers from your Windows Store device app.

## <span id="PrinterExtensionHelperLibrary"></span><span id="printerextensionhelperlibrary"></span><span id="PRINTEREXTENSIONHELPERLIBRARY"></span>PrinterExtensionHelperLibrary


In order to convert the C# interfaces, classes and methods to something supported in JavaScript, this project will create a WinMD file. WinMD files specify Windows Runtime APIs. Additionally, this library can be used to expose convenience objects that are specific to the Windows Store device apps, such as parsing out different activation contexts, or creating toast UI for notifications.

-   **PrintHelperClass.cs** includes the PrinterExtensionLibrary namespaces in order to expose them to JavaScript layers in the app. It also includes some convenience methods for PrintTicket and Bidi.

-   **PrinterNotificationHelper.cs** demonstrates how to show toast UI for notifications.

**Note**  The **Output type** for the PrinterExtensionHelperLibrary assembly is specified on **Application** page of the project properties window.

 

## <span id="related_topics"></span>Related topics


[Developing v4 print drivers](http://go.microsoft.com/fwlink/p/?LinkId=314231)

[Printer Extension Interfaces (v4 Print Driver)](http://go.microsoft.com/fwlink/p/?LinkID=299887)

[Job Management (v4 Printer Driver)](https://msdn.microsoft.com/library/windows/hardware/dn265419)

[Device Maintenance (v4 Printer Driver)](https://msdn.microsoft.com/library/windows/hardware/dn265274)

[Bidirectional Communications](http://go.microsoft.com/fwlink/p/?LinkId=317192)

[Getting started with Windows Store apps](getting-started.md)

[Create a Windows Store device app (step-by-step guide)](step-1--create-a-windows-store-device-app.md)

[Create device metadata for a Windows Store device app (step-by-step guide)](step-2--create-device-metadata.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devapps\devapps]:%20Printer%20extension%20library%20overview%20for%20Windows%20Store%20device%20apps%20%20RELEASE:%20%281/20/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





