---
title: wdfkd.wdfforwardprogress
description: The wdfkd.wdfforwardprogress extension displays information about the forward progress of a specified framework queue object.
ms.assetid: 3062d914-4fd4-4e33-8cf0-562484380184
keywords: ["wdfkd.wdfforwardprogress Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- wdfkd.wdfforwardprogress
api_type:
- NA
---

# !wdfkd.wdfforwardprogress


The **!wdfkd.wdfforwardprogress** extension displays information about the forward progress of a specified framework queue object.

```
!wdfkd.wdfforwardprogress Handle
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Handle______"></span><span id="_______handle______"></span><span id="_______HANDLE______"></span> *Handle*   
A handle to a framework queue object.

### <span id="DLL"></span><span id="dll"></span>DLL

Wdfkd.dll

### <span id="Frameworks"></span><span id="frameworks"></span><span id="FRAMEWORKS"></span>Frameworks

KMDF 1

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about how to debug Kernel-Mode Driver Framework (KMDF) drivers, see [Kernel-Mode Driver Framework Debugging](kernel-mode-driver-framework-debugging.md).

Remarks
-------

This extension will succeed only if the specified framework queue object is configured to support forward progress. If this extension is used with other objects, an error message will be displayed.

The following example shows the display from a **!wdfkd.wdfforwardprogress** extension.

```
kd> !wdfkd.wdfforwardprogress 0x79af3250 

# Dumping forward progress fields for WDFQUEUE 0x79af3250
=================================================
    ForwardProgressReservedPolicy: UseExamine (0x2)

    Total reserved requests: 44 

    Number of available reserved requests in list: 41
            !WDFREQUEST 0x7bcaf4c0 (Reserved) !IRP 0x00000000
            !WDFREQUEST 0x7bc67eb0 (Reserved) !IRP 0x00000000
            !WDFREQUEST 0x7bccf678 (Reserved) !IRP 0x00000000
            !WDFREQUEST 0x7bb6ce40 (Reserved) !IRP 0x00000000
            !WDFREQUEST 0x7be30a58 (Reserved) !IRP 0x00000000
            !WDFREQUEST 0x79af37d0 (Reserved) !IRP 0x00000000
            !WDFREQUEST 0x7bc7f428 (Reserved) !IRP 0x00000000
            !WDFREQUEST 0x7bbd40f0 (Reserved) !IRP 0x00000000
            !WDFREQUEST 0x7bd333a8 (Reserved) !IRP 0x00000000
            !WDFREQUEST 0x7bd241d8 (Reserved) !IRP 0x00000000
            !WDFREQUEST 0x7bd594e0 (Reserved) !IRP 0x00000000
            !WDFREQUEST 0x7bd80d10 (Reserved) !IRP 0x00000000
            !WDFREQUEST 0x78ea2d50 (Reserved) !IRP 0x00000000
            !WDFREQUEST 0x792020f0 (Reserved) !IRP 0x00000000
            !WDFREQUEST 0x7bc37258 (Reserved) !IRP 0x00000000
            !WDFREQUEST 0x7bbc1fb0 (Reserved) !IRP 0x00000000
            !WDFREQUEST 0x7bbc4fb0 (Reserved) !IRP 0x00000000
            !WDFREQUEST 0x7be0cb80 (Reserved) !IRP 0x00000000
            !WDFREQUEST 0x7bc84890 (Reserved) !IRP 0x00000000
            !WDFREQUEST 0x78acbd18 (Reserved) !IRP 0x00000000
            !WDFREQUEST 0x7bcf1ad8 (Reserved) !IRP 0x00000000
            !WDFREQUEST 0x7bead540 (Reserved) !IRP 0x00000000
            !WDFREQUEST 0x7922c0f0 (Reserved) !IRP 0x00000000
            !WDFREQUEST 0x7a34a0f0 (Reserved) !IRP 0x00000000
            !WDFREQUEST 0x625195d0 (Reserved) !IRP 0x00000000
            !WDFREQUEST 0x7bc33640 (Reserved) !IRP 0x00000000
            !WDFREQUEST 0x7bba9f28 (Reserved) !IRP 0x00000000
            !WDFREQUEST 0x7bba44c8 (Reserved) !IRP 0x00000000
            !WDFREQUEST 0x7bb77cd8 (Reserved) !IRP 0x00000000
            !WDFREQUEST 0x7a2b89a8 (Reserved) !IRP 0x00000000
            !WDFREQUEST 0x7a41ab88 (Reserved) !IRP 0x00000000
            !WDFREQUEST 0x7bc7cc88 (Reserved) !IRP 0x00000000
            !WDFREQUEST 0x7bd37180 (Reserved) !IRP 0x00000000
            !WDFREQUEST 0x7bca40f0 (Reserved) !IRP 0x00000000
            !WDFREQUEST 0x64b4af20 (Reserved) !IRP 0x00000000
            !WDFREQUEST 0x7bd01a40 (Reserved) !IRP 0x00000000
            !WDFREQUEST 0x7a25cfb0 (Reserved) !IRP 0x00000000
            !WDFREQUEST 0x7bba9330 (Reserved) !IRP 0x00000000
            !WDFREQUEST 0x7bd14a40 (Reserved) !IRP 0x00000000
            !WDFREQUEST 0x7bcc0210 (Reserved) !IRP 0x00000000
            !WDFREQUEST 0x7a54eb00 (Reserved) !IRP 0x00000000

    Number of reserved requests in use: 3
            !WDFREQUEST 0x7bf0ab80 (Reserved) !IRP 0x8438f008
            !WDFREQUEST 0x7bc53ca8 (Reserved) !IRP 0x875f59f0
            !WDFREQUEST 0x7bced8b8 (Reserved) !IRP 0x85c25348

    Number of undispatched IRP's in list: 0

    EvtIoReservedResourcesAllocate: (0x9a3f1b70) mqueue!EvtIoAllocateResourcesForReservedRequest
    EvtIoExamineIrp: (0x9a3f19d0) mqueue!EvtIoWdmIrpForForwardProgress
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!wdfkd.wdfforwardprogress%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




