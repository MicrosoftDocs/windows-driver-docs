---
title: KSPROPSETID\_FMRXTopology
description: The KSPROPSETID\_FMRXTopology property set is used to set FM radio properties.
ms.assetid: 66ACE82D-F0C2-4BF8-9B16-8A1B3A2C05E0
ms.date: 11/28/2017
ms.localizationpriority: medium
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

 

 





