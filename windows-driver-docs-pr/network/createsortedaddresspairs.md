---
title: CreateSortedAddressPairs function (Windows Drivers)
description: Learn more about the CreateSortedAddressPairs function.
keywords:
- CreateSortedAddressPairs
- netioapi/CreateSortedAddressPairs
ms.date: 10/25/2022
---

# CreateSortedAddressPairs function

From a supplied list of potential IP destination addresses, the **CreateSortedAddressPairs** function pairs the destination addresses together with the host machine's local IP addresses and sorts the pairs according to the preferred order of communication.

## Syntax

``` c++
NETIOAPI_API CreateSortedAddressPairs(
  _In_opt_ const PSOCKADDR_IN6      SourceAddressList,
  _In_           ULONG              SourceAddressCount,
  _In_     const PSOCKADDR_IN6      DestinationAddressList,
  _In_           ULONG              DestinationAddressCount,
  _In_           ULONG              AddressSortOptions,
  _In_           PSOCKADDR_IN6_PAIR *SortedAddressPairList,
  _Out_          ULONG              *SortedAddressPairCount
);
```

## Parameters

- *SourceAddressList* \[in, optional\]  
   Reserved. This parameter must be **NULL**.

- *SourceAddressCount* \[in\]  
   Reserved. This parameter must be zero.

- *DestinationAddressList* \[in\]  
   A pointer to a list of potential destination addresses of type [**SOCKADDR\_IN6**](/windows/win32/api/ws2ipdef/ns-ws2ipdef-sockaddr_in6_lh).

- *DestinationAddressCount* \[in\]  
   The number of addresses in the list that the *DestinationAddressList* parameter points to.

- *AddressSortOptions* \[in\]  
   Reserved. This parameter must be zero.

- *SortedAddressPairList* \[in\]  
   A pointer to a list of pairs of source and destination addresses, sorted in the preferred order of communication. For more information about this parameter, see the following Remarks section.

- *SortedAddressPairCount* \[out\]  
   The number of address pairs in the list that the *SortedAddressPairList* parameter points to.

## Return value

**CreateSortedAddressPairs** returns STATUS\_SUCCESS if the function succeeds.

If the function fails, **CreateSortedAddressPairs** returns one of the following error codes:

<table>
<thead>
<tr class="header">
<th>Return code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>STATUS_INVALID_PARAMETER</strong></td>
<td><p>An invalid parameter was passed to the function.</p></td>
</tr>
<tr class="even">
<td><strong>STATUS_NOT_ENOUGH_MEMORY</strong></td>
<td><p>Insufficient memory resources were available to complete the operation.</p></td>
</tr>
<tr class="odd">
<td><strong>Other</strong></td>
<td><p>Use the <a href="/windows/win32/api/winbase/nf-winbase-formatmessage">FormatMessage</a> function to obtain the message string for the returned error.</p></td>
</tr>
</tbody>
</table>

## Remarks

The **CreateSortedAddressPairs** function automatically pairs the host machine's local addresses together with the supplied list of potential destination addresses that the *DestinationAddressList* parameter points to.

The returned list of pairs of addresses that the *SortedAddressPairList* parameter points to is sorted so that the address pairs that are best suited for communication between two peers occurr earlier in the list.

The *SortedAddressPairList* parameter is of type PSOCKADDR\_IN6\_PAIR, which is defined in the Ws2ipdef.h header as follows.

```cpp
    typedef struct _sockaddr_in6_pair
    {
        PSOCKADDR_IN6  SourceAddress;
        PSOCKADDR_IN6  DestinationAddress;
    } SOCKADDR_IN6_PAIR, *PSOCKADDR_IN6_PAIR;

  - **SourceAddress**  
    The IP source address.

  - **DestinationAddress**  
    The IP destination address.
```

## Requirements

<table>
<tbody>
<tr class="odd">
<td><p>Target platform</p></td>
<td><a href="/windows-hardware/drivers/develop/target-platforms">Universal</a></td>
</tr>
<tr class="even">
<td><p>Version</p></td>
<td><p>Available in Windows Vista and later versions of the Windows operating systems.</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Netioapi.h (include Netioapi.h)</td>
</tr>
<tr class="even">
<td><p>Library</p></td>
<td>Netio.lib</td>
</tr>
<tr class="odd">
<td><p>IRQL</p></td>
<td><p>&lt; DISPATCH_LEVEL</p></td>
</tr>
</tbody>
</table>

## See also

[FormatMessage](/windows/win32/api/winbase/nf-winbase-formatmessage)

[**SOCKADDR\_IN6**](/windows/win32/api/ws2ipdef/ns-ws2ipdef-sockaddr_in6_lh)
