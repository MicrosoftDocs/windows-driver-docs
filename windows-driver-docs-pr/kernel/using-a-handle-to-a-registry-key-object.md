---
title: Using a Handle to a Registry-Key Object
description: Using a Handle to a Registry-Key Object
keywords: ["handle to registry-key object WDK kernel", "registry WDK kernel , object routines", "driver registry information WDK kernel , object routines", "object routines WDK kernel", "registry-key objects WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Using a Handle to a Registry-Key Object





The following table lists the operations that drivers can perform on an open key as well as the appropriate routines to call.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Operation</th>
<th>Routine to call</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Examine the key's properties, such as its name or the number of its subkeys.</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-zwquerykey" data-raw-source="[&lt;strong&gt;ZwQueryKey&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwquerykey)"><strong>ZwQueryKey</strong></a></p></td>
</tr>
<tr class="even">
<td><p>Iterate through the key's subkeys, examining the properties of each one.</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-zwenumeratekey" data-raw-source="[&lt;strong&gt;ZwEnumerateKey&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwenumeratekey)"><strong>ZwEnumerateKey</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>Examine the properties of a key value, including the value's data.</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-zwqueryvaluekey" data-raw-source="[&lt;strong&gt;ZwQueryValueKey&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwqueryvaluekey)"><strong>ZwQueryValueKey</strong></a></p></td>
</tr>
<tr class="even">
<td><p>Iterate through a key's values, examining the properties of each one.</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-zwenumeratevaluekey" data-raw-source="[&lt;strong&gt;ZwEnumerateValueKey&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwenumeratevaluekey)"><strong>ZwEnumerateValueKey</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>Set the data for a value associated with a key.</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-zwsetvaluekey" data-raw-source="[&lt;strong&gt;ZwSetValueKey&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwsetvaluekey)"><strong>ZwSetValueKey</strong></a></p></td>
</tr>
<tr class="even">
<td><p>Delete a key.</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-zwdeletekey" data-raw-source="[&lt;strong&gt;ZwDeleteKey&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwdeletekey)"><strong>ZwDeleteKey</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>Delete a key value.</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-zwdeletevaluekey" data-raw-source="[&lt;strong&gt;ZwDeleteValueKey&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwdeletevaluekey)"><strong>ZwDeleteValueKey</strong></a></p></td>
</tr>
</tbody>
</table>

 

Once the driver has finished its manipulations, it must call [**ZwClose**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntclose) to close the handle—even if it has already called **ZwDeleteKey** to delete the key. (Once a key is deleted, all the open handles to it become invalid, however the driver must still close the handle.)

The following code example illustrates how to open a handle for a key named **\\Registry\\Machine\\Software\\**<em>MyCompany</em>\\*MyApp*, then retrieve key data and close the handle.

```cpp
//
// Get the frame location from the registry key
// HKLM\SOFTWARE\MyCompany\MyApp.
// For example: "FrameLocation"="X:\\MyApp\\Frames"
// 
HANDLE              handleRegKey = NULL;
for (int n = 0; n < 1; n++) 
{
    NTSTATUS           status = NULL;
    UNICODE_STRING     RegistryKeyName;
    OBJECT_ATTRIBUTES  ObjectAttributes;

    RtlInitUnicodeString(&RegistryKeyName, L"\\Registry\\Machine\\Software\\MyCompany\\MyApp");
    InitializeObjectAttributes(&ObjectAttributes, 
                               &RegistryKeyName,
                               OBJ_CASE_INSENSITIVE | OBJ_KERNEL_HANDLE,
                               NULL,    // handle
                               NULL);
    status = ZwOpenKey(&handleRegKey, KEY_READ, &ObjectAttributes);

    // If the driver cannot open the key, the driver cannot continue. 
    // In this situation, the driver was probably set up incorrectly 
    // and worst case, the driver cannot stream.
    if( NT_SUCCESS(status) == FALSE ) 
    {
        break;
    }
    // The driver obtained the registry key.
    PKEY_VALUE_FULL_INFORMATION  pKeyInfo = NULL;
    UNICODE_STRING               ValueName;
    ULONG                        ulKeyInfoSize = 0;
    ULONG                        ulKeyInfoSizeNeeded = 0;

    // The driver requires the following value.
    RtlInitUnicodeString(&ValueName, L"FrameLocation");

    // Determine the required size of keyInfo.
    status = ZwQueryValueKey( handleRegKey,
                              &ValueName,
                              KeyValueFullInformation,
                              pKeyInfo,
                              ulKeyInfoSize,
                              &ulKeyInfoSizeNeeded );

    // The driver expects one of the following errors.
    if( (status == STATUS_BUFFER_TOO_SMALL) || (status == STATUS_BUFFER_OVERFLOW) )
    {
        // Allocate the memory required for the key.
        ulKeyInfoSize = ulKeyInfoSizeNeeded;
        pKeyInfo = (PKEY_VALUE_FULL_INFORMATION) ExAllocatePoolWithTag( NonPagedPool, ulKeyInfoSizeNeeded, g_ulTag);
        if( NULL == pKeyInfo )
        {
            break;
        }
        RtlZeroMemory( pKeyInfo, ulKeyInfoSize );

        // Get the key data.
        status = ZwQueryValueKey( handleRegKey,
                                  &ValueName,
                                  KeyValueFullInformation,
                                  pKeyInfo,
                                  ulKeyInfoSize,
                                  &ulKeyInfoSizeNeeded );
        if( (status != STATUS_SUCCESS) || (ulKeyInfoSizeNeeded != ulKeyInfoSize) || (NULL == pKeyInfo) )
        {
            break;
        }

        // Fill in the frame location if it has not been filled in already.
        if ( NULL == m_szwFramePath )
        {
            m_ulFramePathLength = pKeyInfo->DataLength;
            ULONG_PTR   pSrc = NULL;

            pSrc = (ULONG_PTR) ( (PBYTE) pKeyInfo + pKeyInfo->DataOffset);

            m_szwFramePath = (LPWSTR) ExAllocatePoolWithTag( NonPagedPool, m_ulFramePathLength, g_ulTag);
            if ( NULL == m_szwFramePath )
            {
                m_ulFramePathLength = 0;
                break;
            }

            // Copy the frame path.
            RtlCopyMemory(m_szwFramePath, (PVOID) pSrc, m_ulFramePathLength);
        }
        // The driver is done with the pKeyInfo.
        xFreePoolWithTag(pKeyInfo, g_ulTag);

    } // if( (status == STATUS_BUFFER_TOO_SMALL) || (status == STATUS_BUFFER_OVERFLOW) )
} // Get the Frame location from the registry key.

// All done with the registry.
if (NULL != handleRegKey)
{
    ZwClose(handleRegKey);
}
```

The system caches key changes in memory and writes them to disk every few seconds. To force a key change to disk, call [**ZwFlushKey**](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwflushkey).

To manipulate the registry through a simpler interface, drivers can also call the **Rtl*Xxx*Registry*Xxx*** routines. For more information, see [Registry Run-Time Library Routines](registry-run-time-library-routines.md).

