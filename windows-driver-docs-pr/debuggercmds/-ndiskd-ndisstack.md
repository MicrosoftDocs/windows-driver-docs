---
title: ndiskd.ndisstack
description: The !ndiskd.ndisstack extension displays a debug stack trace.
keywords: ["ndiskd.ndisstack Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- ndiskd.ndisstack
api_type:
- NA
---

# !ndiskd.ndisstack


**Note**  Third party network driver developers are not expected to manually use this extension command. You can run it to see the information it displays but you are not able to reuse the details it provides in your driver.

 

The **!ndiskd.ndisstack** extension displays a debug stack trace.

```console
!ndiskd.ndisstack -handle <x> [-statistics]
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______-handle______"></span><span id="_______-HANDLE______"></span> *-handle*   
Required. Handle of the stack block.

<span id="_______-statistics______"></span><span id="_______-STATISTICS______"></span> *-statistics*   
Shows debugging statistics.

### <span id="DLL"></span><span id="dll"></span>DLL

Ndiskd.dll

## <span id="see_also"></span>See also


[Network Driver Design Guide](../network/index.md)

[Windows Vista and Later Networking Reference](/windows-hardware/drivers/ddi/_netvista/)

[Debugging the Network Stack](/shows/defrag-tools/175-debugging-network-stack)

[**NDIS extensions (Ndiskd.dll)**](ndis-extensions--ndiskd-dll-.md)

[**!ndiskd.help**](-ndiskd-help.md)

 

