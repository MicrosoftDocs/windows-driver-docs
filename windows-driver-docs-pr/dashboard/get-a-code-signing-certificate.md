---
title: Get a code signing certificate
description: Get a code signing certificate
ms.assetid: 6CF4111A-C645-40F5-8D45-55F46B3C0740
ms.topic: article
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Get a code signing certificate

Before you can establish a Hardware Dev Center hardware dashboard account, you need to get a code signing certificate to secure your digital information. This certificate is the accepted standard for establishing your company’s ownership of the code you submit. It allows you to digitally sign PE binaries, such as .exe, .cab, .dll, .ocx, .msi, .xpi and .xap files.

## <span id="Step_1__Determine_which_type_of_code_signing_certificate_you_need"></span><span id="step_1__determine_which_type_of_code_signing_certificate_you_need"></span><span id="STEP_1__DETERMINE_WHICH_TYPE_OF_CODE_SIGNING_CERTIFICATE_YOU_NEED"></span>Step 1: Determine which type of code signing certificate you need


-   Microsoft accepts standard code signing and extended validation (EV) code signing certificates from partners enrolled and authorized for Kernel Mode Code Signing as part of the Microsoft Trusted Root Certificate Program. If you already have an approved standard or EV certificate from one of these authorities, you can use it to establish a Hardware Dev Center hardware dashboard account. If you don’t have a certificate, you’ll need to buy a new one.

-   The table below provides the details of the Certificate requirements for each of the dashboard services.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Dashboard service/permission</th>
<th>Code signing certificate requirement</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Bug management</p></td>
<td><p>Standard or EV</p></td>
</tr>
<tr class="even">
<td><p>DDC – Driver Distribution Center</p></td>
<td><p>Standard or EV</p></td>
</tr>
<tr class="odd">
<td><p>Device Metadata</p></td>
<td><p>Standard or EV</p></td>
</tr>
<tr class="even">
<td><p>Report Data</p></td>
<td><p>Standard or EV</p></td>
</tr>
<tr class="odd">
<td><p>Submissions</p></td>
<td><p>Standard or EV</p></td>
</tr>
<tr class="even">
<td><p>WRD – Windows Remote Debugging</p></td>
<td><p>Standard or EV</p></td>
</tr>
<tr class="odd">
<td><p>LSA</p></td>
<td><p>EV</p></td>
</tr>
<tr class="even">
<td><p>UEFI</p></td>
<td><p>EV</p></td>
</tr>
<tr class="odd">
<td><p>Windows Reference Design</p></td>
<td><p>Standard or EV</p></td>
</tr>
<tr class="even">
<td><p>Attestation Driver Signing</p></td>
<td><p>EV</p></td>
</tr>
</tbody>
</table>

 
> [!NOTE] 
> The Hardware Dev Center dashboard will enforce mandatory EV certificates for submissions later this year.

 

### <span id="standardcode"></span><span id="STANDARDCODE"></span>Code signing certificates for Hardware Dev Center Dashboard

There are two types of code signing certificates available today:

**Standard Code Signing**

-   Provides standard level of identity validation

-   Requires shorter processing times and lower cost

-   Can be used for all Hardware Dev Center hardware dashboard services except LSA, and UEFI file signing services.

