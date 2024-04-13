---
title: Can I Preserve the Last-Error Code Before TraceMessage is Called
description: Can I preserve the last-error code before TraceMessage is called
ms.date: 04/20/2017
---

# Can I preserve the last-error code before TraceMessage is called?


By default, [TraceMessage](/windows/win32/api/evntrace/nf-evntrace-tracemessage) is called by using the WPP\_TRACE macro. In versions of Windows earlier than Windows Vista, the [last-error code](/windows/win32/debug/last-error-code) was overwritten by **TraceMessage**.

Starting with Windows Vista, you can preserve the last-error code by defining a custom WPP\_TRACE macro. You must define your version of this macro before you include the [trace message header (.tmh) file](trace-message-header-file.md) in the source file of your [trace provider](trace-provider.md), such as a kernel-mode driver or user-mode application..

The following examples show how you can preserve the last-error code before you call **TraceMessage**:

-   Make a wrapper to **TraceMessage** that is called from the WPP\_TRACE macro. You can then call [TraceMessageVa](/windows/win32/api/evntrace/nf-evntrace-tracemessageva), from the wrapper function.

    The following example shows how to write a wrapper to **TraceMessage**:

    ```
    #define WPP_TRACE WppTraceMessageWrapper
    DWORD
    WppTraceMessageWrapper(
        __in TRACEHANDLE LoggerHandle,
        __in ULONG MessageFlags,
        __in LPCGUID MessageGuid,
        __in USHORT Message Number,
        ...)
    {
        DWORD TraceError = ERROR_SUCCESS;
        DWORD LastError = ERROR_SUCCESS;
        va_list Args = NULL;
     
        LastError = GetLastError();
     
        va_start(Args, Message Number);
        TraceError = TraceMessageVa(LoggerHandle, MessageFlags, MessageGuid, Message Number, Args);
        va_end(Args);
     
        SetLastError(LastError);
     return TraceError;
    }
    ```

-   Modify the WPP\_TRACE macro, as shown in the following example:
    ```
    #define WPP_TRACE(...)                              \
     do                                              \
        {                                               \
            DWORD LastError = GetLastError();           \
            TraceMessage(__VA_ARGS__);                  \
            SetLastError(LastError);                    \
        }                                               \
     while (FALSE, FALSE)
    ```

    **Note**   This method increases the code size of your binary files because the same code will be generated for each WPP\_SF function.

     

 

