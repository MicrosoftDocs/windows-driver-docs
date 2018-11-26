---
title: Extended Camera Control Payloads
description: The control properties within the KSPROPERTYSETID_ExtendedCameraControl property set use a common payload format for getting and setting the property data.
ms.assetid: 347413DB-229B-40D7-BD3E-931493EE1FBC
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Extended Camera Control Payloads


The control properties within the [KSPROPERTYSETID\_ExtendedCameraControl](https://msdn.microsoft.com/library/windows/hardware/dn567570) property set use a common payload format for getting and setting the property data.

## Extended camera property header


All payloads begin with a [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) structure. This structure contains the PIN target with the associated control flags and capabilities. Depending on the particular control, the **Capabilities** member will contain a set of capabilities provided by the control. The **Flags** member will contain the actual capabilities currently set or to be set for the control.

The **PinId** member specifies the target which is either the camera PIN or the filter PIN. If the property is a filter level control, then **PinId** is set to KSCAMERA\_EXTENDEDPROP\_FILTERSCOPE.

A property control is either synchronous or asynchronous. If the control is synchronous, then the KSCAMERA\_EXTENDEDPROP\_CAPS\_ASYNCCONTROL flag is set in **Capabilities**. Also, if the control is cancelable, the **Capabilities** member includes the KSCAMERA\_EXTENDEDPROP\_CAPS\_CANCELLABLE flag.

The payload size is set in the Size member. The value for **Size** is the entire size of the payload. If the property uses only the header, then **Size** = **sizeof**(KSCAMERA\_EXTENDEDPROP\_HEADER). Otherwise, **Size** = **sizeof**(KSCAMERA\_EXTENDEDPROP\_HEADER) + **sizeof**(control specific data).

## Control specific data


Some property controls use an additional structure to hold additional data. Where single data values are used, the property data will contain an [**KSCAMERA\_EXTENDEDPROP\_VALUE**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_value) structure after [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header). The **KSCAMERA\_EXTENDEDPROP\_VALUE** structure allows the property to express a single value as one of several data types.

To get or set additional data, a property will have its own special data structure following the [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header). The following example shows a driver code fragment setting the property specific data for a KSPROPERTY\_TYPE\_GET request of the [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FIELDOFVIEW**](https://msdn.microsoft.com/library/windows/hardware/dn567574) property.

```cpp
#define FL_WIDE_ANGLE 35
#define FL_NORMAL     50

PBYTE Payload = (PBYTE)PropData;
PKSCAMERA_EXTENDEDPROP_HEADER ExtendedPropHeader = (PKSCAMERA_EXTENDEDPROP_HEADER)Payload;
PKSCAMERA_EXTENDEDPROP_FIELDOFVIEW ExtendedDataFov = (PKSCAMERA_EXTENDEDPROP_FIELDOFVIEW)(Payload + sizeof(KSCAMERA_EXTENDEDPROP_HEADER));

ExtendedPropHeader->Version = 1;
ExtendedPropHeader->PinId = KSCAMERA_EXTENDEDPROP_FILTERSCOPE;
ExtendedPropHeader->Size = sizeof(KSCAMERA_EXTENDEDPROP_HEADER) + sizeof(KSCAMERA_EXTENDEDPROP_FIELDOFVIEW);
ExtendedPropHeader->Result = 0;
ExtendedPropHeader->Flags = 0;
ExtendedPropHeader->Capability = 0;

ExtendedDataFov->NormalizedFocalLengthX = FL_WIDE_ANGLE;
ExtendedDataFov->NormalizedFocalLengthY = FL_WIDE_ANGLE;
ExtendedDataFov->Flag = 0;
ExtendedDataFov->Reserved = 0;
```

 

 




