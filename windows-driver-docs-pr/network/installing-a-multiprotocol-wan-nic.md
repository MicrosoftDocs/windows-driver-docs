---
title: Installing a Multiprotocol WAN NIC
description: Installing a Multiprotocol WAN NIC
ms.assetid: 7000040c-8a26-496d-ae26-580aace68160
keywords:
- add-registry-sections WDK networking , multiprotocol WAN NIC
- multiprotocol WAN NIC WDK networking
- WAN NIC WDK networking
- NIC multiprotocol WAN WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installing a Multiprotocol WAN NIC





A multiprotocol WAN NIC provides more than one WAN protocol. For example, such a NIC might allow the user to select ISDN, Frame Relay, or channelized T1. The user selects the WAN protocol during installation of the NIC or when configuring the NIC.

> [!NOTE]
> ISDN capabilities have been deprecated in Windows 10 and later. 


A vendor of a multiprotocol WAN NIC must provide a co-installer that installs a wizard page. (For more information about co-installers, see [Writing a Co-installer](https://msdn.microsoft.com/library/windows/hardware/ff554011)). The wizard page prompts the user to select a WAN protocol:

-   If the user selects ISDN, the ISDN Wizard is displayed. The ISDN Wizard prompts the user for the ISDN switch type and, depending on the selected switch type, other ISDN parameter values. For more information, see [Specifying ISDN Keys and Values for an ISDN Adapter](specifying-isdn-keys-and-values-for-an-isdn-adapter.md).

-   If the user selects a WAN protocol other than ISDN, the Wizard adds the **ShowIsdnPages** registry value to the WAN NIC's instance key. The Wizard, in this case, sets **ShowIsdnPages** to zero to suppress the display of the ISDN Wizard. As long as **ShowIsdnPages** is zero, the ISDN Wizard is suppressed.

After the WAN NIC has been installed, the user can reconfigure the NIC, using the NIC's property page:

-   If the user changes the protocol from ISDN to another WAN protocol, the property page adds the **ShowIsdnPages** registry value to the WAN NIC's instance key, if necessary. The property page sets **ShowIsdnPages** to zero to suppress the display of the ISDN Wizard.

-   If the user changes the protocol to ISDN, the property page for the WAN NIC displays a dialog box that prompts the user to apply the change. When the user applies the change, the property page sets **ShowIsdnPages** to 1. When the user again opens the NIC's property page, the ISDN Wizard is displayed.

Note that the **LowerRange** binding interface for a multiprotocol WAN NIC that supports ISDN must be set to **isdn**. For more information, see [Specifying Binding Interfaces](specifying-binding-interfaces.md). If the **ShowIsdnPages** registry value is not present and if the NIC's **LowerRange** is set to **isdn**, the ISDN Wizard is displayed during installation and configuration of the NIC. If **ShowIsdnPages** is set to zero, the ISDN Wizard is not displayed. If **ShowIsdnPages** is set to 1, the ISDN Wizard is displayed during configuration of the NIC.

 

 





