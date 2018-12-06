---
title: USB Video Class Properties
description: Clients of the USB Video Class can use the following video capture property sets described in this topic.
ms.assetid: 6295926b-4ec5-42f5-98ca-a375d36f917b
keywords:
- USB Video Class drivers WDK AVStream , properties
- Video Class drivers WDK USB , properties
- UVC drivers WDK AVStream , properties
- property sets WDK USB Video Class
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# USB Video Class Properties


Clients of the USB Video Class can use the following video capture property sets:

[PROPSETID\_VIDCAP\_CAMERACONTROL](https://msdn.microsoft.com/library/windows/hardware/ff567802)
[PROPSETID\_VIDCAP\_VIDEOPROCAMP](https://msdn.microsoft.com/library/windows/hardware/ff568122)
Clients of the USB Video Class can make requests on filters or individual nodes. The functionality of the node-based properties is identical to that of the pre-USB Video Class filter-based properties.

To specify a node-based property, set the KSPROPERTY\_TYPE\_TOPOLOGY flag in the Flags member of the [**KSPROPERTY**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier) structure contained in the property descriptor structure—for example, [**KSPROPERTY\_CAMERACONTROL\_NODE\_S**](https://msdn.microsoft.com/library/windows/hardware/ff564420).

Because clients can address multiple nodes on a single filter, the USB Video Class enables IHVs to support cameras that have multiple independently controlled lenses.

Additionally, a new property set has been defined:

[PROPSETID\_VIDCAP\_SELECTOR](https://msdn.microsoft.com/library/windows/hardware/ff567810)
The property items contained in PROPSETID\_VIDCAP\_SELECTOR are node-based.

Call [**KsSynchronousDeviceControl**](https://msdn.microsoft.com/library/windows/hardware/ff567142) or **DeviceIoControl** to make property requests from a user-mode component. **DeviceIoControl** is documented in the Microsoft Windows SDK documentation.

Each of the property items contained in the four property sets above has a corresponding method in a DirectShow COM interface. For more information about the methods, see the DirectShow documentation in the Windows SDK.

USB Video Class devices can support some or all of the property sets listed above.

 

 




