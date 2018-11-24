---
title: Predictive Failure Analysis (PFA)
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
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Predictive Failure Analysis (PFA)


The Windows Hardware Error Architecture (WHEA) supports Predictive Failure Analysis (PFA) for ECC memory. By using PFA, WHEA can monitor one or more ECC memory pages that have encountered previous errors. If the number of errors exceeds a threshold for the same page within a configurable time interval, WHEA attempts to take the memory page offline.

Computer systems, especially server systems, are typically equipped with Error Correction Code (ECC) memory that can automatically correct certain types of memory errors. In systems that have ECC memory, information about the corrected errors and their frequency is available to the operating system and can be used to predict impending failures, including uncorrectable failures that can be catastrophic and lead to unplanned downtime.

You can configure the PFA error threshold, time interval, and other parameters for WHEA by using registry settings. For more information about how to do this, see [WHEA Policy Settings](whea-pfa-registry-settings.md).

For an overview of how WHEA performs PFA, see [PFA Performed by WHEA](pfa-performed-by-whea.md).

A [platform-specific hardware error driver (PSHED) plug-in driver](platform-specific-hardware-error-driver-plug-ins2.md) can also perform PFA on ECC memory. In this way, the plug-in (not WHEA) must monitor ECC memory pages. For more information about how PSHED plug-ins perform PFA, see [PFA Performed by a PSHED Plug-In](pfa-performed-by-a-pshed-plug-in.md).

When PFA predicts an ECC memory page will fail, it saves (or *persists*) the results in the Boot Configuration Data (BCD) system store. For more information about this process, see [Persistence of PFA Results](persistence-of-pfa-results.md).

WHEA supports PFA on Windows 7 and later versions of Windows.

 

 




