---
title: Jack Descriptions for Dynamic Audio Subdevices
description: Jack Descriptions for Dynamic Audio Subdevices
ms.assetid: e04f4000-3b93-4f4b-afec-007e5821f125
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Jack Descriptions for Dynamic Audio Subdevices


In Windows Vista and later, the [**KSPROPERTY\_JACK\_DESCRIPTION**](https://msdn.microsoft.com/library/windows/hardware/ff537364) property provides information about a jack or a collection of jacks on a subdevice in an audio adapter. (In this context, the term *subdevice* is synonymous with *KS filter*.) The property value is an array of one or more [**KSJACK\_DESCRIPTION**](https://msdn.microsoft.com/library/windows/hardware/ff537136) structures. Each structure describes the color, connector type, and physical location of a jack. In addition, the structure contains an **IsConnected** member that is **TRUE** if an audio endpoint device such as a microphone or headphones is plugged into the jack, and is **FALSE** if the jack is empty. To provide an up-to-date value for **IsConnected**, the adapter driver for a dynamic subdevice relies on the jack-presence detection capabilities of the audio hardware. For a static subdevice (with no jack-presence detection), the **IsConnected** member should always be **TRUE**. For more information, see [Jack Description Property](jack-description-property.md).

When the user inserts a plug into a jack on a dynamic subdevice, the adapter driver should call the [**PcRegisterSubdevice**](https://msdn.microsoft.com/library/windows/hardware/ff537731) function to register the subdevice. While the subdevice remains registered, if the adapter driver receives an IOCTL containing a KSPROPERTY\_JACK\_DESCRIPTION request for the subdevice, the driver should set the **IsConnected** member of the property value to **TRUE**.

When the user removes the plug from the jack on the dynamic subdevice, the adapter driver should call the [**IUnregisterSubdevice::UnregisterSubdevice**](https://msdn.microsoft.com/library/windows/hardware/ff537032) method to delete the subdevice's registration. While the subdevice is not registered, if the adapter driver receives an IOCTL containing a KSPROPERTY\_JACK\_DESCRIPTION request for the subdevice, the driver should set the **IsConnected** member of the property value to **FALSE**.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Jack%20Descriptions%20for%20Dynamic%20Audio%20Subdevices%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


