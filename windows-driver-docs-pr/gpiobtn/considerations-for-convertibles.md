---
title: Considerations for convertibles
description: This topic discusses timing and performance considerations for convertibles.
ms.assetid: 2353023A-989A-4836-A39C-0B5F749E7FF2
ms.localizationpriority: medium
ms.date: 10/17/2018
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

 

 




