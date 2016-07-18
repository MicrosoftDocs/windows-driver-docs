---
title: Replacing System-supplied sAPOs
description: Replacing System-supplied sAPOs
ms.assetid: 9d87b28a-a79f-4e40-b999-e8f4901e3b3d
---

# Replacing System-supplied sAPOs


When you develop your sAPOs to replace the system-supplied ones, you must use the same names in the following list, for the interfaces and methods. Some of the interfaces have more methods in addition to the listed required methods. See the reference pages for those interfaces to determine if you want to implement all the methods or only the required ones.

To develop an sAPO to replace a system-supplied one, complete the following steps:

1.  Develop a DSP algorithm to produce the custom system effects.

2.  Develop a [COM component](http://go.microsoft.com/fwlink/p/?linkid=106012) that will host the DSP algorithm.

3.  Implement the following interfaces and methods for the COM component:
    -   [IAudioProcessingObject](https://msdn.microsoft.com/library/windows/hardware/ff536501). The required methods for this interface are: [**Initialize**](https://msdn.microsoft.com/library/windows/hardware/ff536510) and [**IsInputFormatSupported.**](https://msdn.microsoft.com/library/windows/hardware/ff536511)
    -   [IAudioProcessingObjectConfiguration](https://msdn.microsoft.com/library/windows/hardware/ff536502). The required methods for this interface are: [**LockForProcess**](https://msdn.microsoft.com/library/windows/hardware/ff536503) and [**UnlockForProcess**](https://msdn.microsoft.com/library/windows/hardware/ff536504)
    -   [IAudioProcessingObjectRT](https://msdn.microsoft.com/library/windows/hardware/ff536505). The required method for this interface is [**APOProcess**](https://msdn.microsoft.com/library/windows/hardware/ff536506) and it is the method that implements the DSP algorithm.
    -   [IAudioSystemEffects](https://msdn.microsoft.com/library/windows/hardware/ff536514). This interface makes the audio engine recognize a DLL as an sAPO.

4.  Package the COM component as a [DLL](http://go.microsoft.com/fwlink/p/?linkid=106014)

5.  [Provide an INF file](https://msdn.microsoft.com/library/windows/hardware/ff549520) to copy and register the DLL during installation of your audio driver.

6.  Implement a user interface to configure the custom sAPO. See the [Custom UI Design Information](custom-ui-design-information.md) topic for more details.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Replacing%20System-supplied%20sAPOs%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




