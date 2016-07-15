---
Description: Format Negotiation
MS-HAID: 'audio.format\_negotiation'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Format Negotiation
---

# Format Negotiation


After an application initiates audio processing, the graph builder configures the sAPOs into an audio graph and also initializes the sAPOs. The audio service then negotiates with the LFX sAPO to establish the format for the audio data at the input and output of the sAPO. This negotiation process is known as format negotiation.

All sAPOs that provide audio systems effects for Windows Vista must have certain interfaces and methods. The methods used by the sAPO and the audio engine to negotiate the data format are: the **IsInputFormatSupported** method of the **IAudioProcessingObject** interface and the **LockForProcess** and **UnlockForProcess** methods of the **IAudioProcessingObjectConfiguration** interface. For more information about these methods and interfaces, see the [Wrapping System-supplied sAPOs](wrapping-system-supplied-sapos.md) and the [Replacing System-supplied sAPOs](replacing-system-supplied-sapos.md) topics.

To initiate format negotiation, the audio service first sets the output of the LFX sAPO to the default float32-based format. The audio service then calls the **IAudioProcessingObject::IsInputFormatSupported** method of the LFX sAPO, suggests the default format, and monitors the HRESULT response of this method. If the LFX sAPO can support the suggested format, it returns S\_OK, together with a reference to the supported format. If the LFX sAPO cannot support the suggested format, it returns S\_FALSE together with a reference to a format that is the closest match to the suggested one. If the LFX sAPO cannot support the suggested format and does not have a close match, it returns APOERR\_FORMAT\_NOT\_SUPPORTED. The GFX sAPO works with the output format of the LFX sAPO. So the GFX sAPO is not involved in the format negotiation process.

After a data format is selected to process the audio data, the audio processing graph builder calls the **IAudioProcessingObjectConfiguration::LockForProcess** method of the sAPOs, causing the format selection to be finalized.

If the Windows Vista sAPO returns an error to the wrapping custom sAPO in response to a call to the **LockForProcess** method, the custom sAPO must handle the error the same way it handles an error from **CoCreateInstance** when an attempt to instantiate an sAPO fails. See the [Spkrfill sample](windows-vista-sapo-feature-reference.md) and refer to the Spkrfill.cpp file for details about how to overwrite the system-supplied LockForProcess method.

Because of the way that the audio service operates, the LFX and GFX sAPOs must be able to respond independently of each other to queries from the audio service regarding data formats.

**Important**   When you implement a custom sAPO that wraps a Windows Vista LFX sAPO, do not specify the APO\_FLAG\_FRAMESPERSECOND\_MUST\_MATCH flag in the registration properties of the custom sAPO. If you specify this flag, the Windows Vista LFX sAPO will be unable to perform speaker fill, headphone virtualization, or virtual surround. Additionally, your custom sAPO will not be able to down-mix any audio streams. For example, your custom sAPO will not be able to mix a 5.1 audio stream down to a two-channel stereo audio stream.

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Format%20Negotiation%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")


