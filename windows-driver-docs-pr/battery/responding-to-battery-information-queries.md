---
title: Responding to Battery Information Queries
description: Responding to Battery Information Queries
ms.assetid: 5d215ff8-d41f-471e-bc54-570a94f3c23f
keywords: ["battery information WDK"]
---

# Responding to Battery Information Queries


## <span id="ddk_responding_to_battery_information_queries_dg"></span><span id="DDK_RESPONDING_TO_BATTERY_INFORMATION_QUERIES_DG"></span>


The battery class driver calls the [*BatteryMiniQueryInformation*](https://msdn.microsoft.com/library/windows/hardware/ff536273) routine to get a variety of information about the current battery. This routine is declared as follows:

```
typedef 
NTSTATUS
(*BCLASS_QUERY_INFORMATION)(
    IN PVOID Context,
    IN ULONG BatteryTag,
    IN BATTERY_QUERY_INFORMATION_LEVEL Level,
    IN LONG AtRate OPTIONAL,
    OUT PVOID Buffer,
    IN ULONG BufferLength,
    OUT PULONG ReturnedLength
    );
```

The *Context* parameter is a pointer to the context area that is allocated by the miniclass driver and passed to the class driver in the [**BATTERY\_MINIPORT\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff536287) structure at device initialization. The *BatteryTag* parameter is a value previously returned by [*BatteryMiniQueryTag*](https://msdn.microsoft.com/library/windows/hardware/ff536275).

The *Level* parameter specifies the kind of information requested. The miniclass driver formats the information as a [**BATTERY\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff536283) structure and returns it at the address supplied by *Buffer*, with a pointer to its length in *ReturnedLength*.

A miniclass driver should be prepared to handle requests for the following:

-   Battery capabilities, chemistry, capacity, low-capacity alert levels, and reserve charge

-   Temperature, in tenths of a degree Kelvin

-   Estimated remaining run time, in seconds

-   Device name

-   Manufacturer's battery model name

-   Date of manufacture

-   Unique ID

-   Serial number

Some batteries are not capable of reporting all this information. A miniclass driver should return STATUS\_INVALID\_DEVICE\_REQUEST for any information that its device cannot supply.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[battery\battery]:%20Responding%20to%20Battery%20Information%20Queries%20%20RELEASE:%20%286/7/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


