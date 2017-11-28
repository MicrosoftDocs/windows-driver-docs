---
title: Audio Miniport Auxiliary Interfaces
description: Audio Miniport Auxiliary Interfaces
ms.assetid: cda22e86-f3f7-430c-856d-a2c868caa975
---

# Audio Miniport Auxiliary Interfaces


## <span id="ddk_audio_miniport_auxiliary_interfaces_ks"></span><span id="DDK_AUDIO_MINIPORT_AUXILIARY_INTERFACES_KS"></span>


Some miniport drivers support auxiliary interfaces that are optional and provide access to specialized miniport driver capabilities. This section describes the auxiliary interfaces that are implemented by a miniport driver and exposed to the port driver.

The following interfaces are discussed in this section:

[IMusicTechnology](https://msdn.microsoft.com/library/windows/hardware/ff536778)- Used to change the DirectMusic synthesizer technology that is specified in the data ranges for the DMus miniport driver's pins.

[IPinCount](https://msdn.microsoft.com/library/windows/hardware/ff536832) - Provides a means for the miniport driver to dynamically monitor and manipulate its pin counts.

[IPinName](https://msdn.microsoft.com/library/windows/hardware/ff536840) - Allows the port driver to dynamically update the name of an endpoint.

[IAdapterPnpManagement](https://msdn.microsoft.com/library/windows/hardware/mt604850) - Allows adapters to register to receive PnP management messages.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Audio%20Miniport%20Auxiliary%20Interfaces%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




