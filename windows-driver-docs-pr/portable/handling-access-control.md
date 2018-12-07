---
Description: Handling Access Control
title: Handling Access Control
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling Access Control


WPD drivers must verify that the WPD command payload was sent with the correct I/O Control Code (IOCTL) to ensure that the I/O manager performed the appropriate ACL check. Because every driver must perform this verification, WPD supplies macros to automate the process.

These macros are defined in the file *PortableDevice.h*. They are described in the following table.

| Macro                                            | Description                                                                                                                                  |
|--------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| BEGIN\_WPD\_COMMAND\_ACCESS\_MAP                 | Defines the beginning of the command-access table.                                                                                           |
| DECLARE\_VERIFY\_WPD\_COMMAND\_ACCESS            | Declares an instance of the function that is used to verify that a given WPD command is sent with the appropriate access flags in the IOCTL. |
| DECLARE\_WPD\_STANDARD\_COMMAND\_ACCESS\_ENTRIES | Declares entries for all the standard WPD commands that are contained in *PortableDevice.h*.                                                 |
| END\_WPD\_COMMAND\_ACCESS\_MAP                   | Defines the end of the command-access table.                                                                                                 |
| IS\_WPD\_IOCTL                                   | Determines whether a given IOCTL is specific to WPD.                                                                                         |
| VERIFY\_WPD\_COMMAND\_ACCESS                     | Compares a given IOCTL and its parameters against the command-access table that is defined in one of the driver modules.                     |
| WPD\_COMMAND\_ACCESS\_ENTRY                      | Adds a custom entry to the command-access table.                                                                                             |

 

In the sample driver, the access control verification is performed in the **CQueue::OnDeviceIoControl** and **CQueue::ProcessWpdMessage** methods. These methods are found in the *Queue.cpp* file. In addition, this file contains a command-access table that lists the WPD as well as any custom IOCTLs and their access levels.

```ManagedCPlusPlus
// Add table used to lookup the Access required for Wpd Commands
BEGIN_WPD_COMMAND_ACCESS_MAP(g_WpdCommandAccessMap)
    DECLARE_WPD_STANDARD_COMMAND_ACCESS_ENTRIES
    // Add any custom commands here e.g.
    // WPD_COMMAND_ACCESS_ENTRY(MyCustomCommand, WPD_COMMAND_ACCESS_READWRITE)
END_WPD_COMMAND_ACCESS_MAP

// This allows driver developers to use VERIFY_WPD_COMMAND_ACCESS to check command access function for us.
DECLARE_VERIFY_WPD_COMMAND_ACCESS;
```

The **OnDeviceIoControl** method uses the IS\_WPD\_IOCTL macro to identify WPD IOCTLs and then processes them by calling the **ProcessWpdMessage** method.

```ManagedCPlusPlus
STDMETHODIMP_ (void)
CQueue::OnDeviceIoControl(
        /* [in] */ IWDFIoQueue*     pQueue,
        /* [in] */ IWDFIoRequest*   pRequest,
        /* [in] */ ULONG            ControlCode,
        /* [in] */ SIZE_T           InputBufferSizeInBytes,
        /* [in] */ SIZE_T           OutputBufferSizeInBytes
        )
{
    HRESULT hr              = S_OK;
    DWORD   dwBytesWritten  = 0;

    if(IS_WPD_IOCTL(ControlCode))
    {
        BYTE*       pInputBuffer         = NULL;
        SIZE_T      cbInputBuffer        = 0;
        BYTE*       pOutputBuffer        = NULL;
        SIZE_T      cbOutputBuffer       = 0;
        ContextMap* pClientContextMap    = NULL;
        CComPtr<IWDFMemory> pMemoryIn;
        CComPtr<IWDFMemory> pMemoryOut;
        CComPtr<IWDFDevice> pDevice;
        CComPtr<IWDFFile>   pFileObject;

        //
        // Get input memory buffer, the memory object is always returned even if the
        // underlying buffer is NULL
        //
        pRequest->GetInputMemory(&pMemoryIn);
        pInputBuffer = (BYTE*) pMemoryIn->GetDataBuffer(&cbInputBuffer);

        //
        // Get output memory buffer, the memory object is always returned even if the
        // underlying buffer is NULL
        //
        pRequest->GetOutputMemory(&pMemoryOut);
        pOutputBuffer = (BYTE*) pMemoryOut->GetDataBuffer(&cbOutputBuffer);

        
        // Get the Context map for this client
        pRequest->GetFileObject(&pFileObject);
        if (pFileObject != NULL)
        {
            hr = pFileObject->RetrieveContext((void**)&pClientContextMap);
            CHECK_HR(hr, "Failed to get Contextmap from WDF File Object");
        }

        if (hr == S_OK)
        {
            // Get the device object
            pQueue->GetDevice(&pDevice );
            hr = ProcessWpdMessage(ControlCode,
                                   pClientContextMap,
                                   pDevice,
                                   pInputBuffer,
                                   (DWORD)cbInputBuffer,
                                   pOutputBuffer,
                                   (DWORD)cbOutputBuffer,
                                   &dwBytesWritten);
        }

   
    }
    else
    {
        hr = E_UNEXPECTED;
        CHECK_HR(hr, "Received invalid/unsupported IOCTL code &#39;0x%lx&#39;",ControlCode);
    }

    // Complete the request
    if (hr == S_OK)
    {
        pRequest->CompleteWithInformation(hr, dwBytesWritten);
    }
    else
    {
        pRequest->Complete(hr);
    }

    return;
}
```

The **ProcessWpdMessage** method uses the VERIFY\_WPD\_COMMAND\_ACCESS macro to check the IOCTL and command parameters against the command-access table that is defined in the beginning of *Queue.cpp*.

```ManagedCPlusPlus
HRESULT CQueue::ProcessWpdMessage(
    ULONG       ControlCode,
    ContextMap* pClientContextMap,
    IWDFDevice* pDevice,
    PVOID       pInBuffer,
    ULONG       ulInputBufferLength,
    PVOID       pOutBuffer,
    ULONG       ulOutputBufferLength,
    DWORD*      pdwBytesWritten)
{
    HRESULT                        hr = S_OK;
    CComPtr<IPortableDeviceValues> pParams;

    CComPtr<IPortableDeviceValues> pResults;

    CComPtr<WpdBaseDriver>         pWpdBaseDriver;

    if (hr == S_OK)
    {
        hr = m_pWpdSerializer->GetIPortableDeviceValuesFromBuffer((BYTE*)pInBuffer,
                                                                  ulInputBufferLength,
                                                                  &pParams);
        CHECK_HR(hr, "Failed to deserialize command parameters from input buffer");
    }

    // Verify that the command was sent with the appropriate access
    if (hr == S_OK)
    {
        hr = VERIFY_WPD_COMMAND_ACCESS(ControlCode, pParams, g_WpdCommandAccessMap);
        CHECK_HR(hr, "Wpd Command was sent with incorrect access flags");
    }

}
```

## <span id="related_topics"></span>Related topics


****
[The WPD Driver Samples](the-wpd-driver-samples.md)

 

 





