---
title: Supporting a Mixture of 2D and 3D Pins
description: Supporting a Mixture of 2D and 3D Pins
ms.assetid: 26d98eca-b70a-4244-a7c3-d3a19930a96a
keywords:
- hardware acceleration WDK DirectSound , 2D and 3D pin mixture
- 3D mixing WDK audio
- 2D mixing WDK audio
- pins WDK audio , 2D
- pins WDK audio , 3D
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Supporting a Mixture of 2D and 3D Pins


## <span id="supporting_a_mixture_of_2d_and_3d_pins"></span><span id="SUPPORTING_A_MIXTURE_OF_2D_AND_3D_PINS"></span>


If your WDM audio driver supports a mixture of 2D and 3D pins, a 3D pin can double for use as a 2D pin, but not vice versa. When DirectSound requires a 2D pin, it can substitute an unused 3D pin for that purpose, if one is available from the driver. If DirectSound requires a 3D pin, however, it continues to search the driver's list of pin instances until it finds a 3D pin, ignoring any 2D pins encountered during the search. DirectSound checks the driver's list of pin factories in the order in which they are listed until it finds a pin instance that satisfies its requirements.

When reporting the 2D-pin count, your driver should specify the number of 2D-pin instances plus the number of 3D-pin instances. When reporting the 3D-pin count, your driver should ignore the 2D pins and specify only the number of 3D-pin instances.

DirectSound versions that were distributed with Microsoft Windows 2000 and Windows 98 have a known problem in dealing with a pin factory that exposes a mixture of 2D and 3D pins: DirectSound incorrectly reports the 3D-pin count to be the number of 2D pin instances plus the number of 3D pin instances. A workaround solution to this problem is to write your driver so that it segregates the 2D and 3D pins into two separate pin factories. One factory exposes only the 2D pins, and the other factory exposes only the 3D pins.

With WDM drivers, DirectSound correctly reports the 2D-pin count as the sum of the counts of the 2D and 3D pins from the two factories, and it correctly reports the 3D-pin count as the number of 3D pins from the one 3D-pin factory. When exposing separate factories for 2D and 3D pins, your driver should list the 2D-pin factory before the 3D-pin factory. This is necessary because when DirectSound is looking for a 2D pin, it uses the first 2D or 3D pin that it finds, and DirectSound checks the pin factories in the order in which the driver lists them. If the driver lists the 3D factory first, it risks having DirectSound deplete the supply of 3D pins by unnecessarily using them in place of 2D pins.

In summary, if your driver exposes a mixture of 2D and 3D pins, it should follow these rules to run correctly on earlier versions of DirectSound:

-   Provide two separate pin factories for the 2D and 3D pins, respectively.

-   List the 2D-pin factory ahead of the 3D-pin factory.

These workarounds are unnecessary with later versions of DirectSound. The problem that is described above is fixed in Windows Me and in Windows XP and later. It is also fixed in DirectSound 8, which is redistributed for use with earlier Windows versions. With this fix, your driver can safely combine 2D and 3D pins in a single pin factory and DirectSound will correctly report the 2D- and 3D-pin counts. Also, when DirectSound requires a 2D pin, it uses a 3D pin in place of a 2D pin only when it has exhausted the supply of 2D pins from all pin factories.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Supporting%20a%20Mixture%20of%202D%20and%203D%20Pins%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


