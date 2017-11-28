---
title: SRB\_UNKNOWN\_DEVICE\_COMMAND
description: SRB\_UNKNOWN\_DEVICE\_COMMAND
ms.assetid: 89bc2176-e384-48bf-82d8-4a8ab2bd5159
---

# SRB\_UNKNOWN\_DEVICE\_COMMAND


## <span id="ddk_srb_unknown_device_command_ks"></span><span id="DDK_SRB_UNKNOWN_DEVICE_COMMAND_KS"></span>


The class driver sends this request to pass IRPs that it does not know how to handle to the minidriver. *pSrb*-&gt;**Irp** points to the unhandled IRP. See [**HW\_STREAM\_REQUEST\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff559702).

This request can be used as an IRP pass-through mechanism for IRPs that the stream class does not understand, but that the minidriver might. For example, there are several Plug and Play (PnP) IRPs that the stream class does not process, but that a 1394 camera driver does.

If the minidriver does not support SRB\_UNKNOWN\_DEVICE\_COMMAND or does not handle the IRP, it should set pSRB-&gt;Status to STATUS\_NOT\_IMPLEMENTED.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20SRB_UNKNOWN_DEVICE_COMMAND%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




