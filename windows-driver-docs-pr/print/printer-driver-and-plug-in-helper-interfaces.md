---
title: Printer Driver and Plug-in Helper Interfaces
description: Printer Driver and Plug-in Helper Interfaces
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Printer Driver and Plug-in Helper Interfaces


The [IPrintCoreHelper](/windows-hardware/drivers/ddi/prcomoem/nn-prcomoem-iprintcorehelper) interface, which is available in Windows Vista and later, provides basic functionality that is available in all four core driver modules--Unidrv rendering, Unidrv user interface (UI), Pscript5 rendering, and Pscript5 UI. A single interface is provided to all four modules because:

-   The interface reflects the underlying architecture.

-   The interface provides the ability to write common code modules for plug-ins to perform certain behavior, such as constraints resolution.

You can use the **IPrintCoreHelper** interface to write a single UI replacement plug-in for Unidrv-based and Pscript5-based drivers.

Because of the differences between the Pscript5 and Unidrv driver infrastructures, there are two additional interfaces, [IPrintCoreHelperUni](/windows-hardware/drivers/ddi/prcomoem/nn-prcomoem-iprintcorehelperuni) and [IPrintCoreHelperPS](/windows-hardware/drivers/ddi/prcomoem/nn-prcomoem-iprintcorehelperps), that inherit from the **IPrintCoreHelper** interface and that provide extended services based on the individual drivers. These interfaces are available only in their respective modules. The Pscript5 helper interface, **IPrintCoreHelperPS**, provides access to certain PostScript printer description (PPD) data, while the Unidrv helper interface, **IPrintCoreHelperUni**, provides the ability to access generic printer configuration (GPD) files by means of the GDL parser, which is new for Windows Vista.

This section provides the following topics:

[Unidrv and Pscript5 Helper Interfaces for Plug-ins](unidrv-and-pscript5-helper-interfaces-for-plug-ins.md)

[Publishing the Interfaces](publishing-the-interfaces.md)

[Details of the IPrintCoreHelper Interface](details-of-the-iprintcorehelper-interface.md)

 

