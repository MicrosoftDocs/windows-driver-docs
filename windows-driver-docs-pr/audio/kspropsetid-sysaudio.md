---
title: KSPROPSETID\_Sysaudio
description: KSPROPSETID\_Sysaudio
ms.assetid: 817cbda5-9d37-4c12-8749-98a86540609f
keywords: ["KSPROPSETID_Sysaudio"]
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KSPROPSETID\_Sysaudio


## <span id="ddk_kspropsetid_sysaudio_ks"></span><span id="DDK_KSPROPSETID_SYSAUDIO_KS"></span>


The `KSPROPSETID_Sysaudio` property set is used to access the properties of the [SysAudio system driver](https://msdn.microsoft.com/library/windows/hardware/ff537039#sysaudio-system-driver). Sysaudio is the driver that creates and manages [virtual audio devices](https://msdn.microsoft.com/library/windows/hardware/ff538734) on behalf of DirectSound and other clients.

SysAudio's clients use this property set to do the following:

-   Enumerate the virtual audio devices that are available to SysAudio's clients.

-   Enumerate the pins that SysAudio is capable of instantiating on a virtual audio device.

-   Determine the capabilities of those pins.

-   Enumerate the nodes that lie along the path of the data stream that flows through each pin.

-   Configure the data path through a pin to either include or bypass an AEC node.

After exploring the properties of the available virtual audio devices, the client should be ready to select one of the virtual audio devices and create a pin on that device. Some clients might choose to create more than one pin on a virtual audio device or to create pins on more than one device. For information about creating pins, see [Pin Factories](https://msdn.microsoft.com/library/windows/hardware/ff537747).

After the pin is created, the client can use the [KSPROPSETID\_Sysaudio\_Pin](kspropsetid-sysaudio-pin.md) property set to manage the pin.

The following properties are members of the `KSPROPSETID_Sysaudio` property set:

[**KSPROPERTY\_SYSAUDIO\_COMPONENT\_ID**](ksproperty-sysaudio-component-id.md)

[**KSPROPERTY\_SYSAUDIO\_CREATE\_VIRTUAL\_SOURCE**](ksproperty-sysaudio-create-virtual-source.md)

[**KSPROPERTY\_SYSAUDIO\_DEVICE\_COUNT**](ksproperty-sysaudio-device-count.md)

[**KSPROPERTY\_SYSAUDIO\_DEVICE\_FRIENDLY\_NAME**](ksproperty-sysaudio-device-friendly-name.md)

[**KSPROPERTY\_SYSAUDIO\_DEVICE\_INSTANCE**](ksproperty-sysaudio-device-instance.md)

[**KSPROPERTY\_SYSAUDIO\_DEVICE\_INTERFACE\_NAME**](ksproperty-sysaudio-device-interface-name.md)

[**KSPROPERTY\_SYSAUDIO\_INSTANCE\_INFO**](ksproperty-sysaudio-instance-info.md)

[**KSPROPERTY\_SYSAUDIO\_SELECT\_GRAPH**](ksproperty-sysaudio-select-graph.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSPROPSETID_Sysaudio%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




