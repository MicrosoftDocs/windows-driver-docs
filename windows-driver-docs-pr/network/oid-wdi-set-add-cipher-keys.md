---
title: OID_WDI_SET_ADD_CIPHER_KEYS
description: OID_WDI_SET_ADD_CIPHER_KEYS adds or overwrites cipher keys in the key table of a port. This is a set-only property.
ms.assetid: d10fc976-9e51-4bbb-8f29-caf8c600618a
ms.date: 07/18/2017
keywords:
 - OID_WDI_SET_ADD_CIPHER_KEYS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WDI\_SET\_ADD\_CIPHER\_KEYS


OID\_WDI\_SET\_ADD\_CIPHER\_KEYS adds or overwrites cipher keys in the key table of a port. This is a set-only property.

| Scope | Set serialized with task | Normal execution time (seconds) |
|-------|--------------------------|---------------------------------|
| Port  | Yes                      | 1                               |

 

Cipher keys that are marked as Static should not be cleared on a roam. They can only be cleared on a [OID\_WDI\_TASK\_DOT11\_RESET](oid-wdi-task-dot11-reset.md) or if they are overwritten with a new OID\_WDI\_SET\_ADD\_CIPHER\_KEYS.

## Set property parameters


| TLV                                                                          | Multiple TLV instances allowed | Optional | Description                                                              |
|------------------------------------------------------------------------------|--------------------------------|----------|--------------------------------------------------------------------------|
| [**WDI\_TLV\_SET\_CIPHER\_KEY\_INFO**](https://msdn.microsoft.com/library/windows/hardware/dn898056) | X                              |          | The cipher keys to be added or overwritten in the key table of the port. |

 

## Set property results


No additional data. The data in the header is sufficient.
Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Minimum supported client</p></td>
<td><p>Windows 10</p></td>
</tr>
<tr class="even">
<td><p>Minimum supported server</p></td>
<td><p>Windows Server 2016</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Dot11wdi.h</td>
</tr>
</tbody>
</table>

## See also


[OID\_WDI\_SET\_DELETE\_CIPHER\_KEYS](oid-wdi-set-delete-cipher-keys.md)

 

 




