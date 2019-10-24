---
title: Designing WMI Miniport Driver Callback Routines
description: Designing WMI Miniport Driver Callback Routines
ms.assetid: 3bf5b214-e09c-48bc-832b-d0efd3bc8875
keywords:
- WMI SRBs WDK storage , designing callback routines
- callback routines WDK WMI SRBs
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Designing WMI Miniport Driver Callback Routines


## <span id="ddk_designing_wmi_miniport_driver_callback_routines_kg"></span><span id="DDK_DESIGNING_WMI_MINIPORT_DRIVER_CALLBACK_ROUTINES_KG"></span>


To use the SCSI Port WMI library, you must implement the following miniport driver callback routines in your miniport driver:

[**HwScsiWmiExecuteMethod**](https://docs.microsoft.com/windows-hardware/drivers/ddi/scsiwmi/nc-scsiwmi-pscsiwmi_execute_method)

[**HwScsiWmiFunctionControl**](https://docs.microsoft.com/windows-hardware/drivers/ddi/scsiwmi/nc-scsiwmi-pscsiwmi_function_control)

[**HwScsiWmiQueryDataBlock**](https://docs.microsoft.com/windows-hardware/drivers/ddi/scsiwmi/nc-scsiwmi-pscsiwmi_query_datablock)

[**HwScsiWmiQueryReginfo**](https://docs.microsoft.com/windows-hardware/drivers/ddi/scsiwmi/nc-scsiwmi-pscsiwmi_query_reginfo)

[**HwScsiWmiSetDataBlock**](https://docs.microsoft.com/windows-hardware/drivers/ddi/scsiwmi/nc-scsiwmi-pscsiwmi_set_datablock)

[**HwScsiWmiSetDataItem**](https://docs.microsoft.com/windows-hardware/drivers/ddi/scsiwmi/nc-scsiwmi-pscsiwmi_set_dataitem)

The following sections will help you design the *HwScsiWmiExecuteMethod* callback routine and the callback routines that manage data fields:

[Designing a Miniport Driver Callback Routine that Handles WMI Classes with Methods](designing-a-miniport-driver-callback-routine-that-handles-wmi-classes-.md)

[Designing a Miniport Driver Callback Routine that Handles WMI Classes with Data Fields](designing-a-miniport-driver-callback-routine-that-handles-wmi-classes-.md)

 

 




