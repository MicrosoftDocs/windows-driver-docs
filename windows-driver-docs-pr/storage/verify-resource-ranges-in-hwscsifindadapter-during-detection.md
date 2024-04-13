---
title: Verify Resource Ranges in HwScsiFindAdapter During Detection
description: Verify Resource Ranges in HwScsiFindAdapter During Detection
keywords:
- SCSI miniport drivers WDK storage , PnP
- PnP WDK SCSI
- Plug and Play WDK SCSI
- converting SCSI miniport drivers
- resource ranges WDK SCSI
- HwScsiFindAdapter
ms.date: 04/20/2017
---

# Verify Resource Ranges in HwScsiFindAdapter During Detection


## <span id="ddk_verify_resource_ranges_in_hwscsifindadapter_during_detection_kg"></span><span id="DDK_VERIFY_RESOURCE_RANGES_IN_HWSCSIFINDADAPTER_DURING_DETECTION_KG"></span>


Although detection of devices by drivers is usually unnecessary under Plug and Play, the port driver might call a Plug and Play miniport driver's [*HwScsiFindAdapter*](/previous-versions/windows/hardware/drivers/ff557300(v=vs.85)) routine to detect devices on a nonenumerable bus. Although this operation is similar to detection in Microsoft Windows NT 4.0, the miniport driver must take care not to operate on ranges that might be in use by another device.

The miniport driver should call [**ScsiPortValidateRange**](/windows-hardware/drivers/ddi/srb/nf-srb-scsiportvalidaterange) before calling [**ScsiPortGetDeviceBase**](/windows-hardware/drivers/ddi/srb/nf-srb-scsiportgetdevicebase) to ensure that the miniport driver-supplied range is safe to use. The miniport driver must be prepared for **ScsiPortGetDeviceBase** to fail and return a **NULL** pointer. The miniport driver should also avoid mapping memory starting at address zero, which makes it impossible to detect the failure of **ScsiPortGetDeviceBase** on some systems.

 

