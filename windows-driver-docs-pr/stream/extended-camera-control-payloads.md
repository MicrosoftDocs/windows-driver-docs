---
title: Extended Camera Control Payloads
author: windows-driver-content
description: The control properties within the KSPROPERTYSETID\_ExtendedCameraControl property set use a common payload format for getting and setting the property data.
ms.assetid: 347413DB-229B-40D7-BD3E-931493EE1FBC
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Extended Camera Control Payloads


The control properties within the [KSPROPERTYSETID\_ExtendedCameraControl](https://msdn.microsoft.com/library/windows/hardware/dn567570) property set use a common payload format for getting and setting the property data.

## Extended camera property header


All payloads begin with a [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn567563) structure. This structure contains the PIN target with the associated control flags and capabilities. Depending on the particular control, the **Capabilities** member will contain a set of capabilities provided by the control. The **Flags** member will contain the actual capabilities currently set or to be set for the control.

The **PinId** member specifies the target which is either the camera PIN or the filter PIN. If the property is a filter level control, then **PinId** is set to KSCAMERA\_EXTENDEDPROP\_FILTERSCOPE.

A property control is either synchronous or asynchronous. If the control is synchronous, then the KSCAMERA\_EXTENDEDPROP\_CAPS\_ASYNCCONTROL flag is set in **Capabilities**. Also, if the control is cancelable, the **Capabilities** member includes the KSCAMERA\_EXTENDEDPROP\_CAPS\_CANCELLABLE flag.

The payload size is set in the Size member. The value for **Size** is the entire size of the payload. If the property uses only the header, then **Size** = **sizeof**(KSCAMERA\_EXTENDEDPROP\_HEADER). Otherwise, **Size** = **sizeof**(KSCAMERA\_EXTENDEDPROP\_HEADER) + **sizeof**(control specific data).

## Control specific data


Some property controls use an additional structure to hold additional data. Where single data values are used, the property data will contain an [**KSCAMERA\_EXTENDEDPROP\_VALUE**](https://msdn.microsoft.com/library/windows/hardware/dn567565) structure after [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn567563). The **KSCAMERA\_EXTENDEDPROP\_VALUE** structure allows the property to express a single value as one of several data types.

To get or set additional data, a property will have its own special data structure following the [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn567563). The following example shows a driver code fragment setting the property specific data for a KSPROPERTY\_TYPE\_GET request of the [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FIELDOFVIEW**](https://msdn.microsoft.com/library/windows/hardware/dn567574) property.

```ManagedCPlusPlus
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Extended%20Camera%20Control%20Payloads%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


