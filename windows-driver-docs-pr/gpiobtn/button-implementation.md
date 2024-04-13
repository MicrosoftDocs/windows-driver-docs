---
title: Button Implementation
description: We recommend that you use a physical GPIO resource for both the buttons and state indicators.
ms.date: 10/17/2018
---

# Button implementation


We recommend that you use a physical GPIO resource for both the buttons and state indicators.

On systems that do not have a physical GPIO resource for a required/optional hardware button or for a GPIO indicator (laptop/slate mode indication or docked indication), a user mode or kernel mode driver can inject state changes directly to the inbox driver instead of a physical hardware resource that is attributed to the button array device (\_CID PNP0C40), laptop/slate mode state indicator (\_CID PNP0C60) or docking state indicator (\_CID PNP0C70).

To use an interface, an entry must exist in the ACPI table that defines each of the respective device(s) for which the interface is to be utilized. However, the existence of any GPIO resources for a device is optional. See [ACPI descriptor samples](acpi-descriptor-samples.md).

 

 




