---
title: Processing Notify Callouts
description: Processing Notify Callouts
ms.assetid: d686989e-97f0-4095-b172-1c2ccf7a26e6
keywords:
- Windows Filtering Platform callout drivers WDK , notify callouts
- callout drivers WDK Windows Filtering Platform , notify callouts
- notifyFn
- notify callouts WDK Windows Filtering Platform
- Windows Filtering Platform callout drivers WDK , filter additions and deletions
- callout drivers WDK Windows Filtering Platform , filter additions and deletions
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Processing Notify Callouts


The filter engine calls a callout's [*notifyFn*](https://msdn.microsoft.com/library/windows/hardware/ff568803) callout function to notify the callout driver about events that are associated with the callout.

### <a href="" id="filter-addition"></a> Filter Addition

When a filter that specifies a callout for the filter's action is added to the filter engine, the filter engine calls the callout's [*notifyFn*](https://msdn.microsoft.com/library/windows/hardware/ff568803) callout function, passing FWPS\_CALLOUT\_NOTIFY\_ADD\_FILTER in the *notifyType* parameter.

A callout driver can register a callout with the filter engine after filters that specify the callout for the filter's action have already been added to the filter engine. In this situation, the filter engine does not call the callout's [*notifyFn*](https://msdn.microsoft.com/library/windows/hardware/ff568803) callout function to notify the callout about any of the existing filters.

The filter engine only calls the callout's *notifyFn* callout function to notify the callout when new filters that specify the callout for the filter's action are added to the filter engine. In this situation, a callout's *notifyFn* callout function might not get called for every filter in the filter engine that specifies the callout for the filter's action.

If a callout driver registers a callout after the filter engine is started and the callout must receive information about every filter in the filter engine that specifies the callout for the filter's action, the callout driver must call the appropriate management functions to enumerate all the filters in the filter engine. The callout driver must sort through the resulting list of all the filters to find those filters that specify the callout for the filter's action. See [Calling Other Windows Filtering Platform Functions](calling-other-windows-filtering-platform-functions.md) for more information about calling these functions.

### <a href="" id="filter-deletion"></a> Filter Deletion

When a filter that specifies a callout for the filter's action is deleted from the filter engine, the filter engine calls the callout's [*notifyFn*](https://msdn.microsoft.com/library/windows/hardware/ff568803) callout function and passes FWPS\_CALLOUT\_NOTIFY\_DELETE\_FILTER in the *notifyType* parameter and **NULL** in the *filterKey* parameter. The filter engine calls the callout's *notifyFn* callout function for every deleted filter in the filter engine that specifies the callout for the filter's action. This includes any filters that were added to the filter engine before the callout driver registered the callout with the filter engine. Therefore, a callout might receive filter delete notifications for filters for which it did not receive filter add notifications.

If the callout's [*notifyFn*](https://msdn.microsoft.com/library/windows/hardware/ff568803) callout function does not recognize the kind of notification that is passed in the *notifyType* parameter, it should ignore the notification and return STATUS\_SUCCESS.

A callout driver can specify a context to be associated with a filter when the filter is added to the filter engine. Such a context is opaque to the filter engine. The callout's [*classifyFn*](https://msdn.microsoft.com/library/windows/hardware/ff544890) callout function can use this context to save state information for the next time that it is called by the filter engine. When the filter is deleted from the filter engine, the callout driver performs any necessary cleanup of the context.

For example:

```C++
// Context structure to be associated with the filters
typedef struct FILTER_CONTEXT_ {
  .
  .  // Driver-specific content
  .
} FILTER_CONTEXT, *PFILTER_CONTEXT;

// Memory pool tag for filter context structures
#define FILTER_CONTEXT_POOL_TAG &#39;fcpt&#39;

// notifyFn callout function
NTSTATUS NTAPI
 NotifyFn(
    IN FWPS_CALLOUT_NOTIFY_TYPE  notifyType,
    IN const GUID  *filterKey,
    IN const FWPS_FILTER0  *filter
    )
{
  PFILTER_CONTEXT context;

 ASSERT(filter != NULL);

  // Switch on the type of notification
 switch(notifyType) {

    // A filter is being added to the filter engine
 case FWPS_CALLOUT_NOTIFY_ADD_FILTER:

      // Allocate the filter context structure
 context =
        (PFILTER_CONTEXT)ExAllocatePoolWithTag(
 NonPagedPool,
 sizeof(FILTER_CONTEXT),
          FILTER_CONTEXT_POOL_TAG
          );

      // Check the result of the memory allocation
 if (context == NULL) {

        // Return error
 return STATUS_INSUFFICIENT_RESOURCES;
      }

      // Initialize the filter context structure
      ...

      // Associate the filter context structure with the filter
 filter->context = (UINT64)context;

 break;

    // A filter is being removed from the filter engine
 case FWPS_CALLOUT_NOTIFY_DELETE_FILTER:

      // Get the filter context structure from the filter
 context = (PFILTER_CONTEXT)filter->context;

 // Check whether the filter has a context
 if (context) {

        // Cleanup the filter context structure
        ...

        // Free the memory for the filter context structure
 ExFreePoolWithTag(
 context,
          FILTER_CONTEXT_POOL_TAG
          );

      }
 break;

    // Unknown notification
 default:

      // Do nothing
 break;
  }

 return STATUS_SUCCESS;
}
```

 

 





