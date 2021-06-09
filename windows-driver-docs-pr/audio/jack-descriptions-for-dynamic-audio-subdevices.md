---
title: Jack Descriptions for Dynamic Audio Subdevices
description: Jack Descriptions for Dynamic Audio Subdevices
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Jack Descriptions for Dynamic Audio Subdevices


In Windows Vista and later, the [**KSPROPERTY\_JACK\_DESCRIPTION**](./ksproperty-jack-description.md) property provides information about a jack or a collection of jacks on a subdevice in an audio adapter. (In this context, the term *subdevice* is synonymous with *KS filter*.) The property value is an array of one or more [**KSJACK\_DESCRIPTION**](./ksjack-description.md) structures. Each structure describes the color, connector type, and physical location of a jack. In addition, the structure contains an **IsConnected** member that is **TRUE** if an audio endpoint device such as a microphone or headphones is plugged into the jack, and is **FALSE** if the jack is empty. To provide an up-to-date value for **IsConnected**, the adapter driver for a dynamic subdevice relies on the jack-presence detection capabilities of the audio hardware. For a static subdevice (with no jack-presence detection), the **IsConnected** member should always be **TRUE**. For more information, see [Jack Description Property](jack-description-property.md).

When the user inserts a plug into a jack on a dynamic subdevice, the adapter driver should call the [**PcRegisterSubdevice**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcregistersubdevice) function to register the subdevice. While the subdevice remains registered, if the adapter driver receives an IOCTL containing a KSPROPERTY\_JACK\_DESCRIPTION request for the subdevice, the driver should set the **IsConnected** member of the property value to **TRUE**.

When the user removes the plug from the jack on the dynamic subdevice, the adapter driver should call the [**IUnregisterSubdevice::UnregisterSubdevice**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iunregistersubdevice-unregistersubdevice) method to delete the subdevice's registration. While the subdevice is not registered, if the adapter driver receives an IOCTL containing a KSPROPERTY\_JACK\_DESCRIPTION request for the subdevice, the driver should set the **IsConnected** member of the property value to **FALSE**.

 

