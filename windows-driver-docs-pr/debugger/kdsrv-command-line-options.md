---
title: KdSrv Command-Line Options
description: The KdSrv command line uses the following syntax.
ms.assetid: 95b144c0-4507-4ce4-b828-1ac385dd7165
keywords: ["KdSrv Command-Line Options Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- KdSrv Command-Line Options
api_type:
- NA
---

# KdSrv Command-Line Options


The KdSrv command line uses the following syntax.

```
kdsrv -t ServerTransport 
```

## <span id="ddk_kdsrv_command_line_options_dbg"></span><span id="DDK_KDSRV_COMMAND_LINE_OPTIONS_DBG"></span>Parameters


<span id="_______-t_______ServerTransport______"></span><span id="_______-t_______servertransport______"></span><span id="_______-T_______SERVERTRANSPORT______"></span> **-t** *ServerTransport*   
Specifies the transport protocol. For a list of the possible protocols and the syntax for *ServerTransport* in each case, see [**Activating a KD Connection Server**](activating-a-kd-connection-server.md).

If you type **kdsrv** with no parameters, a message box with help text appears.

For information about using KdSrv, see [KD Connection Servers (Kernel Mode)](kd-connection-servers--kernel-mode-.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20KdSrv%20Command-Line%20Options%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




