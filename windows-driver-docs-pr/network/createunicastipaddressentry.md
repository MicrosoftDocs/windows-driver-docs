---
title: CreateUnicastIpAddressEntry function (Windows Drivers)
description: Learn more about the CreateUnicastIpAddressEntry function.
keywords:
- CreateUnicastIpAddressEntry
- netioapi/CreateUnicastIpAddressEntry
ms.date: 10/25/2022
---

# CreateUnicastIpAddressEntry function

The **CreateUnicastIpAddressEntry** function adds a new unicast IP address entry on the local computer.

## Syntax

``` c++
NETIOAPI_API CreateUnicastIpAddressEntry(
  _In_ const MIB_UNICASTIPADDRESS_ROW *Row
);
```

## Parameters

- *Row* \[in\]  
   A pointer to a [**MIB\_UNICASTIPADDRESS\_ROW**](mib-unicastipaddress-row.md) structure entry for a unicast IP address entry.

## Return value

**CreateUnicastIpAddressEntry** returns STATUS\_SUCCESS if the function succeeds.

If the function fails, **CreateUnicastIpAddressEntry** returns one of the following error codes:

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
<td><p>An invalid parameter was passed to the function. This error is returned if a <strong>NULL</strong> pointer is passed in the <em>Row</em> parameter, the <strong>Address</strong> member of the <a href="mib-unicastipaddress-row.md"><strong>MIB_UNICASTIPADDRESS_ROW</strong></a> structure that the <em>Row</em> parameter points to was not set to a valid unicast IPv4 or IPv6 address, or both <strong>InterfaceLuid</strong> and <strong>InterfaceIndex</strong> members of the MIB_UNICASTIPADDRESS_ROW structure were unspecified.</p>
<p>This error is also returned for other errors in the values that are set for members in the MIB_UNICASTIPADDRESS_ROW structure. These errors include the following situations:</p>
<ul>
<li><p>The <strong>ValidLifetime</strong> member is less than than the <strong>PreferredLifetime</strong> member.</p></li>
<li><p>The <strong>PrefixOrigin</strong> member is set to <strong>IpPrefixOriginUnchanged</strong> and the <strong>SuffixOrigin</strong> is not set to IpSuffixOriginUnchanged.</p></li>
<li><p>The <strong>PrefixOrigin</strong> member is not set to <strong>IpPrefixOriginUnchanged</strong> and the <strong>SuffixOrigin</strong> is set to IpSuffixOriginUnchanged.</p></li>
<li><p>The <strong>PrefixOrigin</strong> member is not set to a value from the <a href="nl-prefix-origin.md"><strong>NL_PREFIX_ORIGIN</strong></a> enumeration.</p></li>
<li><p>The <strong>SuffixOrigin</strong> member is not set to a value from the NL_SUFFIX_ORIGIN enumeration.</p></li>
<li><p>The <strong>OnLinkPrefixLength</strong> member is set to a value that is greater than the IP address length, in bits (32 for a unicast IPv4 address or 128 for a unicast IPv6 address).</p></li>
</ul>
<p>For possible values of the NL_PREFIX_ORIGIN and NL_SUFFIX_ORIGIN enumerations, see <a href="mib-unicastipaddress-row.md"><strong>MIB_UNICASTIPADDRESS_ROW</strong></a>.</p></td>
</tr>
<tr class="even">
<td><strong>STATUS_NOT_FOUND</strong></td>
<td><p>The specified interface could not be found. This error is returned if the function cannot find the network interface that is specified by the <strong>InterfaceLuid</strong> or <strong>InterfaceIndex</strong> member of the MIB_UNICASTIPADDRESS_ROW structure that the <em>Row</em> parameter points to.</p></td>
</tr>
<tr class="odd">
<td><strong>STATUS_NOT_SUPPORTED</strong></td>
<td><p>The request is not supported. This error is returned if no IPv4 stack is located on the local computer and an IPv4 address was specified in the <strong>Address</strong> member of the MIB_UNICASTIPADDRESS_ROW structure that the <em>Row</em> parameter points to, or if no IPv6 stack is located on the local computer and an IPv6 address was specified in the <strong>Address</strong> member.</p></td>
</tr>
<tr class="even">
<td><strong>ERROR_OBJECT_ALREADY_EXISTS</strong></td>
<td><p>The object already exists. This error is returned if the <strong>Address</strong> member of the MIB_UNICASTIPADDRESS_ROW structure that the <em>Row</em> parameter points to is a duplicate of an existing unicast IP address on the interface that is specified by the <strong>InterfaceLuid</strong> or <strong>InterfaceIndex</strong> member of the MIB_UNICASTIPADDRESS_ROW.</p></td>
</tr>
<tr class="odd">
<td><strong>Other</strong></td>
<td><p>Use the <a href="/windows/win32/api/winbase/nf-winbase-formatmessage">FormatMessage</a> function to obtain the message string for the returned error.</p></td>
</tr>
</tbody>
</table>

## Remarks

Use the [**InitializeUnicastIpAddressEntry**](initializeunicastipaddressentry.md) function to initialize the members of a [**MIB\_UNICASTIPADDRESS\_ROW**](mib-unicastipaddress-row.md) structure entry with default values. A driver can then change the members in the MIB\_UNICASTIPADDRESS\_ROW entry that it wants to modify, and then call the **CreateUnicastIpAddressEntry** function.

On input, your driver must initialize the following members of the MIB\_UNICASTIPADDRESS\_ROW structure that the *Row* parameter points to.

- **Address**  
   Set to a valid unicast IPv4 or IPv6 address and family.

