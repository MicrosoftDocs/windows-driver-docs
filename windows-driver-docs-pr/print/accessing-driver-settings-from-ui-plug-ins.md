---
title: Accessing Driver Settings from UI Plug-Ins
description: Accessing Driver Settings from UI Plug-Ins
ms.assetid: 898e1cfb-851b-403e-a88b-d38c505c1390
keywords:
- user interface plug-ins WDK print , accessing driver settings
- UI plug-ins WDK print , accessing driver settings
- status information WDK print plug-ins
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Accessing Driver Settings from UI Plug-Ins





A UI plug-in can obtain the current status of printer features and other internal information. The [**IPrintOemDriverUI::DrvGetDriverSetting**](https://msdn.microsoft.com/library/windows/hardware/ff553114) COM interface method is implemented within the printer interface DLL for Microsoft's printer drivers and can be called by UI plug-ins.

Additionally, the following methods allow UI plug-ins to modify driver information:

[**IPrintOemDriverUI::DrvUpdateUISetting**](https://msdn.microsoft.com/library/windows/hardware/ff553115) allows a UI plug-in to notify the driver when a user has modified driver settings.

[**IPrintOemDriverUI::DrvUpgradeRegistrySetting**](https://msdn.microsoft.com/library/windows/hardware/ff553118) allows a UI plug-in to modify device settings in the registry, so that registry settings used by older driver versions can be updated.

 

 




