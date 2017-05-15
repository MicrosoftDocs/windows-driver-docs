---
title: ndiskd.findpacket
description: Warning  This extension is for legacy NDIS 5.x drivers. The NDIS\_PACKET structure and its associated architecture have been deprecated. The ndiskd.findpacket extension finds the specified packets.
ms.assetid: fc07b2d8-85ca-4be1-ae9d-40b7c7f81b08
keywords: ["ndiskd.findpacket Windows Debugging"]
topic_type:
- apiref
api_name:
- ndiskd.findpacket
api_type:
- NA
---

# !ndiskd.findpacket


**Warning**  This extension is for legacy NDIS 5.x drivers. The [NDIS\_PACKET](https://msdn.microsoft.com/library/windows/hardware/ff557086) structure and its associated architecture have been deprecated.

 

The **!ndiskd.findpacket** extension finds the specified packets.

``` syntax
    !ndiskd.findpacket [-VirtualAddress] [-PoolAddress]  
```

## <span id="ddk__ndiskd_findpacket_dbg"></span><span id="DDK__NDISKD_FINDPACKET_DBG"></span>Parameters


<span id="_______VirtualAddress______"></span><span id="_______virtualaddress______"></span><span id="_______VIRTUALADDRESS______"></span> *VirtualAddress*   
Specifies a virtual address that is contained in the desired packet.

<span id="_______PoolAddress______"></span><span id="_______pooladdress______"></span><span id="_______POOLADDRESS______"></span> *PoolAddress*   
Specifies a pool address. All unreturned packets in this pool will be displayed.

### <span id="DLL"></span><span id="dll"></span>DLL

Ndiskd.dll

## <span id="see_also"></span>See also


[Windows 2000 and Windows XP Networking Design Guide](https://msdn.microsoft.com/library/windows/hardware/ff565849)

[Windows 2000 and Windows XP Networking Reference](https://msdn.microsoft.com/library/windows/hardware/ff565850)

[NDIS\_PACKET](https://msdn.microsoft.com/library/windows/hardware/ff557086)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!ndiskd.findpacket%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





