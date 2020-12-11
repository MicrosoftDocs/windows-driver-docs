---
title: Recommendations for Troubleshooting Static Driver Verifier
description: Recommendations for Troubleshooting Static Driver Verifier
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Recommendations for Troubleshooting Static Driver Verifier


When you run Static Driver Verifier (SDV) on your driver source code and SDV reports Timeout, GiveUp, or Spaceout, try the following actions:

-   The following recommendations require changes to the SDV configuration settings. You can set the configuration settings directly in Static Driver Verfier on the **Configure** tab, under Resources, or in an [Static Driver Verifier Options File](static-driver-verifier-options-file.md), Sdv-defaults.xml. The default options file is specific to the driver model and can be found in the \\tools\\sdv\\data\\model\\ directory, where model is WDM, WDF, NDIS, or Storport.
    1.  If your computer has a multicore processor, reduce the number of threads that are used during verification to 1. In the Resources group on the **Configure** tab, select 1 from the drop-down list. In the SDV defaults file, change the value for SDV\_SlamConfig\_NumberOfTheads to 1.
    2.  If SDV reports a Timeout, increase the Timeout limit. This value limits the amount of time SDV spends verifying a rule. The default value is 50 minutes (3000 seconds). In the Resources group on the **Configure** tab, you can adjust the setting by changing the **Maximum time** (minutes). In the options file, you can change the SDV\_SlamConfig\_Timeout value. The minimum is 10(Sec) and the maximum is 86400(Sec). For example, you might want to double the value for SDV\_SlamConfig\_Timeout to 6000.
-   If none of these suggestions help solve the problem, try applying them all together.

**Note**   These techniques increase the actual duration of a run, but they also make it easier for SDV to finish its job and have a useful result (Pass or Defect).
