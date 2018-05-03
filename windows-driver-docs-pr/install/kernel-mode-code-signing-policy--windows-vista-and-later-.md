---
title: Driver Signing Policy
description: Driver Signing Policy
ms.assetid: c3ba672c-5bf2-4885-a85e-fa6d8a47ca54
keywords:
- driver signing WDK , kernel-mode code signing policy
- signing drivers WDK , kernel-mode code signing policy
- digital signatures WDK , kernel-mode code signing policy
- signatures WDK , kernel-mode code signing policy
- kernel-mode code signing policy WDK
- kernel-mode driver signing WDK
- driver package digital signatures WDK
- package digital signatures WDK
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Driver Signing Policy

Starting with new installations of Windows 10, version 1607, Windows will not load any new kernel mode drivers which are not signed by the Dev Portal.  To get your driver signed, follow these steps:

1. [Get an EV Code Signing Certificate](https://msdn.microsoft.com/en-us/library/windows/hardware/hh801887.aspx). An EV Code Signing Certificate is required to establish a Dashboard account.
2. Submit your new driver to the [Windows Hardware Developer Center Dashboard portal](https://sysdev.microsoft.com/hardware).

There are two different ways to submit drivers to the portal.  For production drivers, you should submit HLK/HCK test logs, as described below.  For testing, you can submit your drivers for attestation signing, which does not require HLK testing, but produces a package signed only for Windows 10.

## Exceptions

Cross-signed drivers are still permitted if any of the following are true:

* The PC was upgraded from an earlier release of Windows to Windows 10, version 1607.
* Secure Boot is off in the BIOS.
* Drivers was signed with an end-entity certificate issued prior to July 29th 2015 that chains to a supported cross-signed CA.

For more info, see [Driver Signing Changes in Windows 10, version 1607](https://blogs.msdn.microsoft.com/windows_hardware_certification/2016/07/26/driver-signing-changes-in-windows-10-version-1607/).

## Signing a driver for all client versions of Windows

To sign a driver for Windows Vista, Windows 7, Windows 8, Windows 8.1, and Windows 10, follow these steps:

1. Run the HLK tests for Windows 10.
2. Run the HCK tests for Windows 8.1 and earlier versions.
3. Using the Windows 10 HLK, merge the two test logs.
4. Submit your driver and the merged HLK/HCK test results to the [Windows Hardware Developer Center Dashboard portal](https://sysdev.microsoft.com/hardware).

## Signing a driver for earlier versions of Windows

Before Windows 10 1607, the following types of drivers require an Authenticode certificate used together with Microsoft’s cross-certificate for cross-signing:

* Kernel-mode device drivers
* User-mode device drivers
* Drivers that stream protected content. This includes audio drivers that use Protected User Mode Audio (PUMA) and Protected Audio Path (PAP), and video device drivers that handle protected video path-output protection management (PVP-OPM) commands. For more information, see [Code-signing for Protected Media Components](http://go.microsoft.com/fwlink/p/?linkid=74262).

## Signing requirements by version

There are two different signing policies.  The older policy applies to all Windows versions prior to Windows 10 1607, and to newer Windows 10 systems when Secure Boot is disabled.  The newer policy applies starting with WIndows 10 1607 when Secure Boot is enabled.

<p>
<table border=1 cellspacing=0 background=gray>
<tr>
<th></th>
<th colspan=2 width=40%>Older policy</th>
<th width=40%>Newer policy</th>
</tr>
<tr>
<td><b>Applies to:</b></td>
<td colspan=2>Windows Vista, Windows 7, Windows 8, Windows 8.1, Windows 10 1507 and 1511;
all Windows 10 when Secure Boot disabled</td>
<td>Windows 10 1607 and later with Secure Boot enabled</td>
</tr>
<tr>
<td><b>Architectures:</b></td>
<td>32-bit</td>
<td>64-bit</td>
<td>Both 32-bit and 64-bit</td>
</tr>
<tr>
<td><b>Signature required:</b></td>
<td>None</td>
<td>Embedded or catalog file</td>
<td>Embedded</td>
</tr>
<tr>
<td><b>Signature algorithm:</b></td>
<td></td>
<td>SHA1</td>
<td>SHA2</td>
</tr>
<tr>
<td><b>Certificate:</b></td>
<td></td>
<td>Standard roots trusted by Code Integrity</td>
<td>Microsoft Root Authority 2010</td>
</tr>
</table>
</p>

This chart applies only to client systems.  Windows Server 2016 will only load drivers that have passed HLK and are signed by the Hardware dashboard portal.  It will not load attestation-signed drivers.

For info about signing an ELAM driver, see [Early launch antimalware](http://msdn.microsoft.com/en-us/library/windows/desktop/hh848061(v=vs.85).aspx).

In addition to driver code signing, you also need to meet the PnP device installation signing requirements for installing a driver.  For more info, see [Plug and Play (PnP) device installation signing requirements](pnp-device-installation-signing-requirements--windows-vista-and-later-.md).

## See Also

* [Installing an Unsigned Driver Package during Development and Test](installing-an-unsigned-driver-during-development-and-test.md)
* [Signing Drivers for Public Release](signing-drivers-for-public-release--windows-vista-and-later-.md)
* [Signing Drivers during Development and Test](signing-drivers-during-development-and-test.md)
* [Digital Signatures](driver-signing.md)
* [Troubleshooting Install and Load Problems with Signed Driver Packages](troubleshooting-install-and-load-problems-with-signed-driver-packages.md)
