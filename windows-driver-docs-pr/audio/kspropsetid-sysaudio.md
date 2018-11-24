---
title: KSPROPSETID\_Sysaudio
description: KSPROPSETID\_Sysaudio
ms.assetid: 817cbda5-9d37-4c12-8749-98a86540609f
keywords: ["KSPROPSETID_Sysaudio"]
ms.date: 11/28/2017
ms.localizationpriority: medium
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

 

 





