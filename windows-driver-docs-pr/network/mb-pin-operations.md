---
title: MB PIN Operations
description: MB PIN Operations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# MB PIN Operations


This topic describes the operations related to access control of subscription information stored either in the MB device memory or on the Subscriber Identity Module (SIM card).

## MB PIN Operations for Device Hibernation

Per the [3GPP](https://www.3gpp.org/about-3gpp) standard, there are different types of SIM PINs.  Information on this page applies only to SIM PIN1, also known as the universal PIN of a given SIM card.  

Each time the cellular modem resumes from a low power state, the 3GPP standard requires that SIM credentials be refreshed before connecting to the cellular network.  

Because PC and Windows-based tablet devices power down all peripheral devices when the system enters hibernation, SIM verification is required when the system powers up.  

For modems that are internal to the chassis, Windows caches the SIM PIN and automatically unlocks the SIM PIN when the system is woken up, as long as the modem was unlocked when the system entered hibernation.

Windows does this by detecting when the underlying modem device exits the D3 cold power state.  D3 cold is a device power state that is equivalent to powered off.  

If a cellular modem device does not support D3 cold, Windows does not automatically unlock the modem’s SIM PIN.  Instead, the user must manually enter the PIN to restore the mobile broadband connection.

For information on how to enable D3 cold in your USB modem device, please see:

* [Supporting D3Cold for USB Devices](https://techcommunity.microsoft.com/t5/Microsoft-USB-Blog/bg-p/MicrosoftUSBBlog).
* [Supporting D3cold in a Driver](../kernel/supporting-d3cold-in-a-driver.md)

For additional information about PIN operations, see [OID\_WWAN\_PIN](./oid-wwan-pin.md).
