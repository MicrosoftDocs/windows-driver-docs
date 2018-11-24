---
title: Packet Modification Examples
description: Packet Modification Examples
ms.assetid: dec76575-041b-4cbd-8042-184b15354f61
keywords:
- packet modification WDK Windows Filtering Platform
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Packet Modification Examples


The following example code shows how to modify and inspect packets with WFP.

### Inline packet Modification from Outgoing Transport Layers

```C++
HANDLE gInjectionHandle;

void 
NTAPI
InjectionCompletionFn(
   IN void* context,
   IN OUT NET_BUFFER_LIST* netBufferList,
   IN BOOLEAN dispatchLevel
   )
{
   FWPS_TRANSPORT_SEND_PARAMS0* tlSendArgs
     = (FWPS_TRANSPORT_SEND_PARAMS0*)context;

   //
   // TODO: Free tlSendArgs and embedded allocations.
   //

   //
   // TODO: Check netBufferList->Status for injection result
   //

 FwpsFreeCloneNetBufferList0(netBufferList, 0);
}

void 
NTAPI
WfpTransportSendClassify(
   IN const FWPS_INCOMING_VALUES0* inFixedValues,
   IN const FWPS_INCOMING_METADATA_VALUES0* inMetaValues,
   IN OUT void* layerData,
   IN const FWPS_FILTER0* filter,
   IN UINT64 flowContext,
   IN OUT FWPS_CLASSIFY_OUT0* classifyOut
   )
{
   NTSTATUS status;

   NET_BUFFER_LIST* netBufferList = (NET_BUFFER_LIST*)layerData;
   NET_BUFFER_LIST* clonedNetBufferList = NULL;
   FWPS_PACKET_INJECTION_STATE injectionState;
   FWPS_TRANSPORT_SEND_PARAMS0* tlSendArgs = NULL;
   ADDRESS_FAMILY af = AF_UNSPEC;

 injectionState = FwpsQueryPacketInjectionState0(
 gInjectionHandle,
 netBufferList,
                        NULL);
 if (injectionState == FWPS_PACKET_INJECTED_BY_SELF ||
 injectionState == FWPS_PACKET_PREVIOUSLY_INJECTED_BY_SELF)
   {
 classifyOut->actionType = FWP_ACTION_PERMIT;
 goto Exit;
   }

 if (!(classifyOut->rights & FWPS_RIGHT_ACTION_WRITE))
   {
      //
      // Cannot alter the action.
      //
 goto Exit;
   }

   //
   // TODO: Allocate and populate tlSendArgs by using information from
   // inFixedValues and inMetaValues.
   // Note: 1) Remote address and controlData (if not NULL) must
   // be deep-copied.
   //       2) IPv4 address must be converted to network order.
   //       3) Handle allocation errors.

 ASSERT(tlSendArgs != NULL);

 status = FwpsAllocateCloneNetBufferList0(
 netBufferList,
               NULL,
               NULL,
               0,
               &clonedNetBufferList);

 if (!NT_SUCCESS(status))
   {
 classifyOut->actionType = FWP_ACTION_BLOCK;
 classifyOut->rights &= ~FWPS_RIGHT_ACTION_WRITE;
 
 goto Exit;
   }

   // 
   // TODO: Perform modification to the cloned net buffer list here.
   //

   //
   // TODO: Set af based on inFixedValues->layerId.
   //
 ASSERT(af == AF_INET || af == AF_INET6);

   //
   // Note: For TCP traffic, FwpsInjectTransportReceiveAsync0 and
   // FwpsInjectTransportSendAsync0 must be queued and run by a DPC.
   //

 status = FwpsInjectTransportSendAsync0(
 gInjectionHandle,
               NULL,
 inMetaValues->transportEndpointHandle,
               0,
 tlSendArgs,
 af,
 inMetaValues->compartmentId,
 clonedNetBufferList,
 InjectionCompletionFn,
 tlSendArgs);

 if (!NT_SUCCESS(status))
   {
 classifyOut->actionType = FWP_ACTION_BLOCK;
 classifyOut->rights &= ~FWPS_RIGHT_ACTION_WRITE;

 goto Exit;
   }

 classifyOut->actionType = FWP_ACTION_BLOCK;
 classifyOut->rights &= ~FWPS_RIGHT_ACTION_WRITE;
 classifyOut->flags |= FWPS_CLASSIFY_OUT_FLAG_ABSORB;

   //
   // Ownership of clonedNetBufferList and tlSendArgs
   // now transferred to InjectionCompletionFn.
   //
 clonedNetBufferList = NULL;
 tlSendArgs = NULL;

Exit:

 if (clonedNetBufferList != NULL)
   {
 FwpsFreeCloneNetBufferList0(clonedNetBufferList, 0);
   }
 if (tlSendArgs != NULL)
   {
      //
      // TODO: Free tlSendArgs and embedded allocations.
      //
   }

 return;
}
```

