---
title: ndiskd.nwadapter
description: The ndiskd.nwadapter extension displays information about one or more nwifi ADAPT structures. If you run this extension with no parameters, ndiskd will display a list of all nwifi ADAPT structures.
keywords: ["ndiskd.nwadapter Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- ndiskd.nwadapter
api_type:
- NA
---

# !ndiskd.nwadapter

The **!ndiskd.nwadapter** extension displays information about one or more nwifi!ADAPT structures. If you run this extension with no parameters, !ndiskd will display a list of all nwifi!ADAPT structures.

```console
!ndiskd.nwadapter [-handle <x>]
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters

<span id="_______-handle______"></span><span id="_______-HANDLE______"></span> *-handle*   
Address of an ADAPT block.

### DLL

Ndiskd.dll

## See Also

[Network Driver Design Guide](../network/index.md)

[Windows Vista and Later Networking Reference](/windows-hardware/drivers/ddi/_netvista/)

[Debugging the Network Stack](/shows/defrag-tools/175-debugging-network-stack)

[**NDIS extensions (Ndiskd.dll)**](ndis-extensions--ndiskd-dll-.md)

[**!ndiskd.help**](-ndiskd-help.md)
