---
title: Low Latency Audio
description: This article discusses audio latency changes in Windows 10. It covers API options for application developers and changes in drivers that can be made to support low latency audio.
ms.date: 10/28/2022
---

# Low Latency Audio

This article discusses audio latency changes in Windows 10. It covers API options for application developers and changes in drivers that can be made to support low latency audio. Audio latency is the delay between that time that sound is created and when it's heard. Having low audio latency is important for several key scenarios, such as:

- Pro audio
- Music creation
- Communications
- Virtual reality
- Games

The goals of this document are to:

1. Describe the sources of audio latency in Windows.
1. Explain the changes that reduce audio latency in the Windows 10 audio stack.
1. Provide a reference on how application developers and hardware manufacturers can take advantage of the new infrastructure, in order to develop applications and drivers with low audio latency.

This article covers:

1. The new **[AudioGraph](/uwp/api/Windows.Media.Audio.AudioGraph)** API for interactive and media creation scenarios.
1. Changes in WASAPI to support low latency.
1. Enhancements in the driver DDIs.

## Terminology

| Term | Description |
|---|---|
| Render latency | Delay between the time that an application submits a buffer of audio data to the render APIs, until the time that it's heard from the speakers. |
| Capture latency | Delay between the time that a sound is captured from the microphone, until the time it's sent to the capture APIs that are being used by the application. |
| Roundtrip latency | Delay between the time that a sound is captured from the microphone, processed by the application and submitted by the application for rendering to the speakers. It's roughly equal to render latency + capture latency. |
| Touch-to-app latency | Delay between the time that a user taps the screen until the time that the signal is sent to the application. |
| Touch-to-sound latency | Delay between the time that a user taps the screen, the event goes to the application and a sound is heard via the speakers. It's equal to render latency + touch-to-app latency. |

## Windows audio stack

The following diagram shows a simplified version of the Windows audio stack.

:::image type="content" source="images/low-latency-audio-stack-diagram-1.png" alt-text="Diagram showing the low latency audio stack with apps, audio engine driver, and hardware.":::

Here's a summary of the latencies in the render path:
audio processing objects

1. The application writes the data into a buffer
1. The audio engine reads the data from the buffer and processes it. It also loads audio effects in the form of audio processing objects (APOs). For more information about APOs, see [Windows audio processing objects](windows-audio-processing-objects.md).
1. The latency of the APOs varies based on the signal processing within the APOs.
1. Before Windows 10, the latency of the audio engine was equal to ~12 ms for applications that use floating point data and ~6 ms for applications that use integer data
1. In Windows 10 and later, the latency has been reduced to 1.3 ms for all applications

1. The audio engine writes the processed data to a buffer.
1. Before Windows 10, the buffer was always set to ~10 ms.
1. Starting with Windows 10, the buffer size is defined by the audio driver (more details on the buffer are described later in this article).

1. The Audio driver reads the data from the buffer and writes them to the hardware.
1. The hardware can also process the data again in the form of more audio effects.
1. The user hears audio from the speaker.

Here's a summary of latency in the capture path:

1. Audio is captured from the microphone.
1. The hardware can process the data. For example, to add audio effects.
1. The driver reads the data from the hardware and writes the data into a buffer.
1. Before Windows 10, this buffer was always set to 10 ms.
1. Starting with Windows 10, the buffer size is defined by the audio driver (more details below).

1. The audio engine reads the data from the buffer and processes them. It also loads audio effects in the form of audio processing objects (APOs).
1. The latency of the APOs varies based on the signal processing within the APOs.
1. Before Windows 10, the latency of the audio engine was equal to ~6 ms for applications that use floating point data and ~0ms for applications that use integer data.
1. In Windows 10 and later, the latency has been reduced to ~0ms for all applications.

1. The application is signaled that data is available to be read, as soon as the audio engine finishes with its processing.
    The audio stack also provides the option of exclusive mode. In that case, the data bypasses the audio engine and goes directly from the application to the buffer where the driver reads it from. However, if an application opens an endpoint in exclusive mode, then there's no other application that can use that endpoint to render or capture audio.

Another popular alternative for applications that need low latency is to use the ASIO (Audio Stream Input/Output) model, which utilizes exclusive mode. After a user installs a third-party ASIO driver, applications can send data directly from the application to the ASIO driver. However, the application has to be written in such a way that it talks directly to the ASIO driver.

