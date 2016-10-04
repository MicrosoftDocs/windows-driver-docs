---
title: Driver Signing Policy
description: Driver Signing Policy
ms.assetid: c3ba672c-5bf2-4885-a85e-fa6d8a47ca54
keywords: ["driver signing WDK , kernel-mode code signing policy", "signing drivers WDK , kernel-mode code signing policy", "digital signatures WDK , kernel-mode code signing policy", "signatures WDK , kernel-mode code signing policy", "kernel-mode code signing policy WDK", "kernel-mode driver signing WDK", "driver package digital signatures WDK", "package digital signatures WDK"]
---

# Driver Signing Policy

Starting with new installations of Windows 10, version 1607, Windows will not load any new kernel mode drivers which are not signed by the Dev Portal.  To get your driver signed, follow these steps:

1. [Get an EV Code Signing Certificate](https://msdn.microsoft.com/en-us/library/windows/hardware/hh801887.aspx). All drivers submitted to the portal must be signed by an EV certificate.
2. Submit your new driver to the [Windows Hardware Developer Center Dashboard portal](https://sysdev.microsoft.com/hardware).

## Exceptions

Cross-signed drivers are still permitted if any of the following are true:

* The PC was upgraded from an earlier release of Windows to Windows 10, version 1607.
* Secure Boot is off.
* Driver was signed with cross-signing certificate issued prior to July 29th 2015.

For more info, see [Driver Signing Changes in Windows 10, version 1607](https://blogs.msdn.microsoft.com/windows_hardware_certification/2016/07/26/driver-signing-changes-in-windows-10-version-1607/).

## Signing a driver for earlier versions of Windows

To sign a driver for Windows Vista, Windows 7, Windows 8, Windows 8.1, and Windows 10, follow these steps:

1. Run the HLK tests for Windows 10.
2. Run the HCK tests for Windows 8.1 and earlier versions.
3. Using the Windows 10 HLK, merge the two test logs.
4. Submit your driver and the merged HLK/HCK test results to the [Windows Hardware Developer Center Dashboard portal](https://sysdev.microsoft.com/hardware).

Before Windows 10, the following types of drivers require an Authenticode certificate used together with Microsoft’s cross-certificate for cross-signing:

* Kernel-mode device drivers
* User-mode device drivers
* Drivers that stream protected content. This includes audio drivers that use Protected User Mode Audio (PUMA) and Protected Audio Path (PAP), and video device drivers that handle protected video path-output protection management (PVP-OPM) commands. For more information, see [Code-signing for Protected Media Components](http://go.microsoft.com/fwlink/p/?linkid=74262).

Starting in Windows 8, Secure Boot is on by default.  when Secure Boot is on, Windows loads only drivers that are digitally signed.  The following table lists the signature requirements for different types of drivers based on processor architecture and Secure Boot state.  The table applies to both third party boot drivers and device drivers.</p>
<p>
<table>
<tr>
<th colspan="2">Secure Boot Enabled </th>
<th colspan="2">Secure Boot Disabled </th>
</tr>
<tr>
<th>x86</th>
<th>x64</th>
<th>x86</th>
<th>x64</th>
</tr>
<tr>
<td colspan="2">
<p><b>Signature Algo</b></p>
<p>SHA1 or above</p>
<p><b>Signature type</b></p>
<p>Embedded</p>
<p><b>Signature requirement</b></p>
<p>Microsoft Root Authority 2010</p>
<p>WHQL signature required</p>
</td>
<td>
<p>Unsigned drivers allowed</p>
</td>
<td>
<p><b>Signature Algo</b></p>
<p>SHA1 or above</p>
<p><b>Signature type</b></p>
<p>Embedded or catalog signed</p>
<p><b>Signature requirement</b></p>
<p>Standard roots trusted by Code Integrity 
</p>
</td>
</tr>
</table>

For info about signing an ELAM driver, see [Early launch antimalware](http://msdn.microsoft.com/en-us/library/windows/desktop/hh848061(v=vs.85).aspx).

In addition to driver code signing, you also need to meet the PnP device installation signing requirements for installing a driver.  For more info, see [Plug and Play (PnP) device installation signing requirements](pnp-device-installation-signing-requirements--windows-vista-and-later-.md).

## See Also

* [Installing an Unsigned Driver Package during Development and Test](installing-an-unsigned-driver-during-development-and-test.md)
* [Signing Drivers for Public Release](signing-drivers-for-public-release--windows-vista-and-later-.md)
* [Signing Drivers during Development and Test](signing-drivers-during-development-and-test--windows-vista-and-later-.md)
* [Digital Signatures for Kernel Modules on Windows](http://go.microsoft.com/fwlink/p/?linkid=184997)
* [Troubleshooting Install and Load Problems with Signed Driver Packages](troubleshooting-install-and-load-problems-with-signed-driver-packages.md)

 

 

 





