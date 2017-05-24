---
title: Installing SymProxy
description: Installing SymProxy
ms.assetid: 63633de7-d254-415d-bf06-c0e81bd03e74
keywords: ["SymProxy, installation"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Installing SymProxy


## <span id="Summary_of_installation_tasks"></span><span id="summary_of_installation_tasks"></span><span id="SUMMARY_OF_INSTALLATION_TASKS"></span>Summary of installation tasks


The following summarizes the tasks to install and configure SymProxy.

-   The SymProxy files need to be copied to the %WINDIR%\\system32\\inetsrv folder for IIS. This task is discussed below.

-   The registry needs to be configured for SymProxy. For more information see [Configuring the Registry](configuring-the-registry.md).

-   The manifest needs to be registered as Performance Counters and ETW events, and the Event Log needs to be configured.

-   IIS needs to be configured. For more information, see [Choosing Network Security Credentials](choosing-network-security-credentials.md) and [Configuring IIS for SymProxy](configuring-iis-for-symproxy.md).

-   Confirm that SymProxy is running as expected using the status page. For more information see [Checking and Updating Status](checking-and-updating-status.md).

These steps can be automated using the Install.cmd file. For more information, see [SymProxy Automated Installation](symproxy-automated-installation.md).

## <span id="Copy_the_SymProxy_files_to_IIS"></span><span id="copy_the_symproxy_files_to_iis"></span><span id="COPY_THE_SYMPROXY_FILES_TO_IIS"></span>Copy the SymProxy files to IIS


The SymProxy files are included in the Debuggers directory of the Windows Driver Kit. For example this is the location of the 64 bit files for Windows 10 kit. C:\\Program Files (x86)\\Windows Kits\\10\\Debuggers\\x64\\symproxy.

To install SymProxy on the server, copy symproxy.dll, symsrv.dll and symproxy.man to %WINDIR%\\system32\\inetsrv.

In order to prevent problems that could occur in accessing the Microsoft Symbol Store at http://msdl.microsoft.com/downloads/symbols, create a blank file called %WINDIR%\\system32\\inetsrv\\symsrv.yes. The contents of this file are not important. When symsrv.yes file is present, it automatically accepts the EULA for the Microsoft Public Symbol Store.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Installing%20SymProxy%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




