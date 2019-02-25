---
title: Data Logging
description: Data Logging
ms.assetid: 1e4f00e0-0fc6-459d-bbdd-02fbca5b9945
keywords:
- classify callouts WDK Windows Filtering Platform , data logging
- logging WDK Windows Filtering Platform
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Data Logging


To determine what data should be logged, a callout's [classifyFn](https://msdn.microsoft.com/library/windows/hardware/ff544887) callout function can inspect any combination of the data fields, the metadata fields, and any raw data that is passed to it, as well as any relevant data that has been stored in a context associated with the filter or the data flow.

For example, if a callout keeps track of how many incoming (inbound) IPv4 packets are discarded by a filter at the network layer, the callout is added to the filter engine at the FWPM\_LAYER\_INBOUND\_IPPACKET\_V4\_DISCARD layer. In this situation, the callout's [classifyFn](https://msdn.microsoft.com/library/windows/hardware/ff544887) callout function might resemble the following example:

```C++
ULONG TotalDiscardCount = 0;
ULONG FilterDiscardCount = 0;

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
  // Increment the total count of discarded packets
 InterlockedIncrement(&TotalDiscardCount);


  // Check whether a discard reason metadata field is present
 if (FWPS_IS_METADATA_FIELD_PRESENT(
 inMetaValues,
        FWPS_METADATA_FIELD_DISCARD_REASON))
  {
    // Check whether it is a general discard reason
 if (inMetaValues->discardMetadata.discardModule ==
        FWPS_DISCARD_MODULE_GENERAL)
    {
      // Check whether discarded by a filter
 if (inMetaValues->discardMetadata.discardReason ==
          FWPS_DISCARD_FIREWALL_POLICY)
      {
        // Increment the count of packets discarded by a filter
 InterlockedIncrement(&FilterDiscardCount);
      }
    }
  }

  // Take no action on the data
 classifyOut->actionType = FWP_ACTION_CONTINUE;
}
```

## Related topics


[classifyFn](https://msdn.microsoft.com/library/windows/hardware/ff544887)

 

 






