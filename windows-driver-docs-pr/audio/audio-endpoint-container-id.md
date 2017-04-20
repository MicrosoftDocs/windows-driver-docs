---
title: Audio Endpoint Container ID
description: The Audio Endpoint Container ID topic discusses the reliable methods available for obtaining the container ID of an audio endpoint associated with a Bluetooth audio device.
ms.assetid: 82A852FF-688C-496A-AFF1-C68B0CC1756A
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Audio Endpoint Container ID


The Audio Endpoint Container ID topic discusses the reliable methods available for obtaining the container ID of an audio endpoint associated with a Bluetooth audio device.

The audio endpoint builder uses an enumeration algorithm to determine the container IDs of audio endpoints, and then stores these IDs as properties in the MMDEVAPI endpoint property store. In certain cases, the logic used by the endpoint builder is not sufficient to handle Bluetooth I2S designs where the container ID of an audio endpoint exposed by the audio driver is determined by another enumerator - the Bluetooth enumerator.

This scenario involving a Bluetooth I2S design that uses its own Bluetooth enumerator is rare. But regardless, you can develop your audio driver to provide support for such a scenario. In this case, your audio driver can support a new container ID property for endpoints. The new property is [**KSPROPERTY\_JACK\_CONTAINERID**](https://msdn.microsoft.com/library/windows/hardware/dn265129) and it's been added to the existing [KSPROPSETID\_Jack](https://msdn.microsoft.com/library/windows/hardware/ff537484) property set. The value is a GUID, which is the data type for a container ID.

An audio driver supports **KSPROPERTY\_JACK\_CONTAINERID**, if and only if, it can reliably obtain the correct container ID through some other means; For example, from a Bluetooth enumerator.

If your audio driver supports the **KSPROPERTY\_JACK\_CONTAINERID** property, the audio system reads this property's value from the driver, and then stores the value as the container ID for the audio endpoint.

For more information about container IDs and about the algorithm mentioned in the preceding section, see [Container ID](http://msdn.microsoft.com/library/windows/hardware/ff540024.aspx) and [Audio Endpoint Builder Algorithm](audio-endpoint-builder-algorithm.md).

## <span id="related_topics"></span>Related topics
[Theory of Operation](theory-of-operation.md)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Audio%20Endpoint%20Container%20ID%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


