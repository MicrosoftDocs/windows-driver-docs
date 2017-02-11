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

# NET\_ADAPTER\_PAUSE\_FUNCTIONS enumeration


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Syntax
------

```ManagedCPlusPlus
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

**NetAdapterPauseFunctionsSendOnly**  

**NetAdapterPauseFunctionsReceiveOnly**  

**NetAdapterPauseFunctionsSendAndReceive**  

**NetAdapterPauseFunctionsUnknown**  

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

 

 





