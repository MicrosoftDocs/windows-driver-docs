---
title: Using a Handle to a Registry-Key Object
author: windows-driver-content
description: Using a Handle to a Registry-Key Object
ms.assetid: 25982249-31dc-4542-9ebb-139991619b40
keywords: ["handle to registry-key object WDK kernel", "registry WDK kernel , object routines", "driver registry information WDK kernel , object routines", "object routines WDK kernel", "registry-key objects WDK kernel"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Using a Handle to a Registry-Key Object


## <a href="" id="ddk-using-a-handle-to-a-registry-key-object-kg"></a>


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
<td><p>[<strong>ZwQueryKey</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567060)</p></td>
</tr>
<tr class="even">
<td><p>Iterate through the key's subkeys, examining the properties of each one.</p></td>
<td><p>[<strong>ZwEnumerateKey</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566447)</p></td>
</tr>
<tr class="odd">
<td><p>Examine the properties of a key value, including the value's data.</p></td>
<td><p>[<strong>ZwQueryValueKey</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567069)</p></td>
</tr>
<tr class="even">
<td><p>Iterate through a key's values, examining the properties of each one.</p></td>
<td><p>[<strong>ZwEnumerateValueKey</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566453)</p></td>
</tr>
<tr class="odd">
<td><p>Set the data for a value associated with a key.</p></td>
<td><p>[<strong>ZwSetValueKey</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567109)</p></td>
</tr>
<tr class="even">
<td><p>Delete a key.</p></td>
<td><p>[<strong>ZwDeleteKey</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566437)</p></td>
</tr>
<tr class="odd">
<td><p>Delete a key value.</p></td>
<td><p>[<strong>ZwDeleteValueKey</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566439)</p></td>
</tr>
</tbody>
</table>

 

Once the driver has finished its manipulations, it must call [**ZwClose**](https://msdn.microsoft.com/library/windows/hardware/ff566417) to close the handle—unless it has already called **ZwDeleteKey** to delete the key. (Once a key is deleted, all the open handles to it become invalid, so the driver must not close the handle in this case.)

The following code example illustrates how to open a handle for a key named **\\Registry\\Machine\\Software\\***MyCompany*\\*MyApp*, then retrieve key data and close the handle.

```
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

    RtlInitUnicodeString(&amp;RegistryKeyName, L"\\Registry\\Machine\\Software\\MyCompany\\MyApp");
    InitializeObjectAttributes(&amp;ObjectAttributes, 
                               &amp;RegistryKeyName,
                               OBJ_CASE_INSENSITIVE | OBJ_KERNEL_HANDLE,
                               NULL,    // handle
                               NULL);
    status = ZwOpenKey(&amp;handleRegKey, KEY_READ, &amp;ObjectAttributes);

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
    RtlInitUnicodeString(&amp;ValueName, L"FrameLocation");

    // Determine the required size of keyInfo.
    status = ZwQueryValueKey( handleRegKey,
                              &amp;ValueName,
                              KeyValueFullInformation,
                              pKeyInfo,
                              ulKeyInfoSize,
                              &amp;ulKeyInfoSizeNeeded );

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
                                  &amp;ValueName,
                                  KeyValueFullInformation,
                                  pKeyInfo,
                                  ulKeyInfoSize,
                                  &amp;ulKeyInfoSizeNeeded );
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

The system caches key changes in memory and writes them to disk every few seconds. To force a key change to disk, call [**ZwFlushKey**](https://msdn.microsoft.com/library/windows/hardware/ff566457).

To manipulate the registry through a simpler interface, drivers can also call the **Rtl*Xxx*Registry*Xxx*** routines. For more information, see [Registry Run-Time Library Routines](registry-run-time-library-routines.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Using%20a%20Handle%20to%20a%20Registry-Key%20Object%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


