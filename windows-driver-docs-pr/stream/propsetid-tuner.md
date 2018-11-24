---
title: PROPSETID\_TUNER
description: PROPSETID\_TUNER
ms.assetid: 2697fb71-32da-40d0-aebf-d91b1a0587ba
ms.date: 11/28/2017
ms.localizationpriority: medium
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

 

 





