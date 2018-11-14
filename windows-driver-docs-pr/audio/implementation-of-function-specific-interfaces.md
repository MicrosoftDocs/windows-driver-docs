---
title: Implementation of Function-Specific Interfaces
description: Implementation of Function-Specific Interfaces
ms.assetid: 6a15c8b5-17ca-4658-bf52-cf9b3307e706
keywords:
- audio miniport drivers WDK , Port Class
- miniport drivers WDK audio , Port Class
- miniport interfaces WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Implementation of Function-Specific Interfaces


## <span id="implementation_of_function_specific_interfaces"></span><span id="IMPLEMENTATION_OF_FUNCTION_SPECIFIC_INTERFACES"></span>


A typical audio adapter card contains a collection of audio hardware functions, which the adapter driver can expose to the WDM audio system through a corresponding collection of IMiniport*Xxx* interfaces. All IMiniport*Xxx* interfaces inherit from [IMiniport](https://msdn.microsoft.com/library/windows/hardware/ff536698). Each type of miniport interface--wave, MIDI, topology, and so on--encapsulates a miniport driver for controlling a particular type of audio function on an adapter card. A driver can also expose several instances of the same miniport interface to represent multiple instances of the same (or similar) hardware functions.

For more information, see [Miniport Interfaces](miniport-interfaces.md).

 

 




