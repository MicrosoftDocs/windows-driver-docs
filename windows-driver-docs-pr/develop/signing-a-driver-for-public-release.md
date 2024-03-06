---
title: Signing a Driver for Public Release
description: Before you release a driver package to the public, we recommend that you submit the package for certification.
ms.date: 04/20/2017
---

# Signing a Driver for Public Release

Before you release a driver package to the public, we recommend that you submit the package for certification. For more information, see [Windows Hardware Certification](/previous-versions/windows/hardware/hck/jj124227(v=vs.85)) and [Hardware Dashboard Services](../dashboard/index.yml). To submit a driver package for certification, you must sign the package with a certificate that you obtain from a trusted certification authority like VeriSign. For more information, see [Get a VeriSign Certificate](../dashboard/index.yml). You will also need a cross certificate, which is provided by Microsoft.

Suppose you have obtained a pair of files from Verisign: a private key file (PVK) and a software publishing certificate (SPC). Also suppose you have a Microsoft Visual Studio solution that contains a driver project named MyDriver and a driver package project named MyDriver Package. To sign your driver package, follow these steps.

1.  Use the [**Pvk2Pfx**](../devtest/pvk2pfx.md) tool to create a Personal Information Exchange (PFX) certificate. The **Pvk2Pfx** tool takes your PVK and SPC files as input and creates a single PFX file. For this exercise, assume that your PFX file is named MyCert.pfx.

    **Note**  Once you have created your PFX file, you can reuse it for other driver projects and on other driver development computers.
2.  To determine which cross certificate you need, see [Cross-Certificates for Kernel Mode Code Signing](../install/cross-certificates-for-kernel-mode-code-signing.md). Verify that the required cross certificate is in $(BASEDIR)\\CrossCertificates, where $(BASEDIR) is the base directory of the Windows kits (for example c:\\Program Files (x86)\\Windows Kits\\8.0\\CrossCertificates). If the required cross certificate is not there, download the cross certificate from Microsoft, and copy it to $(BASEDIR)\\CrossCertificates.
3.  In Visual Studio, open the solution that contains the MyDriver and MyDriver Package projects. If the Solution Explorer window is not already open, choose **Solution Explorer** from the **View** menu. In the Solution Explorer window, select and hold (or right-click) the package project, **MyDriver Package**, and choose **Properties**.

4.  In the property pages for the package, navigate to **Configuration Properties &gt; Driver Signing &gt; General**. In the **Sign Mode** drop-down list, select **Production Sign**. For **Production Certificate**, do one of the following:

    -   Enter the path to your signing certificate (for example c:\\Certs\\MyCert.pfx).
    -   Choose **Select From File**, and browse to your signing certificate.
    -   Choose **Select From Store** and choose a certificate that you previously imported into a certificate store.

        **Note**  To import a certificate into a store, select and hold (or right-click) the certificate file (PFX file), and choose **Install PFX**. Follow the instructions in the Certificate Import Wizard.

        **Note**  If you decide to use a different certificate at a later time, be sure that your new certificate gets imported into the certificate store. If you choose **Select From File** and browse to your new certificate, the new certificate will be automatically imported into the certificate store. However, if you manually enter the path to your new certificate, it will not be automatically imported into the certificate store. In that case, you must select and hold (or right-click) your new certificate file and choose **Install PFX**.
5.  On the **Driver Signing &gt; General** property page, for **TimeStampServer**, select one of the time stamp servers in the drop-down list.

    **Note**  Using one of the time stamp servers in the drop-down list requires that you be connected to the Internet when you build your driver package. If you need to be disconnected from the Internet when you build your driver package, clear the **TimeStampServer** field.
6.  In the property pages for the package, navigate to **Configuration Properties &gt; Inf2Cat &gt; General**. In the **Run Inf2Cat** drop-down list, select **Yes**.

7.  Close the property pages for the package.
8.  Select and hold (or right-click) the driver project, **MyDriver**, and choose **Properties**
9.  In the property pages for the driver, navigate to **Configuration Properties &gt; Driver Signing &gt; General**. Set **TimeStampServer** to the same value that you used in the driver package properties. Set **Sign Mode** to **Production Sign**, and set **Production Certificate** to the same value that you used in the driver package properties.

10. When you are ready to build your driver package, press **F5**. Visual Studio will automatically sign your package and your driver file. If you have configured deployment, Visual Studio will also deploy your signed driver package to a test computer. For more information, see [Provision a computer for driver deployment and testing (WDK 8.1)](../gettingstarted/provision-a-target-computer-wdk-8-1.md).