-   In Windows 10 for desktop editions (Home, Pro, Enterprise, and Education), standard code signing cannot be used for kernel-mode drivers. For more info about these changes, see [Code Signing FAQ](#code-signing-faq).

**Extended Validation (EV) Code Signing**

-   Provides the highest level of identity validation

-   Requires longer processing times and higher cost due to an extensive verification process

-   Can be used for all Hardware Dev Center hardware dashboard services, and is required for LSA and UEFI file signing services

-   In Windows 10 for desktop editions, all kernel-mode drivers must be signed by the Hardware Dev Center Dashboard and the Hardware Dev Center Dashboard requires an EV certificate. For more info about these changes, see [Code Signing FAQ](#code-signing-faq).

## <span id="Step_2__Buy_a_new_code_signing_certificate"></span><span id="step_2__buy_a_new_code_signing_certificate"></span><span id="STEP_2__BUY_A_NEW_CODE_SIGNING_CERTIFICATE"></span>Step 2: Buy a new code signing certificate


If you don’t have an approved standard or EV code signing certificate, you can buy one from one of the certificate authorities below.

**Standard code signing certificates**

-   [Buy a Symantec standard code signing certificate](http://go.microsoft.com/fwlink/?LinkId=393247)

-   [Buy a Certum standard code signing cert](https://go.microsoft.com/fwlink/?linkid=843062) (Supported only in the Hardware Dev Center Dashboard)

-   [Buy an Entrust standard code signing cert](https://go.microsoft.com/fwlink/?linkid=843067)

-   [Buy a GlobalSign standard code signing cert](http://go.microsoft.com/fwlink/p/?LinkId=620887)

-   [Buy a Comodo standard code signing cert](https://go.microsoft.com/fwlink/?linkid=863206)

-   [Buy a DigiCert standard code signing certificate](http://go.microsoft.com/fwlink/?LinkId=393249)

    1.  On the **DigiCert Code Signing Certificates for Sysdevs** page, click **Start**.

    2.  On the **DigiCert Order Form** page (Step 1), in the **Code Signing** section, click **Code Signing Certificate**.

    3.  Still on Step 1, scroll down to the **Platform** section, select **Microsoft Authenticode** from the drop-down list, and then click **Continue**.

    4.  Follow the instructions provided by DigiCert to buy a certificate.

**Extended validation code signing certificates** (required for UEFI, kernel-mode drivers, and LSA certifications)

-   [Buy a Symantec EV code signing certificate](http://go.microsoft.com/fwlink/?LinkId=393248)

-   [Buy a Certum EV code signing cert](https://go.microsoft.com/fwlink/?linkid=843061)

-   [Buy an Entrust EV code signing cert](https://go.microsoft.com/fwlink/?linkid=843068)

-   [Buy a GlobalSign EV code signing certificate](http://go.microsoft.com/fwlink/p/?LinkId=620888)

-   [Buy a Comodo EV code signing certificate](https://go.microsoft.com/fwlink/?linkid=863208)

-   [Buy a DigiCert EV code signing certificate](http://go.microsoft.com/fwlink/?LinkId=393249)

    1.  On the **DigiCert Code Signing Certificates for Sysdevs** page, click **Start**.

    2.  On the **DigiCert Order Form** page (Step 1), in the **Code Signing** section, click **EV Code Signing Certificate**, fill out the rest of the form, and then click **Continue**.

    3.  Follow the instructions provided by DigiCert to buy a certificate.

## <span id="Step_3__Retrieve_code_signing_certificates_"></span><span id="step_3__retrieve_code_signing_certificates_"></span><span id="STEP_3__RETRIEVE_CODE_SIGNING_CERTIFICATES_"></span>Step 3: Retrieve code signing certificates


Once the certificate authority has verified your contact information and your certificate purchase is approved, follow their directions to retrieve the certificate.

**Note**  
You must use the same computer and browser to retrieve your certificate.

 

## <span id="Next_steps"></span><span id="next_steps"></span><span id="NEXT_STEPS"></span>Next steps


-   If you’re setting up a new Hardware Dev Center hardware dashboard account, follow the steps in [Register for the Hardware Program](register-for-the-hardware-program.md).

-   If you’ve already set up a Hardware Dev Center hardware dashboard account and need to renew a certificate, follow the steps in [Update a code signing certificate](https://msdn.microsoft.com/library/windows/hardware/update-a-code-signing-certificate).

## Code Signing FAQ


This section provides answers to frequently asked questions about code signing for Windows 10. Additional code signing information is available on the Windows Hardware Certification blog.

-   [Driver Signing Changes in Windows 10](http://blogs.msdn.com/b/windows_hardware_certification/archive/2015/04/01/driver-signing-changes-in-windows-10.aspx)
-   [Update on Sysdev EV Certificate requirement](http://blogs.msdn.com/b/windows_hardware_certification/archive/2015/10/20/update-on-sysdev-ev-certificate-requirement.aspx)

**HLK Tested and Dashboard Signed Drivers**

-   A dashboard signed driver that has passed the HLK tests will work on Windows Vista through Windows 10, including Windows Server editions. This is the recommended method for driver signing, because it allows a single process for all OS versions. In addition, HLK tested drivers demonstrate that a manufacturer has rigorously tested their hardware to meet all of Microsoft's requirements with regards to reliability, security, power efficiency, serviceability, and performance, so as to provide a great Windows experience. This includes compliance with industry standards and adherence with Microsoft specifications for technology-specific features, helping to ensure correct installation, deployment, connectivity and interoperability. For more information about the HLK, see [Windows Hardware Compatibility Program](https://docs.microsoft.com/windows-hardware/design/compatibility/index).

**Windows 10 Desktop Attestation Signing**

-   A dashboard signed driver using attestation signing will only work on Windows 10 Desktop and later versions of Windows.
-   An attestation signed driver will only work for Windows 10 Desktop; it will not work for other versions of Windows, such as Windows Server 2016, Windows 8.1, or Windows 7.
-   Attestation signing supports Windows 10 Desktop kernel mode and user mode drivers. Although user mode drivers do not need to be signed by Microsoft for Windows 10, the same attestation process can be used for both user and kernel mode drivers.

**Windows 10 Earlier Certificate Transition Signing**

-   A driver signed with any certificate issued after July 29th, 2015, with time stamping, is not recommended for Windows 10.
-   A driver signed with any certificate that expires after July 29th, 2015, without time stamping, will work on Windows 10 until the certificate expires.

**Cross-Signing and SHA-256 Certificates**

Cross-signing describes a process where a driver is signed with a certificate issued by a Certificate Authority (CA) that is trusted by Microsoft. For more information, see [Cross-Certificates Overview](https://docs.microsoft.com/windows-hardware/drivers/install/cross-certificates-for-kernel-mode-code-signing).

-   Windows 8 and later versions support SHA-256.
-   Windows 7, if patched, supports SHA-256. If you need to support unpatched devices that run Windows 7, you need to either cross-sign with a SHA-1 certificate or submit to the Dashboard for signing. Otherwise, you can either cross-sign with SHA-1 or SHA-2 certificate or create an HLK/HCK submission for signing.
-   Because Windows Vista doesn’t support SHA-256, you need to either cross-sign with a SHA-1 certificate or create an HLK/HCK submission for Windows Vista driver signing.
-   A driver cross-signed with a SHA-256 certificate (including an EV certificate) issued prior to July 29th, 2015 will work on Windows 8 and later. It will not work on Windows Vista or Windows Server 2008.
-   A driver cross-signed with a SHA-256 certificate (including an EV certificate) issued prior to July 29th, 2015 will work on Windows 7 or Server 2008R2 if the patch issued through Windows Update earlier this year has been applied. For more information, see [Availability of SHA-2 Hashing Algorithm for Windows 7 and Windows Server 2008 R2](https://technet.microsoft.com/library/security/2949927.aspx) and [Microsoft security advisory: Availability of SHA-2 code signing support for Windows 7 and Windows Server 2008 R2: March 10, 2015](https://support.microsoft.com/kb/3033929).
-   A cross-signed driver using a SHA-1 certificate issued prior to July 29th, 2015 will work on all platforms starting with Windows Vista through Windows 10.
-   A cross-signed driver using a SHA-1 or SHA-256 certificate issued after July 29th, 2015 is not recommended for Windows 10.
-   For more information about the effort to move to SHA-256 Certificates, see [Windows Enforcement of Authenticode Code Signing and Timestamping](http://social.technet.microsoft.com/wiki/contents/articles/32288.windows-enforcement-of-authenticode-code-signing-and-timestamping.aspx)

**Device Guard**

-   Enterprises may implement a device guard policy to modify the driver signing requirements using Windows 10 Enterprise edition. Device Guard provides an enterprise-defined code integrity policy, which may be configured to require at least an attestation-signed driver. For more information about Device Guard, see [Device Guard certification and compliance](https://technet.microsoft.com/library/mt219733.aspx).

**Windows Server**

-   The dashboard will not accept attested device and filter driver signing submissions for Windows Server 2016.
-   The dashboard will only sign device and filter drivers that have successfully passed the HLK tests.
-   Windows Server 2016 will only load dashboard signed drivers that have successfully passed the HLK tests.

**EV Certs**

-   As of October 31, 2015, your Sysdev dashboard account must have at least one EV certificate associated with it to submit binaries for attestation signing or to submit binaries for HLK certification.
-   You can sign with either your EV certificate or your existing standard certificates until May 1, 2016. After May 1, 2016, you need to use an EV certificate to sign the cab file that is submitted.
-   The submitted binaries themselves do not need to be signed. Only the submission cab file needs to be signed with an EV certificate.

**OS Support Summary**

This table summarizes the driver signing requirements for Windows.

|                                    |                                |                                    |                                                                                |
|------------------------------------|--------------------------------|------------------------------------|--------------------------------------------------------------------------------|
|                                    | *Attestation Dashboard Signed* | *HLK Test Passed Dashboard Signed* | *Cross-signed using a SHA-1 certificate issued prior to July 29, 2015*         |
| Windows Vista                      | No                             | Yes                                | Yes                                                                            |
| Windows 7                          | No                             | Yes                                | Yes                                                                            |
| Windows 8 / 8.1                    | No                             | Yes                                | Yes                                                                            |
| Windows 10                         | Yes                            | Yes                                | Yes                                                                            |
| Windows 10 - DG Enabled            | \*Configuration Dependent      | \*Configuration Dependent          | \*Configuration Dependent                                                      |
| Windows Server 2008 R2             | No                             | Yes                                | Yes                                                                            |
| Windows Server 2012 R2             | No                             | Yes                                | Yes                                                                            |
| Windows Server 2016                | No                             | Yes                                | Yes                                                                            |
| Windows Server 2016 – DG Enabled   | \*Configuration Dependent      | \*Configuration Dependent          | \*Configuration Dependent                                                      |
| Windows IoT Enterprise             | Yes                            | Yes                                | Yes                                                                            |
| Windows IoT Enterprise- DG Enabled | \*Configuration Dependent      | \*Configuration Dependent          | \*Configuration Dependent                                                      |
| Windows IoT Core(1)                | Yes (Not Required)             | Yes (Not Required)                 | Yes (Cross signing will also work for certificates issued after July 29, 2015) |

 

\*Configuration Dependent –With Windows 10 Enterprise edition, organizations can use Device Guard to define custom driver signing requirements. For more information about Device Guard, see [Device Guard certification and compliance](https://technet.microsoft.com/library/mt219733.aspx).

(1) Driver signing is required for manufacturers building retail products (i.e. for a non-development purpose) with IoT Core. For a list of approved Certificate Authorities (CAs), see [Cross-Certificates for Kernel Mode Code Signing](https://docs.microsoft.com/windows-hardware/drivers/install/cross-certificates-for-kernel-mode-code-signing). Note that if UEFI Secure Boot is enabled, then drivers must be signed.

 

 

