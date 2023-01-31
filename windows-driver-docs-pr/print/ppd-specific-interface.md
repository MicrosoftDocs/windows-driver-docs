---
title: PPD-Specific Interface
description: PPD-Specific Interface
keywords:
- PostScript Printer Driver WDK print , PPD-specific interface
- Pscript WDK print , PPD-specific interface
- IPrintCoreUI2
- PPD files WDK Pscript
- PPD-specific interface WDK Pscript
ms.date: 01/30/2023
---

# PPD-specific interface

[!include[Print Support Apps](../includes/print-support-apps.md)]

The [IPrintCoreUI2 COM Interface](iprintcoreui2-com-interface.md) supports nine methods that a user interface plug-in can call to access information in *PPD* files. Six of these methods are supported in the [IPrintCorePS2 COM Interface](iprintcoreps2-com-interface.md). This section describes the PPD-specific behavior of these methods.

## IPrintCoreUI2 Interface PPD Methods

[**IPrintCoreUI2::EnumConstrainedOptions**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintcoreui2-enumconstrainedoptions)

[**IPrintCoreUI2::EnumFeatures**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintcoreui2-enumfeatures)

[**IPrintCoreUI2::EnumOptions**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintcoreui2-enumoptions)

[**IPrintCoreUI2::GetOptions**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintcoreui2-getoptions)

[**IPrintCoreUI2::GetFeatureAttribute**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintcoreui2-getfeatureattribute)

[**IPrintCoreUI2::GetGlobalAttribute**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintcoreui2-getglobalattribute)

[**IPrintCoreUI2::GetOptionAttribute**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintcoreui2-getoptionattribute)

[**IPrintCoreUI2::SetOptions**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintcoreui2-setoptions)

[**IPrintCoreUI2::WhyConstrained**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintcoreui2-whyconstrained)

### IPrintCorePS2 Interface PPD Methods

[**IPrintCorePS2::EnumFeatures**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintcoreps2-enumfeatures)

[**IPrintCorePS2::EnumOptions**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintcoreps2-enumoptions)

[**IPrintCorePS2::GetOptions**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintcoreps2-getoptions)

[**IPrintCorePS2::GetFeatureAttribute**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintcoreps2-getfeatureattribute)

[**IPrintCorePS2::GetGlobalAttribute**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintcoreps2-getglobalattribute)

[**IPrintCorePS2::GetOptionAttribute**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintcoreps2-getoptionattribute)

Throughout this section, a reference to any method that is a member of both interfaces applies to both methods. For example, a reference to **GetOptions** applies to **IPrintCoreUI2::GetOptions** as well as to **IPrintCorePS2::GetOptions**.

## PPD Feature Availability

In this section, the phrase "PPD feature isn't currently available" means that either the printer doesn't support the feature, or the feature's non-None/False options are constrained by current installable option settings.

For example, "Duplex feature isn't currently available" means either the PPD doesn't specify the \***Duplex** feature keyword, or the \***Duplex** feature keyword's non-None options are currently constrained by the fact that the duplex unit isn't installed.