Both alternatives (exclusive mode and ASIO) have their own limitations. They provide low latency, but they have their own limitations (some of which were described above). As a result, the audio engine has been modified, in order to lower the latency, while retaining the flexibility.

## Audio stack improvements

Windows 10 and later have been enhanced in three areas to reduce latency:

1. All applications that use audio will see a 4.5-16 ms reduction in round-trip latency (as was explained in the section above) without any code changes or driver updates, compared to Windows 8.1.
   1. Applications that use floating point data will have 16-ms lower latency.
   1. Applications that use integer data will have 4.5-ms lower latency.
1. Systems with updated drivers will provide even lower round-trip latency:
   1. Drivers can use new DDIs to report the supported sizes of the buffer that is used to transfer data between Windows and the hardware. Data transfers don't have to always use 10-ms buffers, as they did in previous Windows versions. Instead, the driver can specify if it can use small buffers, for example, 5 ms, 3 ms, 1 ms, etc.
   1. Applications that require low latency can use new audio APIs (AudioGraph or WASAPI), to query the buffer sizes that are supported by the driver and select the one that will be used for the data transfer to/from the hardware.
1. When an application uses buffer sizes below a certain threshold to render and capture audio, Windows enters a special mode, where it manages its resources in a way that avoids interference between the audio streaming and other subsystems. This will reduce the interruptions in the execution of the audio subsystem and minimize the probability of audio glitches. When the application stops streaming, Windows returns to its normal execution mode. The audio subsystem consists of the following resources:
   1. The audio engine thread that is processing low latency audio.
   1. All the threads and interrupts that have been registered by the driver (using the new DDIs that are described in the section about driver resource registration).
   1. Some or all of the audio threads from the applications that request small buffers, and from all applications that share the same audio device graph (for example, same signal processing mode) with any application that requested small buffers:
1. AudioGraph callbacks on the streaming path.
1. If the application uses WASAPI, then only the work items that were submitted to the [Real-Time Work Queue API](/windows/desktop/ProcThread/platform-work-queue-api) or **[MFCreateMFByteStreamOnStreamEx](/windows/win32/api/mfidl/nf-mfidl-mfcreatemfbytestreamonstreamex)** and were tagged as "Audio" or "ProAudio".

## API improvements

The following two Windows 10 APIs provide low latency capabilities:

- **[AudioGraph](/uwp/api/Windows.Media.Audio.AudioGraph)**
- [Windows Audio Session API (WASAPI)](/windows/desktop/CoreAudio/wasapi)

To determine which of the two APIs to use:

- Favor AudioGraph, wherever possible for new application development.
- Only use WASAPI, if:
  - You need more control than that provided by AudioGraph.
  - You need lower latency than that provided by AudioGraph.

