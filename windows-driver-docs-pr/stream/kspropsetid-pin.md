---
title: KSPROPSETID\_Pin
description: KSPROPSETID\_Pin
ms.assetid: a74a9cb2-2809-4e03-95da-71eeb5f079e9
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPSETID_Pin%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




