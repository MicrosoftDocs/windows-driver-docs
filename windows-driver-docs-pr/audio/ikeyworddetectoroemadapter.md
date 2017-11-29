---
title: IKeywordDetectorOemAdapter interface
description: IKeywordDetectorOemAdapter is a Component Object Model (COM) interface for interacting with the Voice Activation Driver Interface. The IKeywordDetectorOemAdapter interface is supported in Windows 10 and later versions of Windows.
ms.assetid: FB243792-C0B0-4BCA-B4C4-B6E17FDB615C
keywords: ["IKeywordDetectorOemAdapter interface Audio Devices", "IKeywordDetectorOemAdapter interface Audio Devices , described"]
topic_type:
- apiref
api_name:
- IKeywordDetectorOemAdapter
api_type:
- COM
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# IKeywordDetectorOemAdapter interface


**IKeywordDetectorOemAdapter** is a Component Object Model (COM) interface for interacting with the Voice Activation Driver Interface. The **IKeywordDetectorOemAdapter** interface is supported in Windows 10 and later versions of Windows.

The OEM supplies a COM object implementation that acts as an intermediary between the operating system and the driver, helping to compute or parse the opaque data that is written and read to the audio driver through [**KSPROPERTY\_SOUNDDETECTOR\_PATTERNS**](ksproperty-sounddetector-patterns.md) and [**KSPROPERTY\_SOUNDDETECTOR\_MATCHRESULT**](ksproperty-sounddetector-matchresult.md).

The class identifier (CLSID) of the COM object is a detector pattern type GUID returned by the [**KSPROPERTY\_SOUNDDETECTOR\_SUPPORTEDPATTERNS**](ksproperty-sounddetector-supportedpatterns.md). The operating system calls [**CoCreateInstance**](https://msdn.microsoft.com/library/windows/desktop/ms686615) passing the pattern type GUID to instantiate the appropriate COM object that is compatible with keyword pattern type and calls methods on the object’s **IKeywordDetectorOemAdapter** interface. The operating supplies a proxy-stub for **IKeywordDetectorOemAdapter**. The OEM’s implementation may choose any of the COM threading models.

The interface design attempts to keep the object implementation stateless. In other words, the implementation should require no state to be stored between method calls. In fact, internal C++ classes likely do not need any member variables beyond those required to implement a COM object in general.

Members
-------

The **IKeywordDetectorOemAdapter** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface but does not have additional members.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20IKeywordDetectorOemAdapter%20interface%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




