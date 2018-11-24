---
title: Wrapping System-supplied sAPOs
description: Wrapping System-supplied sAPOs
ms.assetid: fcde6de0-921c-4c73-8e4d-941a447d35af
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Wrapping System-supplied sAPOs


## <span id="Implementing_your_own_sAPO"></span><span id="implementing_your_own_sapo"></span><span id="IMPLEMENTING_YOUR_OWN_SAPO"></span>Implementing your own sAPO


You can wrap a system-supplied sAPO by basing your custom class on the **CBaseAudioProcessingObject** base class, which is declared in the Baseaudioprocessingobject.h file. This approach involves introducing new functionality into the **CBaseAudioProcessingObject** base class to create a customized sAPO. The **CBaseAudioProcessingObject** base class implements much of the functionality that an sAPO requires. It provides default implementations for most of the methods in the three required interfaces. The primary exception is the [**IAudioProcessingObjectRT::APOProcess**](https://msdn.microsoft.com/library/windows/hardware/ff536506) method.

By using **CBaseAudioProcessingObject**, you can more easily implement an sAPO. If an sAPO has no special format requirements and operates on the default float32 format, the default implementations of the interface methods that are included in **CBaseAudioProcessingObject** should be sufficient. Given the default implementations, only three main methods must be implemented: [**IAudioProcessingObject::IsInputFormatSupported**](https://msdn.microsoft.com/library/windows/hardware/ff536511), [**IAudioProcessingObjectRT::APOProcess**](https://msdn.microsoft.com/library/windows/hardware/ff536506), and **ValidateAndCacheConnectionInfo**.

To develop your sAPOs based on the **CBaseAudioProcessingObject** class, perform the following steps:

1.  Create a class that inherits from **CBaseAudioProcessingObject**.

    The following C++ code example shows the creation of a class that inherits from **CBaseAudioProcessingObject**. For an actual implementation of this concept, follow instructions in the **Audio Processing Objects Driver Sample** section to go to the Swap sample, and then refer to the *Swapapo.h* file.

    ```cpp
    // Custom APO class - LFX
    Class MyCustomSAPOLFX: public CBaseAudioProcessingObject
    {
     public:
    //Code for class goes here
    ...
    };
    ```

    **Note**   Because the signal processing that is performed by an LFX sAPO is different from the signal processing that is performed by a GFX sAPO, you must create separate classes for your LFX and GFX sAPOs.

     

2.  Implement the following three methods:

    -   [**IAudioProcessingObject::IsInputFormatSupported**](https://msdn.microsoft.com/library/windows/hardware/ff536511). This method handles format negotiation with the audio engine.

    -   [**IAudioProcessingObjectRT::APOProcess**](https://msdn.microsoft.com/library/windows/hardware/ff536506). This method uses your custom algorithm to perform signal processing.

    -   **ValidateAndCacheConnectionInfo**. This method allocates memory to store format details, for example, channel count, sampling rate, sample depth, and channel mask.

The following C++ code example shows an implementation of the [**APOProcess**](https://msdn.microsoft.com/library/windows/hardware/ff536506) method for the sample class that you created in step 1. For an actual implementation of this concept, follow instructions in the **Audio Processing Objects Driver Sample** section to go to the Swap sample, and then refer to the *Swapapolfx.cpp* file.

```cpp
// Custom implementation of APOProcess method
STDMETHODIMP_ (Void) MyCustomSAPOLFX::APOProcess (...)
{
// Code for method goes here. This code is the algorithm that actually
// processes the digital audio signal.
...
}
```

The following code example shows an implementation of the **ValidateAndCacheConnectionInfo** method. For an actual implementation of this method, follow instructions in the **Audio Processing Objects Driver Sample** section to go to the Swap sample, and then refer to the *Swapapogfx.cpp* file.

```cpp
// Custom implementation of the ValidateAndCacheConnectionInfo method.
HRESULT CSwapAPOGFX::ValidateAndCacheConnectionInfo( ... )
{
// Code for method goes here.
// The code should validate the input/output format pair.
...
}
```

**Note**  The remaining interfaces and methods that your class inherits from **CBaseAudioProcessingObject** are described in detail in the Audioenginebaseapo.idl file.

 

You must provide a user interface to configure the features that you added to the custom sAPO. For more information about this, see the [Implementing a UI for Configuring sAPOs](implementing-a-ui-for-configuring-sapos.md) topic.

## <span id="Audio_Processing_Objects_Driver_Sample"></span><span id="audio_processing_objects_driver_sample"></span><span id="AUDIO_PROCESSING_OBJECTS_DRIVER_SAMPLE"></span>Audio Processing Objects Driver Sample


The Swap sample is the sample that was developed to illustrate some features of audio processing objects. To access this sample and browse the code files, perform the following steps:

1. Follow this link: [Windows Driver Kit (WDK) 8.1 Samples](https://go.microsoft.com/fwlink/p/?LinkId=618052)
2. Download the samples and unzip them to a hard drive.
3. Locate this directory: *..\\Windows Driver Kit (WDK) 8.1 Samples\\Microsoft slate system virtual audio device driver sample\\C++\\SwapAPO*
4. Open the SwapAPO project in Visual Studio.
5. In the left navigation pane, expand the APO item.
6. Click the file that you would like to browse, to see its contents.
 

 




