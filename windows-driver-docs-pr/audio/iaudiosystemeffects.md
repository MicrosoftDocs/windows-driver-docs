---
title: IAudioSystemEffects
description: IAudioSystemEffects
ms.date: 03/06/2023
ms.topic: reference
---

# IAudioSystemEffects

The IAudioSystemEffects interface uses the basic methods that are inherited from **IUnknown**, and must implement an **Initialize** method. The parameters that are passed to this **Initialize** method must be passed directly to the **IAudioProcessingObject::Initialize** method.

Refer to the [**IAudioProcessingObject::Initialize**](/windows/win32/api/audioenginebaseapo/nf-audioenginebaseapo-iaudioprocessingobject-initialize) method for information about the structure and the parameters that are required to implement the **IAudioSystemEffects::Initialize** method.

## IAudioSystemEffects2 interface

The **IAudioSystemEffects2** interface was introduced with Windows 8.1 for retrieving information about the processing objects in a given mode.

The **IAudioSystemEffects2** interface inherits from IAudioSystemEffects but does not have additional members. For more information, see [IAudioSystemEffects2 interface (audioengineextensionapo.h)](/windows/win32/api/audioenginebaseapo/nn-audioenginebaseapo-iaudiosystemeffects2).

## IAudioSystemEffects3 interface

APOInitSystemEffects3 adds the ability to obtain a service provider such as AudioProcessingObjectLoggingService or IAudioProcessingObjectRTQueueService. For more information, see [IAudioSystemEffects3 interface (audioengineextensionapo.h)](/windows/win32/api/audioengineextensionapo/nn-audioengineextensionapo-iaudiosystemeffects3).
