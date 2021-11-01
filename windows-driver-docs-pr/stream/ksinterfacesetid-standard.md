---
title: KSINTERFACESETID_Standard
description: This interface set contains general interface types that various pins can support.
ms.date: 10/12/2021
ms.localizationpriority: medium
---

# KSINTERFACESETID_Standard

This interface set contains general interface types that various pins can support. To read about how to specify what interfaces your pin type supports, see [KS Interfaces](./ks-interfaces.md).

For memory descriptor list (MDL)-based streaming, the originator of the request must create a stream header for each MDL in the list, and assign a completion routine if the MDL list must not be freed on completion of the IRP.

The following interface types in the KSINTERFACESETID_Standard set are enumerated in KSINTERFACE_STANDARD:

[**KSINTERFACE_STANDARD_STREAMING**](ksinterface-standard-streaming.md)

[**KSINTERFACE_STANDARD_LOOPED_STREAMING**](ksinterface-standard-looped-streaming.md)

[**KSINTERFACE_STANDARD_CONTROL**](ksinterface-standard-control.md)
