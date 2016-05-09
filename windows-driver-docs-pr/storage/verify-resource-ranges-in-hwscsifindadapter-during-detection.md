---
title: Verify Resource Ranges in HwScsiFindAdapter During Detection
description: Verify Resource Ranges in HwScsiFindAdapter During Detection
ms.assetid: 2909aac2-714e-4353-8006-06cf68e4dfc8
keywords: ["SCSI miniport drivers WDK storage , PnP", "PnP WDK SCSI", "Plug and Play WDK SCSI", "converting SCSI miniport drivers", "resource ranges WDK SCSI", "HwScsiFindAdapter"]
---

# Verify Resource Ranges in HwScsiFindAdapter During Detection


## <span id="ddk_verify_resource_ranges_in_hwscsifindadapter_during_detection_kg"></span><span id="DDK_VERIFY_RESOURCE_RANGES_IN_HWSCSIFINDADAPTER_DURING_DETECTION_KG"></span>


Although detection of devices by drivers is usually unnecessary under Plug and Play, the port driver might call a Plug and Play miniport driver's [*HwScsiFindAdapter*](https://msdn.microsoft.com/library/windows/hardware/ff557300) routine to detect devices on a nonenumerable bus. Although this operation is similar to detection in Microsoft Windows NT 4.0, the miniport driver must take care not to operate on ranges that might be in use by another device.

The miniport driver should call [**ScsiPortValidateRange**](https://msdn.microsoft.com/library/windows/hardware/ff564761) before calling [**ScsiPortGetDeviceBase**](https://msdn.microsoft.com/library/windows/hardware/ff564629) to ensure that the miniport driver-supplied range is safe to use. The miniport driver must be prepared for **ScsiPortGetDeviceBase** to fail and return a **NULL** pointer. The miniport driver should also avoid mapping memory starting at address zero, which makes it impossible to detect the failure of **ScsiPortGetDeviceBase** on some systems.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Verify%20Resource%20Ranges%20in%20HwScsiFindAdapter%20During%20Detection%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




