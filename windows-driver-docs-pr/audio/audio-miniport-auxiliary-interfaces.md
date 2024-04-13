---
title: Audio Miniport Auxiliary Interfaces
description: Audio Miniport Auxiliary Interfaces
ms.date: 03/06/2023
ms.topic: reference
---


# Audio Miniport Auxiliary Interfaces


## <span id="ddk_audio_miniport_auxiliary_interfaces_ks"></span><span id="DDK_AUDIO_MINIPORT_AUXILIARY_INTERFACES_KS"></span>


Some miniport drivers support auxiliary interfaces that are optional and provide access to specialized miniport driver capabilities. This section describes the auxiliary interfaces that are implemented by a miniport driver and exposed to the port driver.

The following interfaces are discussed in this section:

[IMusicTechnology](/windows-hardware/drivers/ddi/portcls/nn-portcls-imusictechnology)- Used to change the DirectMusic synthesizer technology that is specified in the data ranges for the DMus miniport driver's pins.

[IPinCount](/windows-hardware/drivers/ddi/portcls/nn-portcls-ipincount) - Provides a means for the miniport driver to dynamically monitor and manipulate its pin counts.

[IPinName](/windows-hardware/drivers/ddi/portcls/nf-portcls-ipinname-getpinname) - Allows the port driver to dynamically update the name of an endpoint.

[IAdapterPnpManagement](/windows-hardware/drivers/ddi/portcls/nn-portcls-iadapterpnpmanagement) - Allows adapters to register to receive PnP management messages.

 

