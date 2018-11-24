---
title: Setting Port Configuration Information with Storport
description: Setting Port Configuration Information with Storport
ms.assetid: dcc2cb3c-2fe6-4f70-814b-66b59a237dd9
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Setting Port Configuration Information with Storport


## <span id="ddk_setting_port_configuration_information_with_storport_kg"></span><span id="DDK_SETTING_PORT_CONFIGURATION_INFORMATION_WITH_STORPORT_KG"></span>


When the Microsoft Windows PnP manager discovers an adapter managed by Storport, it notifies the Storport driver to start it. Next, Storport calls the miniport driver's [**HwStorFindAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff557390) routine, passing in a [**PORT\_CONFIGURATION\_INFORMATION (STORPORT)**](https://msdn.microsoft.com/library/windows/hardware/ff563901) structure.

Because all adapters managed by Storport are PnP devices, *HwStorFindAdapter* does not physically search for the adapter. Instead, this miniport driver routine attempts to initialize the adapter using the parameters specified in the PORT\_CONFIGURATION\_INFORMATION structure, and completes the initialization of PORT\_CONFIGURATION\_INFORMATION, storing those values in PORT\_CONFIGURATION\_INFORMATION that Storport might require in order to initialize the device extension.

For more information, see [**PORT\_CONFIGURATION\_INFORMATION (SCSI)**](https://msdn.microsoft.com/library/windows/hardware/ff563900) and [**PORT\_CONFIGURATION\_INFORMATION (STORPORT)**](https://msdn.microsoft.com/library/windows/hardware/ff563901).

 

 




