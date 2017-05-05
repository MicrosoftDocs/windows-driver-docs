---
title: Accessing Driver Settings from UI Plug-Ins
author: windows-driver-content
description: Accessing Driver Settings from UI Plug-Ins
ms.assetid: 898e1cfb-851b-403e-a88b-d38c505c1390
keywords:
- user interface plug-ins WDK print , accessing driver settings
- UI plug-ins WDK print , accessing driver settings
- status information WDK print plug-ins
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Accessing Driver Settings from UI Plug-Ins


## <a href="" id="ddk-accessing-driver-settings-from-ui-plug-ins-gg"></a>


A UI plug-in can obtain the current status of printer features and other internal information. The [**IPrintOemDriverUI::DrvGetDriverSetting**](https://msdn.microsoft.com/library/windows/hardware/ff553114) COM interface method is implemented within the printer interface DLL for Microsoft's printer drivers and can be called by UI plug-ins.

Additionally, the following methods allow UI plug-ins to modify driver information:

[**IPrintOemDriverUI::DrvUpdateUISetting**](https://msdn.microsoft.com/library/windows/hardware/ff553115) allows a UI plug-in to notify the driver when a user has modified driver settings.

[**IPrintOemDriverUI::DrvUpgradeRegistrySetting**](https://msdn.microsoft.com/library/windows/hardware/ff553118) allows a UI plug-in to modify device settings in the registry, so that registry settings used by older driver versions can be updated.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Accessing%20Driver%20Settings%20from%20UI%20Plug-Ins%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


