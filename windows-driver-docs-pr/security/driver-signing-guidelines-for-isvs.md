---
title: Driver signing guidelines for ISVs
description: Your company's quality assurance processes are responsible for testing driver functionality during product development.
ms.assetid: 3E14DA54-8F37-4C5F-BF26-3AB13F8457D5
ms.author: windowsdriverdev
ms.date: 06/06/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Driver signing guidelines for ISVs


Your company's quality assurance processes are responsible for testing driver functionality during product development. When the driver is complete, you can verify that the driver is compatible with Windows and submit it to the Windows Certification Program for certification or signature. Any signed drivers may be distributed on Windows Update, regardless of whether the signature is obtained through certification or unclassified testing.

Windows 7 drivers that pass the tests for the Unclassified category in the Windows Logo Kit (WLK) qualify for a digital signature. These drivers may also be tested for certification using the Windows Hardware Certification Kit (HCK).

Windows 8 drivers receive more robust testing in the HCK. Filter drivers that meet the filter driver requirements and pass the tests for the filter driver certification program qualify for certification and listing in the Windows Compatibility Center.

The Windows 7, Windows 8, and Windows Server 2012 Certification Programs for software have the following digital signature requirements:

-   Kernel-mode software must be digitally signed to be loaded on x64-based versions of Windows 7, Windows Server 2008 R2, Windows 8, and Windows Server 2012, and must be signed by Microsoft for the Windows Logo Program (formerly known as "WHQL signature").
-   Drivers that are loaded by the Windows operating system loader (boot-start drivers) must contain an embedded signature, for both x86-based and x64-based versions of Windows 7, Windows Server 2008 R2, Windows 8, and Windows Server 2012.
-   Filter drivers that are included in the Filter Drivers Certification Program must meet the filter driver requirements and pass the Windows HCK to be certified.

For a list of support contacts for logo and certification program procedures and tools, see [Certification Program Support Contacts](http://msdn.microsoft.com/en-US/library/windows/hardware/gg487491).

To test drivers by using the Windows Logo Program and Windows Certification Program tests, follow these steps:

1.  [Establish a Hardware Dashboard account in the Windows Dev Center](https://sysdev.microsoft.com/).

    You must have a dashboard account in order to submit drivers to the Windows Certification Program. To get one, follow these steps:

    1.  Get a VeriSign certificate. The certificate is required for submitting your product to the Windows Certification Program, to ensure that your organization is authentic and to secure transmission of drivers and test results to Microsoft.
    2.  Provide account administrator contact information.
    3.  Sign the latest Windows Certification Program Testing Agreement and the latest applicable Certification License.
    4.  Provide billing information.

2.  Review the latest requirements for the [Unclassified category in the Windows Logo Program](http://msdn.microsoft.com/library/windows/hardware/dn423132) and/or [Filter Driver Product Type in the Windows Certification Program](http://msdn.microsoft.com/en-US/library/windows/hardware/jj128255).

    To get a digital signature or certification for a software driver, you must qualify your driver through the Unclassified category of the Windows Logo Program or Filter Driver Product Type of the Windows Certification Program.

    -   The Unclassified category is described in the requirement POLICY-0021.
    -   Boot start drivers must be self-signed with an embedded signature, as described in the requirement DEVFUND-0029.
    -   The Filter Drivers Product Type is described in the Filter Drivers area of the Windows 8 Filter Driver requirements.

3.  Install the [Windows Logo Kit](http://msdn.microsoft.com/en-US/library/windows/hardware/gg487530) and/or [Windows HCK](https://go.microsoft.com/fwlink/p/?LinkId=733613) and review the instructions for using it.
    -   The Windows Logo Kit and Windows HCK page explains how to decide which version of the kit to use. In most cases, it’s best to use the latest version of the kit.
    -   The training videos and other documentation help you set up and use the kit, which you’ll use to test your driver in the next step. You should take some time to review these materials before testing your driver.

4.  Run the tests for the [Unclassified category](http://msdn.microsoft.com/library/windows/hardware/dn423132) and/or [Filter Drivers Product Type](http://msdn.microsoft.com/en-US/library/windows/hardware/jj124779).
    -   Before testing, make sure you have installed all the latest updates for the [Windows Logo Kit](http://msdn.microsoft.com/en-US/library/windows/hardware/gg487530) or [Windows HCK](https://go.microsoft.com/fwlink/p/?LinkId=733613).
    -   Use the kit to automatically detect the appropriate tests.
    -   Run all tests listed in the kit for your driver. If you want to qualify for multiple operating system families, you must test separately for each family.
    -   Subscribe to the [Windows Hardware Certification blog](http://blogs.msdn.com/b/windows_hardware_certification/) for updates in test policies and processes. Previously published editions are available in the archives.

5.  [Solve test failures](http://msdn.microsoft.com/en-US/library/windows/hardware/jj124946).

    Use a systematic strategy for solving failures encountered during testing and in test logs:

    -   If a test results in a false failure, this is called an erratum. The Hardware Dashboard provides filters (called [DTM filters](http://sysdev.microsoft.com/en-US/Hardware/EC/)) that eliminate these false failures in known cases. To get the latest filters, log on to the dashboard with your account, navigate to the **Hardware certification** and click **WLK Filters** or **HCK Filters** in the **Downloads** section.
    -   For information about technical support, see [Certification Program Support Contacts](http://msdn.microsoft.com/en-US/library/windows/hardware/gg487491).

6.  [Prepare your test submission for the Hardware Dashboard](http://msdn.microsoft.com/windows/hardware/br230803.aspx).

    After all test failures have been fixed or clearly resolved by errata or contingencies, you are ready to submit your test logs and driver packages to the dashboard. You must submit separate packages for each operating system family.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[hw_design\hw_design]:%20Driver%20signing%20guidelines%20for%20ISVs%20%20RELEASE:%20%286/16/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




