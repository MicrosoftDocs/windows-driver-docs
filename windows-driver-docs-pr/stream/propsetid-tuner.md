---
title: PROPSETID\_TUNER
description: PROPSETID\_TUNER
ms.assetid: 2697fb71-32da-40d0-aebf-d91b1a0587ba
---

# PROPSETID\_TUNER


## <span id="ddk_propsetid_tuner_ks"></span><span id="DDK_PROPSETID_TUNER_KS"></span>


The PROPSETID\_TUNER property set controls devices that support TV or radio tuning. This property set provides support for multistandard video tuners, as well as tuners with multiple inputs.

The KSPROPERTY\_TUNER enumeration in *ksmedia.h* specifies the properties of this set.

Support for this property set is optional and should be implemented only by minidrivers that support TV or radio tuning.

Tuner capture minidrivers are required to implement the following properties:

[**KSPROPERTY\_TUNER\_CAPS**](ksproperty-tuner-caps.md)

[**KSPROPERTY\_TUNER\_FREQUENCY**](ksproperty-tuner-frequency.md)

[**KSPROPERTY\_TUNER\_INPUT**](ksproperty-tuner-input.md)

[**KSPROPERTY\_TUNER\_MODE**](ksproperty-tuner-mode.md)

[**KSPROPERTY\_TUNER\_MODE\_CAPS**](ksproperty-tuner-mode-caps.md)

[**KSPROPERTY\_TUNER\_SCAN\_CAPS**](ksproperty-tuner-scan-caps.md) new for Windows Vista

[**KSPROPERTY\_TUNER\_STANDARD**](ksproperty-tuner-standard.md)

[**KSPROPERTY\_TUNER\_STATUS**](ksproperty-tuner-status.md)

Tuner capture minidrivers can optionally implement the following properties:

[**KSPROPERTY\_TUNER\_IF\_MEDIUM**](ksproperty-tuner-if-medium.md)

[**KSPROPERTY\_TUNER\_NETWORKTYPE\_SCAN\_CAPS**](ksproperty-tuner-networktype-scan-caps.md) new for Windows Vista

[**KSPROPERTY\_TUNER\_SCAN\_STATUS**](ksproperty-tuner-scan-status.md) new for Windows Vista

[**KSPROPERTY\_TUNER\_STANDARD\_MODE**](ksproperty-tuner-standard-mode.md) new for Windows Vista

### <span id="directshow_interface"></span><span id="DIRECTSHOW_INTERFACE"></span>DirectShow Interface

The DirectShow **IAMTVTuner** interface (see the DirectShow documentation in the Microsoft Windows SDK) provides access to the properties of this set.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20PROPSETID_TUNER%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




