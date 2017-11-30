---
title: Example boilerplate for issuing a Regular OID request
description: This topic describes example boilerplate code for issuing a Regular OID request
ms.assetid: 0805FC9D-1161-4333-BCDF-BE2E6B996BD7
ms.author: windowsdriverdev
ms.date: 09/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Example boilerplate for issuing a Regular OID request

This topic provides example boilerplate code for issuing a Regular OID request, to contrast against the examples in [Synchronous OID Request Interface in NDIS 6.80](synchronous-oid-request-interface-in-ndis-6-80.md). The Synchronous OID Request Interface is available on Windows 10, version 1709 and later.

This example is taken from the sample filter driver available on GitHub: [https://github.com/Microsoft/Windows-driver-samples/tree/master/network/ndis/filter](https://go.microsoft.com/fwlink/p/?linkid=859443).

```cpp
Status = filterDoInternalRequest(pFilter,
                 NdisRequestQueryInformation,
                 OID_802_3_CURRENT_ADDRESS,
                 MacAddress,
                 sizeof(MacAddress),
                 0,
                 0,
                 &BytesProcessed);

_IRQL_requires_max_(DISPATCH_LEVEL)
NDIS_STATUS
filterDoInternalRequest(
  _In_ PMS_FILTER          FilterModuleContext,
  _In_ NDIS_REQUEST_TYPE      RequestType,
  _In_ NDIS_OID           Oid,
  _Inout_updates_bytes_to_(InformationBufferLength, *pBytesProcessed)
     PVOID            InformationBuffer,
  _In_ ULONG            InformationBufferLength,
  _In_opt_ ULONG          OutputBufferLength,
  _In_ ULONG            MethodId,
  _Out_ PULONG           pBytesProcessed
  )
{
  FILTER_REQUEST       FilterRequest;
  PNDIS_OID_REQUEST      NdisRequest = &FilterRequest.Request;
  NDIS_STATUS         Status;
  BOOLEAN           bFalse;

  bFalse = FALSE;
  *pBytesProcessed = 0;
  NdisZeroMemory(NdisRequest, sizeof(NDIS_OID_REQUEST));

  NdisInitializeEvent(&FilterRequest.ReqEvent);

  NdisRequest->Header.Type = NDIS_OBJECT_TYPE_OID_REQUEST;
  NdisRequest->Header.Revision = NDIS_OID_REQUEST_REVISION_1;
  NdisRequest->Header.Size = sizeof(NDIS_OID_REQUEST);
  NdisRequest->RequestType = RequestType;

  switch (RequestType)
  {
    case NdisRequestQueryInformation:
       NdisRequest->DATA.QUERY_INFORMATION.Oid = Oid;
       NdisRequest->DATA.QUERY_INFORMATION.InformationBuffer =
                  InformationBuffer;
       NdisRequest->DATA.QUERY_INFORMATION.InformationBufferLength =
                  InformationBufferLength;
      break;

    case NdisRequestSetInformation:
       NdisRequest->DATA.SET_INFORMATION.Oid = Oid;
       NdisRequest->DATA.SET_INFORMATION.InformationBuffer =
                  InformationBuffer;
       NdisRequest->DATA.SET_INFORMATION.InformationBufferLength =
                  InformationBufferLength;
      break;

    case NdisRequestMethod:
       NdisRequest->DATA.METHOD_INFORMATION.Oid = Oid;
       NdisRequest->DATA.METHOD_INFORMATION.MethodId = MethodId;
       NdisRequest->DATA.METHOD_INFORMATION.InformationBuffer =
                  InformationBuffer;
       NdisRequest->DATA.METHOD_INFORMATION.InputBufferLength =
                  InformationBufferLength;
       NdisRequest->DATA.METHOD_INFORMATION.OutputBufferLength = OutputBufferLength;
       break;



    default:
      FILTER_ASSERT(bFalse);
      break;
  }

  NdisRequest->RequestId = (PVOID)FILTER_REQUEST_ID;

  Status = NdisFOidRequest(FilterModuleContext->FilterHandle,
              NdisRequest);


  if (Status == NDIS_STATUS_PENDING)
  {
    NdisWaitEvent(&FilterRequest.ReqEvent, 0);
    Status = FilterRequest.Status;
  }

  if (Status == NDIS_STATUS_SUCCESS)
  {
    if (RequestType == NdisRequestSetInformation)
    {
      *pBytesProcessed = NdisRequest->DATA.SET_INFORMATION.BytesRead;
    }

    if (RequestType == NdisRequestQueryInformation)
    {
      *pBytesProcessed = NdisRequest->DATA.QUERY_INFORMATION.BytesWritten;
    }

    if (RequestType == NdisRequestMethod)
    {
      *pBytesProcessed = NdisRequest->DATA.METHOD_INFORMATION.BytesWritten;
    }

    //
    // The driver below should set the correct value to BytesWritten
    // or BytesRead. But now, we just truncate the value to InformationBufferLength
    //
    if (RequestType == NdisRequestMethod)
    {
      if (*pBytesProcessed > OutputBufferLength)
      {
        *pBytesProcessed = OutputBufferLength;
      }
    }
    else
    {

      if (*pBytesProcessed > InformationBufferLength)
      {
        *pBytesProcessed = InformationBufferLength;
      }
    }
  }

  return Status;
}

VOID
filterInternalRequestComplete(
  _In_ NDIS_HANDLE         FilterModuleContext,
  _In_ PNDIS_OID_REQUEST      NdisRequest,
  _In_ NDIS_STATUS         Status
  )
{
  PFILTER_REQUEST       FilterRequest;
  FilterRequest = CONTAINING_RECORD(NdisRequest, FILTER_REQUEST, Request);
  FilterRequest->Status = Status;
  NdisSetEvent(&FilterRequest->ReqEvent);
}

_Use_decl_annotations_
VOID
FilterOidRequestComplete(
  NDIS_HANDLE     FilterModuleContext,
  PNDIS_OID_REQUEST  Request,
  NDIS_STATUS     Status
  )
{
  PMS_FILTER             pFilter = (PMS_FILTER)FilterModuleContext;
  PNDIS_OID_REQUEST          OriginalRequest;
  PFILTER_REQUEST_CONTEXT       Context;

  Context = (PFILTER_REQUEST_CONTEXT)(&Request->SourceReserved[0]);
  OriginalRequest = (*Context);

  //
  // This is an internal request
  //
  if (OriginalRequest == NULL)
  {
    filterInternalRequestComplete(pFilter, Request, Status);
    return;
  }

  // . . . other code for handling completion of non-"internal" requests
}
```

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")