---
title: Setting Port Configuration Information with Storport
description: Setting Port Configuration Information with Storport
ms.date: 04/20/2017
---

# Setting Port Configuration Information with Storport


## <span id="ddk_setting_port_configuration_information_with_storport_kg"></span><span id="DDK_SETTING_PORT_CONFIGURATION_INFORMATION_WITH_STORPORT_KG"></span>


When the Microsoft Windows PnP manager discovers an adapter managed by Storport, it notifies the Storport driver to start it. Next, Storport calls the miniport driver's [**HwStorFindAdapter**](/windows-hardware/drivers/ddi/storport/nc-storport-hw_find_adapter) routine, passing in a [**PORT\_CONFIGURATION\_INFORMATION (STORPORT)**](/previous-versions/windows/hardware/drivers/ff563901(v=vs.85)) structure.

Because all adapters managed by Storport are PnP devices, *HwStorFindAdapter* does not physically search for the adapter. Instead, this miniport driver routine attempts to initialize the adapter using the parameters specified in the PORT\_CONFIGURATION\_INFORMATION structure, and completes the initialization of PORT\_CONFIGURATION\_INFORMATION, storing those values in PORT\_CONFIGURATION\_INFORMATION that Storport might require in order to initialize the device extension.

For more information, see [**PORT\_CONFIGURATION\_INFORMATION (SCSI)**](/windows-hardware/drivers/ddi/srb/ns-srb-_port_configuration_information) and [**PORT\_CONFIGURATION\_INFORMATION (STORPORT)**](/previous-versions/windows/hardware/drivers/ff563901(v=vs.85)).

 

