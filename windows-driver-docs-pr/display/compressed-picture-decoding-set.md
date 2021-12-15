---
title: Compressed Picture Decoding Set
description: Compressed Picture Decoding Set
keywords:
- compressed picture decoding set WDK DirectX VA
ms.date: 04/20/2017
---

# Compressed Picture Decoding Set


## <span id="ddk_compressed_picture_decoding_set_gg"></span><span id="DDK_COMPRESSED_PICTURE_DECODING_SET_GG"></span>


This section defines the minimal interoperability configuration set for compressed picture decoding. This entire set of configurations must be supported by a decoder, and one or more configurations in this set must be supported by an accelerator. An [additional configuration set](additional-encouraged-configuration-set.md) is provided for which support is encouraged (these configurations are not required).

The first six configurations in this set are for all [restricted profiles](restricted-profiles.md). The seventh configuration in this set is defined only for MPEG2\_C and MPEG2\_D.

The minimal interoperability configuration set of configurations for compressed picture decoding is defined by the third through the last members of the [**DXVA\_ConfigPictureDecode**](/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_configpicturedecode) structure.

 

