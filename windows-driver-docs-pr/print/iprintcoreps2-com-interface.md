---
title: IPrintCorePS2 COM interface
description: IPrintCorePS2 COM interface
keywords:
- IPrintCorePS2
ms.date: 06/26/2023
---

# IPrintCorePS2 COM interface

[!include[Print Support Apps](../includes/print-support-apps.md)]

The `IPrintCorePS2` COM interface provides a set of helper methods for Pscript5 render plug-ins. The following table lists and describes all of the methods defined by the `IPrintCorePS2` interface.

| Method | Description |
|--|--|
| [**IPrintCorePS2::DrvWriteSpoolBuf**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintcoreps2-drvwritespoolbuf)> | Is provided by the Pscript5 driver so that [rendering plug-ins]  can send printer data to the spooler. |
| [**IPrintCorePS2::EnumFeatures**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintcoreps2-enumfeatures) | Enumerates a printer's available features. |
| [**IPrintCorePS2::EnumOptions**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintcoreps2-enumoptions) | Enumerates the available options of a specific feature. |
| [**IPrintCorePS2::GetFeatureAttribute**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintcoreps2-getfeatureattribute) | Retrieves the feature attribute list or the value of a specific feature attribute. |
| [**IPrintCorePS2::GetGlobalAttribute**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintcoreps2-getglobalattribute) | Retrieves the global attribute list or the value of a specific global attribute. |
| [**IPrintCorePS2::GetOptionAttribute**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintcoreps2-getoptionattribute) | Retrieves the option attribute list or the value of a specific option attribute. |
| [**IPrintCorePS2::GetOptions**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintcoreps2-getoptions) | Retrieves the driver's current feature settings in the format of a list of feature/option keyword pairs. |

For more information, see [Implementing Printer Driver COM Interfaces](implementing-printer-driver-com-interfaces.md).
