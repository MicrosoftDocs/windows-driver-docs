---
title: Dynamic Subdevice Registration and Unregistration
description: Dynamic Subdevice Registration and Unregistration
ms.assetid: 7157b7b3-655b-49d9-be45-c4a86a3cc82d
keywords:
- dynamic subdevice WDK audio
- audio subdevices WDK
- registering audio subdevices WDK
- deregistering audio subdevices WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Dynamic Subdevice Registration and Unregistration


Devices that support some form of jack presence detection are called dynamic devices, and their jacks must support the [**KSPROPERTY\_JACK\_DESCRIPTION**](https://msdn.microsoft.com/library/windows/hardware/ff537364) property. The following steps show the algorithm that is used by the driver of a dynamic device to create, register, or unregister the associated subdevices for these dynamic devices. The subdevices are created in the form of filters.

The following steps show what happens when there is an audio device plugged into the jack when the audio device driver is loaded:

1.  The driver uses jack presence detection to determine that there is a device plugged into the jack. The driver calls [**PcRegisterSubdevice**](https://msdn.microsoft.com/library/windows/hardware/ff537731) to register a topology filter with [Portcls](introduction-to-port-class.md). A [**KSCATEGORY\_AUDIO**](https://msdn.microsoft.com/library/windows/hardware/ff548261) interface is created as a result of the topology filter registration.

2.  The audio stack is notified when the **KSCATEGORY\_AUDIO** interface is created and the [AudioEndpoint Builder](audio-endpoint-builder-algorithm.md) creates and initializes an associated endpoint, and then sets its state to active.

3.  The driver registers a wave filter with Portcls and the audio stack is notified.

4.  The driver calls [**PcRegisterPhysicalConnection**](https://msdn.microsoft.com/library/windows/hardware/ff537726) to connect the wave filter with the topology filter. This physical connection is then registered with Portcls.

5.  The driver sets the IsConnected member of the [**KSJACK\_DESCRIPTION**](https://msdn.microsoft.com/library/windows/hardware/ff537136) structure to **TRUE** to indicate that there is a device plugged into the jack.

**Note**   If the audio device lacks jack presence detection, the **IsConnected** member must always be **TRUE**. To confirm whether the device supports jack presence detection, a client application can call [IKsJackDescription2::GetJackDescription2](https://go.microsoft.com/fwlink/p/?linkid=143698) to read the JackCapabilities flag of the [**KSJACK\_DESCRIPTION2**](https://msdn.microsoft.com/library/windows/hardware/ff537138) structure. If this flag has the JACKDESC2\_PRESENCE\_DETECT\_CAPABILITY bit set, it indicates that the endpoint supports jack presence detection. In that case, the return value of the **IsConnected** member can be interpreted as an accurate reflection of the insertion status of the jack.

 

The following steps explain what happens if there is no audio device plugged into the jack when the driver is loaded:

1.  The driver uses jack presence detection to determine that there is no device plugged into the jack. But it registers a topology filter with Portcls for the jack, and a **KSCATEGORY\_AUDIO** interface is created.

2.  The audio stack is notified when the **KSCATEGORY\_AUDIO** interface is created. The AudioEndpointBuilder queries the miniport driver to determine from the **KSJACK\_DESCRIPTION** property whether to set the state of the endpoint as unplugged.

3.  The driver sets the **IsConnected** member of the **KSJACK\_DESCRIPTION** structure to **FALSE** to indicate that there is no device plugged into the jack.

For more information about the different states of an audio endpoint, see [Audio Endpoint Builder Algorithm](audio-endpoint-builder-algorithm.md).

To comply with the preceding description of the subdevice registration and unregistration processes, devices drivers that support jack presence detection must react in the following manner, in response to plug insertion and removal:

**Device driver response to a plug insertion**

1.  Driver must call **PcRegisterSubdevice** to register a wave filter with Portcls.
    **Note**   The driver already called **PcRegisterSubdevice** on the topology filter when the driver was loaded with no device plugged into the jack.

     

2.  The driver must call **PcRegisterPhysicalConnection** to register the "wave to topology filter" connection with Portcls.

3.  The driver must set the **IsConnected** member of the **KSJACK\_DESCRIPTION** structure to **TRUE**.

**Device driver response to a plug removal**

1.  Driver must call [**IUnregisterPhysicalConnection::UnregisterPhysicalConnection**](https://msdn.microsoft.com/library/windows/hardware/ff537024) to unregister the physical connection between the wave filter and the topology filter.

2.  Driver must call [**IUnregisterSubdevice::UnregisterSubdevice**](https://msdn.microsoft.com/library/windows/hardware/ff537032) to unregister the wave filter.

3.  Driver must set the **IsConnected** member of the **KSJACK\_DESCRIPTION** structure **FALSE**.

 

 




