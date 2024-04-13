---
title: PnP and Power Management Callback Sequences
description: The following topics show the sequence in which the framework calls a WDF driver's PnP and Power Management event callback functions
ms.date: 04/20/2017
---

# PnP and Power Management Callback Sequences


The following topics show the sequence in which the framework calls a WDF (KMDF and UMDF v2) driver's PnP and Power Management event callback functions:

-   [Power-Up Sequence for a Function or Filter Driver](power-up-sequence-for-a-function-or-filter-driver.md)
-   [Power-Up Sequence for a Bus Driver](power-up-sequence-for-a-bus-driver.md)
-   [Power-Down and Removal Sequence for a Function or Filter Driver](power-down-and-removal-sequence-for-a-function-or-filter-driver.md)
-   [Power-Down and Removal Sequence for a Bus Driver](power-down-and-removal-sequence-for-a-bus-driver.md)
-   [Surprise-Removal Sequence](surprise-removal-sequence.md)
-   [WDM IRPs and corresponding WDF event callbacks](./wdm-irps-and-kmdf-event-callback-functions.md)

The following topics identify typical PnP and power management scenarios and show the sequence in which the framework calls a driver's event callback functions during these scenarios:

- [A User Plugs in a Device](a-user-plugs-in-a-device.md)
- [A User Unplugs a Device](a-user-unplugs-a-device.md)
- [A Device Enters a Low-Power State](a-device-enters-a-low-power-state.md)
- [A Device Returns to Its Working State](a-device-returns-to-its-working-state.md)
- [The PnP Manager Redistributes System Resources](the-pnp-manager-redistributes-system-resources.md)
 

