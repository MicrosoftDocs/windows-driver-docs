---
title: Bass Management
description: Bass Management
ms.date: 11/07/2018
ms.localizationpriority: medium
---

# Bass Management


There are two bass management modes: forward bass management and reverse bass management.

-   Forward bass management filters out the low frequency content of the audio data stream. The forward bass management algorithm redirects the filtered output to the subwoofer or to the front-left and front-right loudspeaker channels, depending on the channels that can handle deep bass frequencies. This decision is based on the setting of the LRBig flag.

    To set the LRBig flag, the user uses the Sound applet in Control Panel to access the Bass Management Settings dialog box. The user selects a check box to indicate, for example, that the front-right and front-left speakers are full range and this action sets the LRBig flag. To clear this flag, click the check box to clear it.

-   Reverse bass management distributes the signal from the subwoofer channel to the other output channels. The signal is directed either to all channels or to the front-left and front-right channels, depending on the setting of the LRBig flag. This process uses a substantial gain reduction when mixing the subwoofer signal into the other channels.

    The bass management mode that is used depends on the availability of a subwoofer and the bass-handling capability of the main speakers. In Windows, the user provides this information via the Sound applet in Control Panel.

 

 




