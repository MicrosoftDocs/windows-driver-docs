---
title: Responding to Battery Tag Queries
description: Responding to Battery Tag Queries
ms.assetid: ac22a1d3-413c-4991-ac9c-fbfb2c6f16c6
keywords:
- battery tags WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Responding to Battery Tag Queries


## <span id="ddk_responding_to_battery_tag_queries_dg"></span><span id="DDK_RESPONDING_TO_BATTERY_TAG_QUERIES_DG"></span>


The battery tag is a ULONG counter initialized and incremented by the miniclass driver. The battery class driver calls [*BatteryMiniQueryTag*](https://msdn.microsoft.com/library/windows/hardware/ff536275) to request the current value of the tag.

This miniclass driver routine is declared as follows:

```cpp
typedef
NTSTATUS
(*BCLASS_QUERY_TAG)(
    IN PVOID Context,
    OUT PULONG BatteryTag
    );
```

The *Context* parameter is a pointer to the context area that is allocated by the miniclass driver and passed to the class driver in the BATTERY\_MINIPORT\_INFO structure at device initialization ([**BatteryClassInitializeDevice**](https://msdn.microsoft.com/library/windows/hardware/ff536266)). The *BatteryTag* value is created and maintained by the miniclass driver.

Each time a battery is inserted, the miniclass driver must increment the value of the tag, regardless of whether this is a new battery or the same battery that was previously present.

If no battery is present, or if the miniclass driver cannot determine whether a battery is present, the miniclass driver should return STATUS\_NO\_SUCH\_DEVICE and set the value of the tag to BATTERY\_TAG\_INVALID.

The class driver uses the battery tag internally and in calls to the miniclass driver to identify a specific instance of a battery. The miniclass driver should check the value of the battery tag that is passed to each of its standard routines to ensure that it corresponds to the current battery. If the tag is incorrect, the miniclass driver should return STATUS\_NO\_SUCH\_DEVICE.

 

 




