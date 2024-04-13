---
title: Setting Copy Protection Hardware
description: Setting Copy Protection Hardware
keywords:
- copy protection WDK video miniport , setting
ms.date: 04/20/2017
---

# Setting Copy Protection Hardware


## <span id="ddk_setting_copy_protection_hardware_gg"></span><span id="DDK_SETTING_COPY_PROTECTION_HARDWARE_GG"></span>


Miniport drivers that returned VP\_FLAGS\_PROTECTED in [**VIDEOPARAMETERS**](/windows/win32/api/tvout/ns-tvout-videoparameters)'s **dwFlags** member on a VP\_COMMAND\_GET should do the following in response to the VP\_COMMAND\_SET command, depending on the **dwCPCommand** member of the VIDEOPARAMETERS structure:

-   If **dwCPCommand** is VP\_CP\_CMD\_ACTIVATE, the miniport driver should turn on copy protection and generate and return a unique copy protection key in **dwCPKey**.

-   If **dwCPCommand** is VP\_CP\_CMD\_DEACTIVATE and the copy protection key in **dwCPKey** is valid, the miniport driver should turn off copy protection.

-   If **dwCPCommand** is VP\_CP\_CMD\_CHANGE and the copy protection key in **dwCPKey** is valid, the miniport driver should change copy protection based on the data in based on the trigger data in **bCP\_APSTriggerBits**.

Miniport drivers of devices that do not have copy protection hardware should simply return NO\_ERROR in the **Status** field of the [**VRP**](/windows-hardware/drivers/ddi/video/ns-video-_video_request_packet)'s **StatusBlock**.

 

