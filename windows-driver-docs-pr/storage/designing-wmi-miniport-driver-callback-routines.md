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

[**HwScsiWmiExecuteMethod**](https://msdn.microsoft.com/library/windows/hardware/ff557332)

[**HwScsiWmiFunctionControl**](https://msdn.microsoft.com/library/windows/hardware/ff557338)

[**HwScsiWmiQueryDataBlock**](https://msdn.microsoft.com/library/windows/hardware/ff557340)

[**HwScsiWmiQueryReginfo**](https://msdn.microsoft.com/library/windows/hardware/ff557344)

[**HwScsiWmiSetDataBlock**](https://msdn.microsoft.com/library/windows/hardware/ff557349)

[**HwScsiWmiSetDataItem**](https://msdn.microsoft.com/library/windows/hardware/ff557357)

The following sections will help you design the *HwScsiWmiExecuteMethod* callback routine and the callback routines that manage data fields:

[Designing a Miniport Driver Callback Routine that Handles WMI Classes with Methods](designing-a-miniport-driver-callback-routine-that-handles-wmi-classes-.md)

[Designing a Miniport Driver Callback Routine that Handles WMI Classes with Data Fields](designing-a-miniport-driver-callback-routine-that-handles-wmi-classes-.md)

 

 




