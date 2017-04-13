---
title: Introduction to Spooler Components
author: windows-driver-content
description: Introduction to Spooler Components
ms.assetid: 4eb6e84a-f75f-4ec2-af4f-0007678d120b
keywords: ["spooler component diagram WDK print", "print spooler component diagram WDK"]
---

# Introduction to Spooler Components


## <a href="" id="ddk-introduction-to-spooler-components-gg"></a>


The primary components of the Microsoft Windows 2000 and later print spooler are illustrated in the following diagram.

![diagram illustrating the primary components of the windows 2000 and later print spooler](images/spoocomp.png)

<a href="" id="application-"></a>**Application**   
The print application creates a print job by calling GDI functions.

<a href="" id="gdi-"></a>**GDI**   
The Graphics Device Interface ([*GDI*](https://msdn.microsoft.com/library/windows/hardware/ff556283#wdkgloss-graphics-device-interface--gdi-)) includes both user-mode and kernel-mode components. The user-mode component, Microsoft Win32 GDI, is used by Win32 applications that require graphics support. The kernel-mode component, the [*graphics engine*](https://msdn.microsoft.com/library/windows/hardware/ff556283#wdkgloss-graphics-engine) (or graphics rendering engine), exports services and functions that graphics device drivers can use.

<a href="" id="winspool-drv-"></a>**Winspool.drv**   
Winspool.drv is the client interface into the spooler. It exports the functions that make up the spooler's Win32 API, and provides RPC stubs for accessing the server. (GDI is the primary client, but applications also call some of its Win32 functions.)

<a href="" id="spoolsv-exe-"></a>**Spoolsv.exe**   
Spoolsv.exe is the spooler's API server. It is implemented as a Windows 2000 (or later) service that is started when the operating system is started. This module exports an RPC interface to the server side of the spooler's Win32 API. Clients of Spoolsv.exe include Winspool.drv (locally) and Win32spl.dll (remotely). The module implements some API functions, but most function calls are passed to a [print provider](print-providers.md) by means of the router (Spoolss.dll).

<a href="" id="router-"></a>**Router**   
The router, Spoolss.dll, determines which print provider to call, based on a printer name or handle supplied with each function call, and passes the function call to the correct provider.

<a href="" id="print-provider-"></a>**Print Provider**   
The print provider that supports the specified print device.

<a href="" id="print-monitor-"></a>**Print Monitor**   
Windows XP supports two types of print monitors: language monitors, and port monitors.

If printer hardware is local to the system on which the application is running, the "client" and "server" are the same system (although this is not evident in the diagram).

All spooler components execute in user mode.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Introduction%20to%20Spooler%20Components%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


