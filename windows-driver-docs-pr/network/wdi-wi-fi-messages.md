---
title: WDI message structure
description: This section describes the structure for WDI command messages
ms.assetid: 09663C5F-A458-479F-B450-A994486A6C18
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WDI message structure


All WDI command messages must start with a [**WDI\_MESSAGE\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn926074) structure. The command header is followed by zero or more type-length-value (TLV) structures.

The command message IDs defined for messages sent from the host to the Wi-Fi device are documented in [WDI Task OIDs](https://msdn.microsoft.com/library/windows/hardware/dn926082), [WDI Property OIDs](https://msdn.microsoft.com/library/windows/hardware/dn926079), and [WDI Status Indications](https://msdn.microsoft.com/library/windows/hardware/dn926080).

## TLVs


The structure of TLVs is defined in the following table. The data in TLVs is in little-endian byte order.

| Field                      | Type     | Description                                                                                                                                   |
|----------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Type                       | UINT16   | The type of the TLV structure. Unrecognized TLV types must be skipped without triggering errors.                                              |
| Length of the Value buffer | UINT16   | The size of the Value buffer in bytes.                                                                                                        |
| Value                      | BYTE\[\] | The payload buffer, which may contain a structure, a list of structures, or other TLVs. The data size must exactly match the expected length. |

 

There are two types of TLV groupings: statically sized TLV lists, and multi-TLV groups.

## Statically sized TLV lists


Statically-sized TLV lists contain several statically sized members. They are analogous to standard C-style arrays.

In this example, [**WDI\_TLV\_UNICAST\_ALGORITHM\_LIST**](https://msdn.microsoft.com/library/windows/hardware/dn898073) is defined as a list of WDI\_ALGO\_PAIRS.

|        |                                    |
|--------|------------------------------------|
| Type   | WDI\_TLV\_UNICAST\_ALGORITHM\_LIST |
| Length | N \* sizeof(WDI\_ALGO\_PAIRS)      |
| Value  | WDI\_ALGO\_PAIRS\[N\]              |

 

This usage is specified in the TLV reference topics with array notation.

## Multi-TLV groups


When the size of a given object is not known ahead of time, multi-TLV groups are used. This usage pattern specifies that N different variably sized TLVs are expected within a given buffer. The number of entries (N) is not known ahead of time, and is inferred by the number of matching TLVs in the given buffer.

In this example, the parent buffer is a [**WDI\_MESSAGE\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn926074), which defines the end of the TLV buffer. Note that [**WDI\_TLV\_BSS\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/dn926162) may be interspersed between other different TLV types in the parent buffer.

| Offset                         | Field                       | Type                |
|--------------------------------|-----------------------------|---------------------|
| 0                              | WDI\_MESSAGE\_HEADER        | Message header      |
| sizeof(WDI\_MESSAGE\_HEADER)   | TLV₀ (WDI\_TLV\_BSS\_ENTRY) | WDI\_BSS\_ENTRY     |
| TLV₀ + L₀ + sizeof(TLV Header) | TLV₁ (WDI\_TLV\_BSS\_ENTRY) | WDI\_BSS\_ENTRY     |
| TLV₁ + L₁ + sizeof(TLV Header) | TLV₂ (WDI\_TLV\_BSS\_ENTRY) | WDI\_BSS\_ENTRY     |
| TLV₂ + L₂ + sizeof(TLV Header) | TLV₃ (OTHER\_TLV\_TYPE)     | Some other TLV type |
| TLV₃ + L₃ + sizeof(TLV Header) | TLV₄ (WDI\_TLV\_BSS\_ENTRY) | WDI\_BSS\_ENTRY     |

 

For TLVs that contain other TLVs, the TLV reference topics have a *Multiple TLV instances allowed* column. If this column is checked, the specified TLV is allowed to appear multiple times. For an example of this, see [**WDI\_TLV\_CONNECT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/dn926266).

 

 





