---
title: Designing WMI Miniport Driver Callback Routines
description: Designing WMI Miniport Driver Callback Routines
ms.assetid: 3bf5b214-e09c-48bc-832b-d0efd3bc8875
keywords: ["WMI SRBs WDK storage , designing callback routines", "callback routines WDK WMI SRBs"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Designing%20WMI%20Miniport%20Driver%20Callback%20Routines%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




