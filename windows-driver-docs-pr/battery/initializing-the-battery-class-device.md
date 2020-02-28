---
title: Initializing the Battery Class Device
description: Initializing the Battery Class Device
ms.assetid: d385533e-790a-47b3-a3d2-d620cbd40a4d
keywords:
- battery class drivers WDK , device initializations
- battery miniclass drivers WDK , registering
- registering battery devices
- initializing battery devices
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Initializing the Battery Class Device


## <span id="ddk_initializing_the_battery_class_device_dg"></span><span id="DDK_INITIALIZING_THE_BATTERY_CLASS_DEVICE_DG"></span>


The [*AddDevice*](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_add_device) routine must initialize the battery class device and register the miniclass driver with the class driver. To do so, the miniclass driver calls the [**BatteryClassInitializeDevice**](https://docs.microsoft.com/windows/desktop/api/batclass/nf-batclass-batteryclassinitializedevice) routine. This call registers the miniclass driver with the class driver, so that the two drivers can use each other's support routines. This call also registers the battery device with the system so that it can be seen by the composite battery and the power meter.

**BatteryClassInitializeDevice** requires a pointer to a [**BATTERY\_MINIPORT\_INFO**](https://docs.microsoft.com/windows/desktop/api/batclass/ns-batclass-battery_miniport_info) structure that contains the following information:

-   In **MajorVersion** and **MinorVersion**, the major and minor version numbers of the class driver that this miniclass driver supports.

    The version numbers are defined in Batclass.h as BATTERY\_CLASS\_MAJOR\_VERSION and BATTERY\_CLASS\_MINOR\_VERSION, respectively.

-   In **QueryTag**, the entry point of the miniclass driver's [*BatteryMiniQueryTag*](https://docs.microsoft.com/windows/desktop/api/batclass/nc-batclass-bclass_query_tag_callback) routine.

-   In **QueryInformation**, the entry point of the miniclass driver's [*BatteryMiniQueryInformation*](https://docs.microsoft.com/windows/desktop/api/batclass/nc-batclass-bclass_query_information_callback) routine.

-   In **SetInformation**, the entry point of the miniclass driver's [*BatteryMiniSetInformation*](https://docs.microsoft.com/windows/desktop/api/batclass/nc-batclass-bclass_set_information_callback) routine.

-   In **SetStatusNotify**, the entry point of the miniclass driver's [*BatteryMiniSetStatusNotify*](https://docs.microsoft.com/windows/desktop/api/batclass/nc-batclass-bclass_set_status_notify_callback) routine.

-   In **DisableStatusNotify**, the entry point of the miniclass driver's [*BatteryMiniDisableStatusNotify*](https://docs.microsoft.com/windows/desktop/api/batclass/nc-batclass-bclass_disable_status_notify_callback) routine.

-   In **Context**, a pointer to the miniclass driver's context information.

    The context information is typically a pointer to the FDO device extension, which is passed back to the miniclass driver each time the class driver calls a [BatteryMini*Xxx*](https://docs.microsoft.com/windows-hardware/drivers/ddi/_battery/) routine.

-   In **Pdo**, a pointer to the PDO for the device.

-   In **DeviceName**, a NULL parameter; PnP devices should not have names.

After setting up this structure, the miniclass driver attaches itself to the battery class driver by calling **BatteryClassInitializeDevice**, and passing a pointer to the BATTERY\_MINIPORT\_INFO structure. In return, it receives a handle to be used in subsequent calls to battery class driver support routines. The miniclass driver should store the returned class handle in nonpaged memory.

After calling **BatteryClassInitializeDevice**, the [*AddDevice*](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_add_device) routine might also need to initialize other device-specific data.

 

 




