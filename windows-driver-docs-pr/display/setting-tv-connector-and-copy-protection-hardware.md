---
title: Setting TV Connector and Copy Protection Hardware
description: Setting TV Connector and Copy Protection Hardware
ms.assetid: 2de45c31-6a44-4a57-84b9-3cb21c905f4b
keywords:
- TV connector WDK video miniport
- copy protection WDK video miniport , setting
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Setting TV Connector and Copy Protection Hardware


## <span id="ddk_setting_tv_connector_and_copy_protection_hardware_gg"></span><span id="DDK_SETTING_TV_CONNECTOR_AND_COPY_PROTECTION_HARDWARE_GG"></span>


For any bit set by a miniport driver in the **dwFlags** member of [**VIDEOPARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff570173) on a VP\_COMMAND\_GET, the miniport driver can perform a set on a VP\_COMMAND\_SET. It is the caller's responsibility to call the miniport driver to set only that functionality for which the miniport driver indicated support on a VP\_COMMAND\_GET. The miniport driver should respond to a VP\_COMMAND\_SET by setting the hardware with the value of each VIDEOPARAMETERS field for which the corresponding bit is set in **dwFlags**. For example:

-   If the miniport driver set the VP\_FLAGS\_TV\_MODE bit on a VP\_COMMAND\_GET, then the miniport driver should change the TV mode to the value specified by **dwMode** when VP\_FLAGS\_TV\_MODE is set on a VP\_COMMAND\_SET.

-   If the miniport driver set the VP\_FLAGS\_TV\_STANDARD bit on a VP\_COMMAND\_GET, then the miniport driver should change the TV standard to the value specified by **dwTVStandard** when VP\_FLAGS\_TV\_STANDARD is set on a VP\_COMMAND\_SET.

-   If the miniport driver set the VP\_FLAGS\_CONTRAST bit on a VP\_COMMAND\_GET, then the miniport driver should set the contrast to the value specified by **dwContrast** when VP\_FLAGS\_CONTRAST is set on a VP\_COMMAND\_SET.

A VIDEOPARAMETERS field contains undefined data if the corresponding bit is not set in **dwFlags**.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Setting%20TV%20Connector%20and%20Copy%20Protection%20Hardware%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




