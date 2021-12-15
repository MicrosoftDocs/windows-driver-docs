---
title: Processing Flow Delete Callouts
description: Processing Flow Delete Callouts
keywords:
- Windows Filtering Platform callout drivers WDK , flow delete callouts
- callout drivers WDK Windows Filtering Platform , flow delete callouts
- flow delete callouts WDK Windows Filtering Platform
- flowDeleteFn
ms.date: 04/20/2017
---

# Processing Flow Delete Callouts


When a data flow that is being processed by a callout is stopped, the filter engine calls the callout's [*flowDeleteFn*](/windows-hardware/drivers/ddi/fwpsk/nc-fwpsk-fwps_callout_flow_delete_notify_fn0) callout function if the callout driver previously associated a context with the data flow. A callout's *flowDeleteFn* callout function performs any necessary clean up of the context that the callout driver associated with the data flow before the data flow is stopped.

For example:

```C++
// Context structure to be associated with data flows
typedef struct FLOW_CONTEXT_ {
  ...
} FLOW_CONTEXT, *PFLOW_CONTEXT;

#define FLOW_CONTEXT_POOL_TAG 'fcpt'

// flowDeleteFn callout function
VOID NTAPI
 FlowDeleteFn(
    IN UINT16  layerId,
    IN UINT32  calloutId,
    IN UINT64  flowContext
    )
{
  PFLOW_CONTEXT context;

  // Get the flow context structure
 context = (PFLOW_CONTEXT)flowContext;

  // Cleanup the flow context structure
  ...

  // Free the memory for the flow context structure
 ExFreePoolWithTag(
 context,
    FLOW_CONTEXT_POOL_TAG
    );
}
```

The filter engine automatically removes the context that a callout associated with a data flow when the data flow is stopped. Therefore, a callout is not required to call the [**FwpsFlowRemoveContext0**](/windows-hardware/drivers/ddi/fwpsk/nf-fwpsk-fwpsflowremovecontext0) function from its [*flowDeleteFn*](/windows-hardware/drivers/ddi/fwpsk/nc-fwpsk-fwps_callout_flow_delete_notify_fn0) callout function to remove the context from the data flow.

 

