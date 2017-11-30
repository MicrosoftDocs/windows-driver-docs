---
title: KSPROPSETID\_FMRXTopology
description: The KSPROPSETID\_FMRXTopology property set is used to set FM radio properties.
ms.assetid: 66ACE82D-F0C2-4BF8-9B16-8A1B3A2C05E0
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KSPROPSETID\_FMRXTopology


The `KSPROPSETID_FMRXTopology` property set is used to set FM radio properties.

The `KSPROPSETID_FMRXTopology` property set includes the following properties:

-   [**KSPROPERTY\_FMRX\_ANTENNAENDPOINTID**](ksproperty-fmrx-antennaendpointid.md)

-   [**KSPROPERTY\_FMRX\_ENDPOINTID**](ksproperty-fmrx-endpointid.md)

-   [**KSPROPERTY\_FMRX\_VOLUME**](ksproperty-fmrx-volume.md)

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


FM radio can be enabled or disabled by setting the [**KSPROPERTY\_FMRX\_STATE**](ksproperty-fmrx-state.md) property on the wave filter. The FM volume and routing (endpoint selection) is controlled by the [**KSPROPERTY\_FMRX\_VOLUME**](ksproperty-fmrx-volume.md) and [**KSPROPERTY\_FMRX\_ENDPOINTID**](ksproperty-fmrx-endpointid.md) properties on the topology filter. Basic support for the **KSPROPERTY\_FMRX\_VOLUME** property should return the minimum volume, maximum volume, and the volume ranges.

A new [**KSNODETYPE\_FM\_RX**](ksnodetype-fm-rx.md) topology node endpoint is implemented as any other audio endpoint is in the system, and it supports all audio endpoint properties. This endpoint also supports jack properties that are defined under the [KSPROPSETID\_Jack](kspropsetid-jack.md) property set. This endpoint is in the unplugged state at boot. If capturing FM radio is supported by driver, this endpoint becomes active when FM radio is enabled. Creating a capture pin on the **KSNODETYPE\_FM\_RX** topology node allows audio capture that comes over from FM receiver.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSPROPSETID_FMRXTopology%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




