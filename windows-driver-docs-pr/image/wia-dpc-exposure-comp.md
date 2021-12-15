---
title: WIA_DPC_EXPOSURE_COMP
description: The WIA_DPC_EXPOSURE_COMP property enables you to adjust the set point of a digital camera's auto-exposure control.
keywords: ["WIA_DPC_EXPOSURE_COMP Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPC_EXPOSURE_COMP
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 09/29/2021
---

# WIA_DPC_EXPOSURE_COMP

The WIA_DPC_EXPOSURE_COMP property enables you to adjust the set point of a digital camera's auto-exposure control.

Property Type: VT_I4

Valid Values: WIA_PROP_RANGE or WIA_PROP_LIST

Access Rights: Read/write

## Remarks

You can use the WIA_DPC_EXPOSURE_COMP property to adjust the set point of a digital camera's auto-exposure control. Setting WIA_DPC_EXPOSURE_COMP to zero does not change the factory-set auto-exposure level.

The units of WIA_DPC_EXPOSURE_COMP are in "stops" that are scaled by a factor of 1000, to allow for fractional stop values. Setting WIA_DPC_EXPOSURE_COMP to 2000 corresponds to two stops more exposure (four times more energy on the sensor), so images will be brighter. Setting WIA_DPC_EXPOSURE_COMP to −1000 corresponds to one stop less exposure (one-half the energy on the sensor), so images will be darker.

The setting values are in Additive System of Photographic Exposure (APEX) units.

This property may be expressed as either a list or a range of values. This property is typically used only when a device has the [**WIA_DPC_EXPOSURE_MODE**](wia-dpc-exposure-mode.md) property set to EXPOSUREMODE_MANUAL.

## Requirements

**Version:** Obsolete in Windows Vista and later operating systems and should not be used.

**Header:** wiadef.h (include Wiadef.h)

## See also

[**WIA_DPC_EXPOSURE_MODE**](wia-dpc-exposure-mode.md)
