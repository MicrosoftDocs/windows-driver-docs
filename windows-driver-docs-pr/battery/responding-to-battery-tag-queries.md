---
title: Responding to Battery Tag Queries
description: Responding to Battery Tag Queries
ms.assetid: ac22a1d3-413c-4991-ac9c-fbfb2c6f16c6
keywords: ["battery tags WDK"]
---

# Responding to Battery Tag Queries


## <span id="ddk_responding_to_battery_tag_queries_dg"></span><span id="DDK_RESPONDING_TO_BATTERY_TAG_QUERIES_DG"></span>


The battery tag is a ULONG counter initialized and incremented by the miniclass driver. The battery class driver calls [*BatteryMiniQueryTag*](https://msdn.microsoft.com/library/windows/hardware/ff536275) to request the current value of the tag.

This miniclass driver routine is declared as follows:

```
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[battery\battery]:%20Responding%20to%20Battery%20Tag%20Queries%20%20RELEASE:%20%286/7/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


