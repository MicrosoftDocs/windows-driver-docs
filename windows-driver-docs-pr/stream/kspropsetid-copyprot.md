---
title: KSPROPSETID\_CopyProt
description: KSPROPSETID\_CopyProt
ms.assetid: f5596bed-e7be-4ad0-aaf7-cb34550e0726
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPSETID\_CopyProt


## <span id="ddk_kspropsetid_copyprot_ks"></span><span id="DDK_KSPROPSETID_COPYPROT_KS"></span>


The KSPROPSETID\_CopyProt property set defines properties to specify the level of copyright protection for DVD streams.

The KSPROPERTY\_COPYPROT enumeration in *Ksmedia.h* specifies the properties of this set.

DVD decoder minidrivers must implement support for the following properties:

[**KSPROPERTY\_DVDCOPY\_CHLG\_KEY**](ksproperty-dvdcopy-chlg-key.md)

[**KSPROPERTY\_DVDCOPY\_DVD\_KEY1**](ksproperty-dvdcopy-dvd-key1.md)

[**KSPROPERTY\_DVDCOPY\_DEC\_KEY2**](ksproperty-dvdcopy-dec-key2.md)

[**KSPROPERTY\_DVDCOPY\_TITLE\_KEY**](ksproperty-dvdcopy-title-key.md)

[**KSPROPERTY\_COPY\_MACROVISION**](ksproperty-copy-macrovision.md)

[**KSPROPERTY\_DVDCOPY\_REGION**](ksproperty-dvdcopy-region.md)

[**KSPROPERTY\_DVDCOPY\_DISC\_KEY**](ksproperty-dvdcopy-disc-key.md)

DVD decoder minidrivers can optionally implement the following property:

[**KSPROPERTY\_DVDCOPY\_SET\_COPY\_STATE**](ksproperty-dvdcopy-set-copy-state.md)

 

 





