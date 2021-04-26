---
title: Example boilerplate for issuing a Regular OID request
description: This topic describes example boilerplate code for issuing a Regular OID request
ms.date: 09/28/2017
ms.localizationpriority: medium
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

