---
title: MB PIN Operations
description: MB PIN Operations
ms.assetid: ca9e1537-29e8-4849-a634-5c2177886321
---

# MB PIN Operations


This topic describes the operations related to access control of subscription information stored either in the MB device memory or on the Subscriber Identity Module (SIM card).

For more information about PIN operations, see [OID\_WWAN\_PIN](https://msdn.microsoft.com/library/windows/hardware/ff569828).

# MB PIN Operations for Device Hibernation
Per 3GPP standard, there are different types of SIM PINs.  For the purpose of this document, all described behaviors are only related to SIM PIN1 or also known as the universal PIN of a given SIM card.  SIM PIN2 or other types of SIM PIN is out of scope for this documentation.
As prescribed by 3GPP standard, every time the device power cycles the SIM security should be refreshed.  This means that when user reboots the device, the SIM card would require SIM PIN from the user to be able to connect to cellular network.  While this works great for a phone device, PC and tablet devices have more complicated system power states that need to be taken into consideration. 
PC and tablet devices would shut down all peripheral devices when the system enters hibernation (S4).  Although the user does not consider the device being power cycled, in reality the modem has been powered off.   When resuming from hibernation the SIM security state would have been refreshed and verification is required.  This would require user to enter SIM PIN every time the system restores from lower power states.  For most users that have configured the device to connect automatically would expect the device to connect to the mobile broadband network when the device resumes from sleep or hibernation.  With SIM PIN being locked, a manual SIM PIN step would be required prior connections could be established.
To provide a seamless connection experience similar to Wi-Fi, Windows would cache the SIM PIN code and automatically unlock the SIM PIN on the modem when system is woken up if the modem is unlocked by the user before it entered hibernation.  This only applies to modems that are internal in the chassis as it is impossible for Windows to distinguish whether a modem was removed from the device if the modem is unpluggable (USB modem dongles) during sleep or hibernation. Windows does this by detecting the underneath modem device has executed D3 cold exit.  D3 cold is a device power state that is equivalent to powered off.  When the system is woken up, if the modem was previously power off due to sleep or hibernation the modem would have to be powered back to D0 state and a D3 exit indication would be provided to Windows.  
Whether the system overall supports D3 cold or not is IHV’s decision.  If the modem device does not support D3 cold, then Windows would not unlock the modem’s SIM PIN automatically and users’ unlock action is required for mobile broadband connection.  For detail on what is required for a USB modem device to support D3 cold please refer to the following link:
https://blogs.msdn.microsoft.com/usbcoreblog/2013/02/18/supporting-d3cold-for-usb-devices/



 

 





