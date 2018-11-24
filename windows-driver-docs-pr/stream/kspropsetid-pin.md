---
title: KSPROPSETID\_Pin
description: KSPROPSETID\_Pin
ms.assetid: a74a9cb2-2809-4e03-95da-71eeb5f079e9
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPSETID\_Pin


## <span id="ddk_kspropsetid_pin_ks"></span><span id="DDK_KSPROPSETID_PIN_KS"></span>


Clients use the properties in the KSPROPSETID\_Pin property set to query a KS filter For information about each pin factory that it supports.

The [**KSPROPERTY\_PIN\_CTYPES**](ksproperty-pin-ctypes.md) property specifies how many pin factories the KS filter supports. All other properties in this property set specify information about an individual pin factory. The KS filter identifies each pin factory by an ID, which ranges from zero to the number of pin factories minus one. The client includes the pin factory T within the [**KSP\_PIN**](https://msdn.microsoft.com/library/windows/hardware/ff566722) structure that it uses when it issues the property request.

The KSPROPSETID\_Pin property set includes:

[**KSPROPERTY\_PIN\_CATEGORY**](ksproperty-pin-category.md)

[**KSPROPERTY\_PIN\_CINSTANCES**](ksproperty-pin-cinstances.md)

[**KSPROPERTY\_PIN\_COMMUNICATION**](ksproperty-pin-communication.md)

[**KSPROPERTY\_PIN\_CONSTRAINEDDATARANGES**](ksproperty-pin-constraineddataranges.md)

[**KSPROPERTY\_PIN\_CTYPES**](ksproperty-pin-ctypes.md)

[**KSPROPERTY\_PIN\_DATAFLOW**](ksproperty-pin-dataflow.md)

[**KSPROPERTY\_PIN\_DATAINTERSECTION**](ksproperty-pin-dataintersection.md)

[**KSPROPERTY\_PIN\_DATARANGES**](ksproperty-pin-dataranges.md)

[**KSPROPERTY\_PIN\_GLOBALCINSTANCES**](ksproperty-pin-globalcinstances.md)

[**KSPROPERTY\_PIN\_INTERFACES**](ksproperty-pin-interfaces.md)

[**KSPROPERTY\_PIN\_MEDIUMS**](ksproperty-pin-mediums.md)

[**KSPROPERTY\_PIN\_NAME**](ksproperty-pin-name.md)

[**KSPROPERTY\_PIN\_NECESSARYINSTANCES**](ksproperty-pin-necessaryinstances.md)

[**KSPROPERTY\_PIN\_PHYSICALCONNECTION**](ksproperty-pin-physicalconnection.md)

[**KSPROPERTY\_PIN\_PROPOSEDATAFORMAT**](ksproperty-pin-proposedataformat.md)

[**KSPROPERTY\_PIN\_PROPOSEDATAFORMAT2**](ksproperty-pin-proposedataformat2.md)

 

 





