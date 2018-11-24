---
title: Associating Context with a Data Flow
description: Associating Context with a Data Flow
ms.assetid: 75f5838e-626d-4a59-810e-fec9a40640ed
keywords:
- classify callouts WDK Windows Filtering Platform , context associated with data flow
- context WDK Windows Filtering Platform
- flowContext parameter WDK Windows Filtering Platform
- associating context with data flow WDK Windows Filtering Platform
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Associating Context with a Data Flow


For callouts that process data at a filtering layer that supports data flows, the callout driver can associate a context with each data flow. Such a context is opaque to the filter engine. The callout's [classifyFn](https://msdn.microsoft.com/library/windows/hardware/ff544887) callout function can use this context to save state information specific to the data flow for the next time that it is called by the filter engine for that data flow. The filter engine passes this context to the callout's classifyFn callout function through the *flowContext* parameter. If no context is associated with the data flow, the *flowContext* parameter is zero.

To associate a context with a data flow, a callout's [classifyFn](https://msdn.microsoft.com/library/windows/hardware/ff544887) callout function calls the [**FwpsFlowAssociateContext0**](https://msdn.microsoft.com/library/windows/hardware/ff551165) function. For example:

```C++
// Context structure to be associated with data flows
typedef struct FLOW_CONTEXT_ {
  .
  .  // Driver-specific content
  .
} FLOW_CONTEXT, *PFLOW_CONTEXT;

#define FLOW_CONTEXT_POOL_TAG &#39;fcpt&#39;

// classifyFn callout function
VOID NTAPI
 ClassifyFn(
    IN const FWPS_INCOMING_VALUES0  *inFixedValues,
    IN const FWPS_INCOMING_METADATA_VALUES0  *inMetaValues,
    IN OUT VOID  *layerData,
    IN const FWPS_FILTER0  *filter,
    IN UINT64  flowContext,
    IN OUT FWPS_CLASSIFY_OUT  *classifyOut
    )
{
  PFLOW_CONTEXT context;
  UINT64 flowHandle;
  NTSTATUS status;

  ...

  // Check for the flow handle in the metadata
 if (FWPS_IS_METADATA_FIELD_PRESENT(
 inMetaValues,
        FWPS_METADATA_FIELD_FLOW_HANDLE))
  {
    // Get the flow handle
 flowHandle = inMetaValues->flowHandle;

    // Allocate the flow context structure
 context =
      (PFLOW_CONTEXT)ExAllocatePoolWithTag(
 NonPagedPool,
 sizeof(FLOW_CONTEXT),
        FLOW_CONTEXT_POOL_TAG
        );

    // Check the result of the memory allocation
 if (context == NULL) {
 
      // Handle memory allocation error
      ...
    }
 else
    {

      // Initialize the flow context structure
      ...

      // Associate the flow context structure with the data flow
 status = FwpsFlowAssociateContext0(
 flowHandle,
        FWPS_LAYER_INBOUND_IPPACKET_V4,
 calloutId,
        (UINT64)context
        );

      // Check the result
 if (status != STATUS_SUCCESS)
      {
        // Handle error
        ...
      }
    }
  }

  ...

}
```

If a context is already associated with a data flow, it must first be removed before a new context may be associated with the data flow. To remove a context from a data flow, a callout's [classifyFn](https://msdn.microsoft.com/library/windows/hardware/ff544887) callout function calls the [**FwpsFlowRemoveContext0**](https://msdn.microsoft.com/library/windows/hardware/ff551169) function. For example:

```C++
// Context structure to be associated with data flows
typedef struct FLOW_CONTEXT_ {
  ...
} FLOW_CONTEXT, *PFLOW_CONTEXT;

#define FLOW_CONTEXT_POOL_TAG &#39;fcpt&#39;

// classifyFn callout function
VOID NTAPI
 ClassifyFn(
    IN const FWPS_INCOMING_VALUES0  *inFixedValues,
    IN const FWPS_INCOMING_METADATA_VALUES0  *inMetaValues,
    IN OUT VOID  *layerData,
    IN const FWPS_FILTER0  *filter,
    IN UINT64  flowContext,
    OUT FWPS_CLASSIFY_OUT  *classifyOut
    )
{
  PFLOW_CONTEXT context;
  UINT64 flowHandle;
  NTSTATUS status;

  ...

  // Check for the flow handle in the metadata
 if (FWPS_IS_METADATA_FIELD_PRESENT(
 inMetaValues,
        FWPS_METADATA_FIELD_FLOW_HANDLE))
  {
    // Get the flow handle
 flowHandle = inMetaValues->flowHandle;

    // Check whether there is a context associated with the data flow
 if (flowContext != 0) {

      // Get a pointer to the flow context structure
 context = (PFLOW_CONTEXT)flowContext;

      // Remove the flow context structure from the data flow
 status = FwpsFlowRemoveContext0(
 flowHandle,
        FWPS_LAYER_INBOUND_IPPACKET_V4,
 calloutId
        );

      // Check the result
 if (status != STATUS_SUCCESS)
      {
        // Handle error
        ...
      }

      // Cleanup the flow context structure
      ...

      // Free the memory for the flow context structure
 ExFreePoolWithTag(
 context,
        FLOW_CONTEXT_POOL_TAG
        );
    }
  }

  ...

}
```

In the previous examples, the *calloutId* variable contains the run-time identifier for the callout. The run-time identifier is the same identifier that was returned to the callout driver when the callout driver registered the callout with the filter engine.

 

 





