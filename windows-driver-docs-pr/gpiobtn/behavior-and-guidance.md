---
title: Behavior and guidance
description: The states of the two indicators available (mode and docking) play an important role in determining the user experience around touch keyboard and screen auto-rotation.
ms.assetid: C5A0B339-3159-4AFF-B322-D041E49D875A
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Behavior and guidance


The states of the two indicators available (mode and docking) play an important role in determining the user experience around touch keyboard and screen auto-rotation.

When you determine the modes that are to be reported for the indicators, consider the scenarios and behaviors that are described in *Table 1 Expected Behaviors*.

**Table 1 Expected Behaviors**

| Mode indicator | Dock indicator | On screen keyboard displayed | Auto-rotation enabled |
|----------------|----------------|------------------------------|-----------------------|
| Laptop         | Undocked       | No                           | No                    |
| Laptop         | Docked         | No                           | No                    |
| Slate          | Undocked       | Yes                          | Yes                   |
| Slate          | Docked         | Yes                          | No                    |

 

When the system is in slate mode:

-   Touch screen keyboard is auto-invoked
-   Rotation lock is unlocked (unless previously locked by the user)
-   Rotation lock can be toggled
-   Display can freely rotate

When the system is in laptop mode:

-   Touch screen keyboard is suppressed
-   Rotation is set to landscape and locked
-   Rotation lock cannot be toggled
-   Display cannot freely rotate

To match this behavior, the mode and dock indicators must be implemented according to the guidance that is described in *Table 2 Implementation Guidance*.

**Table 2 Implementation Guidance**

| Indicator | State    | Implementation guidance                                                                                                                                                                                                                                                                                                                   |
|-----------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Mode      | Laptop   | Report laptop if a keyboard is attached and comfortably accessible to the user. (For convertibles, the system can be in clamshell or equivalent mode from a keyboard accessibility perspective.)                                                                                                                                          |
| Mode      | Slate    | Report slate if the physical keyboard is not available to the user. (This includes the case where they don’t have complete access or they can’t type comfortably.)                                                                                                                                                                        |
| Dock      | Docked   | Report Dock if the system is stationary (attached to a docking system or a port replicator). Stand-alone AC power supply does not apply as long as the system can be freely moved.                                                                                                                                                        |
| Dock      | Undocked | Report undocked if the system is not stationary. This applies to the case of having the device connected to general power supply because it can still be freely moved. A power supply is not mandatory for reporting undocked. This is the natural state of any system when it is not connected to a port replicator or docking solution. |

 

 

 




