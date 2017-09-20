---
title: NET_ADAPTER_PAUSE_FUNCTIONS enumeration
topic_type:
- apiref
api_name:
- NET_ADAPTER_PAUSE_FUNCTIONS, PNET_ADAPTER_PAUSE_FUNCTIONS
api_location:
- netadapter.h
api_type:
- HeaderDef
---

# NET_ADAPTER_PAUSE_FUNCTIONS enumeration

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Specifies a client driver's support for the IEEE 802.3 pause frames.

Syntax
------

```cpp
typedef enum _NET_ADAPTER_PAUSE_FUNCTIONS { 
  NetAdapterPauseFunctionsUnsupported     = NdisPauseFunctionsUnsupported,
  NetAdapterPauseFunctionsSendOnly        = NdisPauseFunctionsSendOnly,
  NetAdapterPauseFunctionsReceiveOnly     = NdisPauseFunctionsReceiveOnly,
  NetAdapterPauseFunctionsSendAndReceive  = NdisPauseFunctionsSendAndReceive,
  NetAdapterPauseFunctionsUnknown         = NdisPauseFunctionsUnknown
} NET_ADAPTER_PAUSE_FUNCTIONS, *PNET_ADAPTER_PAUSE_FUNCTIONS;
```

Constants
---------

**NetAdapterPauseFunctionsUnsupported**  
Indicates that the adapter or link partner does not support pause frames.

**NetAdapterPauseFunctionsSendOnly**  
Indicates that the adapter and link partner only support sending pause frames from the adapter to the link partner.

**NetAdapterPauseFunctionsReceiveOnly**  
Indicates that the adapter and link partner only support sending pause frames from the link partner to the adapter.

**NetAdapterPauseFunctionsSendAndReceive**  
Indicates that the adapter and link partner support sending and receiving pause frames in both transint and receive directions.

**NetAdapterPauseFunctionsUnknown**  
Indicates that pause frame negotiation is in progress. The pause frame support that the link partner provides is unknown.

Remarks
---
The **NET_ADAPTER_PAUSE_FUNCTIONS** enumeration is used to specify pause frame support in the [**NET_ADAPTER_LINK_STATE**](net-adapter-link-state.md) structure.

An initialized [**NET_ADAPTER_LINK_STATE**](net-adapter-link-state.md) structure is an input to [**NetAdapterSetCurrentLinkState**](netadaptersetcurrentlinkstate.md).

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Minimum KMDF version</p></td>
<td align="left"><p>1.21</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum NetAdapterCx version</p></td>
<td align="left"><p>1.0</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Netadapter.h</td>
</tr>
</tbody>
</table>

 

 





