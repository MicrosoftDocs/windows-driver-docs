---
Description: DRM Functions and Interfaces
MS-HAID: 'audio.drm\_functions\_and\_interfaces'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: DRM Functions and Interfaces
---

# DRM Functions and Interfaces


## <span id="drm_functions_and_interfaces"></span><span id="DRM_FUNCTIONS_AND_INTERFACES"></span>


The system driver components *Drmk.sys* and *Portcls.sys* implement a collection of DRM functions and interfaces that drivers use for managing the digital rights of kernel-streaming audio content. The *Drmk.sys* component implements a number of **DrmXxx** functions, and *Portcls.sys* implements a DRM-specific set of **PcXxx** functions, and also the [IDrmPort](audio.idrmport) and [IDrmPort2](audio.idrmport2) interfaces.

The following DRM functions are available:

[**DrmAddContentHandlers**](audio.drmaddcontenthandlers)

Provides the system with a driver interface consisting of a list of functions for handling protected content.
[**DrmCreateContentMixed**](audio.drmcreatecontentmixed)

Creates a DRM content ID to identify a KS audio stream containing mixed content from several input streams.
[**DrmDestroyContent**](audio.drmdestroycontent)

Deletes a DRM content ID.
[**DrmForwardContentToDeviceObject**](audio.drmforwardcontenttodeviceobject)

Authenticates a driver and sends it the DRM content ID and content rights that the system has assigned to a stream containing protected content.
[**DrmForwardContentToFileObject**](audio.drmforwardcontenttofileobject)

Obsolete function.
[**DrmForwardContentToInterface**](audio.drmforwardcontenttointerface)

Authenticates a driver object and sends it the DRM content ID and content rights that the system has assigned to a stream containing protected content.
[**DrmGetContentRights**](audio.drmgetcontentrights)

Retrieves the DRM content rights that the system has assigned to a DRM content ID.
The functions in this list are declared in header file Drmk.h. The kernel-mode [DRMK system driver](kernel-mode-wdm-audio-components.md#drmk-system-driver), Drmk.sys, exports the entry points for these functions.

In Windows XP and later, the PortCls system driver, Portcls.sys, exports a different set of entry points for the same set of DRM functions. The names of the PortCls functions are similar to those in the previous list, except that they use the prefix Pc instead of Drm:

[**PcAddContentHandlers**](audio.pcaddcontenthandlers)

[**PcCreateContentMixed**](audio.pccreatecontentmixed)

[**PcDestroyContent**](audio.pcdestroycontent)

[**PcForwardContentToDeviceObject**](audio.pcforwardcontenttodeviceobject)

[**PcForwardContentToFileObject**](audio.pcforwardcontenttofileobject)

[**PcForwardContentToInterface**](audio.pcforwardcontenttointerface)

[**PcGetContentRights**](audio.pcgetcontentrights)

These function names are declared in header file Portcls.h. The entry points in Portcls.sys do nothing more than call the corresponding functions in Drmk.sys. The PortCls entry points are provided simply for convenience so that an audio driver that is already connected to Portcls.sys does not need to explicitly load Drmk.sys.

In Windows XP and later, the same set of functions is also exposed as methods in the [IDrmPort](audio.idrmport) and [IDrmPort2](audio.idrmport2) interfaces:

[**IDrmPort2::AddContentHandlers**](audio.idrmport2_addcontenthandlers)

[**IDrmPort::CreateContentMixed**](audio.idrmport_createcontentmixed)

[**IDrmPort::DestroyContent**](audio.idrmport_destroycontent)

[**IDrmPort2::ForwardContentToDeviceObject**](audio.idrmport2_forwardcontenttodeviceobject)

[**IDrmPort::ForwardContentToFileObject**](audio.idrmport_forwardcontenttofileobject)

[**IDrmPort::ForwardContentToInterface**](audio.idrmport_forwardcontenttointerface)

[**IDrmPort::GetContentRights**](audio.idrmport_getcontentrights)

The **IDrmPort** and **IDrmPort2** interfaces are declared in header file Portcls.h and are implemented in Portcls.sys. These methods do nothing more than call the corresponding functions in Drmk.sys. A miniport driver obtains a reference to a **IDrmPort***x* interface by querying its port driver for this interface. The advantage to using a **IDrmPort***x* interface instead of the corresponding Drm*Xxx* or Pc*Xxx* functions is that the driver can use this query to determine at run time whether the operating system version supports DRM or not. This simplifies the task of writing a single driver that can run both in newer versions of Windows that support DRM and in older versions that do not. **IDrmPort2** is derived from **IDrmPort** and provides two additional methods.

The WaveCyclic and WavePci port drivers use the [IDrmAudioStream](audio.idrmaudiostream) interface if it is supported by the corresponding miniport driver. The port driver calls the [**IDrmAudioStream::SetContentId**](audio.idrmaudiostream_setcontentid) method to assign DRM protection to the digital content in an audio stream.

The [**DEFINE\_DRMRIGHTS\_DEFAULT**](audio.define_drmrights_default) macro, which is defined in header file Drmk.h, initializes the members of a [**DRMRIGHTS**](audio.drmrights) structure to their default values.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20DRM%20Functions%20and%20Interfaces%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



