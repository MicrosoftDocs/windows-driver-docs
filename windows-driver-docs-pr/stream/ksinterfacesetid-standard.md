---
title: KSINTERFACESETID\_Standard
description: KSINTERFACESETID\_Standard
ms.assetid: f921ffba-04dd-4900-8825-5b3486009bca
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSINTERFACESETID\_Standard


## <span id="ddk_ksinterfacesetid_standard_ks"></span><span id="DDK_KSINTERFACESETID_STANDARD_KS"></span>


This interface set contains general interface types that various pins can support. To read about how to specify what interfaces your pin type supports, see [KS Interfaces](https://msdn.microsoft.com/library/windows/hardware/ff567652).

For memory descriptor list (MDL)-based streaming, the originator of the request must create a stream header for each MDL in the list, and assign a completion routine if the MDL list must not be freed on completion of the IRP.

The following interface types in the KSINTERFACESETID\_Standard set are enumerated in KSINTERFACE\_STANDARD:

[**KSINTERFACE\_STANDARD\_STREAMING**](ksinterface-standard-streaming.md)

[**KSINTERFACE\_STANDARD\_LOOPED\_STREAMING**](ksinterface-standard-looped-streaming.md)

[**KSINTERFACE\_STANDARD\_CONTROL**](ksinterface-standard-control.md)

 

 