## <span id="Viewing_the_driver_package_files"></span><span id="viewing_the_driver_package_files"></span><span id="VIEWING_THE_DRIVER_PACKAGE_FILES"></span>Viewing the driver package files


After you build your solution, navigate in File Explorer to the folder that contains your driver package. One of the files in the package is a catalog file. The catalog file contains the digital signature for the package. For an example of viewing the files in a signed package, see [Writing a KMDF driver based on a template](../gettingstarted/writing-a-kmdf-driver-based-on-a-template.md).

## <span id="Getting_a_WHQL_release_signature"></span><span id="getting_a_whql_release_signature"></span><span id="GETTING_A_WHQL_RELEASE_SIGNATURE"></span>Getting a WHQL release signature


When your driver package passes the certification tests, it can be signed by Windows Hardware Quality Labs (WHQL). If your driver package is signed by WHQL, it can be distributed through the Windows Update program or other Microsoft-supported distribution mechanisms.

To install on Windows 10, 8.1, 8, and 7, your driver package can have a single SHA1 signature.

Starting in Windows 10, you also need to submit any new Windows 10 kernel mode driver for digital signing on the [Windows Hardware Developer Center Dashboard portal](https://partner.microsoft.com/dashboard).  Both kernel and user mode driver submissions must have a valid [Extended Validation (“EV”) Code Signing Certificate](../dashboard/index.yml).

** Note **  SHA1 deprecation does not apply to drivers.

## <span id="Signing_a_package_compared_to_signing_an_individual_driver_file"></span><span id="signing_a_package_compared_to_signing_an_individual_driver_file"></span><span id="SIGNING_A_PACKAGE_COMPARED_TO_SIGNING_AN_INDIVIDUAL_DRIVER_FILE"></span>Signing a package compared to signing an individual driver file


A driver package contains several files. Typically a driver package has one or more driver files, an information file (INF file), and a catalog file. The catalog file contains information about the other files in the package. When you sign the catalog file, the signature in the catalog file serves as the signature for the entire driver package. In other words, *signing the catalog file* is the same as *signing the driver package*.

In most cases, it is sufficient to sign the driver package, and it is not necessary to sign individual driver files. Sometimes, however, you need to sign both the package and the individual driver files. For example, boot-start driver files must be individually signed. Signing an individual driver file is referred to as *embedding a signature in the driver file*.

Suppose you have a Visual Studio solution that contains a driver project named MyDriver and a driver package project named MyDriver Package. Visual Studio provides two sets of property pages: one for My Driver and one for My Driver Package. To sign the driver package, set the **Driver Signing** properties of My Driver Package. To embed a signature in the individual driver file, set the **Driver Signing** properties of My Driver.

When you set the driver package properties for production signing, remember to adjust the signing properties of the individual driver files accordingly. Either turn off signing for the individual driver files, or set the individual driver files to use the same certificate that you specified for the package.

**Note**  To see the hash (also called the thumb print) of a certificate, open a Command Prompt window and navigate to the directory that contains your certificate. Enter the command **certutil -dump** *CertName.pfx*, where *CertName.pfx* is the name of your certificate.

     

## <span id="related_topics"></span>Related topics


* [Driver Signing changes in Windows 10](https://techcommunity.microsoft.com/t5/Windows-Hardware-Certification/bg-p/WindowsHardwareCertification)
* [Availability of SHA-2 Code Signing Support for Windows 7 and Windows Server 2008 R2](/security-updates/SecurityAdvisories/2015/3033929)
* [Signing a Driver](signing-a-driver.md)
* [Windows Hardware Certification](/previous-versions/windows/hardware/hck/jj124227(v=vs.85))
* [Hardware Dashboard Services](../dashboard/index.yml)
* [Driver Signing Requirements for Windows](/previous-versions/windows/hardware/design/dn653563(v=vs.85))
* [Cross-Certificates for Kernel Mode Code Signing](../install/cross-certificates-for-kernel-mode-code-signing.md)
* [Kernel-Mode Code Signing Walkthrough](/previous-versions/windows/hardware/design/dn653569(v=vs.85))
* [Driver Signing](../install/driver-signing.md)
* [Installing a Boot-Start Driver](../install/installing-a-boot-start-driver.md)
* [Tools for Signing Drivers](../devtest/tools-for-signing-drivers.md)
