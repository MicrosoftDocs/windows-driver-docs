---
title: Persistence of GFX Settings
description: Persistence of GFX Settings
ms.assetid: 91423829-7c8f-455b-bdfe-8f57f8656581
keywords:
- GFX filters WDK audio , settings persistence
- persistence WDK GFX filters
- set-property WDK audio
- get-property WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Persistence of GFX Settings


## <span id="persistence_of_gfx_settings"></span><span id="PERSISTENCE_OF_GFX_SETTINGS"></span>


A GFX filter does not explicitly save any of its settings persistently from one filter instance to the next. Instead, it relies on the operating system to keep track of its settings between instantiations. The operating system uses get and set property requests to save and restore the state of a GFX filter.

The GFX filter implements the KS property [**KSPROPERTY\_AUDIO\_FILTER\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff537285) to identify the property sets that must be saved persistently. This property's get request retrieves an array of property set GUIDs.

Immediately after the operating system instantiates the GFX filter, it queries the filter for its KSPROPERTY\_AUDIO\_FILTER\_STATE property to obtain the list of property sets to restore. Next, by using KS serialization (described in [KS Properties](https://msdn.microsoft.com/library/windows/hardware/ff567671)), the operating system reviews each property in each property set and restores each to its previously saved value.

Similarly, just before it closes a GFX instance, the operating system queries the KSPROPERTY\_AUDIO\_FILTER\_STATE property to obtain the list of property sets to save. Again, the operating system uses KS serialization to review each property in each property set, get each value, and save the value persistently.

 

 




