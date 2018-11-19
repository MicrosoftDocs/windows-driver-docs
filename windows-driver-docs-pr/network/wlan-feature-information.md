---
title: WLAN feature information
description: This section contains specific WLAN feature information.
ms.assetid: E8B759CC-695E-418A-A93F-FA7F0E302D6D
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WLAN feature information


This section contains specific WLAN feature information.

## Wi-Fi network preference


Wi-Fi network preference is as follows.

1.  User-defined networks are used first. These are listed in the Wi-Fi CPL as *Known networks*. A network becomes a *Known network* in the following cases.

    -   The user manually taps on the network (including hotspots) in the Wi-Fi CPL.

    -   The user adds the network manually from the Wi-Fi CPL.

    -   Wireless network profiles that are roamed to the phone from Windows PCs.

    If multiple user-defined networks are found during the network scan, the most recently connected network is used.

    **Note**  
    Wireless network profiles that are roamed to the phone from Windows PCs do not show up in the *Known networks* list until the phone has connected to the network once.

     

2.  Hotspots (from a Store application or OEM plug-in) are prioritized next. If multiple hotspots are found, the following factors are used to decide preference.

    -   Network security. Secure networks (any security type) are preferred over open networks.

    -   Signal strength.

**Note**  
When there are multiple networks that have the same name or SSID, only the first configured network that uses the name or SSID is accepted. 

Windows does not disconnect from a network once it is connected if the signal from the network is still present, even when a more preferred network becomes available. For example, if a user connects to a mobile operator hotspot at a store, and walks home while the signal from the hotspot is still present, the phone will not move to the user's configured home Wi-Fi network.

## Also in this section:

-   [Fast Roaming with 802.11k, 802.11v, and 802.11r](fast-roaming-with-802-11k--802-11v--and-802-11r.md)