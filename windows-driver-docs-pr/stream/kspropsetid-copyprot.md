---
title: KSPROPSETID\_CopyProt
description: KSPROPSETID\_CopyProt
ms.assetid: f5596bed-e7be-4ad0-aaf7-cb34550e0726
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPSETID_CopyProt%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




