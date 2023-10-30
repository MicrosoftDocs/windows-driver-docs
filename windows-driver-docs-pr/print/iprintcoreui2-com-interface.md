---
title: IPrintCoreUI2 COM interface
description: IPrintCoreUI2 COM interface
keywords:
- IPrintCoreUI2
ms.date: 06/26/2023
---

# IPrintCoreUI2 COM interface

[!include[Print Support Apps](../includes/print-support-apps.md)]

The `IPrintCoreUI2` COM interface extends the [IPrintOemDriverUI COM interface](iprintoemdriverui-com-interface.md). In Windows XP and later, Pscript5 driver provides the `IPrintCoreUI2` COM interface. The methods in this interface are for use only by Pscript5 UI plug-ins.

| Method | Description |
|--|--|
| [**IPrintCoreUI2::DrvGetDriverSetting**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintcoreui2-drvgetdriversetting) | Enables a UI plug-in to obtain the current status of printer features and other internal information. |
| [**IPrintCoreUI2::DrvUpdateUISetting**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintcoreui2-drvupdateuisetting) | Enables a UI plug-in to notify the driver of a modified user interface option. |
| [**IPrintCoreUI2::DrvUpgradeRegistrySetting**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintcoreui2-drvupgraderegistrysetting) | Enables OEM plug-ins to upgrade private registry settings. |
| [**IPrintCoreUI2::EnumConstrainedOptions**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintcoreui2-enumconstrainedoptions) | Determines which options of a feature are constrained. |
| [**IPrintCoreUI2::EnumFeatures**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintcoreui2-enumfeatures) | Enumerates a printer's available features. |
| [**IPrintCoreUI2::EnumOptions**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintcoreui2-enumoptions) | Enumerates the available options of a specific feature. |
| [**IPrintCoreUI2::GetFeatureAttribute**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintcoreui2-getfeatureattribute) | Retrieves the feature attribute list or the value of a specific feature attribute. |
| [**IPrintCoreUI2::GetGlobalAttribute**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintcoreui2-getglobalattribute) | Retrieves the global attribute list or the value of a specific global attribute. |
| [**IPrintCoreUI2::GetOptionAttribute**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintcoreui2-getoptionattribute) | Retrieves the option attribute list or the value of a specific option attribute. |
| [**IPrintCoreUI2::GetOptions**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintcoreui2-getoptions) | Retrieves the driver's current feature settings in the format of a list of feature/option keyword pairs. |
| [**IPrintCoreUI2::QuerySimulationSupport**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintcoreui2-querysimulationsupport) | Retrieves a spooler simulation capability structure, which indicates the kinds of simulation the spooler supports. |
| [**IPrintCoreUI2::SetOptions**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintcoreui2-setoptions) | Sets the driver's feature settings. |
| [**IPrintCoreUI2::WhyConstrained**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintcoreui2-whyconstrained) | Determines why the specified feature/option selection is constrained. |

For more information, see [Implementing Printer Driver COM Interfaces](implementing-printer-driver-com-interfaces.md).
