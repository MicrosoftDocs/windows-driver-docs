---
title: DRM Functions and Interfaces
description: DRM Functions and Interfaces
keywords:
- Digital Rights Management WDK audio , functions
- DRM WDK audio , functions
- Digital Rights Management WDK audio , interfaces
- DRM WDK audio , interfaces
- interfaces WDK DRM
- functions WDK DRM
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DRM Functions and Interfaces


## <span id="drm_functions_and_interfaces"></span><span id="DRM_FUNCTIONS_AND_INTERFACES"></span>


The system driver components *Drmk.sys* and *Portcls.sys* implement a collection of DRM functions and interfaces that drivers use for managing the digital rights of kernel-streaming audio content. The *Drmk.sys* component implements a number of **DrmXxx** functions, and *Portcls.sys* implements a DRM-specific set of **PcXxx** functions, and also the [IDrmPort](/windows-hardware/drivers/ddi/portcls/nn-portcls-idrmport) and [IDrmPort2](/windows-hardware/drivers/ddi/portcls/nn-portcls-idrmport2) interfaces.

The following DRM functions are available:

[**DrmAddContentHandlers**](/windows-hardware/drivers/ddi/drmk/nf-drmk-drmaddcontenthandlers)

Provides the system with a driver interface consisting of a list of functions for handling protected content.
[**DrmCreateContentMixed**](/windows-hardware/drivers/ddi/drmk/nf-drmk-drmcreatecontentmixed)

Creates a DRM content ID to identify a KS audio stream containing mixed content from several input streams.
[**DrmDestroyContent**](/windows-hardware/drivers/ddi/drmk/nf-drmk-drmdestroycontent)

Deletes a DRM content ID.
[**DrmForwardContentToDeviceObject**](/windows-hardware/drivers/ddi/drmk/nf-drmk-drmforwardcontenttodeviceobject)

Authenticates a driver and sends it the DRM content ID and content rights that the system has assigned to a stream containing protected content.
[**DrmForwardContentToFileObject**](/windows-hardware/drivers/ddi/drmk/nf-drmk-drmforwardcontenttofileobject)

Obsolete function.
[**DrmForwardContentToInterface**](/windows-hardware/drivers/ddi/drmk/nf-drmk-drmforwardcontenttointerface)

Authenticates a driver object and sends it the DRM content ID and content rights that the system has assigned to a stream containing protected content.
[**DrmGetContentRights**](/windows-hardware/drivers/ddi/drmk/nf-drmk-drmgetcontentrights)

Retrieves the DRM content rights that the system has assigned to a DRM content ID.
The functions in this list are declared in header file Drmk.h. The kernel-mode [DRMK system driver](kernel-mode-wdm-audio-components.md#drmk_system_driver), Drmk.sys, exports the entry points for these functions.

In Windows XP and later, the PortCls system driver, Portcls.sys, exports a different set of entry points for the same set of DRM functions. The names of the PortCls functions are similar to those in the previous list, except that they use the prefix Pc instead of Drm:

[**PcAddContentHandlers**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcaddcontenthandlers)

[**PcCreateContentMixed**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pccreatecontentmixed)

[**PcDestroyContent**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcdestroycontent)

[**PcForwardContentToDeviceObject**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcforwardcontenttodeviceobject)

[**PcForwardContentToFileObject**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcforwardcontenttofileobject)

[**PcForwardContentToInterface**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcforwardcontenttointerface)

[**PcGetContentRights**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcgetcontentrights)

These function names are declared in header file Portcls.h. The entry points in Portcls.sys do nothing more than call the corresponding functions in Drmk.sys. The PortCls entry points are provided simply for convenience so that an audio driver that is already connected to Portcls.sys does not need to explicitly load Drmk.sys.

In Windows XP and later, the same set of functions is also exposed as methods in the [IDrmPort](/windows-hardware/drivers/ddi/portcls/nn-portcls-idrmport) and [IDrmPort2](/windows-hardware/drivers/ddi/portcls/nn-portcls-idrmport2) interfaces:

[**IDrmPort2::AddContentHandlers**](/windows-hardware/drivers/ddi/portcls/nf-portcls-idrmport2-addcontenthandlers)

[**IDrmPort::CreateContentMixed**](/windows-hardware/drivers/ddi/portcls/nf-portcls-idrmport-createcontentmixed)

[**IDrmPort::DestroyContent**](/windows-hardware/drivers/ddi/portcls/nf-portcls-idrmport-destroycontent)

[**IDrmPort2::ForwardContentToDeviceObject**](/windows-hardware/drivers/ddi/portcls/nf-portcls-idrmport2-forwardcontenttodeviceobject)

[**IDrmPort::ForwardContentToFileObject**](/windows-hardware/drivers/ddi/portcls/nf-portcls-idrmport-forwardcontenttofileobject)

[**IDrmPort::ForwardContentToInterface**](/windows-hardware/drivers/ddi/portcls/nf-portcls-idrmport-forwardcontenttointerface)

[**IDrmPort::GetContentRights**](/windows-hardware/drivers/ddi/portcls/nf-portcls-idrmport-getcontentrights)

The **IDrmPort** and **IDrmPort2** interfaces are declared in header file Portcls.h and are implemented in Portcls.sys. These methods do nothing more than call the corresponding functions in Drmk.sys. A miniport driver obtains a reference to a **IDrmPort***x* interface by querying its port driver for this interface. The advantage to using a **IDrmPort***x* interface instead of the corresponding Drm*Xxx* or Pc*Xxx* functions is that the driver can use this query to determine at run time whether the operating system version supports DRM or not. This simplifies the task of writing a single driver that can run both in newer versions of Windows that support DRM and in older versions that do not. **IDrmPort2** is derived from **IDrmPort** and provides two additional methods.

The WaveCyclic and WavePci port drivers use the [IDrmAudioStream](/windows-hardware/drivers/ddi/drmk/nn-drmk-idrmaudiostream) interface if it is supported by the corresponding miniport driver. The port driver calls the [**IDrmAudioStream::SetContentId**](/windows-hardware/drivers/ddi/drmk/nf-drmk-idrmaudiostream-setcontentid) method to assign DRM protection to the digital content in an audio stream.

The [**DEFINE\_DRMRIGHTS\_DEFAULT**](/previous-versions/ff536254(v=vs.85)) macro, which is defined in header file Drmk.h, initializes the members of a [**DRMRIGHTS**](/windows-hardware/drivers/ddi/drmk/ns-drmk-tagdrmrights) structure to their default values.

 

