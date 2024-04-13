---
title: WIA_IPS_FEEDER_CONTROL
description: The WIA_IPS_FEEDER_CONTROL property is used to configure manual control over the feeder motor. The WIA minidriver creates and maintains this property.
keywords: ["WIA_IPS_FEEDER_CONTROL Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_FEEDER_CONTROL
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/05/2023
---

# WIA_IPS_FEEDER_CONTROL

The **WIA_IPS_FEEDER_CONTROL** property is used to configure manual control over the feeder motor. The WIA minidriver creates and maintains this property.

Property Type: VT_I4

Valid Values: WIA_PROP_LIST

Access Rights: Read/Write

## Remarks

The following table describes the valid values for the **WIA_IPS_FEEDER_CONTROL** property.

| Value | Definition |
|--|--|
| WIA_FEEDER_CONTROL_AUTO | The device controls the feeder motor operation. The feeder is started and stopped for each scan job [**IWiaMiniDrv::drvAcquireItemData&**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvacquireitemdata) call. This is the required default value if the property is supported. |
| WIA_FEEDER_CONTROL_MANUAL | The application controls the feeder motor operation. The feeder is started when the WIA minidriver receives a WIA_COMMAND_START_FEEDER command request and stopped when the WIA minidriver receives a WIA_COMMAND_STOP_FEEDER command request. |

When the device supports this feature, the WIA application can use it to start the feeder motor before executing the first scan job (the first **IWiaTransfer::Download** call) and stop the feeder after the last scan job (the last **IWiaTransfer::Download** call in the current WIA application session) is complete. Between the individual jobs (**IWiaTransfer::Download** calls), the feeder is kept to its operating speed and is ready to continue the next job without delay.

If the WIA minidriver receives an [**IWiaMiniDrv::drvAcquireItemData**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvacquireitemdata) request while WIA_FEEDER_CONTROL_MANUAL is set and without receiving a WIA_COMMAND_START_FEEDER command, the WIA minidriver must revert to WIA_FEEDER_COMMAND_AUTO before executing the scan job.

If WIA_FEEDER_CONTROL_MANUAL is set and the WIA minidriver receives a [**IWiaMiniDrv::drvUnInitializeWia**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvuninitializewia) request without receiving a WIA_COMMAND_STOP_FEEDER command, the WIA minidriver must stop the feeder before returning to the call.

This property is valid only for the Feeder item (WIA_CATEGORY_FEEDER) and is optional.

## Requirements

**Header:** wiadef.h (include Wiadef.h)
