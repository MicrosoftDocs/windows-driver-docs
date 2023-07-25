---
title: IPrintOemDriverUI COM Interface
description: IPrintOemDriverUI COM Interface
keywords:
- IPrintOemDriverUI
ms.date: 07/14/2023
---

# IPrintOemDriverUI COM Interface

[!include[Print Support Apps](../includes/print-support-apps.md)]

The `IPrintOemDriverUI` COM interface enables a UI plug-in to view and modify information managed by the [printer interface DLL](printer-interface-dll.md) for Unidrv or Pscript.

The following table lists and describes all the methods that the `IPrintOemDriverUI` interface defines.

| Method | Description |
|--|--|
| [**IPrintOemDriverUI::DrvGetDriverSetting**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemdriverui-drvgetdriversetting) | Enables a UI plug-in to obtain the current status of printer features and other internal information. |
| [**IPrintOemDriverUI::DrvUpdateUISetting**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemdriverui-drvupdateuisetting) | Enables a UI plug-in to notify the driver of a modified user interface option. |
| [**IPrintOemDriverUI::DrvUpgradeRegistrySetting**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemdriverui-drvupgraderegistrysetting) | Enables a UI plug-in to update device settings stored in the registry. |

For more information, see [Implementing Printer Driver COM Interfaces](implementing-printer-driver-com-interfaces.md).
