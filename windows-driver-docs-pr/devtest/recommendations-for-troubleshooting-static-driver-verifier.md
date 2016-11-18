---
title: Recommendations for Troubleshooting Static Driver Verifier
description: Recommendations for Troubleshooting Static Driver Verifier
ms.assetid: 14c39437-12ca-4938-93bb-79bbcb192de2
---

# Recommendations for Troubleshooting Static Driver Verifier


When you run Static Driver Verifier (SDV) on your driver source code and SDV reports Timeout, GiveUp, or Spaceout, try the following actions:

-   Use the **/refine** command option to run SDV. For more information, see [Static Driver Verifier commands (MSBuild)](-static-driver-verifier-commands--msbuild-.md).

-   The following recommendations require changes to the SDV configuration settings. You can set the configuration settings directly in Static Driver Verfier on the **Configure** tab, under Resources, or in an [Static Driver Verifier Options File](static-driver-verifier-options-file.md), Sdv-defaults.xml. The default options file is specific to the driver model and can be found in the \\tools\\sdv\\data\\model\\ directory, where model is WDM, WDF, NDIS, or Storport.
    1.  If your computer has a multicore processor, reduce the number of threads that are used during verification to 1. In the Resources group on the **Configure** tab, select 1 from the drop-down list. In the SDV defaults file, change the value for SDV\_SlamConfig\_NumberOfTheads to 1.
    2.  If SDV reports a Timeout, increase the Timeout limit. This value limits the amount of time SDV spends verifying a rule. The default value is 50 minutes (3000 seconds). In the Resources group on the **Configure** tab, you can adjust the setting by changing the **Maximum time** (minutes). In the options file, you can change the SDV\_SlamConfig\_Timeout value. The minimum is 10(Sec) and the maximum is 86400(Sec). For example, you might want to double the value for SDV\_SlamConfig\_Timeout to 6000.
-   If none of these suggestions help solve the problem, try applying them all together.

**Note**   These techniques increase the actual duration of a run, but they also make it easier for SDV to finish its job and have a useful result (Pass or Defect).

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Recommendations%20for%20Troubleshooting%20Static%20Driver%20Verifier%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




