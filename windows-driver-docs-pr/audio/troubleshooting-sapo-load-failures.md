---
title: Troubleshooting sAPO Load Failures
description: Troubleshooting sAPO Load Failures
ms.assetid: 245ff082-7cdc-4ecf-aee6-57fd7c418523
keywords:
- audio graph WDK
- sAPO WDK
- IsInputFormatSupported WDK
- LockForProcess WDK
- DisableProtectedAudioDG WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Troubleshooting sAPO Load Failures


The following information is provided to help you understand how failure is monitored for sAPOs. You can use this information to troubleshoot sAPOs that fail to get incorporated into the audio graph.

The audio system monitors sAPO return codes to determine whether sAPOs are being successfully incorporated into the graph. It monitors the return codes by tracking the HRESULT values that are returned by any one of the designated methods. The system maintains a separate failure count value for each LFX sAPO and the GFX sAPO that is being incorporated into the graph.

The audio system monitors the returned HRESULT values from the following four methods.

-   CoCreateInstance

-   IsInputFormatSupported

-   IsOutputFormatSupported

-   LockForProcess

The failure count value is incremented for an sAPO every time one of these methods returns a failure code. The failure count is reset to zero when an sAPO returns a code that indicates that it was successfully incorporated into the audio graph. A successful call to the [**LockForProcess**](https://msdn.microsoft.com/library/windows/hardware/ff536503) method is a good indication that the sAPO was successfully incorporated.

For [**CoCreateInstance**](https://msdn.microsoft.com/library/windows/desktop/ms686615) in particular, there are a number of reasons why the returned HRESULT code could indicate a failure. The three primary reasons are as follows:

-   The graph is running protected content, and the sAPO is not properly signed.

-   The sAPO is not registered.

-   The sAPO has been renamed or tampered with.

The audio engine does not load unsigned sAPOs into the audio processing graph. So while you are testing your sAPO, you must disable the protected process for Audiodg.exe. To disable the protected process, set the value of the **DisableProtectedAudioDG** registry key to '1'. The following registry excerpt shows this.

```text
...
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Audio
 "DisableProtectedAudioDG" = dword:00000001
...
```

Also, if the failure count value for an LFX or a GFX sAPO reaches a system-specified limit, both the LFX and the GFX sAPOs are disabled by setting the PKEY\_Endpoint\_Disable\_SysFx registry key to '1'. The system-specified limit is currently a value of 10.

 

 




