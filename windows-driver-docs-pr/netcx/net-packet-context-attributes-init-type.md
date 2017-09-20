---
title: NET_PACKET_CONTEXT_ATTRIBUTES_INIT_TYPE macro
description: NET_PACKET_CONTEXT_ATTRIBUTES_INIT_TYPE macro
ms.assetid: F57152AE-B507-4AAF-9769-4FB47858F7FE
keywords:
- WDF Network Adapter Class Extension NET_PACKET_CONTEXT_ATTRIBUTES_INIT_TYPE, NetAdapterCx NET_PACKET_CONTEXT_ATTRIBUTES_INIT_TYPE, NetCx NET_PACKET_CONTEXT_ATTRIBUTES_INIT_TYPE
ms.author: windowsdriverdev
ms.date: 09/05/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# NET_PACKET_CONTEXT_ATTRIBUTES_INIT_TYPE macro

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The **NET_PACKET_CONTEXT_ATTRIBUTES_INIT_TYPE** macro initializes a NetAdapterCx client driver's [NET_PACKET_CONTEXT_ATTRIBUTES](net-packet-context-attributes.md) structure for a [NET_PACKET](net-packet.md) and inserts driver-defined context information into the structure.

## Syntax

```cpp
void NET_PACKET_CONTEXT_ATTRIBUTES_INIT_TYPE(
    _packetcontextattributes,
    _contexttype
);
```

## Parameters

*_packetcontextattributes*  
A pointer to a [NET_PACKET_CONTEXT_ATTRIBUTES](net-packet-context-attributes.md) structure.

*_contexttype*  
The structure type name of a driver-defined structure that describes the contents of the packet's context space.

## Return value

This macro does not return a value.

## Remarks

Before calling NET_PACKET_CONTEXT_ATTRIBUTES_INIT_TYPE, you must first declare a custom structure for this packet context, then call [NET_PACKET_DECLARE_CONTEXT_TYPE_WITH_NAME](net-packet-declare-context-type-with-name.md) globally (not within a function).

## Example

In this example, the client driver defines a packet context called **MY_TCB** for its transmit queue, then invokes the [NET_PACKET_DECLARE_CONTEXT_TYPE_WITH_NAME](net-packet-declare-context-type-with-name.md) macro to register the structure and specify that the context accessor method will be named **GetMyTcbFromPacket**.

**MY_TCB** is a simple packet context that contains a hardware descriptor for this example client's NIC. TCB stands for Transmit Control Block, indicating that this example context would be used for assistance in transmit operations.

```cpp
// in global scope

typedef struct _MY_TCB{
    MY_TX_DESC  *TxDesc;
} MY_TCB;

NET_PACKET_DECLARE_CONTEXT_TYPE_WITH_NAME(MY_TCB, GetMyTcbFromPacket);
```

Then, in its [EVT_NET_ADAPTER_CREATE_TXQUEUE](evt-net-adapter-create-txqueue.md) callback, the example driver allocates a [NET_PACKET_CONTEXT_ATTRIBUTES](net-packet-context-attributes.md) structure and calls [NET_PACKET_CONTEXT_ATTRIBUTES_INIT_TYPE](net-packet-context-attributes-init-type.md) to initialize it with the **MY_TCB** type.

```cpp
...

NET_PACKET_CONTEXT_ATTRIBUTES packetContextAttributes;
NET_PACKET_CONTEXT_ATTRIBUTES_INIT_TYPE(&packetContextAttributes, MY_TCB);
```

## Requirements

|     |     |
| --- | --- |
| Target platform | Universal |
| Minimum KMDF version | 1.23 |
| Minimum NetAdapterCx version | 1.1 |
| Header | NetAdapterPacket.h (include NetAdapterCx.h) |

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")