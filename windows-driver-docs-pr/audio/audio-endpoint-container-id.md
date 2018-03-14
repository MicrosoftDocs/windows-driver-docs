---
title: Audio Endpoint Container ID
description: The Audio Endpoint Container ID topic discusses the reliable methods available for obtaining the container ID of an audio endpoint associated with a Bluetooth audio device.
ms.assetid: 82A852FF-688C-496A-AFF1-C68B0CC1756A
ms.author: windowsdriverdev
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



