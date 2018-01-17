---
title: Windows Hardware Dev Center dashboard
description: The Windows Hardware Dev Center dashboard allows you to submit hardware for certification, and code sign and publish your drivers to Windows Update.
ms.assetid: da6fe9f5-7495-4aec-b6c2-c53402cb8ea0
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Windows Hardware Dev Center dashboard


The Windows Hardware Dev Center dashboard allows you to submit hardware for certification, and code sign and publish your drivers to Windows Update. You can also now use shipping labels to easily collaborate on driver development with your business partners.

To get started watch our [introductory video series](http://go.microsoft.com/fwlink/?LinkID=828003) to learn more about the new dashboard. See [Get started with the Hardware Program](get-started-with-the-hardware-dashboard.md) for registering and using.

## <span id="What_s_new_in_the_Windows_Hardware_Dev_Center_dashboard"></span><span id="what_s_new_in_the_windows_hardware_dev_center_dashboard"></span><span id="WHAT_S_NEW_IN_THE_WINDOWS_HARDWARE_DEV_CENTER_DASHBOARD"></span>What's new in the Windows Hardware Dev Center dashboard


The Windows Hardware Dev Center dashboard replaces the [Hardware Dev Center (Sysdev)](dashboard-services.md) for most hardware tasks. The dashboard allows you to create and manage your submissions quickly and easily, with improved experiences for:

-   HCK/HLK device certification submissions
-   Publishing to Windows Update. You can now create shipping labels with promotions (critical and/or dynamic update) directly from the dashboard.
-   Sharing your driver with another company (Resell)
-   Customizing your driver after initial certification (DUA)
-   Managing your users and legal agreements
-   System/Hardware certification submissions

## <span id="Currently_unsupported_tasks"></span><span id="currently_unsupported_tasks"></span><span id="CURRENTLY_UNSUPPORTED_TASKS"></span>Currently unsupported tasks


You must continue to use [Hardware Dev Center (Sysdev)](dashboard-services.md) to complete the following tasks.

> [!IMPORTANT]  
> The dashboard submission REST APIs will no longer be available for use as of November 10th, 2016. APIs for driver submissions are under consideration for a future release.

 

-   [WLK device certification submissions](https://go.microsoft.com/fwlink/?linkid=830380)
-   [Attestation signing](attestation-signing-a-kernel-driver-for-public-release.md)
-   [Device Metadata](https://go.microsoft.com/fwlink/?linkid=830383)
-   [Bug management](https://go.microsoft.com/fwlink/?linkid=830385)
-   [Remote Debugging](https://go.microsoft.com/fwlink/?linkid=830386) (WRD)
-   [Win32 app certification submissions](https://go.microsoft.com/fwlink/?linkid=830388)
-   [Certified Products List](https://go.microsoft.com/fwlink/?linkid=830390)

## <span id="Transition_timeframes"></span><span id="transition_timeframes"></span><span id="TRANSITION_TIMEFRAMES"></span>Transition timeframes


This transition timeframe table contains estimates of when features will be available in the Windows Hardware Dev Center dashboard. Feature specific legal and administration tasks will transition when the feature transitions.

| Task                                 | Transition timeframe | Documentation link (if available) |
|--------------------------------------|----------------------|----------------------|
| WLK device certification submissions | March 2018          | |
| Attestation signing                  | Completed         | [Attestation signing a kernel driver for public release](https://docs.microsoft.com/en-us/windows-hardware/drivers/dashboard/attestation-signing-a-kernel-driver-for-public-release) |
| Hardware certification submissions   | Completed          | [Hardware certification submissions](https://docs.microsoft.com/en-us/windows-hardware/drivers/dashboard/hardware-certification-submissions)
| UEFI and LSA                         | March 2018           | |
| Device metadata                      | March 2018      | |
| Bug management                       | Migrated      | [Bug management](http://aka.ms/collaboratedocs) |
| Remote debugging (WRD)               | Retiring      | |
| Win32 app certification              | New landing page coming soon      | |

 

## <span id="in_this_section"></span>In this section


-   [Hardware Program dashboard FAQ](hardware-dashboard-faq.md)
-   [Hardware submissions](hardware-certification-submissions.md)
-   [Manage driver distribution with shipping labels](manage-driver-distribution-by-submission.md)
-   [Dashboard Administration](dashboard-administration.md)
-   [Legacy Dashboard](dashboard-services.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhw_dashboard\hw_dashboard%5D:%20Windows%20Hardware%20Dev%20Center%20dashboard%20%20RELEASE:%20%281/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")