The [measurement tools](#measurement-tools) section of this article, shows specific measurements from a Haswell system using the inbox HDAudio driver.

The following sections will explain the low latency capabilities in each API. As it was noted in the previous section, in order for the system to achieve the minimum latency, it needs to have updated drivers that support small buffer sizes.

### AudioGraph

AudioGraph is a new Universal Windows Platform API in Windows 10 and later that is aimed at realizing interactive and music creation scenarios with ease. AudioGraph is available in several programming languages (C++, C#, JavaScript) and has a simple and feature-rich programming model.

In order to target low latency scenarios, AudioGraph provides the **[AudioGraphSettings::QuantumSizeSelectionMode](/uwp/api/Windows.Media.Audio.AudioGraphSettings#Windows_Media_Audio_AudioGraphSettings_QuantumSizeSelectionMode)** property. This property can be any of the values shown in the table below:

| Value | Description |
|---|---|
| SystemDefault | Sets the buffer to the default buffer size (~10 ms) |
| LowestLatency | Sets the buffer to the minimum value that is supported by the driver |
| ClosestToDesired | Sets the buffer size to be either equal either to the value defined by the DesiredSamplesPerQuantum property or to a value that is as close to DesiredSamplesPerQuantum as is supported by the driver. |

The [AudioCreation sample](https://github.com/Microsoft/Windows-universal-samples/tree/master/Samples/AudioCreation) shows how to use AudioGraph for low latency. The following code snippet shows how to set the minimum buffer size:

```csharp
AudioGraphSettings settings = new AudioGraphSettings(AudioRenderCategory.Media);
settings.QuantumSizeSelectionMode = QuantumSizeSelectionMode.LowestLatency;
CreateAudioGraphResult result = await AudioGraph.CreateAsync(settings);
```

### Windows audio session API (WASAPI)

Starting in Windows 10, WASAPI has been enhanced to:

- Allow an application to discover the range of buffer sizes (that is, periodicity values) that are supported by the audio driver of a given audio device. This makes it possible for an application to choose between the default buffer size (10 ms) or a small buffer (less than 10 ms) when opening a stream in shared mode. If an application doesn't specify a buffer size, then it will use the default buffer size.
- Allow an application to discover the current format and periodicity of the audio engine. This allows applications to snap to the current settings of the audio engine.
- Allow an app to specify that it wishes to render/capture in the format it specifies without any resampling by the audio engine

The above features will be available on all Windows devices. However, certain devices with enough resources and updated drivers will provide a better user experience than others.

The above functionality is provided by a new interface, called **[IAudioClient3](/windows/win32/api/audioclient/nn-audioclient-iaudioclient3)**, which derives from **[IAudioClient2](/windows/win32/api/audioclient/nn-audioclient-iaudioclient2)**.

**[IAudioClient3](/windows/win32/api/audioclient/nn-audioclient-iaudioclient3)** defines the following 3 methods:

| Method | Description |
|---|---|
| GetCurrentSharedModeEnginePeriod | Returns the current format and periodicity of the audio engine |
| GetSharedModeEnginePeriod | Returns the range of periodicities supported by the engine for the specified stream format |
| InitializeSharedAudioStream | Initializes a shared stream with the specified periodicity |

The [WASAPIAudio sample](https://github.com/Microsoft/Windows-universal-samples/tree/master/Samples/WindowsAudioSession) shows how to use IAudioClient3 for low latency.

The following code snippet shows how a music creation app can operate in the lowest latency setting that is supported by the system.

```cpp
// 1. Activation

// Get a string representing the Default Audio (Render|Capture) Device
m_DeviceIdString = MediaDevice::GetDefaultAudio(Render|Capture)Id(
Windows::Media::Devices::AudioDeviceRole::Default );

// This call must be made on the main UI thread.  Async operation will call back to
// IActivateAudioInterfaceCompletionHandler::ActivateCompleted, which must be an agile // interface implementation
hr = ActivateAudioInterfaceAsync( m_DeviceIdString->Data(), __uuidof(IAudioClient3),
nullptr, this, &asyncOp );

// 2. Setting the audio client properties – note that low latency offload is not supported

AudioClientProperties audioProps = {0};
audioProps.cbSize = sizeof( AudioClientProperties );
audioProps.eCategory = AudioCategory_Media;

// if the device has System.Devices.AudioDevice.RawProcessingSupported set to true and you want to use raw mode
// audioProps.Options |= AUDCLNT_STREAMOPTIONS_RAW;
//
// if it is important to avoid resampling in the audio engine, set this flag
// audioProps.Options |= AUDCLNT_STREAMOPTIONS_MATCH_FORMAT;


hr = m_AudioClient->SetClientProperties( &audioProps ); if (FAILED(hr)) { ... }

// 3. Querying the legal periods

hr = m_AudioClient->GetMixFormat( &mixFormat ); if (FAILED(hr)) { ... }

hr = m_AudioClient->GetSharedModeEnginePeriod(wfx, &defaultPeriodInFrames, &fundamentalPeriodInFrames, &minPeriodInFrames, &maxPeriodInFrames); if (FAILED(hr)) { ... }

// legal periods are any multiple of fundamentalPeriodInFrames between
// minPeriodInFrames and maxPeriodInFrames, inclusive
// the Windows shared-mode engine uses defaultPeriodInFrames unless an audio client // has specifically requested otherwise

// 4. Initializing a low-latency client

hr = m_AudioClient->InitializeSharedAudioStream(
         AUDCLNT_STREAMFLAGS_EVENTCALLBACK,
         desiredPeriodInFrames,
         mixFormat,
         nullptr); // audio session GUID
         if (AUDCLNT_E_ENGINE_PERIODICITY_LOCKED == hr) {
         /* engine is already running at a different period; call m_AudioClient->GetSharedModeEnginePeriod to see what it is */
         } else if (FAILED(hr)) {
             ...
         }

// 5. Initializing a client with a specific format (if the format needs to be different than the default format)

AudioClientProperties audioProps = {0};
audioProps.cbSize = sizeof( AudioClientProperties );
audioProps.eCategory = AudioCategory_Media;
audioProps.Options |= AUDCLNT_STREAMOPTIONS_MATCH_FORMAT;

hr = m_AudioClient->SetClientProperties( &audioProps );
if (FAILED(hr)) { ... }

hr = m_AudioClient->IsFormatSupported(AUDCLNT_SHAREMODE_SHARED, appFormat, &closest);
if (S_OK == hr) {
       /* device supports the app format */
} else if (S_FALSE == hr) {
       /* device DOES NOT support the app format; closest supported format is in the "closest" output variable */
} else {
       /* device DOES NOT support the app format, and Windows could not find a close supported format */
}

hr = m_AudioClient->InitializeSharedAudioStream(
       AUDCLNT_STREAMFLAGS_EVENTCALLBACK,
       defaultPeriodInFrames,
       appFormat,
       nullptr); // audio session GUID
if (AUDCLNT_E_ENGINE_FORMAT_LOCKED == hr) {
       /* engine is already running at a different format */
} else if (FAILED(hr)) {
       ...
}
```

Also, Microsoft recommends for applications that use WASAPI to also use the [Real-Time Work Queue API](/windows/desktop/ProcThread/platform-work-queue-api) or the **[MFCreateMFByteStreamOnStreamEx](/windows/win32/api/mfidl/nf-mfidl-mfcreatemfbytestreamonstreamex)** to create work items and tag them as Audio or Pro Audio, instead of their own threads. This will allow Windows to manage them in a way that will avoid interference non-audio subsystems. In contrast, all AudioGraph threads are automatically managed correctly by Windows. The following code snippet from the WASAPIAudio sample shows how to use the MF Work Queue APIs.

```cpp
// Specify Source Reader Attributes
Attributes->SetUnknown( MF_SOURCE_READER_ASYNC_CALLBACK, static_cast<IMFSourceReaderCallback *>(this) );
    if (FAILED( hr ))
    {
        goto exit;
    }
    Attributes->SetString( MF_READWRITE_MMCSS_CLASS_AUDIO, L"Audio" );
    if (FAILED( hr ))
    {
        goto exit;
    }
    Attributes->SetUINT32( MF_READWRITE_MMCSS_PRIORITY_AUDIO, 0 );
    if (FAILED( hr ))
    {
        goto exit;
    }
    // Create a stream from IRandomAccessStream
    hr = MFCreateMFByteStreamOnStreamEx (reinterpret_cast<IUnknown*>(m_ContentStream), &ByteStream );
    if ( FAILED( hr ) )
    {
        goto exit;
    }
    // Create source reader
    hr = MFCreateSourceReaderFromByteStream( ByteStream, Attributes, &m_MFSourceReader );
```

Alternatively, the following code snippet shows how to use the RT Work Queue APIs.

```cpp
#define INVALID_WORK_QUEUE_ID 0xffffffff
DWORD g_WorkQueueId = INVALID_WORK_QUEUE_ID;
//#define MMCSS_AUDIO_CLASS    L"Audio"
//#define MMCSS_PROAUDIO_CLASS L"ProAudio"

STDMETHODIMP TestClass::GetParameters(DWORD* pdwFlags, DWORD* pdwQueue)
{
       HRESULT hr = S_OK;
       *pdwFlags = 0;
       *pdwQueue = g_WorkQueueId;
       return hr;
}

//-------------------------------------------------------
STDMETHODIMP TestClass::Invoke(IRtwqAsyncResult* pAsyncResult)
{
       HRESULT hr = S_OK;
       IUnknown *pState = NULL;
       WCHAR className[20];
       DWORD  bufferLength = 20;
       DWORD taskID = 0;
       LONG priority = 0;

       printf("Callback is invoked pAsyncResult(0x%0x)  Current process id :0x%0x Current thread id :0x%0x\n", (INT64)pAsyncResult, GetCurrentProcessId(), GetCurrentThreadId());

       hr = RtwqGetWorkQueueMMCSSClass(g_WorkQueueId, className, &bufferLength);
       IF_FAIL_EXIT(hr, Exit);

       if (className[0])
       {
              hr = RtwqGetWorkQueueMMCSSTaskId(g_WorkQueueId, &taskID);
              IF_FAIL_EXIT(hr, Exit);

              hr = RtwqGetWorkQueueMMCSSPriority(g_WorkQueueId, &priority);
              IF_FAIL_EXIT(hr, Exit);
              printf("MMCSS: [%ws] taskID (%d) priority(%d)\n", className, taskID, priority);
       }
       else
       {
              printf("non-MMCSS\n");
       }
       hr = pAsyncResult->GetState(&pState);
       IF_FAIL_EXIT(hr, Exit);

Exit:
       return S_OK;
}
//-------------------------------------------------------

int _tmain(int argc, _TCHAR* argv[])
{
       HRESULT hr = S_OK;
       HANDLE signalEvent;
       LONG Priority = 1;
       IRtwqAsyncResult *pAsyncResult = NULL;
       RTWQWORKITEM_KEY workItemKey = NULL;;
       IRtwqAsyncCallback *callback = NULL;
       IUnknown *appObject = NULL;
       IUnknown *appState = NULL;
       DWORD taskId = 0;
       TestClass cbClass;
       NTSTATUS status;

       hr = RtwqStartup();
       IF_FAIL_EXIT(hr, Exit);

       signalEvent = CreateEvent(NULL, true, FALSE, NULL);
       IF_TRUE_ACTION_EXIT(signalEvent == NULL, hr = E_OUTOFMEMORY, Exit);

       g_WorkQueueId = RTWQ_MULTITHREADED_WORKQUEUE;

       hr = RtwqLockSharedWorkQueue(L"Audio", 0, &taskId, &g_WorkQueueId);
       IF_FAIL_EXIT(hr, Exit);

       hr = RtwqCreateAsyncResult(NULL, reinterpret_cast<IRtwqAsyncCallback*>(&cbClass), NULL, &pAsyncResult);
       IF_FAIL_EXIT(hr, Exit);

       hr = RtwqPutWaitingWorkItem(signalEvent, Priority, pAsyncResult, &workItemKey);
       IF_FAIL_EXIT(hr, Exit);

       for (int i = 0; i < 5; i++)
       {
              SetEvent(signalEvent);
              Sleep(30);
              hr = RtwqPutWaitingWorkItem(signalEvent, Priority, pAsyncResult, &workItemKey);
              IF_FAIL_EXIT(hr, Exit);
    }

Exit:
       if (pAsyncResult)
       {
              pAsyncResult->Release();
       }

      if (INVALID_WORK_QUEUE_ID != g_WorkQueueId)
      {
        hr = RtwqUnlockWorkQueue(g_WorkQueueId);
        if (FAILED(hr))
        {
            printf("Failed with RtwqUnlockWorkQueue 0x%x\n", hr);
        }

        hr = RtwqShutdown();
        if (FAILED(hr))
        {
            printf("Failed with RtwqShutdown 0x%x\n", hr);
        }
      }

       if (FAILED(hr))
       {
          printf("Failed with error code 0x%x\n", hr);
       }
       return 0;
}
```

Finally, application developers that use WASAPI need to tag their streams with the audio category and whether to use the raw signal processing mode, based on the functionality of each stream. Microsoft recommends that all audio streams not use the raw signal processing mode, unless the implications are understood. Raw mode bypasses all the signal processing that has been chosen by the OEM, so:

- The render signal for a particular endpoint might be suboptimal.
- The capture signal might come in a format that the application can't understand.
- The latency might be improved.

## Driver improvements

In order for audio drivers to support low latency, Windows 10 and later provide the following features:

1. \[Mandatory\] Declare the minimum buffer size that is supported in each mode.
1. \[Optional, but recommended\] Improve the coordination for the data flow between the driver and Windows.
1. \[Optional, but recommended\] Register the driver resources (interrupts, threads), so that they can be protected by Windows in low latency scenarios.
HDAudio miniport function drivers that are enumerated by the inbox HDAudio bus driver hdaudbus.sys don't need to register the HDAudio interrupts, as this is already done by hdaudbus.sys. However, if the miniport driver creates its own threads, then it needs to register them.

The following three sections will explain each new feature in more depth.

### Declare the minimum buffer size

A driver operates under various constraints when moving audio data between Windows, the driver, and the hardware. These constraints may be due to the physical hardware transport that moves data between memory and hardware, or due to the signal processing modules within the hardware or associated DSP.

Beginning in Windows 10, version 1607, the driver can express its buffer size capabilities using the DEVPKEY_KsAudio_PacketSize_Constraints2 device property. This property allows the user to define the absolute minimum buffer size that is supported by the driver, and specific buffer size constraints for each signal processing mode. The mode-specific constraints need to be higher than the drivers minimum buffer size, otherwise they're ignored by the audio stack.

For example, the following code snippet shows how a driver can declare that the absolute minimum supported buffer size is 2 ms, but default mode supports 128 frames, which corresponds to 3 ms if we assume a 48-kHz sample rate.

```cpp
 
//
// Describe buffer size constraints for WaveRT buffers
//
static struct
{
    KSAUDIO_PACKETSIZE_CONSTRAINTS2 TransportPacketConstraints;
    KSAUDIO_PACKETSIZE_PROCESSINGMODE_CONSTRAINT AdditionalProcessingConstraints[1];
} SysvadWaveRtPacketSizeConstraintsRender =
{
    {
        2 * HNSTIME_PER_MILLISECOND,                // 2 ms minimum processing interval
        FILE_BYTE_ALIGNMENT,                        // 1 byte packet size alignment
        0,                                          // no maximum packet size constraint
        2,                                          // 2 processing constraints follow
        {
            STATIC_AUDIO_SIGNALPROCESSINGMODE_DEFAULT,          // constraint for default processing mode
            128,                                                // 128 samples per processing frame
            0,                                                  // NA hns per processing frame
        },
    },
    {
        {
            STATIC_AUDIO_SIGNALPROCESSINGMODE_MOVIE,            // constraint for movie processing mode
            1024,                                               // 1024 samples per processing frame
            0,                                                  // NA hns per processing frame
        },
    }
};
```

See the following articles for more in-depth information regarding these structures:

- **[KSAUDIO_PACKETSIZE_CONSTRAINTS structure](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ksaudio_packetsize_constraints)**
- **[KSAUDIO_PACKETSIZE_CONSTRAINTS2 structure](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ksaudio_packetsize_constraints2)**
- **[KSAUDIO_PACKETSIZE_PROCESSINGMODE_CONSTRAINT structure](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ksaudio_packetsize_signalprocessingmode_constraint)**

Also, the [sysvad sample](https://github.com/Microsoft/Windows-driver-samples/tree/main/audio/sysvad) shows how to use these properties, in order for a driver to declare the minimum buffer for each mode.

### Improve the coordination between driver and OS

The DDIs that are described in this section allow the driver to:

- Clearly indicate which half (packet) of the buffer is available to Windows, rather than the OS guessing based on a codec link position. This helps Windows to recover from audio glitches faster.
- Optionally optimize or simplify its data transfers in and out of the WaveRT buffer. The amount of benefit here depends on DMA engine design or other data transfer mechanism between the WaveRT buffer and (possibly DSP) hardware.
- "Burst" captured data faster than real-time if the driver has internally accumulated captured data. This is primarily intended for voice activation scenarios but can apply during normal streaming as well.
- Provide timestamp information about its current stream position rather than Windows guessing, potentially allowing for accurate position information.

This DDI is useful in the case, where a DSP is used. However, a standard HD Audio driver or other simple circular DMA buffer designs might not find much benefit in these new DDIs listed here.

- [IMiniportWaveRTInputStream](/windows-hardware/drivers/ddi/portcls/nn-portcls-iminiportwavertinputstream)
- [IMiniportWaveRTOutputStream](/windows-hardware/drivers/ddi/portcls/nn-portcls-iminiportwavertoutputstream)

Several of the driver routines return Windows performance counter timestamps reflecting the time at which samples are captured or presented by the device.

In devices that have complex DSP pipelines and signal processing, calculating an accurate timestamp may be challenging and should be done thoughtfully. The timestamps shouldn't reflect the time at which samples were transferred to or from Windows to the DSP.

To calculate the performance counter values, the driver and DSP might employ some of the following methods.

- Within the DSP, track sample timestamps using some internal DSP wall clock.
- Between the driver and DSP, calculate a correlation between the Windows performance counter and the DSP wall clock. Procedures for this can range from simple (but less precise) to fairly complex or novel (but more precise).
- Factor in any constant delays due to signal processing algorithms or pipeline or hardware transports, unless these delays are otherwise accounted for.

The [sysvad sample](https://github.com/Microsoft/Windows-driver-samples/tree/main/audio/sysvad) shows how to use the above DDIs.

### Register driver resources

To help ensure glitch-free operation, audio drivers must register their streaming resources with Portcls. This allows Windows to manage resources to avoid interference between audio streaming and other subsystems.

Stream resources are any resources used by the audio driver to process audio streams or ensure audio data flow. Only two types of stream resources are supported: interrupts and driver-owned threads. Audio drivers should register a resource after creating the resource, and unregister the resource before deleted it.

Audio drivers can register resources at initialization time when the driver is loaded, or at run-time, for example when there's an I/O resource rebalance. Portcls uses a global state to keep track of all the audio streaming resources.

In some use cases, such as those requiring very low latency audio, Windows attempts to isolate the audio driver's registered resources from interference from other OS, application, and hardware activity. The OS and audio subsystem do this as-needed without interacting with the audio driver, except for the audio driver's registration of the resources.

This requirement to register stream resources implies that all drivers that are in the streaming pipeline path must register their resources directly or indirectly with Portcls. The audio miniport driver has these options:

- The audio miniport driver is the bottom driver of its stack (interfacing the h/w directly), in this case, the driver knows its stream resources and it can register them with Portcls.
- The audio miniport driver is streaming audio with the help of other drivers (example audio bus drivers). These other drivers also use resources that must be registered with Portcls. These parallel/bus driver stacks can expose a public (or private interface, if a single vendor owns all the drivers) that audio miniport drivers use to collect this info.
- The audio miniport driver is streaming audio with the help of other drivers (example hdaudbus). These other drivers also use resources that must be registered with Portcls. These parallel/bus drivers can link with Portcls and directly register their resources. The audio miniport drivers must let Portcls know that they depend on the resources of these other parallel/bus devices (PDOs). The HD audio infrastructure uses this option, that is, the HD audio-bus driver links with Portcls and automatically performs the following steps:
  - registers its bus driver's resources, and
  - notifies Portcls that the children's resources depend on the parent's resources. In the HD audio architecture, the audio miniport driver just needs to register its own driver-owned thread resources.

Notes:

- HDAudio miniport function drivers that are enumerated by the inbox HDAudio bus driver hdaudbus.sys don't need to register the HDAudio interrupts, as this is already done by hdaudbus.sys. However, if the miniport driver creates its own threads, then it needs to register them.
- Drivers that link with Portcls only for registering streaming resources must update their INFs to include wdmaudio.inf and copy portcls.sys (and dependent files). A new INF copy section is defined in wdmaudio.inf to only copy those files.
- Audio drivers that only run in Windows 10 and later can hard-link to:
  - **[PcAddStreamResource](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcaddstreamresource)**
  - **[PcRemoveStreamResource](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcremovestreamresource)**
- Audio drivers that must run on a down-level OS can use the following interface (the miniport can call QueryInterface for the IID_IPortClsStreamResourceManager interface and register its resources only when PortCls supports the interface).
  - [IPortClsStreamResourceManager](/windows-hardware/drivers/ddi/portcls/nn-portcls-iportclsstreamresourcemanager)
        -   **[AddStreamResource](/windows-hardware/drivers/ddi/portcls/nf-portcls-iportclsstreamresourcemanager-addstreamresource)**
        -   **[RemoveStreamResource](/windows-hardware/drivers/ddi/portcls/nf-portcls-iportclsstreamresourcemanager-removestreamresource)**
- These DDIs, use this enumeration and structure:
  - **[PcStreamResourceType](/windows-hardware/drivers/ddi/portcls/ne-portcls-_pcstreamresourcetype)**
  - **[PCSTREAMRESOURCE_DESCRIPTOR](/windows-hardware/drivers/ddi/portcls/ns-portcls-_pcstreamresource_descriptor)**

Finally, drivers that link-in PortCls for the sole purpose of registering resources must add the following two lines in their inf's DDInstall section. Audio miniport drivers don't need this because they already have include/needs in wdmaudio.inf.

```inf
[<install-section-name>]
Include=wdmaudio.inf
Needs=WDMPORTCLS.CopyFilesOnly
```

The above lines make sure that PortCls and its dependent files are installed.

## Measurement tools

In order to measure roundtrip latency, user can user utilize tools that play pulses via the speakers and capture them via the microphone. They measure the delay of the following path:

1. The application calls the render API (AudioGraph or WASAPI) to play the pulse
1. The audio is played via the speakers
1. The audio is captured from the microphone
1. The pulse is detected by the capture API (AudioGraph or WASAPI)
In order to measure the roundtrip latency for different buffer sizes, users need to install a driver that supports small buffers. The inbox HDAudio driver has been updated to support buffer sizes between 128 samples (2.66ms@48kHz) and 480 samples (10ms@48kHz). The following steps show how to install the inbox HDAudio driver (which is part of all Windows 10 and later SKUs):

- Start Device Manager.
- Under **Sound video and game controllers**, double-click on the device that corresponds to your internal speakers.
- In the next window, go to the **Driver** tab.
- Select **Update driver** -> **Browse my computer for driver software** -> **Let me pick from a list of device drivers in this computer** -> **Select High Definition Audio Device** and select **Next**.
- If a window titled "Update driver warning" appears, select **Yes**.
- Select **close**.
- If you're asked to reboot the system, select **Yes** to reboot.
- After rebooting, the system will be using the inbox Microsoft HDAudio driver and not the third-party codec driver. Remember which driver you were using before so that you can fall back to that driver if you want to use the optimal settings for your audio codec.

:::image type="content" source="images/low-latency-audio-roundtrip-latency.png" alt-text="Graph illustrating roundtrip latency differences between WASAPI and AudioGraph for various buffer sizes.":::

The differences in the latency between WASAPI and AudioGraph are due to the following reasons:

- AudioGraph adds one buffer of latency in the capture side, in order to synchronize render and capture, which isn't provided by WASAPI. This addition simplifies the code for applications written using AudioGraph.
- There's another buffer of latency in AudioGraph's render side when the system is using greater than 6-ms buffers.
- AudioGraph doesn't have the option to disable capture audio effects.

## Samples

- [WASAPI audio sample](https://github.com/Microsoft/Windows-universal-samples/tree/master/Samples/WindowsAudioSession)
- [AudioCreation sample (AudioGraph)](https://github.com/Microsoft/Windows-universal-samples/tree/master/Samples/AudioCreation)
- [Sysvad driver sample](https://github.com/Microsoft/Windows-driver-samples/tree/main/audio/sysvad)

## FAQ

**Wouldn't it be better, if all applications use the new APIs for low latency? Doesn't low latency always guarantee a better user experience?**

Not necessarily. Low latency has its tradeoffs:

- Low latency means higher power consumption. If the system uses 10-ms buffers, it means that the CPU will wake up every 10 ms, fill the data buffer and go to sleep. However, if the system uses 1-ms buffers, it means that the CPU will wake up every 1 ms. In the second scenario, this means that the CPU will wake up more often and the power consumption will increase. This will decrease battery life.
- Most applications rely on audio effects to provide the best user experience. For example, media players want to provide high-fidelity audio. Communication applications want to minimum echo and noise. Adding these types of audio effects to a stream increases its latency. These applications are more interested in audio quality than in audio latency.

In summary, each application type has different needs regarding audio latency. If an application doesn't need low latency, then it shouldn't use the new APIs for low latency.

**Will all systems that update to Windows 10 and later be automatically update to support small buffers? Will all systems support the same minimum buffer size?**

No, in order for a system to support small buffers it needs to have updated drivers. It's up to the OEMs to decide which systems will be updated to support small buffers. Also, newer systems are more likely to support smaller buffers than older systems. The latency in new systems will most likely be lower than older systems.

**If a driver supports small buffer sizes, will all applications in Windows 10 and later automatically use small buffers to render and capture audio?**

No, by default all applications in Windows 10 and later will use 10-ms buffers to render and capture audio. If an application needs to use small buffers, then it needs to use the new AudioGraph settings or the WASAPI IAudioClient3 interface, in order to do so. However, if one application requests the usage of small buffers, then the audio engine will start transferring audio using that particular buffer size. In that case, all applications that use the same endpoint and mode will automatically switch to that small buffer size. When the low latency application exits, the audio engine will switch to 10-ms buffers again.
