---
title: Setting TV Connector and Copy Protection Hardware
description: Setting TV Connector and Copy Protection Hardware
ms.assetid: 2de45c31-6a44-4a57-84b9-3cb21c905f4b
keywords:
- TV connector WDK video miniport
- copy protection WDK video miniport , setting
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Setting TV Connector and Copy Protection Hardware


## <span id="ddk_setting_tv_connector_and_copy_protection_hardware_gg"></span><span id="DDK_SETTING_TV_CONNECTOR_AND_COPY_PROTECTION_HARDWARE_GG"></span>


For any bit set by a miniport driver in the **dwFlags** member of [**VIDEOPARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff570173) on a VP\_COMMAND\_GET, the miniport driver can perform a set on a VP\_COMMAND\_SET. It is the caller's responsibility to call the miniport driver to set only that functionality for which the miniport driver indicated support on a VP\_COMMAND\_GET. The miniport driver should respond to a VP\_COMMAND\_SET by setting the hardware with the value of each VIDEOPARAMETERS field for which the corresponding bit is set in **dwFlags**. For example:

-   If the miniport driver set the VP\_FLAGS\_TV\_MODE bit on a VP\_COMMAND\_GET, then the miniport driver should change the TV mode to the value specified by **dwMode** when VP\_FLAGS\_TV\_MODE is set on a VP\_COMMAND\_SET.

-   If the miniport driver set the VP\_FLAGS\_TV\_STANDARD bit on a VP\_COMMAND\_GET, then the miniport driver should change the TV standard to the value specified by **dwTVStandard** when VP\_FLAGS\_TV\_STANDARD is set on a VP\_COMMAND\_SET.

-   If the miniport driver set the VP\_FLAGS\_CONTRAST bit on a VP\_COMMAND\_GET, then the miniport driver should set the contrast to the value specified by **dwContrast** when VP\_FLAGS\_CONTRAST is set on a VP\_COMMAND\_SET.

A VIDEOPARAMETERS field contains undefined data if the corresponding bit is not set in **dwFlags**.

 

 





