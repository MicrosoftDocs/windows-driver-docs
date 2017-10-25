---
title: Behavior and guidance
author: windows-driver-content
description: The states of the two indicators available (mode and docking) play an important role in determining the user experience around touch keyboard and screen auto-rotation.
ms.assetid: C5A0B339-3159-4AFF-B322-D041E49D875A
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

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[gpiobtn\gpiobtn]:%20Behavior%20and%20guidance%20%20RELEASE:%20%289/25/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