- **InterfaceLuid** or **InterfaceIndex**  
   These members are used in the order that is listed earlier. So if **InterfaceLuid** is specified, this member is used to determine the interface to add the unicast IP address to. If no value was set for the **InterfaceLuid** member (the value of this member was set to zero), the **InterfaceIndex** member is next used to determine the interface.

If the **OnLinkPrefixLength** member of the MIB\_UNICASTIPADDRESS\_ROW structure that the *Row* parameter points to is set to 255, **CreateUnicastIpAddressEntry** adds the new unicast IP address with the **OnLinkPrefixLength** member set equal to the length of the IP address. So for a unicast IPv4 address, the **OnLinkPrefixLength** is set to 32 and the **OnLinkPrefixLength** is set to 128 for a unicast IPv6 address. If this setting would result in the incorrect subnet mask for an IPv4 address or the incorrect link prefix for an IPv6 address, the driver should set the **OnLinkPrefixLength** member to the correct value before calling **CreateUnicastIpAddressEntry**.

If a unicast IP address is created with the **OnLinkPrefixLength** member set incorrectly, your driver can change the IP address by calling [**SetUnicastIpAddressEntry**](setunicastipaddressentry.md) with the **OnLinkPrefixLength** member set to the correct value.

The **DadState**, **ScopeId**, and **CreationTimeStamp** members of the MIB\_UNICASTIPADDRESS\_ROW structure that the *Row* parameter points to are ignored when the **CreateUnicastIpAddressEntry** function is called. These members are set by the network stack. The **ScopeId** member is automatically determined by the interface that the address is added on.

The **CreateUnicastIpAddressEntry** function fails if the unicast IP address that is passed in the **Address** member of the MIB\_UNICASTIPADDRESS\_ROW structure that the *Row* parameter points to is a duplicate of an existing unicast IP address on the interface. Note that your driver can add a loopback IP address to a loopback interface only by using the **CreateUnicastIpAddressEntry** function.

The unicast IP address that is passed in the **Address** member of the MIB\_UNICASTIPADDRESS\_ROW structure that the *Row* parameter points to is not usable immediately. The IP address is usable after the duplicate address detection process has completed successfully. It can take several seconds for the duplicate address detection process to complete because IP packets must be sent and potential responses must be waited for. For IPv6, the duplicate address detection process typically takes about 1 second. For IPv4, the duplicate address detection process typically takes about 3 seconds.

After a driver calls the **CreateUnicastIpAddressEntry** function, it can use the following methods to determine if an IP address is still usable:

- **Use polling and the GetUnicastIpAddressEntry function**   
   After the call to the **CreateUnicastIpAddressEntry** function returns successfully, pause for 1 to 3 seconds (depending on whether an IPv6 or IPv4 address is being created) to allow time for the successful completion of the duplication address detection process. Then, call **GetUnicastIpAddressEntry** to retrieve the updated MIB\_UNICASTIPADDRESS\_ROW structure and examine the value of the **DadState** member. If the value of the **DadState** member is set to IpDadStatePreferred, the IP address is now usable. If the value of the **DadState** member is set to IpDadStateTentative, duplicate address detection has not yet completed. In this case, call the **GetUnicastIpAddressEntry** function again every 0.5 seconds while the **DadState** member is still set to IpDadStateTentative. If the value of the **DadState** member returns with some value other than **IpDadStatePreferred** or IpDadStateTentative, duplicate address detection has failed and the IP address is not usable.

- **Call one of the IP Helper NotifyXxx notification functions to set up an asynchronous notification for when an address changes**  
   After the call to the **CreateUnicastIpAddressEntry** function returns successfully, call the [**NotifyUnicastIpAddressChange**](notifyunicastipaddresschange.md) function to register the driver to be notified of changes to either IPv6 or IPv4 unicast IP addresses, depending on the type of IP address that is being created. When a notification is received for the IP address that is being created, call the **GetUnicastIpAddressEntry** function to retrieve the **DadState** member. If the value of the **DadState** member is set to IpDadStatePreferred, the IP address is now usable. If the value of the **DadState** member is set to IpDadStateTentative, duplicate address detection has not yet completed and the driver must wait for future notifications. If the value of the **DadState** member returns with some value other than **IpDadStatePreferred** or IpDadStateTentative, duplicate address detection has failed and the IP address is not usable.

   If, during the duplicate address detection process, the media is disconnected and then reconnected, the duplicate address detection process is restarted. So the time to complete the process might increase beyond the typical 1 second value for IPv6 or 3 second value for IPv4.

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

[**DeleteUnicastIpAddressEntry**](deleteunicastipaddressentry.md)

[**GetUnicastIpAddressEntry**](getunicastipaddressentry.md)

[**GetUnicastIpAddressTable**](getunicastipaddresstable.md)

[**InitializeUnicastIpAddressEntry**](initializeunicastipaddressentry.md)

[**MIB\_UNICASTIPADDRESS\_ROW**](mib-unicastipaddress-row.md)

[**MIB\_UNICASTIPADDRESS\_TABLE**](mib-unicastipaddress-table.md)

[**NL\_PREFIX\_ORIGIN**](nl-prefix-origin.md)

[**NL\_SUFFIX\_ORIGIN**](nl-suffix-origin.md)

[**NotifyIpInterfaceChange**](notifyipinterfacechange.md)

[**NotifyRouteChange2**](notifyroutechange2.md)

[**NotifyStableUnicastIpAddressTable**](notifystableunicastipaddresstable.md)

[**NotifyTeredoPortChange**](notifyteredoportchange.md)

[**NotifyUnicastIpAddressChange**](notifyunicastipaddresschange.md)

[**SetUnicastIpAddressEntry**](setunicastipaddressentry.md)
