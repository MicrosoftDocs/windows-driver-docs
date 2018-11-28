---
title: PPD-Specific Interface
description: PPD-Specific Interface
ms.assetid: 12d5baa2-4fd4-4eca-84c7-1ee168ee8259
keywords:
- PostScript Printer Driver WDK print , PPD-specific interface
- Pscript WDK print , PPD-specific interface
- IPrintCoreUI2
- PPD files WDK Pscript
- PPD-specific interface WDK Pscript
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# PPD-Specific Interface





The [IPrintCoreUI2 COM Interface](iprintcoreui2-com-interface.md) supports nine methods that a user interface plug-in can call to access information in [*PPD*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-postscript-printer-description--ppd-) files. Six of these methods are supported in the [IPrintCorePS2 COM Interface](iprintcoreps2-com-interface.md). This section describes the PPD-specific behavior of these methods.

### IPrintCoreUI2 Interface PPD Methods

[**IPrintCoreUI2::EnumConstrainedOptions**](https://msdn.microsoft.com/library/windows/hardware/ff553045)

[**IPrintCoreUI2::EnumFeatures**](https://msdn.microsoft.com/library/windows/hardware/ff553050)

[**IPrintCoreUI2::EnumOptions**](https://msdn.microsoft.com/library/windows/hardware/ff553052)

[**IPrintCoreUI2::GetOptions**](https://msdn.microsoft.com/library/windows/hardware/ff553069)

[**IPrintCoreUI2::GetFeatureAttribute**](https://msdn.microsoft.com/library/windows/hardware/ff553056)

[**IPrintCoreUI2::GetGlobalAttribute**](https://msdn.microsoft.com/library/windows/hardware/ff553059)

[**IPrintCoreUI2::GetOptionAttribute**](https://msdn.microsoft.com/library/windows/hardware/ff553064)

[**IPrintCoreUI2::SetOptions**](https://msdn.microsoft.com/library/windows/hardware/ff553081)

[**IPrintCoreUI2::WhyConstrained**](https://msdn.microsoft.com/library/windows/hardware/ff553087)

### IPrintCorePS2 Interface PPD Methods

[**IPrintCorePS2::EnumFeatures**](https://msdn.microsoft.com/library/windows/hardware/ff552990)

[**IPrintCorePS2::EnumOptions**](https://msdn.microsoft.com/library/windows/hardware/ff552996)

[**IPrintCorePS2::GetOptions**](https://msdn.microsoft.com/library/windows/hardware/ff553019)

[**IPrintCorePS2::GetFeatureAttribute**](https://msdn.microsoft.com/library/windows/hardware/ff553006)

[**IPrintCorePS2::GetGlobalAttribute**](https://msdn.microsoft.com/library/windows/hardware/ff553009)

[**IPrintCorePS2::GetOptionAttribute**](https://msdn.microsoft.com/library/windows/hardware/ff553013)

Throughout this section, a reference to any method that is a member of both interfaces applies to both methods. For example, a reference to **GetOptions** applies to **IPrintCoreUI2::GetOptions** as well as to **IPrintCorePS2::GetOptions**.

### PPD Feature Availability

Note that in this section, the phrase "PPD feature is not currently available" means that either the printer does not support the feature, or the feature's non-None/False options are constrained by current installable option settings.

For example, "Duplex feature is not currently available" means either the PPD does not specify the \***Duplex** feature keyword, or the \***Duplex** feature keyword's non-None options are currently constrained by the fact that the duplex unit is not installed.

 

 




