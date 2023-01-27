---
title: Accessing Driver Settings from UI Plug-Ins
description: Accessing Driver Settings from UI Plug-Ins
keywords:
- user interface plug-ins WDK print , accessing driver settings
- UI plug-ins WDK print , accessing driver settings
- status information WDK print plug-ins
ms.date: 01/26/2023
---

# Accessing Driver Settings from UI Plug-Ins

[!include[Print Support Apps](../includes/print-support-apps.md)]

A UI plug-in can obtain the current status of printer features and other internal information. The [**IPrintOemDriverUI::DrvGetDriverSetting**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemdriverui-drvgetdriversetting) COM interface method is implemented within the printer interface DLL for Microsoft's printer drivers and can be called by UI plug-ins.

Additionally, the following methods allow UI plug-ins to modify driver information:

[**IPrintOemDriverUI::DrvUpdateUISetting**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemdriverui-drvupdateuisetting) allows a UI plug-in to notify the driver when a user has modified driver settings.

[**IPrintOemDriverUI::DrvUpgradeRegistrySetting**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemdriverui-drvupgraderegistrysetting) allows a UI plug-in to modify device settings in the registry, so that registry settings used by older driver versions can be updated.
