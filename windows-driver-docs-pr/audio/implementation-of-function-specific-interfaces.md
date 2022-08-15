---
title: Implementation of Function-Specific Interfaces
description: Implementation of Function-Specific Interfaces
keywords:
- audio miniport drivers WDK , Port Class
- miniport drivers WDK audio , Port Class
- miniport interfaces WDK audio
ms.date: 04/20/2017
---

# Implementation of Function-Specific Interfaces


## <span id="implementation_of_function_specific_interfaces"></span><span id="IMPLEMENTATION_OF_FUNCTION_SPECIFIC_INTERFACES"></span>


A typical audio adapter card contains a collection of audio hardware functions, which the adapter driver can expose to the WDM audio system through a corresponding collection of IMiniport*Xxx* interfaces. All IMiniport*Xxx* interfaces inherit from [IMiniport](/windows-hardware/drivers/ddi/portcls/nn-portcls-iminiport). Each type of miniport interface--wave, MIDI, topology, and so on--encapsulates a miniport driver for controlling a particular type of audio function on an adapter card. A driver can also expose several instances of the same miniport interface to represent multiple instances of the same (or similar) hardware functions.

For more information, see [Miniport Interfaces](miniport-interfaces.md).

 

