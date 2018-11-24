---
title: Using a Callout for Deep Inspection
description: Using a Callout for Deep Inspection
ms.assetid: 464c74ae-5e37-41f1-b305-ef57039b28ba
keywords:
- classify callouts WDK Windows Filtering Platform , deep inspection
- deep inspection WDK Windows Filtering Platform
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using a Callout for Deep Inspection


When a callout is performing deep inspection, its [classifyFn](https://msdn.microsoft.com/library/windows/hardware/ff544887) callout function can inspect any combination of the fixed data fields, the metadata fields, and any raw packet data that is passed to it, and any relevant data that has been stored in a context associated with the filter or the data flow.

For example:

```C++
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
  PNET_BUFFER_LIST rawData;
  ...

  // Test for the FWPS_RIGHT_ACTION_WRITE flag to check the rights
  // for this callout to return an action. If this flag is not set,
  // a callout can still return a BLOCK action in order to VETO a
  // PERMIT action that was returned by a previous filter. In this
  // example the function just exits if the flag is not set.
 if (!(classifyOut->rights & FWPS_RIGHT_ACTION_WRITE))
  {
    // Return without specifying an action
 return;
  }

  // Get the data fields from inFixedValues
  ...

  // Get any metadata fields from inMetaValues
  ...

  // Get the pointer to the raw data
 rawData = (PNET_BUFFER_LIST)layerData;

  // Get any filter context data from filter->context
  ...

  // Get any flow context data from flowContext
  ...

  // Inspect the various data sources to determine
  // the action to be taken on the data
  ...

  // If the data should be permitted...
 if (...) {

    // Set the action to permit the data
 classifyOut->actionType = FWP_ACTION_PERMIT;

    // Check whether the FWPS_RIGHT_ACTION_WRITE flag should be cleared
 if (filter->flags & FWPS_FILTER_FLAG_CLEAR_ACTION_RIGHT)
    {
       // Clear the FWPS_RIGHT_ACTION_WRITE flag
 classifyOut->rights &= ~FWPS_RIGHT_ACTION_WRITE;
    }

 return;
  }

  ...

  // If the data should be blocked...
 if (...) {

    // Set the action to block the data
 classifyOut->actionType = FWP_ACTION_BLOCK;

    // Clear the FWPS_RIGHT_ACTION_WRITE flag
 classifyOut->rights &= ~FWPS_RIGHT_ACTION_WRITE;

 return;
  }

  ...

  // If the decision to permit or block should be passed
  // to the next filter in the filter engine...
 if (...) {

    // Set the action to continue with the next filter
 classifyOut->actionType = FWP_ACTION_CONTINUE;

 return;
  }

  ...
}
```

The value in *filter-&gt;action.type* determines which actions the callout's [classifyFn](https://msdn.microsoft.com/library/windows/hardware/ff544887) callout function should return in the **actionType** member of the structure pointed to by the *classifyOut* parameter. For more information about these actions, see the [**FWPS\_ACTION0**](https://msdn.microsoft.com/library/windows/hardware/ff551215) structure.

If a callout must perform additional processing of packet data outside its [classifyFn](https://msdn.microsoft.com/library/windows/hardware/ff544887) callout function before it can determine whether the data should be permitted or blocked, it must pend the packet data until the processing of the data is completed. For information about how to pend packet data, see [Types of Callouts](types-of-callouts.md) and [**FwpsPendOperation0**](https://msdn.microsoft.com/library/windows/hardware/ff551199).

At some filtering layers, the *layerData* parameter that is passed by the filter engine to a callout's [classifyFn](https://msdn.microsoft.com/library/windows/hardware/ff544887) callout function is **NULL**.

For information about how to perform deep inspection of stream data, see [Using a Callout for Deep Inspection of Stream Data](using-a-callout-for-deep-inspection-of-stream-data.md).

 

 





