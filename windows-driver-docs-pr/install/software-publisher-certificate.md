---
title: Software Publisher Certificate
description: Software Publisher Certificate
ms.assetid: eb06c630-9a3d-4f53-b00b-b1254c8bbaec
keywords:
- catalog files WDK driver signing , SPC
- Software Publisher Certificate WDK driver signing
- SPC WDK driver signing
- public release driver signing WDK , SPC
- release signing WDK , SPC
- cross-certificate WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Software Publisher Certificate


To comply with the [kernel-mode code signing policy](kernel-mode-code-signing-policy--windows-vista-and-later-.md) of 64-bit versions of Windows Vista and later versions of Windows, you can sign a kernel-mode driver by using a Software Publisher Certificate (SPC). The SPC is obtained from a third-party certificate authority (CA) that is authorized by Microsoft to issue such certificates. Signatures generated with this type of SPC also comply with the [PnP driver signing requirements](pnp-device-installation-signing-requirements--windows-vista-and-later-.md) for 64-bit and 32-bit versions of Windows Vista and later versions of Windows.

**Note**  Windows 10 for desktop editions (Home, Pro, Enterprise, and Education) and Windows Server 2016 kernel-mode drivers must be signed by the Windows Hardware Dev Center Dashboard and the Windows Hardware Dev Center Dashboard requires an EV certificate. For more info about these changes, see [Driver Signing Changes in Windows 10](http://blogs.msdn.com/b/windows_hardware_certification/archive/2015/04/01/driver-signing-changes-in-windows-10.aspx).

 

### Cross-Certificates

In addition to obtaining an SPC, you must obtain a cross-certificate that is issued by Microsoft. The cross certificate is used to verify that the CA that issued an SPC is a trusted root authority. A cross-certificate is an X.509 certificate issued by a CA that signs the public key for the root certificate of another CA. Cross-certificates allow the system to have a single trusted Microsoft root authority, but also provide the flexibility to extend the chain of trust to commercial CAs that issue SPCs.

Publishers do not have to distribute a cross-certificate with a [driver package](driver-packages.md). The cross-certificate is included with the digital signature for a driver package's [catalog file](catalog-files.md) or the signature that is embedded in a driver file. Users who install the driver package do not have to perform any additional configuration steps caused by the use of cross-certificates.

For a list of certification authorities that provide SPCs and for more information about cross-certificates, see [Microsoft Cross-Certificates for Windows Vista Kernel Mode Code Signing](http://go.microsoft.com/fwlink/p/?linkid=66583). Follow the instructions on the certification authority's website on how to obtain and install the SPC and corresponding cross-certificate on the computer with which you will sign a driver. In addition, you must add the SPC information to the Personal certificate store of the local computer that signs drivers. For information about this requirement, see the [Installing SPC Information in the Personal Certificate Store](#installing-spc-information-in-the-personal-certificate-store).

### Installing SPC Information in the Personal Certificate Store

In order to use an SPC to sign a driver in a manner that complies with the [kernel-mode code signing policy](kernel-mode-code-signing-policy--windows-vista-and-later-.md), the certificate information must first be contained in a Personal Information Exchange (*.pfx*) file. The information that is contained in the *.pfx* file must then be added to the Personal certificate store of the local computer that signs a driver.

A CA might issue a *.pfx* file that contains the necessary certificate information. If so, you can add the .*pfx* file to the Personal certificate store by following the instructions described in [Installing a .pfx File in the Personal Certificate Store](#installing-a--pfx-file-in-the-personal-certificate-store).

However, a CA might issue the following pairs of files:

-   A *.pvk* file that contains the private key information.

-   An *.spc* or *.cer* file that contains the public key information.

In this case, the pair of files (a *.pvk* and an *.spc,* or a *.pvk* and a *.cer*) must be converted to a *.pfx* file in order to add the certificate information to the Personal certificate store.

To create a .*pfx* file from the pair of files issued by the CA, follow these instructions:

-   To convert a *.pvk* file and an *.spc* file to a *.pfx* file, use the following [**Pvk2Pfx**](https://msdn.microsoft.com/library/windows/hardware/ff550672) command at a command prompt:

    ```cpp
    Pvk2Pfx -pvk mypvkfile.pvk -pi mypvkpassword -spc myspcfile.spc -pfx mypfxfile.pfx -po pfxpassword -f
    ```

-   To convert a *.pvk* file and a *.cer* file, to a *.pfx* file, use the following Pvk2Pfx command at a command prompt:

    ```cpp
    Pvk2Pfx -pvk mypvkfile.pvk -pi mypvkpassword -spc mycerfile.cer -pfx mypfxfile.pfx -po pfxpassword -f
    ```

The following describes the parameters that are used in the [**Pvk2Pfx**](https://msdn.microsoft.com/library/windows/hardware/ff550672) command:

-   The **-pvk**  *mypvkfile.pvk* parameter specifies a *.pvk* file.

-   The **-pi**  *mypvkpassword* option specifies the password for the .*pvk* file.

-   The **-spc** *myspcfile.spc* parameter specifies an *.spc* file or the **-spc**  *mycerfile.cer* parameter specifies a *.cer* file.

-   The **-pfx** *mypfxfile.pfx* option specifies the name of a *.pfx* file.

-   The **-po** *pfxpassword* option specifies a password for the *.pfx* file.

-   The **-f** option configures Pvk2Pfx to replace a existing *.pfx* file if one exists.

### <a href="" id="installing-a--pfx-file-in-the-personal-certificate-store"></a> Installing a .pfx File in the Personal Certificate Store

After obtaining a *.pfx* file from a CA, or creating a *.pfx* file from a *.pvk* and either an .*spc* or a *.cer* file, add the information in the *.pfx* file to the Personal certificate store of the local computer that signs the driver. You can use the Certificate Import Wizard to import the information in the *.pfx* file to the Personal certificate store, as follows:

1.  Locate the *.pfx* file in Windows Explorer and double-click the file to open the Certificate Import Wizard.

2.  Follow the procedure in the Certificate Import Wizard to import the code-signing certificate into the Personal certificate store.

 

 





