---
title: Using Bind or Connect Redirection
description: Using Bind or Connect Redirection
ms.assetid: 6b27a9ad-53e9-4e80-bf03-79665f8a82a0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using Bind or Connect Redirection


The connect/bind redirection feature of the Windows Filtering Platform (WFP) enables application layer enforcement (ALE) callout drivers to inspect and, if desired, redirect connections.

This feature is available in Windows 7 and later.

**Note**  The ClassifyFunctions\_ProxyCallouts.cpp module in the [WFP driver sample](http://go.microsoft.com/fwlink/p/?LinkId=618934) includes code that demonstrates connect/bind redirection.

 

A WFP connection redirection callout redirects an application's connection request so that the application connects to a proxy service instead of the original destination. The proxy service has two sockets: one for the redirected original connection and one for the new proxied outbound connection.

A WFP redirect record is a buffer of opaque data that WFP must set on an outbound proxy connection at the **FWPM\_LAYER\_ALE\_AUTH\_CONNECT\_REDIRECT\_V4** and **FWPM\_LAYER\_ALE\_AUTH\_CONNECT\_REDIRECT\_V6** layers, so that the redirected connection and the original connection are logically related.

Because bind redirection is possible, it is not necessary to support local address and port modifications in a connect redirection. Changing the local address and port as part of connect redirection is not supported.

### Layers Used for Redirection

Redirection can be performed by callout drivers at the following layers, which are called "redirect layers":

-   FWPM\_LAYER\_ALE\_BIND\_REDIRECT\_V4 (FWPS\_LAYER\_ALE\_BIND\_REDIRECT\_V4)

-   FWPM\_LAYER\_ALE\_BIND\_REDIRECT\_V6 (FWPS\_LAYER\_ALE\_BIND\_REDIRECT\_V6)

-   FWPM\_LAYER\_ALE\_CONNECT\_REDIRECT\_V4 (FWPS\_LAYER\_ALE\_CONNECT\_REDIRECT\_V4)

-   FWPM\_LAYER\_ALE\_CONNECT\_REDIRECT\_V6 (FWPS\_LAYER\_ALE\_CONNECT\_REDIRECT\_V6)

The layer at which redirection is performed determines the effect of the change. Changes at connect layers affect only the flow being connected. Changes at bind layers affect all connections that are using that socket.

The redirect layers are only available for Windows 7 and later versions of Windows. Callout drivers that support classification at these layers must register using [**FwpsCalloutRegister1**](https://msdn.microsoft.com/library/windows/hardware/ff551143) or higher, not the older [**FwpsCalloutRegister0**](https://msdn.microsoft.com/library/windows/hardware/ff551140) function.

> [!IMPORTANT]
> Redirection is not available for use with all types of network traffic. The types of packets that are supported for redirection are shown in the following list:
> - TCP
> - UDP
> - Raw UDPv4 without the header include option
> - Raw ICMP

### Performing Redirection

To redirect a connection, the callout driver must obtain a writable copy of the TCP 4-tuple information, make changes to it as needed, and apply the changes. A set of new functions are provided to obtain writable layer data and to apply it through the engine. Callout drivers have the option of making changes either inline in their [classifyFn](https://msdn.microsoft.com/library/windows/hardware/ff544887) functions, or asynchronously in another function.

Callout drivers that implement redirection must use [*classifyFn1*](https://msdn.microsoft.com/library/windows/hardware/ff544893) or later instead of [*classifyFn0*](https://msdn.microsoft.com/library/windows/hardware/ff544890) as their classification callout function. To use *classifyFn1* or later, the callout must be registered by calling [**FwpsCalloutRegister1**](https://msdn.microsoft.com/library/windows/hardware/ff551143) or later, not the older [**FwpsCalloutRegister0**](https://msdn.microsoft.com/library/windows/hardware/ff551140).

To perform redirection inline a callout driver must perform the following steps in its implementation of [classifyFn](https://msdn.microsoft.com/library/windows/hardware/ff544887):

1.  Call [**FwpsRedirectHandleCreate0**](https://msdn.microsoft.com/library/windows/hardware/hh439681) to obtain a handle that can be used to redirect TCP connections. This handle should be cached and used for all redirections. (This step is omitted for Windows 7 and earlier.)

2.  In Windows 8 and later, you must query the redirection state of the connection by using the [**FwpsQueryConnectionRedirectState0**](https://msdn.microsoft.com/library/windows/hardware/hh439677) function in your callout driver. This must be done to prevent infinite redirecting.

3.  Call [**FwpsAcquireClassifyHandle0**](https://msdn.microsoft.com/library/windows/hardware/ff550085) to obtain a handle that will be used for subsequent function calls.

4.  Call [**FwpsAcquireWritableLayerDataPointer0**](https://msdn.microsoft.com/library/windows/hardware/ff550087) to get the writable data structure for the layer in which [classifyFn](https://msdn.microsoft.com/library/windows/hardware/ff544887) was called. Cast the *writableLayerData* out parameter to the structure corresponding to the layer, either [**FWPS\_BIND\_REQUEST0**](https://msdn.microsoft.com/library/windows/hardware/ff551221) or [**FWPS\_CONNECT\_REQUEST0**](https://msdn.microsoft.com/library/windows/hardware/ff551231).

    Starting with Windows 8, if your callout driver is redirecting to a local service, you must call [**FwpsRedirectHandleCreate0**](https://msdn.microsoft.com/library/windows/hardware/hh439681) to fill in the **localRedirectHandle** member of the [**FWPS\_CONNECT\_REQUEST0**](https://msdn.microsoft.com/library/windows/hardware/ff551231) structure in order to make local proxying work.

5.  Make changes to the layer data as needed:

    1.  Save the original destination in the local redirect context as shown in the following example:

        ```C++
        FWPS_CONNECT_REQUEST* connectRequest = redirectContext->connectRequest;
        // Replace "..." with your own redirect context size
        connectRequest->localRedirectContextSize = ...;
        // Store original destination IP/Port information in the localRedirectContext member
        connectRequest->localRedirectContext =    ExAllocatePoolWithTag(…);
        ```

    2.  Modify the remote address as shown in the following example:

        ```C++
        // Ensure we don't need to worry about crossing any of the TCP/IP stack's zones
        if(INETADDR_ISANY((PSOCKADDR)&(connectRequest->localAddressAndPort)))
        {
           INETADDR_SETLOOPBACK((PSOCKADDR)&(connectRequest->remoteAddressAndPort));
        }
        else
        {
           INETADDR_SET_ADDRESS((PSOCKADDR)&(connectRequest->remoteAddressAndPort),
                                 INETADDR_ADDRESS((PSOCKADDR)&(connectRequest->localAddressAndPort)));
        }
        INETADDR_SET_PORT((PSOCKADDR)&connectRequest->remoteAddressAndPort,
                          RtlUshortByteSwap(params->proxyPort));
        ```

    3.  If your callout driver is redirecting to a local service, it should set the local proxy PID in the **localRedirectTargetPID** member of the [**FWPS\_CONNECT\_REQUEST0**](https://msdn.microsoft.com/library/windows/hardware/ff551231) structure.
    4.  If your callout driver is redirecting to a local service, it should set the redirect handle returned by FwpsRedirectHandleCreate0 in the **localRedirectHandle** member of the FWPS\_CONNECT\_REQUEST0 structure.

6.  Call [**FwpsApplyModifiedLayerData0**](https://msdn.microsoft.com/library/windows/hardware/ff551137) to apply the changes made to the data.

7.  In your proxy service (which could be in user mode or kernel mode), you should query redirect records and contexts as shown in the following example:

    ```C++
    BYTE* redirectRecords;
    BYTE redirectContext[CONTEXT_SIZE];
    listenSock = WSASocket(…);
    result = bind(listenSock, …);
    result = listen(listenSock, …);
    clientSock = WSAAccept(listenSock, …);
    // opaque data to be set on proxy connection
    result = WSAIoctl(clientSock,
                      SIO_QUERY_WFP_CONNECTION_REDIRECT_RECORDS,
                      redirectRecords, …);
    // callout allocated data, contains original destination information
    result = WSAIoctl(clientSock,
                      SIO_QUERY_WFP_CONNECTION_REDIRECT_CONTEXT,
                      redirectContext, …);
    // extract original destination IP and port from above context
    ```

8.  In your proxy service (which could be in user mode or kernel mode), you should set redirect records on the proxy connection socket as shown in the following example to create a new outbound socket:

    ```C++
    proxySock = WSASocket(…);
    result = WSAIoctl(
                 proxySock,
                 SIO_SET_WFP_CONNECTION_REDIRECT_RECORDS,
                 redirectRecords, …);
    ```

9.  Call [**FwpsReleaseClassifyHandle0**](https://msdn.microsoft.com/library/windows/hardware/ff551208) to release the classification handle obtained in step 2.

10. Call [**FwpsRedirectHandleDestroy0**](https://msdn.microsoft.com/library/windows/hardware/hh439684) to destroy the handle that was obtained in step 1.

To perform redirection asynchronously a callout driver must perform the following steps:

1.  Call [**FwpsRedirectHandleCreate0**](https://msdn.microsoft.com/library/windows/hardware/hh439681) to obtain a handle that can be used to redirect TCP connections. (This step is omitted for Windows 7 and earlier.)

2.  In Windows 8 and later, you must query the redirection state of the connection by using the [**FwpsQueryConnectionRedirectState0**](https://msdn.microsoft.com/library/windows/hardware/hh439677) function in your callout driver.

3.  Call [**FwpsAcquireClassifyHandle0**](https://msdn.microsoft.com/library/windows/hardware/ff550085) to obtain a handle that will be used for subsequent function calls. This step and steps 2 and 3 are performed in the callout driver's [classifyFn](https://msdn.microsoft.com/library/windows/hardware/ff544887) callout function.

4.  Call [**FwpsPendClassify0**](https://msdn.microsoft.com/library/windows/hardware/ff551197) to put the classification in a pending state as shown in the following example:

    ```C++
    FwpsPendClassify(
            redirectContext->classifyHandle,
            0,
            &redirectContext->classifyOut);
    classifyOut->actionType = FWP_ACTION_BLOCK;
    classifyOut->rights &= ~FWPS_RIGHT_ACTION_WRITE;
    ```

> [!NOTE]
> If you are targeting Windows 7, you must perform the following steps in a separate worker function. If you are targeting Windows 8 or later, you can perform all steps for asynchronous redirection from within the *classifyFn* and ignore Step 5.

5.  Send the classification handle and the writable layer data to another function for asynchronous processing. The remaining steps are performed in that function, not in the callout driver's implementation of [classifyFn](https://msdn.microsoft.com/library/windows/hardware/ff544887).

6.  Call [**FwpsAcquireWritableLayerDataPointer0**](https://msdn.microsoft.com/library/windows/hardware/ff550087) to get the writable data structure for the layer in which [classifyFn](https://msdn.microsoft.com/library/windows/hardware/ff544887) was called. Cast the *writableLayerData* out parameter to the structure corresponding to the layer, either [**FWPS\_BIND\_REQUEST0**](https://msdn.microsoft.com/library/windows/hardware/ff551221) or [**FWPS\_CONNECT\_REQUEST0**](https://msdn.microsoft.com/library/windows/hardware/ff551231).

    Starting with Windows 8, if your callout driver is redirecting locally, you must call [**FwpsRedirectHandleCreate0**](https://msdn.microsoft.com/library/windows/hardware/hh439681) to fill in the **localRedirectHandle** member of the [**FWPS\_CONNECT\_REQUEST0**](https://msdn.microsoft.com/library/windows/hardware/ff551231) structure in order to make proxying work.

7.  Store any callout-specific context information in a private context structure as shown in the following example:

    ```C++
    redirectContext->classifyHandle = classifyHandle;
    redirectContext->connectRequest = connectRequest;
    redirectContext->classifyOut = *classifyOut; // deep copy
    // store original destination IP, port
    ```

8.  Make changes to the layer data as needed.

9.  Call [**FwpsApplyModifiedLayerData0**](https://msdn.microsoft.com/library/windows/hardware/ff551137) to apply the changes made to the data. Set the **FWPS_CLASSIFY_FLAG_REAUTHORIZE_IF_MODIFIED_BY_OTHERS** flag if you wish to be re-authorized in the event that another callout modifies the data further.

10. Call [**FwpsCompleteClassify0**](https://msdn.microsoft.com/library/windows/hardware/ff551150) to complete the classify operation asynchronously as shown in the following example:

    ```C++
    FwpsCompleteClassify(
            redirectContext->classifyHandle,
            0,
            &redirectContext->classifyOut);
    classifyOut->actionType = FWP_ACTION_PERMIT;
    classifyOut->rights |= FWPS_RIGHT_ACTION_WRITE;
    ```

11. Call [**FwpsReleaseClassifyHandle0**](https://msdn.microsoft.com/library/windows/hardware/ff551208) to release the classification handle obtained in step 1.

### Handling Connect Redirection from Multiple Callouts

It is possible that more than one callout driver will initiate connect redirection for the same flow. Callouts that perform connect redirection should be aware of other requests and respond appropriately.

The **FWPS\_RIGHT\_ACTION\_WRITE** flag should be set whenever a callout pends a classification. Your callout should test for the **FWPS\_RIGHT\_ACTION\_WRITE** flag to check the rights for your callout to return an action. If this flag is not set, your callout can still return a **FWP\_ACTION\_BLOCK** action in order to veto a **FWP\_ACTION\_PERMIT** action that was returned by a previous callout.

In Windows 8 and later, your callout driver must query the redirection state of the connection (to see if your callout driver or another callout driver has modified it) by using the [**FwpsQueryConnectionRedirectState0**](https://msdn.microsoft.com/library/windows/hardware/hh439677) function. If the connection is redirected by your callout driver, or if it was previously redirected by your callout driver, the callout driver should do nothing. Otherwise, it should also check for local redirection as shown in the following example:

```C++
FwpsAcquireWritableLayerDataPointer(...,(PVOID*)&connectRequest), ...);
if(connectRequest->previousVersion->modifierFilterId != filterId)
{
    if(connectRequest->previousVersion->localRedirectHandle)
    {
        classifyOut->actionType = FWP_ACTION_PERMIT;
        classifyOut->rights &= FWPS_RIGHT_ACTION_WRITE;
        FwpsApplyModifiedLayerData(
                classifyHandle,
                (PVOID)connectRequest,
                FWPS_CLASSIFY_FLAG_REAUTHORIZE_IF_MODIFIED_BY_OTHERS);
    }
}
```

If the connection is to a local proxy, your callout driver should not attempt to redirect it.

Callout drivers that use connect redirection should register at the ALE authorization connect layer (**FWPS\_LAYER\_ALE\_AUTH\_CONNECT\_V4** or **FWPS\_LAYER\_ALE\_AUTH\_CONNECT\_V6**) and check the following two metadata values for indications where the **FWP\_CONDITION\_FLAG\_IS\_CONNECTION\_REDIRECTED** flag is set:

-   **FWPS\_METADATA\_FIELD\_LOCAL\_REDIRECT\_TARGET\_PID** contains the process identifier for the process that is responsible for the redirected flow.

-   **FWPS\_METADATA\_FIELD\_ORIGINAL\_DESTINATION** contains the address of the original destination for the flow.

The [**FWPS\_CONNECT\_REQUEST0**](https://msdn.microsoft.com/library/windows/hardware/ff551231) structure contains a member called **localRedirectTargetPID**. For any loopback connect redirection to be valid, this field must be populated with the PID of the process that will be responsible for the redirected flow. This is the same data that the engine passes at the ALE authorization connect layers as **FWPS\_METADATA\_FIELD\_LOCAL\_REDIRECT\_TARGET\_ID**.

Starting with Windows 8, the proxy service needs to issue the [**SIO\_QUERY\_WFP\_CONNECTION\_REDIRECT\_RECORDS**](https://msdn.microsoft.com/library/windows/hardware/hh802473) and [**SIO\_QUERY\_WFP\_CONNECTION\_REDIRECT\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/hh802472) IOCTLs, using [**WSAIoctl**](https://msdn.microsoft.com/library/windows/desktop/ms741621), against the original endpoint of the proxy service. Additionally, the [**SIO\_SET\_WFP\_CONNECTION\_REDIRECT\_RECORDS**](https://msdn.microsoft.com/library/windows/hardware/hh802474) IOCTL must be issued, using **WSAIoctl**, on the new (proxied) socket.

## Related topics


[WFP Version-Independent Names and Targeting Specific Versions of Windows](https://msdn.microsoft.com/library/windows/desktop/gg176678)

 

 






