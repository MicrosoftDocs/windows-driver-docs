---
title: IKeywordDetectorOemAdapter Interface
description: IKeywordDetectorOemAdapter is a Component Object Model (COM) interface for interacting with the Voice Activation Driver Interface. The IKeywordDetectorOemAdapter interface is supported in Windows 10 and later versions of Windows.
keywords: ["IKeywordDetectorOemAdapter interface Audio Devices", "IKeywordDetectorOemAdapter interface Audio Devices , described"]
topic_type:
- apiref
ms.topic: reference
api_name:
- IKeywordDetectorOemAdapter
api_type:
- COM
ms.date: 03/06/2023
---


# IKeywordDetectorOemAdapter interface

**IKeywordDetectorOemAdapter** is a Component Object Model (COM) interface for interacting with the Voice Activation Driver Interface. The **IKeywordDetectorOemAdapter** interface is supported in Windows 10 and later versions of Windows.

The OEM supplies a COM object implementation that acts as an intermediary between the operating system and the driver, helping to compute or parse the opaque data that is written and read to the audio driver through [**KSPROPERTY\_SOUNDDETECTOR\_PATTERNS**](ksproperty-sounddetector-patterns.md) and [**KSPROPERTY\_SOUNDDETECTOR\_MATCHRESULT**](ksproperty-sounddetector-matchresult.md).

The class identifier (CLSID) of the COM object is a detector pattern type GUID returned by the [**KSPROPERTY\_SOUNDDETECTOR\_SUPPORTEDPATTERNS**](ksproperty-sounddetector-supportedpatterns.md). The operating system calls [**CoCreateInstance**](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance) passing the pattern type GUID to instantiate the appropriate COM object that is compatible with keyword pattern type and calls methods on the object’s **IKeywordDetectorOemAdapter** interface. The operating supplies a proxy-stub for **IKeywordDetectorOemAdapter**. The OEM’s implementation may choose any of the COM threading models.

The interface design attempts to keep the object implementation stateless. In other words, the implementation should require no state to be stored between method calls. In fact, internal C++ classes likely do not need any member variables beyond those required to implement a COM object in general.

## Members

The **IKeywordDetectorOemAdapter** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface but does not have additional members.

 

