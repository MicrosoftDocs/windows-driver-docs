---
title: Using a Callout for Deep Inspection of Stream Data
description: Using a Callout for Deep Inspection of Stream Data
ms.assetid: 433d2d9a-c95e-4315-8678-8614791cd529
keywords:
- classify callouts WDK Windows Filtering Platform , deep inspection
- deep inspection WDK Windows Filtering Platform
- stream data deep inspection WDK Windows Filtering Platform
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using a Callout for Deep Inspection of Stream Data


When a callout inspects stream data, its [classifyFn](https://msdn.microsoft.com/library/windows/hardware/ff544887) callout function can inspect any combination of the fixed data fields, the metadata fields, and the raw stream data that is passed to it, and any relevant data that has been stored in a context associated with the filter or the data flow.

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
  FWPS_STREAM_CALLOUT_IO_PACKET0 *ioPacket;
  FWPS_STREAM_BUFFER0 *dataStream;
  UINT32 bytesRequired;
  SIZE_T bytesToPermit;
  SIZE_T bytesToBlock;
  ...

  // Get a pointer to the stream callout I/O packet
 ioPacket = (FWPS_STREAM_CALLOUT_IO_PACKET0 *)layerData;

  // Get the data fields from inFixedValues
  ...

  // Get any metadata fields from inMetaValues
  ...

  // Get the pointer to the data stream
 dataStream = ioPacket->dataStream;

  // Get any filter context data from filter->context
  ...

  // Get any flow context data from flowContext
  ...

  // Inspect the various data sources to determine
  // the action to be taken on the data
  ...

  // If more stream data is required to make a determination...
 if (...) {

    // Let the filter engine know how many more bytes are needed
 ioPacket->streamAction = FWPS_STREAM_ACTION_NEED_MORE_DATA;
 ioPacket->countBytesRequired = bytesRequired;
 ioPacket->countBytesEnforced = 0;

    // Set the action to continue to the next filter
 classifyOut->actionType = FWP_ACTION_CONTINUE;

 return;
  }
  ...

  // If some or all of the data should be permitted...
 if (...) {

    // No stream-specific action is required
 ioPacket->streamAction = FWPS_STREAM_ACTION_NONE;

    // Let the filter engine know how many of the leading bytes
    // in the stream should be permitted
 ioPacket->countBytesRequired = 0;
 ioPacket->countBytesEnforced = bytesToPermit;

    // Set the action to permit the data
 classifyOut->actionType = FWP_ACTION_PERMIT;

 return;
  }

  ...

  // If some or all of the data should be blocked...
 if (...) {

    // No stream-specific action is required
 ioPacket->streamAction = FWPS_STREAM_ACTION_NONE;

    // Let the filter engine know how many of the leading bytes
    // in the stream should be blocked
 ioPacket->countBytesRequired = 0;
 ioPacket->countBytesEnforced = bytesToBlock;

    // Set the action to block the data
 classifyOut->actionType = FWP_ACTION_BLOCK;

 return;
  }

  ...

  // If the decision to permit or block should be passed
  // to the next filter in the filter engine...
 if (...) {

    // No stream-specific action is required
 ioPacket->streamAction = FWPS_STREAM_ACTION_NONE;

    // No bytes are affected by this callout
 ioPacket->countBytesRequired = 0;
 ioPacket->countBytesEnforced = 0;

 return;
  }

  ...
}
```

The value in *filter-&gt;action.type* determines which actions the callout's [classifyFn](https://msdn.microsoft.com/library/windows/hardware/ff544887) callout function should return in the **actionType** member of the structure pointed to by the *classifyOut* parameter. For more information about these actions, see the [**FWPS\_ACTION0**](https://msdn.microsoft.com/library/windows/hardware/ff551215) structure.

For more information about packet and stream data inspection, see [Inspecting Packet and Stream Data](inspecting-packet-and-stream-data.md).

 

 





