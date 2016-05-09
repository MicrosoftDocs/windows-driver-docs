---
title: Setting Port Configuration Information with Storport
author: windows-driver-content
description: Setting Port Configuration Information with Storport
ms.assetid: dcc2cb3c-2fe6-4f70-814b-66b59a237dd9
---

# Setting Port Configuration Information with Storport


## <span id="ddk_setting_port_configuration_information_with_storport_kg"></span><span id="DDK_SETTING_PORT_CONFIGURATION_INFORMATION_WITH_STORPORT_KG"></span>


When the Microsoft Windows PnP manager discovers an adapter managed by Storport, it notifies the Storport driver to start it. Next, Storport calls the miniport driver's [**HwStorFindAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff557390) routine, passing in a [**PORT\_CONFIGURATION\_INFORMATION (STORPORT)**](https://msdn.microsoft.com/library/windows/hardware/ff563901) structure.

Because all adapters managed by Storport are PnP devices, *HwStorFindAdapter* does not physically search for the adapter. Instead, this miniport driver routine attempts to initialize the adapter using the parameters specified in the PORT\_CONFIGURATION\_INFORMATION structure, and completes the initialization of PORT\_CONFIGURATION\_INFORMATION, storing those values in PORT\_CONFIGURATION\_INFORMATION that Storport might require in order to initialize the device extension.

For more information, see [**PORT\_CONFIGURATION\_INFORMATION (SCSI)**](https://msdn.microsoft.com/library/windows/hardware/ff563900) and [**PORT\_CONFIGURATION\_INFORMATION (STORPORT)**](https://msdn.microsoft.com/library/windows/hardware/ff563901).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Setting%20Port%20Configuration%20Information%20with%20Storport%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