### Out-of-band Packet Modification from Incoming Datagram Data Layers

```C++
typedef struct DD_RECV_CLASSIFY_INFO_ {
   NET_BUFFER_LIST* netBufferList;
   UINT32 nblOffset;
   UINT32 ipHeaderSize;
   UINT32 transportHeaderSize;
   ADDRESS_FAMILY af;
   COMPARTMENT_ID compartmentId;
   IF_INDEX interfaceIndex;
   IF_INDEX subInterfaceIndex;
}DD_RECV_CLASSIFY_INFO;

HANDLE gInjectionHandle;

void 
NTAPI
InjectionCompletionFn(
   IN void* context,
   IN OUT NET_BUFFER_LIST* netBufferList,
   IN BOOLEAN dispatchLevel
   )
{
   DD_RECV_CLASSIFY_INFO* classifyInfo
 = (DD_RECV_CLASSIFY_INFO*)context;

   //
   // TODO: Remove from queue and free classifyInfo.
   //

   //
   // TODO: Check netBufferList->Status for injection result.
   //

 FwpsFreeCloneNetBufferList0(netBufferList, 0);
}

void
DatagramDataReceiveWorker(
   DD_RECV_CLASSIFY_INFO* classifyInfo
   // ... and other parameters
   )
//
// To prevent WFP from making a deep clone (deep-copying MDLs, 
// net buffers, net buffer lists, structures, and data mapped by MDLs, 
// DatagramDataReceiveWorker should be run by a DPC targeting the 
// processor to which the referenced net buffer list was first 
// classified. See KeSetTargetProcessorDpc for DPC targeting.
//
{
   NTSTATUS status;
   NET_BUFFER_LIST* clonedNetBufferList;
   ULONG nblOffset = 
      NET_BUFFER_DATA_OFFSET(NET_BUFFER_LIST_FIRST_NB(classifyInfo->netBufferList));

   //
   // The TCP/IP stack could have retreated the net buffer list by the 
   // transportHeaderSize amount; detect the condition here to avoid
   // retreating two times.
   //
 if (nblOffset != classifyInfo->nblOffset)
   {
 ASSERT(classifyInfo->nblOffset - nblOffset == classifyInfo->transportHeaderSize);
 
 classifyInfo->transportHeaderSize = 0;
   }
 
   //
   // Adjust the net buffer list offset to start by using the IP header.
   //
 NdisRetreatNetBufferDataStart(
      NET_BUFFER_LIST_FIRST_NB(classifyInfo->netBufferList),
 classifyInfo->ipHeaderSize + classifyInfo->transportHeaderSize,
      0,
      NULL
      );

 status = FwpsAllocateCloneNetBufferList0(
 classifyInfo->netBufferList,
               NULL,
               NULL,
               0,
               &clonedNetBufferList);

 if (!NT_SUCCESS(status))
   {
      // TODO: Handle error condition.
 goto Exit;
   }

   //
   // Undo the adjustment on the original net buffer list.
   //

 NdisAdvanceNetBufferDataStart(
      NET_BUFFER_LIST_FIRST_NB(classifyInfo->netBufferList),
 classifyInfo->ipHeaderSize + classifyInfo->transportHeaderSize,
      FALSE,
      NULL);

   //
   // Because the clone references the original net buffer list, 
   // undo the reference that was claimed during classifyFn.
   //
 FwpsDereferenceNetBufferList0(
 classifyInfo->netBufferList,
      FALSE);
 classifyInfo->netBufferList = NULL;

   // 
   // TODO: Modify the cloned net buffer list here.
   // Note: 1) The next protocol field of the IP header could be 
   // AH/ESP, in which case the IP header must be rebuilt (and 
   // the AH/ESP header removed).
   //       2) The callout must re-calculate the IP checksum.
   //

 status = FwpsInjectTransportReceiveAsync0(
 gInjectionHandle,
               NULL,
               NULL,
 0,
 classifyInfo->af,
 classifyInfo->compartmentId,
 classifyInfo->interfaceIndex,
 classifyInfo->subInterfaceIndex,
 clonedNetBufferList,
 InjectionCompletionFn,
 classifyInfo);
 
 if (!NT_SUCCESS(status))
   {
      // TODO: Handle error condition.
 goto Exit;
   }

   //
   // Ownership of clonedNetBufferList and classifyInfo is 
   // now transferred to InjectionCompletionFn.
   //
 clonedNetBufferList = NULL;
 classifyInfo = NULL;

Exit:

 if (clonedNetBufferList != NULL)
   {
 FwpsFreeCloneNetBufferList0(clonedNetBufferList, 0);
   }
 if (classifyInfo->netBufferList != NULL)
   {
 FwpsDereferenceNetBufferList0(
 classifyInfo->netBufferList,
         FALSE);
   }

   // TODO: Free other resources on error.
}

void 
NTAPI
WfpDatagramDataReceiveClassify(
   IN const FWPS_INCOMING_VALUES0* inFixedValues,
   IN const FWPS_INCOMING_METADATA_VALUES0* inMetaValues,
   IN OUT void* layerData,
   IN const FWPS_FILTER0* filter,
   IN UINT64 flowContext,
   OUT FWPS_CLASSIFY_OUT0* classifyOut
   )
{
   NTSTATUS status;

   NET_BUFFER_LIST* netBufferList = (NET_BUFFER_LIST*)layerData;
   FWPS_PACKET_INJECTION_STATE injectionState;
   DD_RECV_CLASSIFY_INFO* classifyInfo = NULL;

 injectionState = FwpsQueryPacketInjectionState0(
 gInjectionHandle,
 netBufferList,
                        NULL);
 if (injectionState == FWPS_PACKET_INJECTED_BY_SELF ||
 injectionState == FWPS_PACKET_PREVIOUSLY_INJECTED_BY_SELF)
   {
 classifyOut->actionType = FWP_ACTION_PERMIT;
 goto Exit;
   }

 if (!(classifyOut->rights & FWPS_RIGHT_ACTION_WRITE))
   {
      //
      // Cannot alter the action.
      //
 goto Exit;
   }

   //
   // TODO: Allocate and populate classifyInfo by using information 
   // from inFixedValues and inMetaValues.
   //

 classifyInfo->nblOffset = 
      NET_BUFFER_DATA_OFFSET(NET_BUFFER_LIST_FIRST_NB(netBufferList));

 ASSERT(classifyInfo != NULL);
 ASSERT(classifyInfo->netBufferList != NULL);

 FwpsReferenceNetBufferList0(
 classifyInfo->netBufferList,
      TRUE // intendToModify
      );

   //
   // TODO: Queue classifyInfo for out-of-band processing.
   //

 classifyInfo = NULL; // Ownership transferred on success.

 classifyOut->actionType = FWP_ACTION_BLOCK;
 classifyOut->rights &= ~FWPS_RIGHT_ACTION_WRITE;
 classifyOut->flags |= FWPS_CLASSIFY_OUT_FLAG_ABSORB;

Exit:

 if (classifyInfo)
   {
      // TODO: Free object here.
   }

 return;
}
```

