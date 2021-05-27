---
title: Restarting Processing in AVStream
description: Restarting Processing in AVStream
keywords:
- restarting AVStream processing
- AVStream process restarting WDK
- resume processing WDK AVStream
- pending status WDK AVStream
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Restarting Processing in AVStream





AVStream stops processing if any of the following conditions are true:

-   In a pin-centric environment, no data is currently available on the pin.

-   In a filter-centric environment, at least one pin for which the **Flags** member of the [**KSPIN\_DESCRIPTOR\_EX**](/windows-hardware/drivers/ddi/ks/ns-ks-_kspin_descriptor_ex) structure does not set KSPIN\_FLAG\_FRAMES\_NOT\_REQUIRED\_FOR\_PROCESSING, does not have data waiting to be processed. By default, this flag is not set.

-   The minidriver's processing dispatch callback routine returns STATUS\_PENDING, regardless of frame availability. Note that the processing dispatch can be either [*AVStrMiniFilterProcess*](/windows-hardware/drivers/ddi/ks/nc-ks-pfnksfilterprocess) or [*AVStrMiniPinProcess*](/windows-hardware/drivers/ddi/ks/nc-ks-pfnkspin), depending on whether the minidriver implements [pin-centric processing](pin-centric-processing.md) or [filter-centric processing](filter-centric-processing.md).

AVStream initiates processing when new data arrives into a previously empty queue. Therefore, if the minidriver's processing dispatch returns STATUS\_PENDING when the associated queues are full, the minidriver will never be called on to resume processing. If the minidriver sets STATUS\_PENDING, the minidriver must call [**KsPinAttemptProcessing**](/windows-hardware/drivers/ddi/ks/nf-ks-kspinattemptprocessing) or [**KsFilterAttemptProcessing**](/windows-hardware/drivers/ddi/ks/nf-ks-ksfilterattemptprocessing) to resume processing.

Do not return STATUS\_SUCCESS from the processing dispatch if the minidriver does not actually process data. This causes AVStream to immediately call the minidriver again, resulting in an infinite loop between AVStream and the processing dispatch.

 

