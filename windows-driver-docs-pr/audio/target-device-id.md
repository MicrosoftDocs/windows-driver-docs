---
title: Target Device ID
description: Target Device ID
ms.assetid: 5275e404-19b9-4a44-88de-1a40f3798ede
keywords:
- GFX filters WDK audio , target device IDs
- target device IDs WDK audio
- device IDs WDK audio
- identifying audio target devices
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Target Device ID


## <span id="target_device_id"></span><span id="TARGET_DEVICE_ID"></span>


Some GFX filters, especially those that are designed to process signals for specific hardware, might require information about the device they are producing data for (in the case of a render GFX filter) or receiving data from (in the case of a capture GFX filter). For example, a filter might need to alter its signal processing algorithm to accommodate different members of a family of related devices.

Just after instantiating a GFX filter, but before restoring the filter's persistent properties, the operating system sets a property called [**KSPROPERTY\_AUDIOGFX\_RENDERTARGETDEVICEID**](https://msdn.microsoft.com/library/windows/hardware/ff537235) or [**KSPROPERTY\_AUDIOGFX\_CAPTURETARGETDEVICEID**](https://msdn.microsoft.com/library/windows/hardware/ff537233) (for render or capture GFX filters, respectively) to inform the GFX filter of the Plug and Play (PnP) device ID of the render or capture device. The format of the property data for KSPROPERTY\_AUDIOGFX\_*Xxx*TARGETDEVICEID is a NULL-terminated, Unicode string.

If a GFX filter detects that the user has connected it to a render or capture device that it does not support (for example, a device made by another vendor), the GFX filter can choose not to perform global-effects processing on that device's stream. In this case, however, the GFX filter should simply pass the stream through unchanged. Under no circumstances should the GFX filter attempt to block or degrade the stream.

 

 




