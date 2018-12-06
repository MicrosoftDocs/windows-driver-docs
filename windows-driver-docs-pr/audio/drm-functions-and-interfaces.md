---
title: DRM Functions and Interfaces
description: DRM Functions and Interfaces
ms.assetid: 62c739da-91e8-428e-b76c-ec9621b12597
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


The system driver components *Drmk.sys* and *Portcls.sys* implement a collection of DRM functions and interfaces that drivers use for managing the digital rights of kernel-streaming audio content. The *Drmk.sys* component implements a number of **DrmXxx** functions, and *Portcls.sys* implements a DRM-specific set of **PcXxx** functions, and also the [IDrmPort](https://msdn.microsoft.com/library/windows/hardware/ff536571) and [IDrmPort2](https://msdn.microsoft.com/library/windows/hardware/ff536573) interfaces.

The following DRM functions are available:

[**DrmAddContentHandlers**](https://msdn.microsoft.com/library/windows/hardware/ff536347)

Provides the system with a driver interface consisting of a list of functions for handling protected content.
[**DrmCreateContentMixed**](https://msdn.microsoft.com/library/windows/hardware/ff536348)

Creates a DRM content ID to identify a KS audio stream containing mixed content from several input streams.
[**DrmDestroyContent**](https://msdn.microsoft.com/library/windows/hardware/ff536349)

Deletes a DRM content ID.
[**DrmForwardContentToDeviceObject**](https://msdn.microsoft.com/library/windows/hardware/ff536351)

Authenticates a driver and sends it the DRM content ID and content rights that the system has assigned to a stream containing protected content.
[**DrmForwardContentToFileObject**](https://msdn.microsoft.com/library/windows/hardware/ff536352)

Obsolete function.
[**DrmForwardContentToInterface**](https://msdn.microsoft.com/library/windows/hardware/ff536353)

Authenticates a driver object and sends it the DRM content ID and content rights that the system has assigned to a stream containing protected content.
[**DrmGetContentRights**](https://msdn.microsoft.com/library/windows/hardware/ff536354)

Retrieves the DRM content rights that the system has assigned to a DRM content ID.
The functions in this list are declared in header file Drmk.h. The kernel-mode [DRMK system driver](kernel-mode-wdm-audio-components.md#drmk_system_driver), Drmk.sys, exports the entry points for these functions.

In Windows XP and later, the PortCls system driver, Portcls.sys, exports a different set of entry points for the same set of DRM functions. The names of the PortCls functions are similar to those in the previous list, except that they use the prefix Pc instead of Drm:

[**PcAddContentHandlers**](https://msdn.microsoft.com/library/windows/hardware/ff537684)

[**PcCreateContentMixed**](https://msdn.microsoft.com/library/windows/hardware/ff537689)

[**PcDestroyContent**](https://msdn.microsoft.com/library/windows/hardware/ff537690)

[**PcForwardContentToDeviceObject**](https://msdn.microsoft.com/library/windows/hardware/ff537696)

[**PcForwardContentToFileObject**](https://msdn.microsoft.com/library/windows/hardware/ff537697)

[**PcForwardContentToInterface**](https://msdn.microsoft.com/library/windows/hardware/ff537698)

[**PcGetContentRights**](https://msdn.microsoft.com/library/windows/hardware/ff537700)

These function names are declared in header file Portcls.h. The entry points in Portcls.sys do nothing more than call the corresponding functions in Drmk.sys. The PortCls entry points are provided simply for convenience so that an audio driver that is already connected to Portcls.sys does not need to explicitly load Drmk.sys.

In Windows XP and later, the same set of functions is also exposed as methods in the [IDrmPort](https://msdn.microsoft.com/library/windows/hardware/ff536571) and [IDrmPort2](https://msdn.microsoft.com/library/windows/hardware/ff536573) interfaces:

[**IDrmPort2::AddContentHandlers**](https://msdn.microsoft.com/library/windows/hardware/ff536575)

[**IDrmPort::CreateContentMixed**](https://msdn.microsoft.com/library/windows/hardware/ff536581)

[**IDrmPort::DestroyContent**](https://msdn.microsoft.com/library/windows/hardware/ff536583)

[**IDrmPort2::ForwardContentToDeviceObject**](https://msdn.microsoft.com/library/windows/hardware/ff536579)

[**IDrmPort::ForwardContentToFileObject**](https://msdn.microsoft.com/library/windows/hardware/ff536584)

[**IDrmPort::ForwardContentToInterface**](https://msdn.microsoft.com/library/windows/hardware/ff536586)

[**IDrmPort::GetContentRights**](https://msdn.microsoft.com/library/windows/hardware/ff536588)

The **IDrmPort** and **IDrmPort2** interfaces are declared in header file Portcls.h and are implemented in Portcls.sys. These methods do nothing more than call the corresponding functions in Drmk.sys. A miniport driver obtains a reference to a **IDrmPort***x* interface by querying its port driver for this interface. The advantage to using a **IDrmPort***x* interface instead of the corresponding Drm*Xxx* or Pc*Xxx* functions is that the driver can use this query to determine at run time whether the operating system version supports DRM or not. This simplifies the task of writing a single driver that can run both in newer versions of Windows that support DRM and in older versions that do not. **IDrmPort2** is derived from **IDrmPort** and provides two additional methods.

The WaveCyclic and WavePci port drivers use the [IDrmAudioStream](https://msdn.microsoft.com/library/windows/hardware/ff536568) interface if it is supported by the corresponding miniport driver. The port driver calls the [**IDrmAudioStream::SetContentId**](https://msdn.microsoft.com/library/windows/hardware/ff536570) method to assign DRM protection to the digital content in an audio stream.

The [**DEFINE\_DRMRIGHTS\_DEFAULT**](https://msdn.microsoft.com/library/windows/hardware/ff536254) macro, which is defined in header file Drmk.h, initializes the members of a [**DRMRIGHTS**](https://msdn.microsoft.com/library/windows/hardware/ff536355) structure to their default values.

 

 




