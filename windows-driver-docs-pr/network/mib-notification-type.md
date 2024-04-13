---
title: MIB_NOTIFICATION_TYPE enumeration (Windows Drivers)
description: Learn more about the MIB_NOTIFICATION_TYPE enumeration.
keywords:
- MIB_NOTIFICATION_TYPE
- MibAddInstance
- MibDeleteInstance
- MibInitialNotification
- MibParameterNotification
- PMIB_NOTIFICATION_TYPE
- netioapi/MIB_NOTIFICATION_TYPE
- netioapi/MibAddInstance
- netioapi/MibDeleteInstance
- netioapi/PMIB_NOTIFICATION_TYPE
- netioapi/MibInitialNotification
- netioapi/MibParameterNotification
ms.date: 10/25/2022
ms.topic: reference
---

# MIB\_NOTIFICATION\_TYPE enumeration

The MIB\_NOTIFICATION\_TYPE enumeration type defines the notification type that is passed to a callback function when a notification occurs.

## Syntax

``` c++
typedef enum _MIB_NOTIFICATION_TYPE { 
  MibParameterNotification  = 0,
  MibAddInstance            = 1,
  MibDeleteInstance         = 2,
  MibInitialNotification    = 3
} MIB_NOTIFICATION_TYPE, *PMIB_NOTIFICATION_TYPE;
```

## Constants

- **MibParameterNotification**  
   A parameter was changed.

- **MibAddInstance**  
   A new MIB instance was added.

- **MibDeleteInstance**  
   An existing MIB instance was deleted.

- **MibInitialNotification**  
   A notification that is invoked immediately after registration for change notification completes. This initial notification does not indicate that a change occurred to a MIB instance. The purpose of this initial notification type is to provide confirmation that the callback function is properly registered.

## Remarks

The MIB\_NOTIFICATION\_TYPE enumerated type is used with the callback function that is specified in the *Callback* parameter of one of the IP Helper **Notify*Xxx*** functions to specify the notification type.

On Windows Vista and later versions of the Windows operating systems, new functions are provided to register the driver to be notified when an IPv6 or IPv4 interface changes, an IPv6 or IPv4 unicast address changes, or an IPv6 or IPv4 route changes. These registration functions require that a callback function be passed that is called when a change occurs. One of the parameters that is passed to the callback function when a notification occurs is a parameter that contains a MIB\_NOTIFICATION\_TYPE value that indicates the notification type.

## Requirements

<table>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Available in Windows Vista and later versions of the Windows operating systems.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Netioapi.h (include Netioapi.h)</td>
</tr>
</tbody>
</table>

## See also

[**NotifyIpInterfaceChange**](notifyipinterfacechange.md)

[**NotifyRouteChange2**](notifyroutechange2.md)

[**NotifyStableUnicastIpAddressTable**](notifystableunicastipaddresstable.md)

[**NotifyTeredoPortChange**](notifyteredoportchange.md)

[**NotifyUnicastIpAddressChange**](notifyunicastipaddresschange.md)
