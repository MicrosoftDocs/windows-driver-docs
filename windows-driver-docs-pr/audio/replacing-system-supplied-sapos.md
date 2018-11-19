---
title: Replacing System-supplied sAPOs
description: Replacing System-supplied sAPOs
ms.assetid: 9d87b28a-a79f-4e40-b999-e8f4901e3b3d
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Replacing System-supplied sAPOs


When you develop your sAPOs to replace the system-supplied ones, you must use the same names in the following list, for the interfaces and methods. Some of the interfaces have more methods in addition to the listed required methods. See the reference pages for those interfaces to determine if you want to implement all the methods or only the required ones.

To develop an sAPO to replace a system-supplied one, complete the following steps:

1.  Develop a DSP algorithm to produce the custom system effects.

2.  Develop a [COM component](https://go.microsoft.com/fwlink/p/?linkid=106012) that will host the DSP algorithm.

3.  Implement the following interfaces and methods for the COM component:
    -   [IAudioProcessingObject](https://msdn.microsoft.com/library/windows/hardware/ff536501). The required methods for this interface are: [**Initialize**](https://msdn.microsoft.com/library/windows/hardware/ff536510) and [**IsInputFormatSupported.**](https://msdn.microsoft.com/library/windows/hardware/ff536511)
    -   [IAudioProcessingObjectConfiguration](https://msdn.microsoft.com/library/windows/hardware/ff536502). The required methods for this interface are: [**LockForProcess**](https://msdn.microsoft.com/library/windows/hardware/ff536503) and [**UnlockForProcess**](https://msdn.microsoft.com/library/windows/hardware/ff536504)
    -   [IAudioProcessingObjectRT](https://msdn.microsoft.com/library/windows/hardware/ff536505). The required method for this interface is [**APOProcess**](https://msdn.microsoft.com/library/windows/hardware/ff536506) and it is the method that implements the DSP algorithm.
    -   [IAudioSystemEffects](https://msdn.microsoft.com/library/windows/hardware/ff536514). This interface makes the audio engine recognize a DLL as an sAPO.

4.  Package the COM component as a [DLL](https://go.microsoft.com/fwlink/p/?linkid=106014)

5.  [Provide an INF file](https://msdn.microsoft.com/library/windows/hardware/ff549520) to copy and register the DLL during installation of your audio driver.

6.  Implement a user interface to configure the custom sAPO. See the [Custom UI Design Information](custom-ui-design-information.md) topic for more details.

 

 




