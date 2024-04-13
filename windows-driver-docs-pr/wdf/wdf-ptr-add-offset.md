---
title: WDF_PTR_ADD_OFFSET Macro
description: The WDF_PTR_ADD_OFFSET macro adds an offset value to an address and returns the resulting address.
keywords:
 - WDF_PTR_ADD_OFFSET macro
ms.date: 08/23/2017
ms.topic: reference
---

# WDF_PTR_ADD_OFFSET macro


The **WDF_PTR_ADD_OFFSET** macro adds an offset value to an address and returns the resulting address.

## Syntax

```ManagedCPlusPlus
PVOID WDF_PTR_ADD_OFFSET(
    _ptr,
    _offset
);
```

## Parameters

*_ptr*   
Specifies an address.

*_offset*   
Specifies the offset value in bytes.

## Return value

Returns a pointer to the resulting address.

## Remarks

This macro invokes [**WDF_PTR_ADD_OFFSET_TYPE**](wdf-ptr-add-offset-type.md) with the *_type* parameter set to PVOID.

The macro is defined as follows:

```ManagedCPlusPlus
#define WDF_PTR_ADD_OFFSET(_ptr, _offset) \
        WDF_PTR_ADD_OFFSET_TYPE(_ptr, _offset, PVOID)
```

Here is an example from the Toaster sample (toaster\\func\\featured\\wmi.c). In the example, the driver calls **WDF_PTR_ADD_OFFSET** to add an offset to an address to determine a destination buffer address to pass to the [**WDF_WMI_BUFFER_APPEND_STRING**](/windows-hardware/drivers/ddi/wdfwmi/nf-wdfwmi-wdf_wmi_buffer_append_string) function.

```cpp
        //
        // Write the instance name
        //
        size -= wnodeSize;
        status = WDF_WMI_BUFFER_APPEND_STRING(
            WDF_PTR_ADD_OFFSET(wnode, wnode->OffsetInstanceName),
            size,
            &deviceName,
            &length
            );

        //
        // Size was precomputed, this should never fail
        //
        ASSERT(NT_SUCCESS(status));


        //
        // Write the data, which is the model name as a string
        //
        size -= wnodeInstanceNameSize;
        WDF_WMI_BUFFER_APPEND_STRING(
            WDF_PTR_ADD_OFFSET(wnode,  wnode->DataBlockOffset),
            size,
            &modelName,
            &length
            );
```

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Target platform</p></td>
<td><a href="https://go.microsoft.com/fwlink/p/?linkid=531356" data-raw-source="[Universal](https://go.microsoft.com/fwlink/p/?linkid=531356)">Universal</a></td>
</tr>
<tr class="even">
<td><p>Minimum KMDF version</p></td>
<td><p>1.5</p></td>
</tr>
<tr class="odd">
<td><p>Minimum UMDF version</p></td>
<td><p>2.0</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Wdfcore.h (include Wdf.h)</td>
</tr>
</tbody>
</table>