### <a href="" id="non-intrusive-out-of-band-inspection-from-incoming-transport-layer-and"></a>Non-intrusive Out-of-band Inspection from Incoming Transport Layer and ALE Receive/Accept Layers

The following is example code for an inspection procedure that views packet data without changing it.

```C++
typedef struct TL_ALE_RECV_CLASSIFY_INFO_ {
   BOOLEAN aleInfo;  // TRUE if information is gathered from Ale receive/accept layer
                     // FALSE if information is gathered from incoming transport layer

   NET_BUFFER_LIST* netBufferList;
   ADDRESS_FAMILY af;
   COMPARTMENT_ID compartmentId;
   IF_INDEX interfaceIndex;
   IF_INDEX subInterfaceIndex;

   HANDLE aleCompletionCtx;

}TL_ALE_RECV_CLASSIFY_INFO;

HANDLE gInjectionHandle;

void 
NTAPI
InjectionCompletionFn(
   IN void* context,
   IN OUT NET_BUFFER_LIST* netBufferList,
   IN BOOLEAN dispatchLevel
   )
{
   TL_ALE_RECV_CLASSIFY_INFO* classifyInfo = (TL_ALE_RECV_CLASSIFY_INFO*)context;

   //
   // TODO: Remove from queue and free classifyInfo.
   //

   //
   // TODO: Check netBufferList->Status for injection result.
   //

 FwpsFreeCloneNetBufferList0(netBufferList, 0);
}

void
TlAleReceiveWorker(
   TL_ALE_RECV_CLASSIFY_INFO* classifyInfo
   // ... and other parameters
   )
{
   NTSTATUS status;

 if (classifyInfo->aleInfo)
   {
 FwpsCompleteOperation0(
 classifyInfo->aleCompletionCtx,
 classifyInfo->netBufferList);
   }

 status = FwpsInjectTransportReceiveAsync0(
 gInjectionHandle,
               NULL,
               NULL,
               0,
 classifyInfo->af,
 classifyInfo->compartmentId,
 classifyInfo->interfaceIndex,
 classifyInfo->subInterfaceIndex,
 classifyInfo->netBufferList,
 InjectionCompletionFn,
 classifyInfo);
 
 if (!NT_SUCCESS(status))
   {
      // TODO: Handle error condition.
 goto Exit;
   }

   //
   // Ownership of classifyInfo now transferred to InjectionCompletionFn.
   //
 classifyInfo = NULL;

Exit:

 if (classifyInfo != NULL)
   {
 FwpsFreeCloneNetBufferList0(classifyInfo->netBufferList, 0);

      // TODO: Remove from queue and free classifyInfo.
   }

   // TODO: Free other resources on error.
}

void 
NTAPI
WfpAleReceiveClassify(
   IN const FWPS_INCOMING_VALUES0* inFixedValues,
   IN const FWPS_INCOMING_METADATA_VALUES0* inMetaValues,
   IN OUT void* layerData,
   IN const FWPS_FILTER0* filter,
   IN UINT64 flowContext,
   OUT FWPS_CLASSIFY_OUT0* classifyOut
   )
{
   NTSTATUS status;

   NET_BUFFER_LIST* netBufferList = (NET_BUFFER_LIST*)layerData;
   NET_BUFFER_LIST* clonedNetBufferList = NULL;   
   FWPS_PACKET_INJECTION_STATE injectionState;
 TL_ALE_RECV_CLASSIFY_INFO* classifyInfo = NULL;

 injectionState = FwpsQueryPacketInjectionState0(
 gInjectionHandle,
 netBufferList,
                        NULL);
 if (injectionState == FWPS_PACKET_INJECTED_BY_SELF ||
 injectionState == FWPS_PACKET_PREVIOUSLY_INJECTED_BY_SELF)
   {
 classifyOut->actionType = FWP_ACTION_PERMIT;
 goto Exit;
   }

 if (!(classifyOut->rights & FWPS_RIGHT_ACTION_WRITE))
   {
      //
      // Cannot alter the action.
      //
 goto Exit;
   }
   //
   // Adjust the net buffer list offset so that it starts with the IP header.
   //
 NdisRetreatNetBufferDataStart(
      NET_BUFFER_LIST_FIRST_NB(netBufferList),
 inMetaValues->ipHeaderSize + inMetaValues->transportHeaderSize,
      0,
      NULL
      );

 status = FwpsAllocateCloneNetBufferList0(
 netBufferList,
               NULL,
               NULL,
               0,
               &clonedNetBufferList);

 if (!NT_SUCCESS(status))
   {
 classifyOut->actionType = FWP_ACTION_BLOCK;
 classifyOut->rights &= ~FWPS_RIGHT_ACTION_WRITE;

 goto Exit;
   }

   //
   // Undo the adjustment on the original net buffer list.
   //

 NdisAdvanceNetBufferDataStart(
      NET_BUFFER_LIST_FIRST_NB(netBufferList),
 inMetaValues->ipHeaderSize + inMetaValues->transportHeaderSize,
      FALSE,
      NULL);

   //
   // Note: 1) The next protocol field of the IP header in the clone net 
   // buffer list could be AH/ESP, in which case the IP header must be 
   // rebuilt (and AH/ESP header removed).
   //       2) The callout must re-calculate the IP checksum.

   //
   // TODO: Allocate and populate classifyInfo by using information from 
   // inFixedValues and inMetaValues.
   //

 ASSERT(classifyInfo != NULL);
 
 classifyInfo->aleInfo = TRUE;

 classifyInfo->netBufferList = clonedNetBufferList;
 clonedNetBufferList = NULL; // Ownership transferred.

 status = FwpsPendOperation0(
 inMetaValues->completionHandle,
               &classifyInfo->aleCompletionCtx);

 if (!NT_SUCCESS(status))
   {
 classifyOut->actionType = FWP_ACTION_BLOCK;
 classifyOut->rights &= ~FWPS_RIGHT_ACTION_WRITE;

 goto Exit;
   }

   //
   // TODO: Queue classifyInfo for out-of-band processing.
   //

 classifyInfo = NULL; // Ownership transferred on success.

 classifyOut->actionType = FWP_ACTION_BLOCK;
 classifyOut->rights &= ~FWPS_RIGHT_ACTION_WRITE;
 classifyOut->flags |= FWPS_CLASSIFY_OUT_FLAG_ABSORB;

Exit:

 if (clonedNetBufferList != NULL)
   {
 FwpsFreeCloneNetBufferList0(clonedNetBufferList, 0);
   }
 if (classifyInfo)
   {
 if (classifyInfo->netBufferList)
      {
 FwpsFreeCloneNetBufferList0(classifyInfo->netBufferList, 0);
      }
      // TODO: Free object here.
   }

 return;
}

void 
NTAPI
WfpTransportReceiveClassify(
   IN const FWPS_INCOMING_VALUES0* inFixedValues,
   IN const FWPS_INCOMING_METADATA_VALUES0* inMetaValues,
   IN OUT void* layerData,
   IN const FWPS_FILTER0* filter,
   IN UINT64 flowContext,
   OUT FWPS_CLASSIFY_OUT0* classifyOut
   )
{
   NTSTATUS status;

   NET_BUFFER_LIST* netBufferList = (NET_BUFFER_LIST*)layerData;
   NET_BUFFER_LIST* clonedNetBufferList = NULL;   
   FWPS_PACKET_INJECTION_STATE injectionState;
 TL_ALE_RECV_CLASSIFY_INFO* classifyInfo = NULL;

 injectionState = FwpsQueryPacketInjectionState0(
 gInjectionHandle,
 netBufferList,
                        NULL);
 if (injectionState == <mark type="enumval">FWPS_PACKET_INJECTED_BY_SELF</mark> ||
 injectionState == FWPS_PACKET_PREVIOUSLY_INJECTED_BY_SELF)
   {
 classifyOut->actionType = FWP_ACTION_PERMIT;
 goto Exit;
   }

 if (!(classifyOut->rights & FWPS_RIGHT_ACTION_WRITE))
   {
      //
      // Cannot alter the action.
      //
 goto Exit;
   }

   //
   // Let go of the packet if it requires ALE classify; the packet can 
   // be inspected from the ALE receive/accept layer. Alternatively, 
   // the callout can use the combination of 
   // FWP_CONDITION_FLAG_REQUIRES_ALE_CLASSIFY and 
   // <mark type="enumval">FWP_MATCH_FLAGS_NONE_SET</mark> when you set up
   // filter conditions for the incoming transport layer.
   //
   // Beginning with Windows Vista SP1 and Windows Server 2008,
   // do not use FWP_CONDITION_FLAG_REQUIRES_ALE_CLASSIFY.
   // Use FWPS_IS_METADATA_FIELD_PRESENT macro to check for
   // metadata fields.
   //
#if (NTDDI_VERSION >= NTDDI_WIN6SP1)
 if (FWPS_IS_METADATA_FIELD_PRESENT(inMetaValues,
                                      FWPS_METADATA_FIELD_ALE_CLASSIFY_REQUIRED))
#else
 if ((inFixedValues->layerId == FWPS_LAYER_INBOUND_TRANSPORT_V4 &&
         (inFixedValues->incomingValue[FWPS_FIELD_INBOUND_TRANSPORT_V4_FLAGS].value.uint32 & 
          FWP_CONDITION_FLAG_REQUIRES_ALE_CLASSIFY)) ||
        (inFixedValues->layerId == FWPS_LAYER_INBOUND_TRANSPORT_V6 &&
         (inFixedValues->incomingValue[FWPS_FIELD_INBOUND_TRANSPORT_V6_FLAGS].value.uint32 & 
          FWP_CONDITION_FLAG_REQUIRES_ALE_CLASSIFY)))
#endif
   {
 classifyOut->actionType = FWP_ACTION_PERMIT;
 goto Exit;
   }
   //
   // Adjust the net buffer list offset so that it starts with the IP header.
   //
 NdisRetreatNetBufferDataStart(
      NET_BUFFER_LIST_FIRST_NB(netBufferList),
 inMetaValues->ipHeaderSize + inMetaValues->transportHeaderSize,
      0,
      NULL
      );

 status = FwpsAllocateCloneNetBufferList0(
 netBufferList,
               NULL,
               NULL,
               0,
               &clonedNetBufferList);

 if (!NT_SUCCESS(status))
   {
 classifyOut->actionType = FWP_ACTION_BLOCK;
 classifyOut->rights &= ~FWPS_RIGHT_ACTION_WRITE;

 goto Exit;
   }

   //
   // Undo the adjustment on the original net buffer list.
   //

 NdisAdvanceNetBufferDataStart(
      NET_BUFFER_LIST_FIRST_NB(netBufferList),
 inMetaValues->ipHeaderSize + inMetaValues->transportHeaderSize,
      FALSE,
      NULL);

   //
   // Notes: 1) The next protocol field of the IP header in the clone net 
   // buffer list could be AH/ESP, in which case the IP header must be 
   // rebuilt (and AH/ESP header removed).
   //        2) The callout must re-calculate the IP checksum.

   //
   // TODO: Allocate and populate classifyInfo by using information from 
   // inFixedValues and inMetaValues.
   //

 ASSERT(classifyInfo != NULL);
 
 classifyInfo->aleInfo = FALSE;

 classifyInfo->netBufferList = clonedNetBufferList;
 clonedNetBufferList = NULL; // ownership transferred

   //
   // TODO: Queue classifyInfo for out-of-band processing.
   //

 classifyInfo = NULL; // Ownership transferred on success.

 classifyOut->actionType = FWP_ACTION_BLOCK;
 classifyOut->rights &= ~FWPS_RIGHT_ACTION_WRITE;
 classifyOut->flags |= FWPS_CLASSIFY_OUT_FLAG_ABSORB;

Exit:

 if (clonedNetBufferList != NULL)
   {
 FwpsFreeCloneNetBufferList0(clonedNetBufferList, 0);
   }
 if (classifyInfo)
   {
 if (classifyInfo->netBufferList)
      {
 FwpsFreeCloneNetBufferList0(classifyInfo->netBufferList, 0);
      }
      // TODO: Free object here.
   }

 return;
}
```

## Related topics


[classifyFn](https://msdn.microsoft.com/library/windows/hardware/ff544887)

[Types of Callouts](types-of-callouts.md)

 

 






