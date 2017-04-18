---
title: Can I preserve the last-error code before TraceMessage is called
description: Can I preserve the last-error code before TraceMessage is called
ms.assetid: 57390fb1-5e01-4b98-960f-0201213d673c
---

# Can I preserve the last-error code before TraceMessage is called?


By default, [TraceMessage](http://go.microsoft.com/fwlink/p/?linkid=179214) is called by using the WPP\_TRACE macro. In versions of Windows earlier than Windows Vista, the [last-error code](http://go.microsoft.com/fwlink/p/?linkid=179346) was overwritten by **TraceMessage**.

Starting with Windows Vista, you can preserve the last-error code by defining a custom WPP\_TRACE macro. You must define your version of this macro before you include the [trace message header (.tmh) file](trace-message-header-file.md) in the source file of your [trace provider](trace-provider.md), such as a kernel-mode driver or user-mode application..

The following examples show how you can preserve the last-error code before you call **TraceMessage**:

-   Make a wrapper to **TraceMessage** that is called from the WPP\_TRACE macro. You can then call [TraceMessageVa](http://go.microsoft.com/fwlink/p/?linkid=179352), from the wrapper function.

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

     

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Can%20I%20preserve%20the%20last-error%20code%20before%20TraceMessage%20is%20called?%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




