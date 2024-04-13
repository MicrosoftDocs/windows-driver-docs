---
title: Installing SymProxy
description: Installing SymProxy
keywords: ["SymProxy, installation"]
ms.date: 03/12/2019
---

# Installing SymProxy


## <span id="Summary_of_installation_tasks"></span><span id="summary_of_installation_tasks"></span><span id="SUMMARY_OF_INSTALLATION_TASKS"></span>Summary of installation tasks


The following summarizes the tasks to install and configure SymProxy.

-   The SymProxy files need to be copied to the %WINDIR%\\system32\\inetsrv folder for IIS. This task is discussed below.

-   The registry needs to be configured for SymProxy. For more information see [Configuring the Registry](configuring-the-registry.md).

-   The manifest needs to be registered as Performance Counters and ETW events, and the Event Log needs to be configured.

-   IIS needs to be configured. For more information, see [Choosing Network Security Credentials](choosing-network-security-credentials.md) and [Configuring IIS for SymProxy](configuring-iis-for-symproxy.md).

These steps can be automated using the Install.cmd file. For more information, see [SymProxy Automated Installation](symproxy-automated-installation.md).

## <span id="Copy_the_SymProxy_files_to_IIS"></span><span id="copy_the_symproxy_files_to_iis"></span><span id="COPY_THE_SYMPROXY_FILES_TO_IIS"></span>Copy the SymProxy files to IIS


The SymProxy files are included in the Debuggers directory of the Windows Driver Kit. For example this is the location of the 64 bit files for Windows 10 kit. C:\\Program Files (x86)\\Windows Kits\\10\\Debuggers\\x64\\symproxy.

To install SymProxy on the server, copy symproxy.dll, symsrv.dll and symproxy.man to %WINDIR%\\system32\\inetsrv.

In order to prevent problems that could occur in accessing the Microsoft Symbol Store, create a blank file called %WINDIR%\\system32\\inetsrv\\symsrv.yes. The contents of this file are not important. When symsrv.yes file is present, it automatically accepts the EULA for the Microsoft Public Symbol Store.

Note that the certificates that are normally installed with IIS and Windows server such as the "Baltimore CyberTrust Root" are used for HTTPS/TLS communication to the upstream provider, and they need to be in the Trusted Root store on the machine where SymProxy is running. For general information on troubleshooting SSL issues, see [Troubleshooting SSL related issues (Server Certificate)](/iis/troubleshoot/security-issues/troubleshooting-ssl-related-issues-server-certificate).

 

