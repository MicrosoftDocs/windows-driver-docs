---
title: Processing Mutex in AVStream
description: Processing Mutex in AVStream
keywords:
- AVStream mutexes WDK
- mutexes WDK AVStream
- processing mutex WDK AVStream
ms.date: 04/20/2017
---

# Processing Mutex in AVStream





The third mutex is the processing mutex. Individual filters and pins have their own processing mutexes. AVStream independently acquires the processing mutex before processing at the filter and pin level, in order to synchronize access to processing-related structures. AVStream also acquires the processing mutex during other operations including binding pins to a pipe section, sleep or wake power operations, and changing descriptors. Minidrivers can manually acquire the mutex to perform a synchronous operation, such as processing or descriptor modification. A minidriver should obtain the processing mutex before it makes any change that cannot happen at the same time as processing.

Like the other two types of mutexes, processing mutexes are not obtained recursively. This means that if a minidriver attempts to grab the processing mutex while processing, a deadlock occurs.

Do not use the processing mutex to suspend processing for long periods of time. Instead, manipulate the processing control gate directly by using the **KSGATE*Xxx*** functions.

A thread that has acquired a processing mutex should not subsequently attempt to acquire the filter control mutex.

To manipulate the processing mutex, use the following functions:

[**KsFilterAcquireProcessingMutex**](/windows-hardware/drivers/ddi/ks/nf-ks-ksfilteracquireprocessingmutex), [**KsPinAcquireProcessingMutex**](/windows-hardware/drivers/ddi/ks/nf-ks-kspinacquireprocessingmutex), [**KsFilterReleaseProcessingMutex**](/windows-hardware/drivers/ddi/ks/nf-ks-ksfilterreleaseprocessingmutex), [**KsPinReleaseProcessingMutex**](/windows-hardware/drivers/ddi/ks/nf-ks-kspinreleaseprocessingmutex)

 

