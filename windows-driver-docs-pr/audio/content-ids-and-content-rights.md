---
title: Content IDs and Content Rights
description: Content IDs and Content Rights
ms.assetid: aee123e4-bc1b-4ba8-9f8d-a9d207297c8d
keywords: ["content rights WDK audio", "content IDs WDK audio", "Digital Rights Management WDK audio , content IDs", "DRM WDK audio , content IDs", "Digital Rights Management WDK audio , content rights", "DRM WDK audio , content rights", "identifiers WDK audio", "mixed streams WDK audio", "DigitalOutputDisable flag", "CopyProtect flag"]
---

# Content IDs and Content Rights


## <span id="content_ids_and_content_rights"></span><span id="CONTENT_IDS_AND_CONTENT_RIGHTS"></span>


A content ID (identifier) is a ULONG value that the [DRMK system driver](kernel-mode-wdm-audio-components.md#drmk_system_driver) generates at runtime to identify DRM-protected content in the audio-data stream that feeds into a particular pin.

Content rights are a digital representation of the rights granted by the content provider to the user for playing and copying DRM-protected content. Content rights are specified in the form of a [**DRMRIGHTS**](https://msdn.microsoft.com/library/windows/hardware/ff536355) structure that DRMK passes to the audio driver.

DRMRIGHTS contains two flags: **DigitalOutputDisable** and **CopyProtect**. If the **DigitalOutputDisable** flag is set, the driver must disable any digital outputs that connect to external devices (through an S/PDIF connector, for example). If the **CopyProtect** flag is set, the driver must disable features that might allow a persistent copy of the secure content to be saved to disk or to any other form of nonvolatile storage. For example, typical audio hardware allows a playback signal to be routed through the capture channel. If this signal is in digital form, the captured signal may be a perfect digital copy of the input signal. If the playback mix contains data from any stream that has a **CopyProtect** flag set, the driver must mute the playback-capture path.

A DRM-compliant audio driver must support the [IDrmAudioStream](https://msdn.microsoft.com/library/windows/hardware/ff536568) interface on its WaveCyclic and WavePci miniport driver objects, which expose sink pins for rendering audio data. In order to obtain a reference to an **IDrmAudioStream** object from the driver, DRMK calls the **QueryInterface** method on the pin. The pin has an interface of type [IMiniportWaveCyclicStream](https://msdn.microsoft.com/library/windows/hardware/ff536715) or [IMiniportWavePciStream](https://msdn.microsoft.com/library/windows/hardware/ff536725). The **IDrmAudioStream** interface supports only one method, [**IDrmAudioStream::SetContentId**](https://msdn.microsoft.com/library/windows/hardware/ff536570) (in addition to the three **IUnknown** methods). When DRMK calls **SetContentId**, it passes in a content ID and content rights, which the driver associates with the pin's data stream.

Instead of calling the DRM functions in Drmk.sys directly, a WaveCyclic or WavePci miniport driver can access the DRM functions through the [IDrmPort2](https://msdn.microsoft.com/library/windows/hardware/ff536573) interface (**IDrmPort2** is derived from base class [IDrmPort](https://msdn.microsoft.com/library/windows/hardware/ff536571)). In Microsoft Windows XP and later, the WaveCyclic and WavePci port drivers support **IDrmPort2**. The miniport driver obtains a reference to the port driver's **IDrmPort2** interface by calling the port object's **QueryInterface** method with REFIID IID\_IDrmPort2.

Some audio drivers support hardware mixing and can handle several input data streams at the same time. This type of driver must keep track of both the content IDs for the individual streams and the composite content rights of all the streams. The driver calls [**IDrmPort::CreateContentMixed**](https://msdn.microsoft.com/library/windows/hardware/ff536581) to determine the composite rights for a mixed stream and to create a content ID to identify that stream. When the driver finishes using the content ID, it must call [**IDrmPort::DestroyContent**](https://msdn.microsoft.com/library/windows/hardware/ff536583) to delete the content ID.

Each time an input stream is added to or removed from a mixer, the driver must delete the content ID for the old mix and create a new content ID for the new mix. Before deleting an old content ID, the driver must first successfully forward a new content ID to all the streams to which it previously forwarded the old content ID. For more information, see [Forwarding DRM Content IDs](forwarding-drm-content-ids.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Content%20IDs%20and%20Content%20Rights%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


