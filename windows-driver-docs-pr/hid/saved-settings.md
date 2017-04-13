---
title: Saved Settings
author: windows-driver-content
description: Saved Settings
ms.assetid: fa3eb2c9-b0ae-4872-b0f4-13fdd3745265
keywords: ["saved registry settings WDK joysticks"]
---

# Saved Settings


## <a href="" id="ddk-saved-settings-di"></a>


When the current joystick settings are saved, the REGSTR\_VAL\_JOYNCONFIG saved under the REGSTR\_KEY\_JOYCURR key is also written under the REGSTR\_KEY\_JOYSETTINGS key in a subkey with the same name as that from which the OEM-defined settings are taken (non-OEM settings are saved in a subkey "predef" plus the type number). When a joystick is replaced, the saved settings remain so that if the joystick is restored, the saved settings are put back into the current settings. These registry values are used only by Control Panel.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20Saved%20Settings%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


