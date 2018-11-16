---
title: WdfObjectAddCustomType macro
description: The WdfObjectAddCustomType macro associates a framework object with a custom type.
ms.assetid: 750CF669-A436-4571-B474-D5447E0AA64F
keywords:
 - WdfObjectAddCustomType macro
ms.date: 08/23/2017
ms.localizationpriority: medium
---

# WdfObjectAddCustomType macro


\[Applies to KMDF and UMDF\]

The **WdfObjectAddCustomType** macro associates a framework object with a custom type.

Syntax
------

```ManagedCPlusPlus
NTSTATUS WdfObjectAddCustomType(
    _handle,
    _type
);
```

Parameters
----------

*_handle*   
A handle to a framework object.

*_type*   
The driver-defined name for the custom type.

Return value
------------

**WdfObjectAddCustomType** returns STATUS_SUCCESS if the operation succeeds. Otherwise, this method might return one of the following values:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Return code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>STATUS_OBJECT_PATH_INVALID</strong></td>
<td><p>The specified handle cannot have a custom type added to it.</p></td>
</tr>
<tr class="even">
<td><strong>STATUS_INSUFFICIENT_RESOURCES</strong></td>
<td><p>The custom type could not be allocated.</p></td>
</tr>
<tr class="odd">
<td><strong>STATUS_OBJECT_NAME_EXISTS</strong></td>
<td><p>The driver has already added the specified custom type.</p></td>
</tr>
<tr class="even">
<td><strong>STATUS_DELETE_PENDING</strong></td>
<td><p>The object that the Handle parameter specifies is being deleted. In this situation, the framework does not add the custom type.</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

**WdfObjectAddCustomType** is a simplified version of [**WdfObjectAddCustomTypeWithData**](wdfobjectaddcustomtypewithdata.md).

For more information about object driver types, see [Framework Object Custom Types](https://msdn.microsoft.com/library/windows/hardware/hh406457).

Examples
--------

This example code shows how to add a custom type to a queue.

```cpp
NTSTATUS                status;
WDF_IO_QUEUE_CONFIG     queueConfig;
WDFQUEUE                queue;  

WDF_IO_QUEUE_CONFIG_INIT(&amp;queueConfig,   
                         WdfIoQueueDispatchParallel);  

status = WdfIoQueueCreate(device,  
                          &amp;queueConfig,  
                          WDF_NO_OBJECT_ATTRIBUTES,  
                          &amp;queue);  
 
if (!NT_SUCCESS(status)) {  
     TraceEvents(TRACE_LEVEL_ERROR, DBG_INFO,
                 "Failed to create queue, status=0x%x\n", status);
     goto Done;  
}  

status = WdfObjectAddCustomType(queue, TEST_TYPE1);  

if (!NT_SUCCESS(status)) {  
    TraceEvents(TRACE_LEVEL_ERROR, DBG_INFO,  
                "Failed to add TEST_TYPE1 to WDFOBJECT 0x%p, status=0x%x\n",   
    queue, status);  
    goto Done;  
}    

End:  
    return status;    
```

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Target platform</p></td>
<td><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" data-raw-source="[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)">Universal</a></td>
</tr>
<tr class="even">
<td><p>Minimum KMDF version</p></td>
<td><p>1.11</p></td>
</tr>
<tr class="odd">
<td><p>Minimum UMDF version</p></td>
<td><p>2.0</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Wdfobject.h (include Wdf.h)</td>
</tr>
</tbody>
</table>

## See also


[**WDF_DECLARE_CUSTOM_TYPE**](wdf-declare-custom-type.md)

[**WdfObjectAddCustomTypeWithData**](wdfobjectaddcustomtypewithdata.md)

[**WdfObjectGetCustomTypeData**](wdfobjectgetcustomtypedata.md)

[**WdfObjectIsCustomType**](wdfobjectiscustomtype.md)

 

 






