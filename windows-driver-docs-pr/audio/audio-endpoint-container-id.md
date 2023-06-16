---
title: Audio endpoint container ID
description: Learn about reliable methods for obtaining the container ID of an audio endpoint associated with a Bluetooth audio device
ms.date: 04/20/2017
---

# Audio endpoint container ID

This article discusses reliable methods for obtaining the container ID of an audio endpoint associated with a Bluetooth audio device.

The audio endpoint builder uses an enumeration algorithm to determine the container IDs of audio endpoints and stores these IDs as properties in the MMDEVAPI endpoint property store. In certain cases, the logic used by the endpoint builder is insufficient for handling Bluetooth I2S designs where the container ID of an audio endpoint exposed by the audio driver is determined by another enumerator — the Bluetooth enumerator.

This scenario involving a Bluetooth I2S design that uses its own Bluetooth enumerator is rare. However, you can develop your audio driver to provide support for such a scenario. In this case, your audio driver can support a new container ID property for endpoints. The new property is [**KSPROPERTY_JACK_CONTAINERID**](./ksproperty-jack-containerid.md) and it has been added to the existing [KSPROPSETID_Jack](./kspropsetid-jack.md) property set. The value is a GUID, which is the data type for a container ID.

An audio driver supports **KSPROPERTY_JACK_CONTAINERID** if, and only if, it can reliably obtain the correct container ID through other means, such as from a Bluetooth enumerator.

If your audio driver supports the **KSPROPERTY_JACK_CONTAINERID** property, the audio system reads this property's value from the driver and stores the value as the container ID for the audio endpoint.

For more information about container IDs and the algorithm mentioned earlier, see [Container ID](../install/container-ids.md) and [Audio endpoint builder algorithm](audio-endpoint-builder-algorithm.md).

## Related topics

[Theory of Bluetooth bypass audio streaming](theory-of-operation.md)