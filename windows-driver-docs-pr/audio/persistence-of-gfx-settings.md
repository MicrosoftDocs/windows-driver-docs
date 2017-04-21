---
title: Persistence of GFX Settings
description: Persistence of GFX Settings
ms.assetid: 91423829-7c8f-455b-bdfe-8f57f8656581
keywords:
- GFX filters WDK audio , settings persistence
- persistence WDK GFX filters
- set-property WDK audio
- get-property WDK audio
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Persistence of GFX Settings


## <span id="persistence_of_gfx_settings"></span><span id="PERSISTENCE_OF_GFX_SETTINGS"></span>


A GFX filter does not explicitly save any of its settings persistently from one filter instance to the next. Instead, it relies on the operating system to keep track of its settings between instantiations. The operating system uses get and set property requests to save and restore the state of a GFX filter.

The GFX filter implements the KS property [**KSPROPERTY\_AUDIO\_FILTER\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff537285) to identify the property sets that must be saved persistently. This property's get request retrieves an array of property set GUIDs.

Immediately after the operating system instantiates the GFX filter, it queries the filter for its KSPROPERTY\_AUDIO\_FILTER\_STATE property to obtain the list of property sets to restore. Next, by using KS serialization (described in [KS Properties](https://msdn.microsoft.com/library/windows/hardware/ff567671)), the operating system reviews each property in each property set and restores each to its previously saved value.

Similarly, just before it closes a GFX instance, the operating system queries the KSPROPERTY\_AUDIO\_FILTER\_STATE property to obtain the list of property sets to save. Again, the operating system uses KS serialization to review each property in each property set, get each value, and save the value persistently.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Persistence%20of%20GFX%20Settings%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


