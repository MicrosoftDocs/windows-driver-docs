---
title: Driver Signing Policy
description: Driver Signing Policy
ms.assetid: c3ba672c-5bf2-4885-a85e-fa6d8a47ca54
keywords: ["driver signing WDK , kernel-mode code signing policy", "signing drivers WDK , kernel-mode code signing policy", "digital signatures WDK , kernel-mode code signing policy", "signatures WDK , kernel-mode code signing policy", "kernel-mode code signing policy WDK", "kernel-mode driver signing WDK", "driver package digital signatures WDK", "package digital signatures WDK"]
---

# Driver Signing Policy


Starting with 64-bit versions of Windows Vista and later versions of Windows, driver code signing policy requires that all driver code have a digital signature. In addition, certain configurations of 32-bit versions of Windows Vista and later versions of Windows also require driver code to be digitally-signed in order to access next generation premium content that is controlled by the content protection policy. Windows Vista and later versions of Windows rely on digital signatures of these components to increase the safety and stability of the Microsoft Windows platform and enable new customer experiences with next generation premium content.

**Note**  Windows 10 for desktop editions (Home, Pro, Enterprise, and Education) and Windows Server 2016 kernel-mode drivers must be signed by the Windows Hardware Dev Center Dashboard and the Windows Hardware Dev Center Dashboard requires an EV certificate. For more info about these changes, see [Driver Signing Changes in Windows 10](http://blogs.msdn.com/b/windows_hardware_certification/archive/2015/04/01/driver-signing-changes-in-windows-10.aspx).

 

Digital signatures allow the administrator or end-user who is installing Windows-based software to know whether a legitimate publisher has provided the software package. When users choose to send Windows Error Reporting data to Microsoft after a fault or other error occurs, Microsoft can analyze the data to know which publishers' software was running on the system at the time of the error. Software publishers can then use the information that is provided by Microsoft to find and fix problems in their software.

The driver code signing policy starting with Windows Vista and later versions of Windows requires that the following types of drivers have digital signatures:

-   For 64-bit versions of Windows, all kernel mode software, including, but not limited to, kernel-mode device drivers.

    **Note**  Windows 10 for desktop editions and Windows Server 2016 kernel-mode drivers must be signed by the Windows Hardware Dev Center Dashboard and the Windows Hardware Dev Center Dashboard requires an EV certificate.

     

-   For 64-bit versions of Windows, user mode drivers, such as printer drivers.

-   Drivers that stream protected content. This includes audio drivers that use Protected User Mode Audio (PUMA) and Protected Audio Path (PAP), and video device drivers that handle protected video path-output protection management (PVP-OPM) commands. Information about these requirements is outside the scope of this documentation. For more information about these requirements, see [Code-signing for Protected Media Components (Windows Vista and Later)](http://go.microsoft.com/fwlink/p/?linkid=74262).

Starting with Windows 8 UEFI Secure Boot-enabled platforms have additional signing requirements, including requirements for ARM platforms. The driver code signing policy for 32-bit versions of Windows 8 UEFI Secure Boot-enabled platforms also requires drivers have a digital signature.

<p>The following table lists the signature requirements for different types of drivers based on processor architecture and Secure Boot state.</p>
<p>
<table>
<tr>
<th></th>
<th></th>
<th colspan="3">Secure Boot Enabled </th>
<th colspan="3">Secure Boot Disabled </th>
</tr>
<tr>
<th></th>
<th></th>
<th>x86</th>
<th>x64</th>
<th>ARM</th>
<th>x86</th>
<th>x64</th>
<th>ARM</th>
</tr>
<tr>
<td>
<p>Kernel Mode Drivers</p>
</td>
<td>
<p>3rd party boot drivers</p>
</td>
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
<p><b>Signature Algo</b></p>
<p>SHA256</p>
<p><b>Signature type</b></p>
<p>Embedded</p>
<p><b>Signature requirement</b></p>
<p>Microsoft Root Authority 2010</p>
<p>WHQL Signature Required</p>
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
<p>Standard roots trusted by CI 
</p>
</td>
<td>
<p>N/A (Secure Boot cannot be disabled)</p>
</td>
</tr>
<tr>
<td>
<p></p>
</td>
<td>
<p>ELAM</p>
</td>
<td colspan="6">
<p>ELAM drivers must be signed by the process described <a href="http://msdn.microsoft.com/en-us/library/windows/desktop/hh848061(v=vs.85).aspx">here</a>.</p>
</td>
</tr>
<tr>
<td>
<p></p>
</td>
<td>
<p>Drivers</p>
</td>
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
<p><b>Signature Algo</b></p>
<p>SHA256</p>
<p><b>Signature type</b></p>
<p>Embedded</p>
<p><b>Signature requirement</b></p>
<p>Microsoft Root Authority 2010</p>
<p>WHQL Signature Required</p>
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
<p>Standard roots trusted by CI 
</p>
</td>
<td>
<p>N/A (Secure Boot cannot be disabled)</p>
</td>
</tr>
</table>


 

Be aware that this code signing policy is in addition to the [Plug and Play (PnP) device installation signing requirements](pnp-device-installation-signing-requirements--windows-vista-and-later-.md) that affect the installation of a device driver. A developer and publisher of a driver must comply with both the driver code signing requirement for loading a kernel-mode driver and the PnP device installation signing requirements for installing a driver. Also be aware that, although an administrator can authorize the preinstallation of an unsigned kernel-mode driver on a 64-bit system, the administrator cannot subsequently load the unsigned driver during the installation of the driver for a device.

Starting with Windows Vista, driver code signing enforcement is implemented by a component known as Code Integrity. Code Integrity is a feature that improves the security of the operating system by verifying the integrity of a file every time that the image of the file is loaded into memory. The function of Code Integrity is to detect if an unsigned driver is being loaded into kernel-mode, or if a system binary file has been modified by malicious code that may have been run by an administrator.

Starting with Windows Vista, Code Integrity helps ensure that the operating system is running known, identifiable code. Code Integrity generates diagnostic events and a system audit log event when the signature of a kernel module fails to verify correctly. You can use the information logged by Code Integrity to [troubleshoot driver load problems](troubleshooting-install-and-load-problems-with-signed-driver-packages.md).

For development and testing purposes only, enforcement of the driver code signing policy can be temporarily disabled. For more information, see [Installing an Unsigned Driver Package during Development and Test](installing-an-unsigned-driver-during-development-and-test.md).

For general information about how to sign a driver for public release on Windows Vista and later versions of Windows, see [Signing Drivers for Public Release (Windows Vista and Later)](signing-drivers-for-public-release--windows-vista-and-later-.md).

For general information about how to test-sign a driver during development and test on Windows Vista and later versions of Windows, see [Signing Drivers during Development and Test (Windows Vista and Later)](signing-drivers-during-development-and-test--windows-vista-and-later-.md).

For more information about driver code signing requirements, see the [Digital Signatures for Kernel Modules on Systems Running Windows Vista](http://go.microsoft.com/fwlink/p/?linkid=184997) website.

**Note**  The information that is provided at that website is also applicable to Windows Server 2008and later versions of Windows.

 

 

 





