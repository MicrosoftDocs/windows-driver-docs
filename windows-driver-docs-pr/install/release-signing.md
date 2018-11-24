---
title: Release Signing
description: After completing test signing and verifying that the driver is ready for release, the driver package has to be release signed. There are two ways of release signing a driver package.
ms.assetid: 71499A0A-95D0-411C-84D1-C4B91FA4E6B1
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Release Signing


After completing test signing and verifying that the driver is ready for release, the driver package has to be release signed. There are two ways of release signing a driver package.

Release-signing identifies the publisher of a kernel-mode or user-mode binaries (for example, .sys or .dll files) that loads into Windows Vista and later versions of Windows.

Kernel-mode binaries are release-signed through either:

1.  Windows Hardware Quality Lab (WHQL also known as Winqual) to release sign a driver package. A WHQL Release Signature is obtained through the Windows Certification Program. The link below describes the five steps from start to finish on Windows Certification Program. See [Windows hardware certification: start here](https://msdn.microsoft.com/windows/hardware/hh833792) for more details about this option. Any questions on the steps in the link above should be directed to <sysdev@microsft.com> alias.
2.  Instead of using the WHQL program, a driver package can be release signed by driver developers and vendors. This program has started from the Vista OS release. A release signature is created through a Software Publisher Certificate (SPC). The SPC is obtained from a third-party certificate authority (CA) that is authorized by Microsoft to issue such certificates. Signatures generated with this type of SPC also comply with the PnP driver signing requirements for 64-bit and 32-bit versions of Windows Vista and later versions of Windows

The steps needed to release sign a driver package for method 2 are described next.

## Obtain a Software Publisher Certificate (SPC)


Release signing requires a code-signing certificate, also referred to as a Software Publisher Certificate (SPC) from a commercial CA.

The [Cross-Certificates for Kernel Mode Code Signing](cross-certificates-for-kernel-mode-code-signing.md) topic provides the list of commercial third-party certificate authorities (CA) authorized by Microsoft. The CA vendors listed must be used to provide a Software Publisher Certificate (SPC) to release sign the driver package.

Follow the CA's instructions for how to acquire the SPC and install the private key on the signing computer. Please note that the SPC is a proprietary instrument of the driver vendor who requested it for signing their driver package. The SPC, the private key, and the password must not be shared with anyone outside the requesting vendor’s organization.

## Cross-Certificates


*Excerpt from* [Software Publisher Certificate](software-publisher-certificate.md):

In addition to obtaining an SPC, you must obtain a cross-certificate that is issued by Microsoft. The cross certificate is used to verify that the CA that issued an SPC is a trusted root authority. A cross-certificate is an X.509 certificate issued by a CA that signs the public key for the root certificate of another CA. Cross-certificates allow the system to have a single trusted Microsoft root authority, but also provide the flexibility to extend the chain of trust to commercial CAs that issue SPCs.

Publishers do not have to distribute a cross-certificate with a [driver package](driver-packages.md). The cross-certificate is included with the digital signature for a driver package's [catalog file](catalog-files.md) or the signature that is embedded in a driver file. Users who install the driver package do not have to perform any additional configuration steps caused by the use of cross-certificates.

*Selected excerpts from* [Cross-Certificates for Kernel Mode Code Signing](cross-certificates-for-kernel-mode-code-signing.md):

A cross-certificate is a digital certificate issued by one Certificate Authority (CA) that is used to sign the public key for the root certificate of another Certificate Authority. Cross-certificates provide a means to create a chain of trust from a single, trusted, root CA to multiple other CAs.

In Windows, cross-certificates:

-   Allow the operating system kernel to have a single trusted Microsoft root authority.
-   Extend the chain of trust to multiple commercial CAs that issue Software Publisher Certificates (SPCs), which are used for code-signing software for distribution, installation, and loading on Windows

The cross-certificates that are provided here are used with the Windows Driver Kit (WDK) code-signing tools for properly signing kernel-mode software. Digitally signing kernel-mode software is similar to code-signing any software that is published for Windows. Cross-certificates are added to the digital signature by the developer or software publisher when signing the kernel-mode software. The cross-certificate itself is added by the code-signing tools to the digital signature of the binary file or catalog.

**Selecting the Correct Cross-certificate**

Microsoft provides a specific cross-certificate for each CA that issues SPCs for code-signing kernel-mode code. For more information about cross-certificates, see [Cross-Certificates for Kernel Mode Code Signing](cross-certificates-for-kernel-mode-code-signing.md). This topic lists the names of the Microsoft authorized CA vendors and the correct cross-certificate for the root authority that issued your SPC. Locate the correct cross-certificate for the SPC issued by your CA vendor and download the cross-certificate to the signing computer you will be using for release signing, and store it in your driver directory. It is advisable to provide the absolute path to this Certificate when using it in any signing command.

## Installing SPC Information in the Personal Certificate Store


*Further excerpts from* [Software Publisher Certificate](software-publisher-certificate.md):

In order to use an SPC to sign a driver in a manner that complies with the [kernel-mode code signing policy](kernel-mode-code-signing-policy--windows-vista-and-later-.md), the certificate information must first be contained in a Personal Information Exchange (*.pfx*) file. The information that is contained in the *.pfx* file must then be added to the Personal certificate store of the local computer that signs a driver.

A CA might issue a *.pfx* file that contains the necessary certificate information. If so, you can add the .*pfx* file to the Personal certificate store by following the instructions described in [Installing a .pfx File in the Personal Certificate Store](software-publisher-certificate.md#installing-a--pfx-file-in-the-personal-certificate-store).

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

**Important**  You should protect your pvk and pfx files with strong passwords.

 

## Installing a .pfx File in the Personal Certificate Store


For signing kernel-mode drivers, the certificates and key stored in the .pfx file must be imported into the local Personal certificate store. Signtool does not support using .pfx files for signing kernel-mode drivers. The restriction is due to a conflict in adding cross-certificates in the signature while using a certificate from a .pfx file

*Final excerpts from* [Software Publisher Certificate](software-publisher-certificate.md):

After obtaining a *.pfx* file from a CA, or creating a *.pfx* file from a *.pvk* and either an .*spc* or a *.cer* file, add the information in the *.pfx* file to the Personal certificate store of the local computer that signs the driver. You can use the Certificate Import Wizard to import the information in the *.pfx* file to the Personal certificate store, as follows:

1.  Locate the *.pfx* file in Windows Explorer and double-click the file to open the Certificate Import Wizard.

2.  Follow the procedure in the Certificate Import Wizard to import the code-signing certificate into the Personal certificate store.

*Excerpt from* [Importing an SPC into a Certificate Store](importing-an-spc-into-a-certificate-store.md):

Starting with Windows Vista, an alternative way to import the *.pfx* file into the local Personal certificate store is with the [CertUtil](http://go.microsoft.com/fwlink/p/?linkid=168888) command-line utility. The following command-line example uses CertUtil to import the *abc.pfx* file into the Personal certificate store:

```cpp
certutil -user -p pfxpassword -importPFX abc.pfx
```

Where:

-   The **-user** option specifies "Current User" Personal store.

-   The **-p** option specifies the password for the *.pfx* file (*pfxpassword*).

-   The **-importPFX** option specifies name of the *.pfx* file (*abc.pfx*).

## View SPC Properties


Use the MMC Certificates snap-in (certmgr.msc) to view the certificates in the Personal certificate store.

1.  Launch the Certificates snap-in, certmgr.msc.
2.  In the snap-in's left pane, select the Personal certificate store folder.
3.  Click the Certificates folder and double-click the certificate that is to be used for release signing.
4.  On the Details tab of the Certificate dialog box, select Subject from the list of fields to highlight the certificate's subject name. This is the name that is used with Signtool's /n argument in the examples in this section.

## Signing


**Based on**[Release-Signing a Driver Package's Catalog File](release-signing-a-driver-package-s-catalog-file.md):

Run the following commands to sign the cat file which signs the driver package. The /n command should use the quoted name of the certificate which you will see under Subject in step 4 above, as CN= MyCompany Inc.

```cpp
signtool sign /v /ac MSCV-VSClass3.cer /s My /n “MyCompany Inc.“ /t http://timestamp.verisign.com/scripts/timestamp.dll  toaster.cat
```

/ac FileName

Specifies a file that contains an additional certificate to add to the signature block. This is the cross signing certificate, MSCV-VSClass3.cer, obtained from Microsoft cross certificate download link. Use a full path name if the cross-certificate is not in the current directory. Though not required, it is advisable to add cross certificate while signing the cat file.

/s StoreName

Specifies the store to open when searching for the certificate. If this option is not specified, the My store is opened, which is the Personal certificate Store.

/n SubjectName

Specifies the name of the subject of the signing certificate. This value can be a substring of the entire subject name.

/t URL

Specifies the URL of the time stamp server. If this option is not present, then the signed file will not be time stamped. **With time stamping, the signed driver package remains valid indefinitely until the SPC signing certificate gets revoked for other reasons.**

You must follow every signing steps correctly as described above, otherwise you will not be able to sign the driver. You may get errors shown below.

```cpp
SignTool Error: No certificates were found that met all the given criteria
```

## Embed Signing


**Based on**[Release-Signing a Driver through an Embedded Signature](release-signing-a-driver-through-an-embedded-signature.md):

Starting with Windows Vista, the kernel-mode code signing policy controls whether a kernel-mode driver will be loaded. 64-bit versions of Windows starting with Windows Vista has stricter requirement compared to 32-bit versions of Windows.

A kernel-mode boot-start driver must have an embedded Software Publisher Certificate (SPC) signature. This applies to any type of PnP or non-PnP kernel-mode boot-start driver. Also applies to the 32-bit versions of Windows. A PnP kernel-mode driver that is not a boot-start driver must have either an embedded SPC signature, a catalog file with a WHQL release signature, or a catalog file with an SPC signature.

Please refer to [Kernel-Mode Code Signing Requirements](kernel-mode-code-signing-requirements--windows-vista-and-later-.md) for additional information.

Command for embed signing the toaster.sys file.

```cpp
signtool sign /v /ac MSCV-VSClass3.cer /s my /n “MyCompany Inc. “ /t http://timestamp.verisign.com/scripts/timestamp.dll   toaster.sys
```

After signing is completed, run the command below to verify the signed driver.

```cpp
signtool verify  /kp  /v  /c  tstamd64.cat  toastpkg.inf
```

Command output:

```cpp
Verifying: toaster.inf
File is signed in catalog: toaster.cat
Hash of file (sha1): 580C2A24C3A9E12817E18ADF1C4FE9CF31B01EA3

Signing Certificate Chain:

    Issued to: VeriSign Class 3 Public Primary Certification Authority - G5
    Issued by: VeriSign Class 3 Public Primary Certification Authority - G5
    Expires:   Wed Jul 16 15:59:59 2036
    SHA1 hash: 4EB6D578499B1CCF5F581EAD56BE3D9B6744A5E5

        Issued to: VeriSign Class 3 Code Signing 2010 CA
        Issued by: VeriSign Class 3 Public Primary Certification Authority - G5
        Expires:   Fri Feb 07 15:59:59 2020
        SHA1 hash: 495847A93187CFB8C71F840CB7B41497AD95C64F

            Issued to: Contoso, Inc
            Issued by: VeriSign Class 3 Code Signing 2010 CA
            Expires:   Thu Dec 04 15:59:59 2014
            SHA1 hash: EFC77FA6BA295580C2A2CD25B56C00606CA21269

The signature is timestamped: Mon Jan 27 14:48:55 2014
Timestamp Verified by:
    Issued to: Thawte Timestamping CA
    Issued by: Thawte Timestamping CA
    Expires:   Thu Dec 31 15:59:59 2020
    SHA1 hash: BE36A4562FB2EE05DBB3D32323ADF445084ED656

        Issued to: Symantec Time Stamping Services CA - G2
        Issued by: Thawte Timestamping CA
        Expires:   Wed Dec 30 15:59:59 2020
        SHA1 hash: 6C07453FFDDA08B83707C09B82FB3D15F35336B1

            Issued to: Symantec Time Stamping Services Signer - G4
            Issued by: Symantec Time Stamping Services CA - G2
            Expires:   Tue Dec 29 15:59:59 2020
            SHA1 hash: 65439929B67973EB192D6FF243E6767ADF0834E4
Cross Certificate Chain:
    Issued to: Microsoft Code Verification Root
    Issued by: Microsoft Code Verification Root
    Expires:   Sat Nov 01 05:54:03 2025
    SHA1 hash: 8FBE4D070EF8AB1BCCAF2A9D5CCAE7282A2C66B3     
       
 Issued to: VeriSign Class 3 Public Primary Certification Authority - G5
        Issued by: Microsoft Code Verification Root
        Expires:   Mon Feb 22 11:35:17 2021
        SHA1 hash: 57534CCC33914C41F70E2CBB2103A1DB18817D8B
            
            Issued to: VeriSign Class 3 Code Signing 2010 CA
            Issued by: VeriSign Class 3 Public Primary Certification Authority -  G5
            Expires:   Fri Feb 07 15:59:59 2020
            SHA1 hash: 495847A93187CFB8C71F840CB7B41497AD95C64F

                Issued to: Contoso, Inc
                Issued by: VeriSign Class 3 Code Signing 2010 CA
                Expires:   Thu Dec 04 15:59:59 2014
                SHA1 hash: EFC77FA6BA295580C2A2CD25B56C00606CA21269

Successfully verified: toaster.inf

Number of files successfully Verified: 1
Number of warnings: 0 
Number of errors: 0
```

Note the presence of Microsoft Code Verification Root in the certificate chain.

Next, check embed signing of the toaster.sys file.

```cpp
signtool verify  /v  /kp  toaster.sys
```

Command output:

```cpp
Verifying: toaster.sys Hash of file (sha1): CCF5F5C02FEDE87D92FCB7B536DBF5D5EFDB7B41

Signing Certificate Chain:
    Issued to: VeriSign Class 3 Public Primary Certification Authority - G5
    Issued by: VeriSign Class 3 Public Primary Certification Authority - G5
    Expires:   Wed Jul 16 15:59:59 2036
    SHA1 hash: 4EB6D578499B1CCF5F581EAD56BE3D9B6744A5E5

        Issued to: VeriSign Class 3 Code Signing 2010 CA
        Issued by: VeriSign Class 3 Public Primary Certification Authority - G5
        Expires:   Fri Feb 07 15:59:59 2020
        SHA1 hash: 495847A93187CFB8C71F840CB7B41497AD95C64F

            Issued to: Contoso, Inc
            Issued by: VeriSign Class 3 Code Signing 2010 CA
            Expires:   Thu Dec 04 15:59:59 2014             SHA1 hash: EFC77FA6BA295580C2A2CD25B56C00606CA21269 
The signature is timestamped: Mon Jan 27 14:48:55 2014 Timestamp Verified by:
    Issued to: Thawte Timestamping CA     Issued by: Thawte Timestamping CA     Expires:   Thu Dec 31 15:59:59 2020     SHA1 hash: BE36A4562FB2EE05DBB3D32323ADF445084ED656 
        Issued to: Symantec Time Stamping Services CA - G2         Issued by: Thawte Timestamping CA         Expires:   Wed Dec 30 15:59:59 2020         SHA1 hash: 6C07453FFDDA08B83707C09B82FB3D15F35336B1 
            Issued to: Symantec Time Stamping Services Signer - G4             Issued by: Symantec Time Stamping Services CA - G2             Expires:   Tue Dec 29 15:59:59 2020             SHA1 hash: 65439929B67973EB192D6FF243E6767ADF0834E4 
Cross Certificate Chain:
    Issued to: Microsoft Code Verification Root     Issued by: Microsoft Code Verification Root     Expires:   Sat Nov 01 05:54:03 2025     SHA1 hash: 8FBE4D070EF8AB1BCCAF2A9D5CCAE7282A2C66B3         
        Issued to: VeriSign Class 3 Public Primary Certification Authority - G5
        Issued by: Microsoft Code Verification Root
        Expires:   Mon Feb 22 11:35:17 2021
        SHA1 hash: 57534CCC33914C41F70E2CBB2103A1DB18817D8B

            Issued to: VeriSign Class 3 Code Signing 2010 CA
            Issued by: VeriSign Class 3 Public Primary Certification Authority -  G5
            Expires:   Fri Feb 07 15:59:59 2020
            SHA1 hash: 495847A93187CFB8C71F840CB7B41497AD95C64F 
                Issued to: Contoso, Inc                 Issued by: VeriSign Class 3 Code Signing 2010 CA                 Expires:   Thu Dec 04 15:59:59 2014                 SHA1 hash: EFC77FA6BA295580C2A2CD25B56C00606CA21269 
Successfully verified: toaster.sys 
Number of files successfully Verified: 1 Number of warnings: 0 Number of errors: 0 
```

Again, note the presence of Microsoft Code Verification Root in the certificate chain.

 

 





