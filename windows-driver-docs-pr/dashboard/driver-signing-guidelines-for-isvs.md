---
title: Driver Signing Guidelines for ISVs
description: Driver Signing Guidelines for ISVs
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 1d909826-bbf2-4a5c-9c6a-10e423880ee5
---

# Driver Signing Guidelines for ISVs


Your company's quality assurance processes are responsible for testing driver functionality during product development. When the driver is complete, you can verify that the driver is compatible with Windows and submit it to the Windows Certification Program for certification or digital signature. Any signed drivers may be distributed on Windows Update, regardless of whether the digital signature is obtained through certification, or through unclassified or “Other Device” testing.

The Windows Hardware Lab Kit (Windows HLK) supports driver testing for Windows 10.

The Windows Hardware Certification Kit (Windows HCK) supports driver testing for Windows 7, Windows 8, Windows 8.1, Windows Server 2008 R2, Windows Server 2012 and Windows Server 2012 R2.

The Windows Logo Kit 1.6 (WLK 1.6) supports driver testing for Windows Server 2003 and Windows Server 2008.

The Windows 10, Windows 8.1, Windows 8, Windows 7, Windows Server 2012 R2, Windows Server 2012, and Windows Server 2008 R2 Certification Programs for software have the following digital signature requirements:

-   Kernel-mode software must be digitally signed to be loaded on x64-based versions of Windows 7, Windows 8, Windows 8.1, Windows Server 2008 R2, Windows Server 2012 and Windows Server 2012 R2 and must be signed by Microsoft for the Windows Hardware Certification Program.

-   Drivers that are loaded by the Windows operating system loader (boot-start drivers) must contain an embedded signature, for both x86-based and x64-based versions of Windows 7, Windows 8, Windows 8.1, Windows Server 2008 R2, Windows Server 2012 and Windows Server 2012 R2.

-   Filter drivers that are included in the Filter Drivers Certification Program must meet the filter driver requirements and pass the Windows HCK to be certified.

For a list of support contacts for logo and certification program procedures and tools, see [Certification Program Support Contacts](http://msdn.microsoft.com/library/windows/hardware/gg487491).

## <span id="How_to_test_drivers_by_using_the_Windows_Logo_Program_and_or_Windows_Certification_Program_tests"></span><span id="how_to_test_drivers_by_using_the_windows_logo_program_and_or_windows_certification_program_tests"></span><span id="HOW_TO_TEST_DRIVERS_BY_USING_THE_WINDOWS_LOGO_PROGRAM_AND_OR_WINDOWS_CERTIFICATION_PROGRAM_TESTS"></span>How to test drivers by using the Windows Logo Program and/or Windows Certification Program tests


To test drivers by using the Windows Logo Program and Windows Certification Program tests, follow these steps:

****

1.  [Establish a Hardware Dashboard account in the Windows Dev Center.](https://sysdev.microsoft.com/)

    You must have a dashboard account in order to submit drivers to the Windows Certification Program. To get one, follow these steps:

    1.  Get a code signing certificate. The certificate is required for submitting your product to the Windows Certification Program, to ensure that your organization is authentic and to secure transmission of drivers and test results to Microsoft.

    2.  Provide account administrator contact information.

    3.  Sign the latest Windows Certification Program Testing Agreement and the latest applicable Certification License.

    4.  Provide company address information.

2.  Review the latest requirements for the [Unclassified category in the Windows Logo Program](http://msdn.microsoft.com/library/windows/hardware/dn423132), [Device Fundamentals that would apply to “Other Device” or Driver in the Windows Hardware Certification Program](http://msdn.microsoft.com/library/windows/hardware/jj134349.aspx), and/or [Filter Driver Product Type in the Windows Certification Program](http://msdn.microsoft.com/library/windows/hardware/jj128255).

    -   The Unclassified and “Other Device” categories are described in this [Windows Certification Program Policy document \[119 KB - DOCX\]](http://download.microsoft.com/download/4/D/D/4DD894CD-62C8-488F-944D-4E5F8BA40114/hardware-certification-policies-processes-hck2-1.docx), requirement

    -   Boot start drivers must be self-signed with an embedded signature, as described in the requirement Device.DevFund.Reliability.Signable section of the [Windows Certification Program, Hardware Certification Requirements](http://msdn.microsoft.com/library/windows/hardware/jj134357) document.

    -   The Filter Drivers Product Type is described in the Filter Drivers area of the Windows 8 Filter Driver requirements.

3.  Install the [Windows Logo Kit](http://msdn.microsoft.com/library/windows/hardware/gg487530) and/or [Windows HCK](https://go.microsoft.com/fwlink/p/?LinkId=733613) and review the instructions for using it.

    -   The Windows Logo Kit and Windows HCK page explains how to decide which version of the kit to use. In most cases, it’s best to use the latest version of the kit.

    -   The training videos and other documentation help you set up and use the kit, which you’ll use to test your driver in the next step. You should take some time to review these materials before testing your driver.

4.  Run the tests for [Unclassified category](http://msdn.microsoft.com/library/windows/hardware/dn423132) “Other Devices”, and/or [Filter Drivers Product Type](http://msdn.microsoft.com/library/windows/hardware/hh998741).

    -   Before testing, make sure you have installed all the latest updates for the [Windows Logo Kit](http://msdn.microsoft.com/library/windows/hardware/gg487530) or [Windows HCK](https://go.microsoft.com/fwlink/p/?LinkId=733613).

    -   Use the kit to automatically detect the appropriate tests. Note that for drivers that do not have features that the Kit detects \[Other Devices\], only a small number of tests may be scheduled.

    -   Run all tests listed in the kit for your driver. If you want to qualify for multiple operating system families, you must test separately for each family.

    -   Check the [Windows Hardware Certification Blog](http://blogs.msdn.com/b/windows_hardware_certification/) for updates in test policies and processes.

5.  [Solve test failures](http://msdn.microsoft.com/library/windows/hardware/jj124946).

    Use a systematic strategy for solving failures encountered during testing and in test logs:

    -   If a test results in a false failure, this is called an erratum. The Hardware Dev Center Dashboard provides [filters]( http://go.microsoft.com/fwlink/p/?LinkId=618594) (called DTM filters) that eliminate these false failures in known cases. To get the latest filters, log on to the dashboard with your account, navigate to **Hardware certification** and click **WLK Filters or HCK Filters** in the **Downloads** section.

    -   For information about technical support, see [Certification Program Support Contacts](http://msdn.microsoft.com/library/windows/hardware/dn251523.aspx).

6.  **Prepare your test submission for the Hardware Dev Center Dashboard.**

    After all test failures have been fixed or clearly resolved by errata or contingencies, you are ready to submit your test logs and driver packages to the dashboard. You must run tests on the driver and submit results for each operating system family. In some cases, it is possible to merge the test results package in order to obtain driver certification for these operating systems. For information about submitting a Windows HCK package, see [Create a New Hardware Certification Submission](http://msdn.microsoft.com/library/windows/hardware/hh973603.aspx). For information about submitting a WLK package, see [Create a New Hardware Logo Submission](http://msdn.microsoft.com/library/windows/hardware/br230808.aspx).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhw_dashboard\hw_dashboard%5D:%20Driver%20Signing%20Guidelines%20for%20ISVs%20%20RELEASE:%20%281/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




