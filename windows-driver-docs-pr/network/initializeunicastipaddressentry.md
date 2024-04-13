---
title: InitializeUnicastIpAddressEntry function (Windows Drivers)
description: Learn more about the InitializeUnicastIpAddressEntry function.
keywords:
- InitializeUnicastIpAddressEntry
- netioapi/InitializeUnicastIpAddressEntry
ms.date: 10/25/2022
ms.topic: reference
---

# InitializeUnicastIpAddressEntry function

The **InitializeUnicastIpAddressEntry** function initializes a [**MIB\_UNICASTIPADDRESS\_ROW**](mib-unicastipaddress-row.md) structure with default values for a unicast IP address entry on a local computer.

## Syntax

``` c++
VOID NETIOAPI_API_ InitializeUnicastIpAddressEntry(
  _Out_ PMIB_UNICASTIPADDRESS_ROW Row
);
```

## Parameters

- *Row* \[out\]  
   On entry, a pointer to a [**MIB\_UNICASTIPADDRESS\_ROW**](mib-unicastipaddress-row.md) structure entry for a unicast IP address entry. On return, the MIB\_UNICASTIPADDRESS\_ROW structure that this parameter points to is initialized with default values for a unicast IP address.

## Return value

None

## Remarks

Your driver must use the **InitializeUnicastIpAddressEntry** function to initialize the members of a [**MIB\_UNICASTIPADDRESS\_ROW**](mib-unicastipaddress-row.md) structure entry with default values for a unicast IP address for later use with the [**CreateUnicastIpAddressEntry**](createunicastipaddressentry.md) function.

On input, your driver must pass **InitializeUnicastIpAddressEntry** a new MIB\_UNICASTIPADDRESS\_ROW structure to initialize.

On output, the members of the MIB\_UNICASTIPADDRESS\_ROW structure that the *Row* parameter points to are initialized as follows.

- **PrefixOrigin**  
   Set to the **IpPrefixOriginUnchanged** value of the [**NL\_PREFIX\_ORIGIN**](nl-prefix-origin.md) enumeration.

- **SuffixOrigin**  
   Set to the **IpSuffixOriginUnchanged** value of the [**NL\_PREFIX\_ORIGIN**](nl-prefix-origin.md) enumeration.

- **OnLinkPrefixLength**  
   Set to an illegal value.

- **PreferredLifetime** and **ValidLifetime**  
   Set to infinite values.

- **SkipAsSource**  
   Set to **FALSE**.

- All other members  
   Set to zero.

After a driver calls **InitializeUnicastIpAddressEntry**, the driver can then change the members in the MIB\_UNICASTIPADDRESS\_ROW entry that it wants to modify, and then call the **CreateUnicastIpAddressEntry** to add the new unicast IP address to the local computer.

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

[**CreateUnicastIpAddressEntry**](createunicastipaddressentry.md)

[**DeleteUnicastIpAddressEntry**](deleteunicastipaddressentry.md)

[**GetUnicastIpAddressEntry**](getunicastipaddressentry.md)

[**GetUnicastIpAddressTable**](getunicastipaddresstable.md)

[**MIB\_UNICASTIPADDRESS\_ROW**](mib-unicastipaddress-row.md)

[**MIB\_UNICASTIPADDRESS\_TABLE**](mib-unicastipaddress-table.md)

[**NotifyUnicastIpAddressChange**](notifyunicastipaddresschange.md)

[**SetUnicastIpAddressEntry**](setunicastipaddressentry.md)
