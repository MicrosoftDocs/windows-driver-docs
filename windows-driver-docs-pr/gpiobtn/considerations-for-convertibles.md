---
title: Considerations for convertibles
author: windows-driver-content
description: This topic discusses timing and performance considerations for convertibles.
ms.assetid: 2353023A-989A-4836-A39C-0B5F749E7FF2
---

# Considerations for convertibles


This topic discusses timing and performance considerations for convertibles.

Convertible systems give users the option to have both a slate and a laptop in one system. This section provides examples of how to create the transition between laptop mode and slate mode.

The main criteria for distinguishing between laptop and tablet modes is determined by the presence of a keyboard. The general rule to follow is, the convertible is a laptop when the keyboard becomes fully accessible to the user and the user can comfortably type in a natural position.

An important aspect to consider when triggering a mode or docking change is to make sure that no undesired state changes are sent when a mode or docking change happens. From this perspective, one approach is to trigger an indicator change as soon as the system has reached a new stable state, but not sooner.

The general rule is to trigger the indicator mode change after the user finishes their action and the system is fully transitioned into the new mode.

Mode indicator examples are as follows:

-   Attach or detach keyboard
-   Flip the screen
-   Swivel the screen
-   Slide the screen to cover or uncover the keyboard

Dock indicator examples are as follows:

-   Attach to a classic docking system
-   Attach to a port replicator

To provide an optimal user experience, the state indicator change should be a fast user experience. The state change notification should be sent no later than 200ms after the system reaches the new state.

The following two examples start with the laptop mode and describe the optimal timing when the indicator state should be toggled:

![keyboard attach and detach for convertible](images/keyboardattachdetachconvertible.jpg)

**Figure 1 Keyboard Attach and Detach for Convertible**

![screen swivel convertible](images/screenswivelconvertible.jpg)

**Figure 2 Screen Swivel Convertible**

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[gpiobtn\gpiobtn]:%20Considerations%20for%20convertibles%20%20RELEASE:%20%289/25/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


