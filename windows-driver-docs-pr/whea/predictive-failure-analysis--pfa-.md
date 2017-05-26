---
title: Predictive Failure Analysis (PFA)
author: windows-driver-content
description: Predictive Failure Analysis (PFA)
ms.assetid: d2ded330-edcc-4bdd-9b52-73c1961d8ef2
keywords:
- Windows Hardware Error Architecture WDK , predictive failure analysis
- Windows Hardware Error Architecture WDK , PFA
- WHEA WDK , predictive failure analysis
- WHEA WDK , PFA
- predictive failure analysis (PFA) WDK WHEA
- PFA WDK WHEA
- failure analysis WDK WHEA
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Predictive Failure Analysis (PFA)


The Windows Hardware Error Architecture (WHEA) supports Predictive Failure Analysis (PFA) for ECC memory. By using PFA, WHEA can monitor one or more ECC memory pages that have encountered previous errors. If the number of errors exceeds a threshold for the same page within a configurable time interval, WHEA attempts to take the memory page offline.

Computer systems, especially server systems, are typically equipped with Error Correction Code (ECC) memory that can automatically correct certain types of memory errors. In systems that have ECC memory, information about the corrected errors and their frequency is available to the operating system and can be used to predict impending failures, including uncorrectable failures that can be catastrophic and lead to unplanned downtime.

You can configure the PFA error threshold, time interval, and other parameters for WHEA by using registry settings. For more information about how to do this, see [WHEA Policy Settings](whea-pfa-registry-settings.md).

For an overview of how WHEA performs PFA, see [PFA Performed by WHEA](pfa-performed-by-whea.md).

A [platform-specific hardware error driver (PSHED) plug-in driver](platform-specific-hardware-error-driver-plug-ins2.md) can also perform PFA on ECC memory. In this way, the plug-in (not WHEA) must monitor ECC memory pages. For more information about how PSHED plug-ins perform PFA, see [PFA Performed by a PSHED Plug-In](pfa-performed-by-a-pshed-plug-in.md).

When PFA predicts an ECC memory page will fail, it saves (or *persists*) the results in the Boot Configuration Data (BCD) system store. For more information about this process, see [Persistence of PFA Results](persistence-of-pfa-results.md).

WHEA supports PFA on Windows 7 and later versions of Windows.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwhea\whea%5D:%20Predictive%20Failure%20Analysis%20%28PFA%29%20%20RELEASE:%20%289/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


