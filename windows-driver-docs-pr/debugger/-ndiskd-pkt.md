---
title: ndiskd.pkt
description: Warning  This extension is for legacy NDIS 5.x drivers. The NDIS\_PACKET structure and its associated architecture have been deprecated. The ndiskd.pkt extension displays information about an NDIS\_PACKET structure.
ms.assetid: 8e704173-3b09-4377-b73a-ba67a3c3c930
keywords: ["ndiskd.pkt Windows Debugging"]
topic_type:
- apiref
api_name:
- ndiskd.pkt
api_type:
- NA
---

# !ndiskd.pkt


**Warning**  This extension is for legacy NDIS 5.x drivers. The [NDIS\_PACKET](https://msdn.microsoft.com/library/windows/hardware/ff557086) structure and its associated architecture have been deprecated.

 

The **!ndiskd.pkt** extension displays information about an [NDIS\_PACKET](https://msdn.microsoft.com/library/windows/hardware/ff557086) structure.

``` syntax
    !ndiskd.pkt [-packet] [-verbosity] 
```

## <span id="ddk__ndiskd_pkt_dbg"></span><span id="DDK__NDISKD_PKT_DBG"></span>Parameters


<span id="_______Packet______"></span><span id="_______packet______"></span><span id="_______PACKET______"></span> *Packet*   
Specifies the address of the packet.

<span id="_______Verbosity______"></span><span id="_______verbosity______"></span><span id="_______VERBOSITY______"></span> *Verbosity*   
Specifies the amount of detail to be displayed.

### <span id="DLL"></span><span id="dll"></span>DLL

Ndiskd.dll

## <span id="see_also"></span>See also


[Windows 2000 and Windows XP Networking Design Guide](https://msdn.microsoft.com/library/windows/hardware/ff565849)

[Windows 2000 and Windows XP Networking Reference](https://msdn.microsoft.com/library/windows/hardware/ff565850)

[NDIS\_PACKET](https://msdn.microsoft.com/library/windows/hardware/ff557086)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!ndiskd.pkt%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





