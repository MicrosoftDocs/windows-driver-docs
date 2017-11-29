---
title: KSINTERFACESETID\_Standard
description: KSINTERFACESETID\_Standard
ms.assetid: f921ffba-04dd-4900-8825-5b3486009bca
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KSINTERFACESETID\_Standard


## <span id="ddk_ksinterfacesetid_standard_ks"></span><span id="DDK_KSINTERFACESETID_STANDARD_KS"></span>


This interface set contains general interface types that various pins can support. To read about how to specify what interfaces your pin type supports, see [KS Interfaces](https://msdn.microsoft.com/library/windows/hardware/ff567652).

For memory descriptor list (MDL)-based streaming, the originator of the request must create a stream header for each MDL in the list, and assign a completion routine if the MDL list must not be freed on completion of the IRP.

The following interface types in the KSINTERFACESETID\_Standard set are enumerated in KSINTERFACE\_STANDARD:

[**KSINTERFACE\_STANDARD\_STREAMING**](ksinterface-standard-streaming.md)

[**KSINTERFACE\_STANDARD\_LOOPED\_STREAMING**](ksinterface-standard-looped-streaming.md)

[**KSINTERFACE\_STANDARD\_CONTROL**](ksinterface-standard-control.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSINTERFACESETID_Standard%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




