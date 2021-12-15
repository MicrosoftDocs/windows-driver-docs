---
title: USB Video Class Properties
description: Clients of the USB Video Class can use the following video capture property sets described in this topic.
keywords:
- USB Video Class drivers WDK AVStream , properties
- Video Class drivers WDK USB , properties
- UVC drivers WDK AVStream , properties
- property sets WDK USB Video Class
ms.date: 04/20/2017
---

# USB Video Class Properties


Clients of the USB Video Class can use the following video capture property sets:

[PROPSETID\_VIDCAP\_CAMERACONTROL](./propsetid-vidcap-cameracontrol.md)
[PROPSETID\_VIDCAP\_VIDEOPROCAMP](./propsetid-vidcap-videoprocamp.md)
Clients of the USB Video Class can make requests on filters or individual nodes. The functionality of the node-based properties is identical to that of the pre-USB Video Class filter-based properties.

To specify a node-based property, set the KSPROPERTY\_TYPE\_TOPOLOGY flag in the Flags member of the [**KSPROPERTY**](ksproperty-structure.md) structure contained in the property descriptor structure—for example, [**KSPROPERTY\_CAMERACONTROL\_NODE\_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_node_s).

Because clients can address multiple nodes on a single filter, the USB Video Class enables IHVs to support cameras that have multiple independently controlled lenses.

Additionally, a new property set has been defined:

[PROPSETID\_VIDCAP\_SELECTOR](./propsetid-vidcap-selector.md)
The property items contained in PROPSETID\_VIDCAP\_SELECTOR are node-based.

Call [**KsSynchronousDeviceControl**](/windows-hardware/drivers/ddi/ksproxy/nf-ksproxy-kssynchronousdevicecontrol) or **DeviceIoControl** to make property requests from a user-mode component. **DeviceIoControl** is documented in the Microsoft Windows SDK documentation.

Each of the property items contained in the four property sets above has a corresponding method in a DirectShow COM interface. For more information about the methods, see the DirectShow documentation in the Windows SDK.

USB Video Class devices can support some or all of the property sets listed above.

 

